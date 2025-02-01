// Import necessary React components and hooks
import React, { useState } from 'react';
// Import the loading spinner icon from lucide-react
import { Loader2 } from 'lucide-react';

// Main component for translating Tibetan text to English
const TibetanTranslator = () => {
  // State management using React hooks
  const [inputText, setInputText] = useState('');      // Stores the input Tibetan text
  const [translation, setTranslation] = useState('');  // Stores the translated English text
  const [isLoading, setIsLoading] = useState(false);   // Tracks loading state during API calls
  const [error, setError] = useState('');              // Stores any error messages

  // Function to handle the translation process
  const handleTranslate = async () => {
    // Validate if input text exists
    if (!inputText.trim()) {
      setError('Please enter some Tibetan text to translate');
      return;
    }

    // Set loading state and clear any previous errors
    setIsLoading(true);
    setError('');

    try {
      // Make API call to HuggingFace's translation model
      const response = await fetch('https://api-inference.huggingface.co/models/billingsmoore/tibetan-to-english-translation-4bit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer INSERT_TOKEN_HERE'  // Replace with actual API token
        },
        body: JSON.stringify({ inputs: inputText }),
      });

      // Log response for debugging purposes
      const text = await response.text();
      console.log('Response status:', response.status);
      console.log('Response text:', text);

      // Check if the API request was successful
      if (!response.ok) {
        throw new Error(`API Error: ${response.status} - ${text}`);
      }

      // Parse the response and update the translation state
      const data = JSON.parse(text);
      setTranslation(data[0]?.translation_text || data[0]?.generated_text);

    } catch (err) {
      // Handle any errors that occur during translation
      setError(`Translation error: ${err.message}`);
      console.error('Full error:', err);
    } finally {
      // Reset loading state regardless of success or failure
      setIsLoading(false);
    }
  };

  // Render the component UI
  return (
    // Main container with styling
    <div className="max-w-2xl mx-auto p-6 bg-white rounded-lg shadow-lg">
      {/* Header section */}
      <h2 className="text-2xl font-bold mb-4">Tibetan-English Translator</h2>
      <p className="text-gray-600 mb-6">Enter Tibetan text below to get an English translation</p>
      
      <div className="space-y-4">
        {/* Input section for Tibetan text */}
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

        {/* Error message display */}
        {error && (
          <div className="p-4 bg-red-50 border-l-4 border-red-500 text-red-700">
            {error}
          </div>
        )}

        {/* Translation output section */}
        <div>
          <label className="block text-sm font-medium mb-2">
            English Translation
          </label>
          <div className="p-4 min-h-[100px] bg-gray-50 rounded-md border border-gray-200">
            {isLoading ? (
              // Loading indicator
              <div className="flex items-center justify-center h-full">
                <Loader2 className="h-6 w-6 animate-spin" />
                <span className="ml-2">Translating...</span>
              </div>
            ) : (
              // Display translation or placeholder text
              translation || 'Translation will appear here...'
            )}
          </div>
        </div>

        {/* Translation button */}
        <button
          onClick={handleTranslate}
          disabled={isLoading || !inputText.trim()}
          className="w-full py-2 px-4 bg-blue-500 text-white rounded-md hover:bg-blue-600 disabled:bg-gray-400 disabled:cursor-not-allowed flex items-center justify-center"
        >
          {isLoading ? (
            // Loading state for button
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

// Export the component for use in other parts of the application
export default TibetanTranslator;
