# Hyperparameter Selection

For this project, only a small number of hyperparameters are relevant. Batch sizes both for training and evaluation were automated using the Transformers library in order to optimize for memory usage.

Of note are the optimizer, learning rate, and learning rate scheduling.

## Optimizer

The optimizer used was [Adafactor](https://paperswithcode.com/method/adafactor). Adafactor substantially reduces memory usage compared to the more popular Adam optimizer, which was essential for local training, and was designed and optimized specifically for translation tasks. 

[Anil, R., Gupta, V., Koren, T., & Singer, Y. (2019, September 11). Memory-efficient adaptive optimization. arXiv.org. https://doi.org/10.48550/arXiv.1901.11150 ](https://arxiv.org/abs/1901.11150)

Adafactor is also the optimizer that was used for the original training of the T5 model.

## Learning Rate

8 different learning rates were tested for 10,000 training steps. Some of these rates were sourced from suggestions.

The T5 model card suggests a learning rate of either 1e-4 or 3e-4, higher than the default learning rate of the Transformers Trainer class, 5e-5. The Huggingface Translation tutorial uses a learning rate of 2e-5.

For thoroughness, 5e-5 and 2e-2 were tested as extremes. Then, 3e-3 and 4e-4 were tested as small adjustments to the 3e-4 suggestion, whose performance appeared to be essentially a happy medium.

Finally, Adafactor was allowed to calculate its learning rate on its own. The learning rate used was: [TODO]

The results of these tests can be seen below.

[PUT-GRAPH-HERE]