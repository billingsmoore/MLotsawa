# Context Experiments

The purpose of this experiment was to determine if providing additional context improved translation quality. Specifically, the contexts used were the phonetic transliteration (or 'transcription') of the Tibetan and/or the tags that Lotsawa House placed on the source text of the Tibetan. For example if a given sentence came from a praise to Amitabha, it might be tagged as 'Praise' and 'Amitabha'.

## Dataset

For this experiment the dataset used was **['billingsmoore/tagged-tibetan-to-english-translation-dataset'](https://huggingface.co/datasets/billingsmoore/tagged-tibetan-to-english-translation-dataset)**. 10% of the dataset was set aside as test data and was not included in the training data. This data consists of Tibetan sentences alongside their phonetics and English translations and tags from Lotsawa House.

## Methods

Four models were trained using the dataset described above. Each model was a T5-small, and the English sentences were used as the target output for all training. Every model was trained for 5 epochs and evaluated using [BLEU](https://en.wikipedia.org/wiki/BLEU), [chrF](https://machinetranslate.org/chrF), and [TER](https://machinetranslate.org/ter) scores.

The first model, 'no-context', was trained using just the Tibetan sentence as input with the prefix 'Translate Tibetan to English: '

The second model, 'phonetic-context', was trained with Tibetan sentences combined with their phonetics as input in the following format (given as a Python f-string): f'Translate Tibetan to English: {tib} \nPhonetic: {phon}'.

The third model, 'tag-context', was trained with Tibetan sentences paired with their associated tags with the following format: f'Translate Tibetan to English: {tib} \nTags: {tags}'

The fourth model, 'both-context' was trained using both phonetics and tags as additional context for the Tibetan inputs in the following format: f'Translate Tibetan to English: {tib} \nPhonetic: {phon} \nTags: {tags}'

## Results

The results of training can be seen in the graphs below.

![BLEU](assets/context/context-bleu.png?raw=true "Graph of Bleu Scores")

![CHRF](assets/context/context-chrf.png?raw=true "Graph of chrF Scores")

![TER](assets/context/context-ter.png?raw=true "Graph of TER Scores")

## Discussion

You can see in the graphs above that adding context of either kind improves translation results. However, the effect of the tags is quite small, whereas the effect of the phonetics is really substantial. Adding tags in addition to the phonetics appears to have only very minimal benefit.

It seems that adding tags is not worth the extra trouble, but adding phonetics very much is, especially where phonetics is being generated anyway.

## Suggestions for Further Work

It should be tested whether adding English as context improves results from a transliteration model. If so, it may then be worth investigating if a feedback loop could be created, where phonetics are generated then used as context to generate a translation which is in turn used to generate better phonetics and so on.