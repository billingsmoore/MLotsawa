# Testing Bidirectional Translation Training (Oct 12, 2024)

## Motivation
Nam (2024) suggests that there may be some reason to believe that training a translation model bidirectionally, source language -> target language 
and target language -> source language, may improve translation quality.

Previous models for this project were trained in only one direction because the intended use case is to translate from Tibetan to English (or some other language) and there was no reason to attempt training in the opposite direction. However, if bidirectional training improves translation quality, it would be worthwhile even if translation into Tibetan was never necessary.

## Testing
To investigate the effects of bidirectional training the [T5-small model](https://huggingface.co/google-t5/t5-small) was twice fine-tuned on
['billingsmoore/tibetan-to-english-translation-dataset'](https://huggingface.co/datasets/billingsmoore/tibetan-to-english-translation-dataset).

The first training was done in unidirectionally, Tibetan to English only. The second was done bidirectionally, both Tibetan to English and English to Tibetan. Both were trained for 3 epochs and evaluated by Loss and BLEU score. Both models were evaluated only on the unidirectional Tibetan to English data. Graphs of training results are can be seen below.

![Losses](readme-assets/bidirectional/bidirectional-losses.png?raw=true "Graph of losses")

![BLEU](readme-assets/bidirectional/bidirectional-bleu.png?raw=true "Graph of BLEU scores")

Note that while both models were trained for 3 epochs, the bidirectional dataset was larger, and thus the bidirectional run consists of significantly more training steps (the horizontal axis of the above graphs).

It can be clearly seen that not only did bidirectional training not improved translation quality, the bidirectional model produced significantly worse BLEU scores.

## Conclusion

There appears to be a substantial negative impact to attempting to train a model bidirectionally which is not warranted for this project, given the lack of use case for bidirectional translations.

Moving forward, models will continue to be trained only unidirectionally.

## Citations

[Nam, Wongyung, and Beakcheol Jang. "A survey on multimodal bidirectional machine learning translation of image and natural language processing." Expert Systems with Applications 235 (2024): 121168.](https://www.sciencedirect.com/science/article/abs/pii/S0957417423016706)