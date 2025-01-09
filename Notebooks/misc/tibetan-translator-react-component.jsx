import React, { useState } from 'react';
import { Loader2 } from 'lucide-react';

const TibetanTranslator = () => {
  const [inputText, setInputText] = useState('');
  const [translation, setTranslation] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  const handleTranslate = async () => {
    if (!inputText.trim()) {
      setError('Please enter some Tibetan text to translate');
      return;
    }

    setIsLoading(true);
    setError('');

    try {
      const response = await fetch('https://api-inference.huggingface.co/models/billingsmoore/tibetan-to-english-translation-4bit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer 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'
        },
        body: JSON.stringify({ inputs: inputText }),
      });

      const text = await response.text();
      console.log('Response status:', response.status);
      console.log('Response text:', text);

      if (!response.ok) {
        throw new Error(`API Error: ${response.status} - ${text}`);
      }

      const data = JSON.parse(text);
      setTranslation(data[0]?.translation_text || data[0]?.generated_text);
    } catch (err) {
      setError(`Translation error: ${err.message}`);
      console.error('Full error:', err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="max-w-2xl mx-auto p-6 bg-white rounded-lg shadow-lg">
      <h2 className="text-2xl font-bold mb-4">Tibetan-English Translator</h2>
      <p className="text-gray-600 mb-6">Enter Tibetan text below to get an English translation</p>
      
      <div className="space-y-4">
        <div>
          <label className="block text-sm font-medium mb-2">
            Tibetan Text
          </label>
          <textarea
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            placeholder="Enter Tibetan text here..."
            className="w-full min-h-[100px] p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        {error && (
          <div className="p-4 bg-red-50 border-l-4 border-red-500 text-red-700">
            {error}
          </div>
        )}

        <div>
          <label className="block text-sm font-medium mb-2">
            English Translation
          </label>
          <div className="p-4 min-h-[100px] bg-gray-50 rounded-md border border-gray-200">
            {isLoading ? (
              <div className="flex items-center justify-center h-full">
                <Loader2 className="h-6 w-6 animate-spin" />
                <span className="ml-2">Translating...</span>
              </div>
            ) : (
              translation || 'Translation will appear here...'
            )}
          </div>
        </div>

        <button
          onClick={handleTranslate}
          disabled={isLoading || !inputText.trim()}
          className="w-full py-2 px-4 bg-blue-500 text-white rounded-md hover:bg-blue-600 disabled:bg-gray-400 disabled:cursor-not-allowed flex items-center justify-center"
        >
          {isLoading ? (
            <>
              <Loader2 className="mr-2 h-4 w-4 animate-spin" />
              Translating...
            </>
          ) : (
            'Translate'
          )}
        </button>
      </div>
    </div>
  );
};

export default TibetanTranslator;