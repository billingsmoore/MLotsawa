# MiniLM-bo

## Introduction

Texts are embedded using a Sentence Piece transformer model. However, these models are not typically trained to effectively handle Tibetan text. Thus, a custom model must be finetuned.

The model used for this is MiniLM (specifically **[sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)**) which has 33 million parameters (compare BERT-Base's 109 million parameters) and is pre-trained using a method known as knowledge distillation. Simply put, this process consists of training a "student" model to mimic the performance of a high quality "teacher" model. A set up based on this approach was used to finetune the model for this pipeline.

The dataset used for finetuning was **[billingsmoore/Aggregated-bo-en](https://huggingface.co/datasets/billingsmoore/Aggregated-bo-en)**. This dataset consists of Tibetan-English sentence pairs aggregated from a number of sources. Full details on this dataset are available on the model card on Hugging Face which can be found by clicking the previous link.

Before a model can be trained, a custom tokenizer first had to be trained in order to transform the Tibetan text into the numerical sequences that the embedding model expects as input. The tokenizer that comes with MiniLM can recognize some Tibetan characters, but this is not sufficient for our use case. Thus, a Sentence Piece tokenizer was trained on the parallel sentence dataset for usage with our model during finetuning and later usage of the model.

The teacher model was used to embed the English sentences from the sentence pairs. The Tibetan sentences were then paired with those teacher embeddings and the student model was trained to reproduce those embeddings using the Tibetan sentences as input.

The evaluation metric for this training was Mean Squared Error. Because the embeddings can be treated as coordinates in space, we can calculate the distance between the predicted embedding and the "correct" embedding from the teacher model. This distance, which could be positive or negative, is squared to account for the different possible sign and to weight evaluation so that smaller errors are considered more acceptable than larger errors during training. The final Mean Squared Error achieve by the student model was 0.174.

This model is available publically on Hugging Face as **[billingsmoore/minilm-bo](https://huggingface.co/billingsmoore/minilm-bo)**.

## Model Details

This is a [sentence-transformers](https://www.SBERT.net) model trained on the aggregated-bo-en dataset. It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more. It is intended primarily for usage with the Tibetan language.

### Model Description
- **Model Type:** Sentence Transformer
<!-- - **Base model:** [Unknown](https://huggingface.co/unknown) -->
- **Maximum Sequence Length:** 512 tokens
- **Output Dimensionality:** 384 dimensions
- **Similarity Function:** Cosine Similarity
- **Training Dataset:**
    - aggregated-bo-en
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/UKPLab/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 384, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("billingsmoore/minilm-bo")
# Run inference
sentences = [
    'He could do it, so he did.',
    'རེས་བྱེད་ཐུབ་པ་དེ་རེད། འོན་ཀྱང་། ཁོ་མོས་',
    'ཕྱི་སྟོང་པ་ཉིད་ཡོངས་སུ་དག་པ། ཕྱི་སྟོང་པ་ཉིད་ཡོངས་སུ་དག་པས། ཤེས་པ་པོ་ཡོངས་སུ་དག་པ་སྟེ། དེ་ལྟར་ན་ཤེས་པ་པོ་ཡོངས་སུ་དག་པ་དང་། ཕྱི་སྟོང་པ་ཉིད་ཡོངས་སུ་དག་པ་འདི་ལ་གཉིས་སུ་མྱེད་དེ་གཉིས་སུ་བྱར་མྱེད་སོ་སོ་མ་ཡིན་ཐ་མྱི་དད་དོ། །ཤེས་པ་པོ་ཡོངས་སུ་དག་པས།',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities.shape)
# [3, 3]
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

## Evaluation

### Metrics

#### Knowledge Distillation

* Dataset: `stsb-dev`
* Evaluated with [<code>MSEEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.MSEEvaluator)

| Metric           | Value       |
|:-----------------|:------------|
| **negative_mse** | **-0.1737** |

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### aggregated-bo-en

* Dataset: aggregated-bo-en
* Size: 878,004 training samples
* Columns: <code>tibetan</code> and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | tibetan                                                                            | label                                |
  |:--------|:-----------------------------------------------------------------------------------|:-------------------------------------|
  | type    | string                                                                             | list                                 |
  | details | <ul><li>min: 4 tokens</li><li>mean: 29.06 tokens</li><li>max: 373 tokens</li></ul> | <ul><li>size: 384 elements</li></ul> |
* Samples:
  | tibetan                                   | label                                                                                                                               |
  |:------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------|
  | <code>ཀི་ལོ་མི་ཊར་ ༤༧.༣༩</code>           | <code>[-0.026894396170973778, 0.07161899656057358, -0.06451261788606644, 0.004668479785323143, -0.13893075287342072, ...]</code>    |
  | <code>ཅ། ཁྱོད་དང་ང་།</code>               | <code>[-0.03711550310254097, 0.04723873734474182, 0.027722617611289024, 0.03208618983626366, 0.0021679026540368795, ...]</code>     |
  | <code>མཚོན་རྨ་གསོ་བ། དེ་བས་མང་། >></code> | <code>[0.016887372359633446, -0.004544022027403116, -0.000849854841362685, -0.046510301530361176, -0.05679721385240555, ...]</code> |
* Loss: [<code>MSELoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#mseloss)

### Evaluation Dataset

#### aggregated-bo-en

* Dataset: aggregated-bo-en
* Size: 878,004 evaluation samples
* Columns: <code>english</code>, <code>tibetan</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | english                                                                           | tibetan                                                                            | label                                |
  |:--------|:----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|:-------------------------------------|
  | type    | string                                                                            | string                                                                             | list                                 |
  | details | <ul><li>min: 3 tokens</li><li>mean: 22.2 tokens</li><li>max: 512 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 32.42 tokens</li><li>max: 487 tokens</li></ul> | <ul><li>size: 384 elements</li></ul> |
* Samples:
  | english                                                                | tibetan                                                                             | label                                                                                                                             |
  |:-----------------------------------------------------------------------|:------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------|
  | <code>East TN Children's Hospital.</code>                              | <code>ཤར་གངས་ཕྲུག་གི་གསས་ཁང་།</code>                                                | <code>[-0.05563941225409508, 0.09337888658046722, 0.01915512979030609, 0.02351493015885353, -0.09008331596851349, ...]</code>     |
  | <code>In this prayer, often called the "high priestly prayer of</code> | <code>སྡེ་ཚན་འདིའི་ནང་དུ་མང་། " མཁན་ཆེན་ཞི་བ་འཚོ། ཇོ་བོ་རྗེ་དཔལ་ལྡན་ཨ་ཏི་ཤ "</code> | <code>[0.033027056604623795, 0.013109864667057991, -0.051157161593437195, -0.07704736292362213, -0.04368748143315315, ...]</code> |
  | <code>Spoilers: Oh, I don't know.</code>                               | <code>ལ་མེད། ཤེས་ཀྱི་མེད། 아니오, 모르겠습니다.</code>                                       | <code>[0.008215248584747314, -0.02530045434832573, -0.029446149244904518, 0.04361790046095848, 0.05075978860259056, ...]</code>   |
* Loss: [<code>MSELoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#mseloss)

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: epoch
- `learning_rate`: 2e-05
- `num_train_epochs`: 25
- `warmup_ratio`: 0.1
- `save_safetensors`: False
- `auto_find_batch_size`: True

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: epoch
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 8
- `per_device_eval_batch_size`: 8
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 2e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0
- `num_train_epochs`: 25
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.1
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `save_safetensors`: False
- `save_on_each_node`: False
- `save_only_model`: False
- `restore_callback_states_from_checkpoint`: False
- `no_cuda`: False
- `use_cpu`: False
- `use_mps_device`: False
- `seed`: 42
- `data_seed`: None
- `jit_mode_eval`: False
- `use_ipex`: False
- `bf16`: False
- `fp16`: False
- `fp16_opt_level`: O1
- `half_precision_backend`: auto
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `local_rank`: 0
- `ddp_backend`: None
- `tpu_num_cores`: None
- `tpu_metrics_debug`: False
- `debug`: []
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_prefetch_factor`: None
- `past_index`: -1
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch
- `optim_args`: None
- `adafactor`: False
- `group_by_length`: False
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `skip_memory_metrics`: True
- `use_legacy_prediction_loop`: False
- `push_to_hub`: False
- `resume_from_checkpoint`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_private_repo`: None
- `hub_always_push`: False
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_inputs_for_metrics`: False
- `include_for_metrics`: []
- `eval_do_concat_batches`: True
- `fp16_backend`: auto
- `push_to_hub_model_id`: None
- `push_to_hub_organization`: None
- `mp_parameters`: 
- `auto_find_batch_size`: True
- `full_determinism`: False
- `torchdynamo`: None
- `ray_scope`: last
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `dispatch_batches`: None
- `split_batches`: None
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: False
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: False
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: proportional

</details>

### Framework Versions
- Python: 3.12.3
- Sentence Transformers: 3.3.1
- Transformers: 4.48.1
- PyTorch: 2.5.1+cu124
- Accelerate: 1.2.0
- Datasets: 3.1.0
- Tokenizers: 0.21.0

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

#### MSELoss
```bibtex
@inproceedings{reimers-2020-multilingual-sentence-bert,
    title = "Making Monolingual Sentence Embeddings Multilingual using Knowledge Distillation",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2020",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/2004.09813",
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->