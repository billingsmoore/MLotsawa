# Hyperparameter Selection

For this project, only a small number of hyperparameters are relevant. Batch sizes both for training and evaluation were automated using the Transformers library in order to optimize for memory usage.

Of note are the optimizer, learning rate, and learning rate scheduling.

## Optimizer

The optimizer used was [Adafactor](https://paperswithcode.com/method/adafactor). Adafactor substantially reduces memory usage compared to the more popular Adam optimizer, which was essential for local training, and was designed and optimized specifically for translation tasks. Adafactor is also the optimizer that was used for the original training of the T5 model. Further information can be found in the source below.

[Anil, R., Gupta, V., Koren, T., & Singer, Y. (2019, September 11). Memory-efficient adaptive optimization. arXiv.org. https://doi.org/10.48550/arXiv.1901.11150 ](https://arxiv.org/abs/1901.11150)



## Learning Rate

8 different learning rates were tested for 10,000 training steps. The learning rate that was selected for further training was 2e-5. The reason for this decision and the sources for the tested rates are explained below.

The T5 model card suggests a learning rate of either 1e-4 or 3e-4, higher than the default learning rate of the Transformers Trainer class, 5e-5. The Huggingface Translation tutorial uses a learning rate of 2e-5.

For thoroughness, 5e-5 and 2e-2 were tested as extremes. Then, 3e-3 and 4e-4 were tested as small adjustments to the 3e-4 suggestion, whose performance was in the middle of the two extremes.

The results of these tests can be seen below.

![Learning Rate Loss](../readme-assets/lr-results.png?raw=true "Learning Rate Loss")

Learning rate substantially impacted the initial training loss of the model with smaller rates producing smaller initial loss. However, the best initial values also seemed to increase rather than decrease over time, potentially because they begin in a local minimum that they cannot escape. 

Conversely, high learning rates have very poor initial losses, higher than the final loss from the last training epoch but decrease over time, suggesting they have careened out of the minimum discovered by previous training and are making their way back to it.

Ultimately, the lower training should be the deciding factor, and thus the 2e-5 learning rate, which was suggested by the Huggingface tutorial was chosen for final training.