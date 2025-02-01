# Hyperparameter Optimization for Translation Topic Modeling

*Nov 2024*

In addition to my previous posts using topic modeling as a tool for data mining in the translation dataset, topic modeling is also used to understand what content users frequently translate.

In my work on the translation training dataset I have developed and used **[easy_text_clustering]** which is aimed at providing extremely simple text clustering tools in as little code as possible. The currently used pipeline for topic modeling of user translations relies on **[BERTopic]** which provides a number of advantages over **easy_text_clustering** and is much more thoroughly developed. 

However, the **BERTopic** pipeline relies on human analysis to improve clustering results. **easy_text_clustering** allows for automating the optimization of both dimensionality reduction and clustering.

Rather than having to choose one library or the other, however, the two libraries can be readily used in conjunction.

**easy_text_clustering** allows for optimization to be done as a standalone process with the following code.

```python
from easy_text_clustering.optimizer import Optimizer

opt = Optimizer()

umap_args, hdbscan_args = opt.fit(texts)
```

**BERTopic** allows for individual pieces of its pipeline to be customized like so:

```python
umap_model = UMAP()
hdbscan_model = HDBSCAN()
topic_model = BERTopic(umap_model=umap_model,
                       hdbscan_model=hdbscan_model).fit(texts)
```

Thus, the following brief script can be used to combine their functionality for a hyperparameter optimized topic model.

```python
from bertopic import BERTopic
from sklearn.cluster import HDBSCAN
from umap import UMAP
from easy_text_clustering.optimizer import Optimizer
from datasets import load_dataset


texts = load_dataset('billingsmoore/text-clustering-example-data', split="train")['text'] # load example data

opt = Optimizer() # instantiate Optimizer object

umap_args, hdbscan_args = opt.fit(texts) # fit optimized hyperparameters

# define optimized models for BERTopic
umap_model = UMAP(**umap_args)
hdbscan_model = HDBSCAN(**hdbscan_args)

# define and fit BERTopic model
topic_model = BERTopic(umap_model=umap_model,
                       hdbscan_model=hdbscan_model).fit(texts)
```

## How It Works

The fit method for the Optimizer optimizes UMAP and HDBSCAN hyperparameters using Optuna, evaluates clustering performance, stores and returns the best parameters.

Optuna finds the best parameters using Bayesian optimization to maximize a metric. The metric used by easy_text_clustering is a composite score composed of *Silhouette Score*, *Calinski-Harabasz Index*, and *Davies-Bouldin Index*.

By default, 100 trials are run to find the optimal hyperparameters. To reduce computation time, underperforming trials pruned using *MedianPruner*.

Source code and full documentation for the Optimizer can be found on my GitHub.