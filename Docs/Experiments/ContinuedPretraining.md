# Continued Pretraining Experiment Results

In Alves (2024), continued pretraining is shown to improve machine translation the Llama. The goal of this experiment is to show that a similar improvement can be produced using T5.

## Methods

The dataset used for this experiment is **billingsmoore/LotsawaHouse-bo-en**.

Two T5-small models were trained for 5 epochs using the same dataset. One model ('baseline') was trained with no continued pretraining.

The second model ('pretrained') was first trained for 3 epochs using continued unsupervised pretraining on the 'train' split of the data, then finetuned for 5 epochs in the same way as the 'baseline' model.

The models were evaluated using [BLEU](https://en.wikipedia.org/wiki/BLEU), [chrF](https://machinetranslate.org/chrF), and [TER](https://machinetranslate.org/ter) scores.

## Results

### Results After 1 Epoch

Model | BLEU | ChrF | TER
------|------|------|-----
Baseline| 3.406000|	13.485600|	155.622000
Pretrained | 5.845900|	17.796200|	108.549300

### Results After 3 Epochs

Model | BLEU | ChrF | TER
------|------|------|-----
Baseline| 9.826900|	22.381300|	101.633600
Pretrained | 10.429200|	22.245400|	96.693400

### Results After 5 Epochs

Model | BLEU | ChrF | TER
------|------|------|-----
Baseline| 11.597400	| 24.264600 |99.973700
Pretrained | 12.175600 | 24.200800 | 93.909700

## Discussion

While the pretrained model outperforms the baseline model initially, the baseline model mostly catches up over time, at least superficially, even scoring slightly higher with respect to ChrF.

The pretrained model continues to be better as measured by BLEU and TER, though, and while the differences appear small, proportionally they are substantial. BLEU is increased by 5% and TER is reduced (improved) by 6%.

This does, however, require additional epochs of training, which may not be desirable. But it is worth noting that almost all of the benefit (in terms of reduced training loss) of the unsupervised pretraining occured not just in the first epoch but in the first 1000 training steps. This seems to imply that one epoch of pretraining would be more than sufficient.

## Citations

Alves, D. M., Pombal, J., Guerreiro, N. M., Martins, P. H., Alves, J., Farajian, A., ... & Martins, A. F. (2024). Tower: An open multilingual large language model for translation-related tasks. arXiv preprint arXiv:2402.17733.