# Mixture of Experts Architecture for Machine Translation on Edge Devices

## Introduction

Mixture of Experts (MoE) is a neural network architecture characterized by dividing tasks among subnetworks referred to as "experts". As a MoE model trains it learns not only to improve its expert subnetworks but also to improve its directing of inputs to individual experts. That is, experts become experts at processing particular types of data and the model learns which expert to direct inputs to. Thus, for processing a particular input, only a given expert subnetwork of model parameters is actually activated.

This contrasts with the standard, "dense", neural network architecture in which all parameters are used to process every input. As a result, MoE models, while having many more parameters than comparable dense models, actually use fewer operations to process a given input.

As an example, Google has produced two architectures which come in relatively small sizes, T5 and Switch. T5 is a dense model, Switch is a MoE model. Both models are pre-trained on the same datasets and the individual experts inside the Switch model are analogous to very small T5's. The smallest T5 model is T5-Small, with the next size up being T5-Base. The smallest Switch model is Switch-Base-8. The default usage of Switch-Base-8 is for each input to be processed by a single expert who is best at that type of input ("top-1 expert").

The compute resources used by these models are given in the following table.

### Performance Comparison Table
| | T5-Small | T5-Base | Switch-Base-8 |
| --- | --- | --- | --- | 
| **Total Params** | 60M | 220M | 1.4B| 
| **Active Params per Token** | 60M | 220M | 152M (if top-1 expert) | 
| **FLOPs per Token** | ~4B | ~14B | ~9B| 
| **RAM Usage** | 0.5 GB| 1.7 GB | 3.5 GB|

You can see in the table above that while Switch-Base-8 has far more parameters than either T5-Small or T5-Base, the number of active parameters when processing a given input falls in between the two T5's. As a result, while Switch-Base-8 requires more RAM than either T5, the number of floating-point operations (FLOPs) performed by Switch-Base-8 is smaller than that of T5-Base, though larger than T5-Small.

In general, the limiting factors for operating language models, processing time and compute costs,  are proportional to the number of FLOPs performed by the model, while RAM usage is generally only a concern for the largest models or on edge devices where RAM is tightly constrained.

Because of these limiting factors, a common approach to machine learning tasks is to use the smallest model that provides acceptable quality. Thus, if we assume that performance scales linearly with the number of FLOPs, one would expect that the MoE model would be preferable when 9B FlOPs per token is an acceptable cost but 14B is too large.

However, the advantage of MoE models is that they are intended to outperform comparably sized dense models. This is because MoE models can make their expert subnetworks more highly optimized for particular subsets of the input data. There is reason to believe then that the MoE model should perform better than just a linear increase over a dense model.

## Study Setup

For this study, I will assume that RAM is unconstrained and that FLOPs are the primary factor of concern. 

The application of interest is machine translation from Tibetan to English and performance will be measured by [BLEU](https://en.wikipedia.org/wiki/BLEU), [chfR](https://machinetranslate.org/chrF), and [TER](https://machinetranslate.org/ter) scores. 

I will treat a MoE model as "preferable" with respect to a metric if performance on the metric scales linearly or better with the number of FLOPs per token.

More formally, the MoE model is "preferable" for a metric, if the percent difference between the actual score and the predicted score is greater than zero for chrF and BLEU or less than zero for TER.

For example, if T5-Small achieves a BLEU score of .5 with 4B FLOPs, and T5-Base achieves a BLEU score of 1 with 14B FLOPs then Switch-Base-8 is preferable with respect to BLEU score if it achieves at least .75 with 9B FLOPs, with linear performance of BLEU score (y) modeled with respect to billions of parameters (x) as $y = .05x + .3$.

To investigate this, I will run two experiments.

In the first experiment (Experiment 1), three models: T5-Small, T5-Base, and Switch-Base-8, will be trained on the dataset **[billings/tibetan-to-english-translation-dataset](https://huggingface.co/datasets/billingsmoore/tibetan-to-english-translation-dataset)**. This dataset consists of ~81,000 training pairs, 10% of which will be used as test data. This dataset is relatively small compared to typical machine translation datasets. Additionally, all of the sentence pairs in this dataset are taken from Buddhist texts. The small dataset size and similar subject matter (and therefore similar grammer and vocabulary) should give a sense of the worst-case performance of the MoE model. The homogeneous data is unlikely to be easy to direct to particular experts and the small sample size should make tuning the large number of over all parameters in the MoE model, compared to the dense model, less optimal. Training on a small dataset can sometimes be unstable, so these models will be trained for three epochs and the best epoch results for each metric will be used.

In the second experiment (Experiment 2) another set of the three models listed above will be trained on the dataset **openpecha/cleaned_MT_v1.0.3**. This dataset is much larger, with approximately 1.2 million training pairs. Additionally, the data is much more varied with sentences from Buddhist texts as well as contemporary fiction and non-fiction writing. As a result, this should provide the exact scenario in which MoE should excel. The larger number of parameters in the MoE model compared to the dense models will be useful on the larger dataset, and the more varied data should lend itself to optimizing individual experts. On the larger dataset, additional epochs should not be necessary, so these models will train for just one epoch.


## Experiment Results

### Experiment 1

**Dataset: billingsmoore/tibetan-to-english-translation-dataset**

**Epochs: 3**

The results of training the three models are shown in the table below. The best score for each model is given and the best score in each metric is bolded.

**model**|**chrf**|**bleu**|**ter (lower is better)**
-----|----|----|---
**t5-small**|4.322|.0436|99.4922
**switch-base-8**|5.554|.0804|**96.1867**
**t5-base**|**5.79**|**.0845**|96.2888

To determine whether or not the MoE model meets the criteria for being "preferable" for each metric (performance on the respective metric scales linearly or better with the number of FLOPs per token), I have provided a linear model of the previously given results from the two dense T5 models as well as the prediction that the linear model produces for the MoE model. I then give the actual score for the MoE model for the respective metric and the percentage difference ($\%\Delta$) achieved. Following our definition above, a model is considered "preferable" if the percentage difference is greater than 0 for chrF and BLEU or less than 0 for TER.

**metric**|**linear model**|**prediction**|**actual**|$$\%\Delta$$
----------|----------------|--------------|----------|------------
chrF|$$y=0.1468x+3.7348$$|$$5.056$$|$$5.554$$|$$+9.85$$
BLEU|$$y=.00409x+.02724$$|$$.06045$$|$$.0804$$|$$+33.0$$
TER (lower is better) |$$y=-0.32034x+100.77356$$|$$97.8905$$|$$96.1867$$|$$-1.74$$

### Experiment 2 Results

**Dataset: openpecha/cleaned_MT_v1.0.3**

**Epochs: 1**

The results of training the three models are shown in the table below. The best score for each model is given and the best score in each metric is bolded.

**model**|**chrf**|**bleu**|**ter (lower is better)**
-----|----|----|---
**t5-small**|12.2718|.8333|92.599
**switch-base-8**|19.6477|3.2027|88.9859
**t5-base**|**22.6354**|**4.6405**|**86.4034**

To determine whether or not the MoE model meets the criteria for being "preferable" for each metric (performance on the respective metric scales linearly or better with the number of FLOPs per token), I have provided a linear model of the previously given results from the two dense T5 models as well as the prediction that the linear model produces for the MoE model. I then give the actual score for the MoE model for the respective metric and the percentage difference ($\%\Delta$) achieved. Following our definition above, a model is considered "preferable" if the percentage difference is greater than 0 for chrF and BLEU or less than 0 for TER.

**metric**|**linear model**|**prediction**|**actual**|$$\%\Delta$$
----------|----------------|--------------|----------|------
chrF|$$y=1.03636x+8.12636$$|$$17.4536$$|$$19.6477$$|$$+12.57$$
BLEU|$$y=.38072x-.68958$$|$$2.7369$$|$$3.2027$$|$$+17.02$$
TER (lower is better)|$$y=-0.61956x+95.07724$$|$$89.5012$$|$$88.9858$$|$$-.57$$

## Discussion

The MoE model met the criteria for "preferable" for every metric in both experiments, and in every case substantially exceeded the linear prediction. Additionally, in Experiment 1, the MoE model beat the larger dense model with respect to the TER metric.

This indicates that where RAM is not a limiting factor, the additional computational costs of the MoE model are justified over the smaller dense model, and implies that a MoE model should be preferred over comparably sized dense models for Tibetan to English machine translation.