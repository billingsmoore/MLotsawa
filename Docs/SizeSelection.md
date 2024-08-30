# Size Selection

## Introduction

An important decision for this project was to select the size of model to be trained for the final product. The size of the model is determined by the number of parameters in the model and effects the amount of memory necessary to run the model as well as how long it takes for the model to produce its output.

Larger models can be more effective at learning from large scale datasets and, in general, can be expected to be 'better' than smaller models for a given use case. However, larger models can also be more prone to 'overfitting', learning the 'accidental' patterns in data that are not useful for prediction.

The T5 model family come in five sizes: small, base, large, XL, and XXL. XL and XXL were previous known as 3B and 11B respectively, for the number of parameters in the model. The full details of the model can be found on [Huggingface](https://huggingface.co/docs/transformers/model_doc/t5).

For this project, only three sizes were tried: small, base, and large. The reason for this is that the intended usage of this model is to be run locally on mid-range commodity hardware by non-technical translators. Therefore, models must be relatively small.

To select the size of model to be trained for the final product, each size of model was trained for three epochs. The metric used for evaluation of these models was the BLEU score as implemented by sacreBLEU. Additionally, each model was used to produce a sample translation of the sample text previously used in the architecture selection process.

## Dataset

To account for the possibility that the larger sizes of model may quickly overfit to a relatively small dataset, a larger sample was used than in the architecture selection process. 

For this phase, a random sample of 1 million text pairs was selected from the full dataset. Additionally, a seperate set of 100 thousand pairs were sampled to be used for evaluation.

## Training Results

Graphs results of training can be seen below:


![Training Loss](../readme-assets/size-select-train-loss.png?raw=true "Training Loss")

![Eval Loss](../readme-assets/size-select-eval-loss.png?raw=true "Eval Loss")

![Eval BLEU](../readme-assets/size-select-eval-bleu.png?raw=true "Eval BLEU")

You can see that each model follows a similar trajectory over the course of training. As expected, the large models quantitatively outperform their smaller counterparts by a significant amount. 

Below is a summary table which includes final BLEU scores as well as training parameters and a sample translation:

|Size     |Parameters  |BLEU  |Translation|
|---------|------------|------|-----------|
|Reference| n/a        |n/a   | ***In the Buddha, the Dharma and the Supreme Assembly***<br>***I take refuge until I attain enlightenment.***<br>***Through the merit of practising generosity and so on,***<br>***May I attain buddhahood for the benefit of all beings.***|
|Small    |60 million  |17.982| ***buddd ch the dchochochoknam the buddddu d the dchochochoque***<br>***i take refuge until until changchub bardu c c chub bdudu to my i***<br>***through the dak dr dak jinsme lords and the rest***<br>***attain attain attainmentmentment attain attainmentmentment in the spontaneous attainment***|
|Base     |220 million |29.165|***in the presence of the buddha the dharma and the supreme assembly<br>until i reach enlightenment i take refuge in you<br>through the merit of practising generosity and so on<br>for the benefit of beings i will accomplish buddhahood for the sake of all beings***|
|Large    |770 million |56.14 |***all of these buddhas dharmas and supreme saghas including the buddha the dharma and<br>i take refuge until enlightenment is realized<br>through the merit of practising generosity and so on<br>for the benefit of all beings i shall attain buddhahood***|

Again, we can see that the larger models both dramatically outperform the 'small' model. However, the difference between the 'large' and 'base' sizes is not straightforwardly substantial.