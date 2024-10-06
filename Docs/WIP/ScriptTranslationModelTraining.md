# Training the Tibetan Script Translation Model

To begin training the translation model to accept Tibetan script, my hope was that using the model that was pre-trained for phonetic translations
would be more effective than training the base T5 model from scratch. My guess being that the pre-trained model would either learn to transliterate 
the inputs for itself, or would have some semblance of the structure of the outputs more readily at hand, even if the inputs are different.

In order to allow the model to take in Tibetan script, the T5 tokenizer needed to be expanded to accomadate the unique characters. In my work with
training a transliteration model, I found that tokenizing the Tibetan script at the level of individual characters produced the best results. Thus,
I repeated that approach here.

I began by testing the base T5-large model against my pretrained phonetic translation model. You can see the results of this training below.

![Comparison Loss](../../readme-assets/script-comparison-loss.png?raw=true "Comparison Loss")

You can see that the pre-trained model does significantly out perform the base model. 

From there, the pre-trained model was trained for an additional 6 epochs. You can see the graph of the final 3 epochs below.


![Eval Loss](../../readme-assets/pre-trained-script-model-losses.png?raw=true "Eval Loss")

![Eval Bleu](../../readme-assets/script-model-bleu.png?raw=true "Eval Bleu")

You can see that the final evaluation loss was [eval loss] and the final bleu score was [bleu score].