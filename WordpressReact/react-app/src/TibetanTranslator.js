import React, { useState, useEffect } from "react";
import { Loader2 } from "lucide-react";
import { pipeline } from "@xenova/transformers";

const TibetanTranslator = () => {
  const [inputText, setInputText] = useState("");
  const [translation, setTranslation] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");
  const [translator, setTranslator] = useState(null);

  useEffect(() => {
    const loadPipeline = async () => {
      try {
        const pipe = await pipeline(
          "translation",
          "billingsmoore/tibetan-to-english-translation-4bit"
        );
        setTranslator(pipe);
      } catch (err) {
        setError("Failed to load translation model.");
        console.error(err);
      }
    };
    loadPipeline();
  }, []);

  const handleTranslate = async () => {
    if (!inputText.trim()) {
      setError("Please enter some Tibetan text to translate");
      return;
    }
    if (!translator) {
      setError("Translation model is still loading. Please wait.");
      return;
    }
    setIsLoading(true);
    setError("");

    try {
      const result = await translator(inputText);
      setTranslation(result[0].translation_text || result[0].generated_text);
    } catch (err) {
      setError("Translation error: " + err.message);
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="max-w-2xl mx-auto p-6 bg-white rounded-lg shadow-lg">
      <h2 className="text-2xl font-bold mb-4">Tibetan-English Translator</h2>
      <p className="text-gray-600 mb-6">
        Enter Tibetan text below to get an English translation
      </p>

      <div className="space-y-4">
        <div>
          <label className="block text-sm font-medium mb-2">Tibetan Text</label>
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
              translation || "Translation will appear here..."
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
            "Translate"
          )}
        </button>
      </div>
    </div>
  );
};

export default TibetanTranslator;
