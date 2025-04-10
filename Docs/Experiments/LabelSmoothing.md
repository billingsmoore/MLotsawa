# Label Smoothing

## Introduction

Label smoothing is a machine learning regularization technique introduced in ["Rethinking the Inception Architecture for Computer Vision" (Szegedy et al., 2016)(https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Szegedy_Rethinking_the_Inception_CVPR_2016_paper.pdf)] in which the correct labels for model outputs are more evenly distributed across possible outputs. Thus, the probability of 'incorrect' labels is artificially made higher, while the probability of the correct label is artificially made lower. For those who are interested, the full details of the math are explained in that paper.

Intuitively, we can see how this might improve translation results by looking at the following example. Consider the Spanish source and English target pair below.

Source Es: "Probablemente me gustaría comer una hamburguesa en su lugar.", 

Target En: "I would probably like to have a hamburger instead."

If a model were to predict a translation like "I would probably like to *eat* a hamburger instead.", the model would be penalized during training. However, this translations would seem perfectly reasonable to a human. When training is performed with label smoothing, the model is penalized much less for mistakes like this, which can improve the models ability to generalize for future cases.

This intuition is borne out by "Attention Is All You Need" (Vaswani et al., 2017) where they find that label smoothing improves translation accuracy.

To verify that label smoothing could improve results for my use case, I have run an experiment to investigate the impact of label smoothing on Tibetan to English translation quality.

## Methods

For this experiment, I have trained T5-small on the ['billingsmoore'LotsawaHouse-bo-en'](https://huggingface.co/datasets/billingsmoore/LotsawaHouse-bo-en) dataset for 3 epochs. 5 models were trained with varying levels of label smoothing. Models were evaluated using [BLEU](https://en.wikipedia.org/wiki/BLEU), [chfR](https://machinetranslate.org/chrF), and [TER](https://machinetranslate.org/ter) scores.

## Results

The evaluation results are shown in the table below with the best performing model for each score bolded.

Label Smoothing Factor | BLEU | chrF | TER
-----------------------|------|------|-----
0 (baseline model)     | 8.907 | 20.179	| 98.449
.01                    |**10.958**	|22.432	|**96.979**
.025                   | 10.606	| **22.521**	| 98.355
.05                    | 10.614	| 22.484	| 97.660
.1                     | 8.309 |	19.674	| 99.218

## Discussion

You can see that label smoothing does, in fact, improve results. However, it's not as simple as an on or off. Very small label smoothing factor values improved results but increasing the factor too high produces performance that is worse than the baseline model.

The exact value is likely to vary with the size and quality of the training data as well. Here a value of only .01 appears to be the best, however Vaswani et al found improvements using a value of .1. 

Thus, label smoothing is recommended for future work, but the exact value of the label smoothing factor should be determined on a case by case basis.