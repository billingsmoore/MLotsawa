# Effective Dialect Finetuning of Tibetan Automatic Speech Recognition Models

In [**Fine-Tuning a Multi-Dialect Speech Recognition Model for Tibetan Languages**](https://forum.openpecha.org/t/fine-tuning-a-multi-dialect-speech-recognition-model-for-tibetan-languages/180) it was demonstrated that, given a model previously trained on Utsang dialect, further finetuning the model on Amdo and Kham dialects improved performance on those dialects but at the cost of severely diminished performance on Utsang dialect material.

In this post I present two means of avoiding this problem by training on balanced finetuning data or by using Low Rank Adaptation (LoRA). I begin by reproducing the general problem of dialect specific performance. Then, I show that finetuning with an evenly balanced dataset can be a way of adding dialect performance to a model. Finally, I demonstrate that LoRA can provide improved performance on a particular dialect without the loss of performance on other dialects.

For each of the experiments described below, I have trained a "tiny" [**Whisper**](https://github.com/openai/whisper) model for 3 epochs on 15,000 training samples. Models were trained on a NVIDIA GeForce RTX 4050 Max-Q GPU with 6GB of VRAM.

The data used for training was audiobook data from [**openpecha/stt-training-data**](https://huggingface.co/datasets/openpecha/stt-training-data)

All models were evaluated using [**Character Error Rate (CER)**](https://huggingface.co/spaces/evaluate-metric/cer) and [**Word Error Rate (WER)**](https://en.wikipedia.org/wiki/Word_error_rate). The **WER** score is the macro-averaged score from the [`tibetan_wer`](https://pypi.org/project/tibetan-wer/) library. You can find more information about calculating WER for Tibetan and how this was implemented for `tibetan_wer` in [**Calculating Word Error Rate for Tibetan Automatic Speech Recognition**](https://forum.openpecha.org/t/calculating-word-error-rate-for-tibetan-automatic-speech-recognition/207). For both of these metrics, lower is better.

## Trade Offs in Training ASR Models With Multiple Dialects

A model trained on mixed training data outperforms a model trained on a single dialect with respect to the dialects that the single dialect model has not seen. However, the mixed training data model is not as performant on the dialect that the single dialect model was trained for. 

To demonstrate this, I trained a model on an equal mix of 5,000 samples from each dialect ('mixed' model) and a model on 15,000 samples of just Amdo dialect material ('single' model). You can see the results in the tables below.

Dialect | Mixed CER | Mixed WER| Single CER | Single WER
--------|-----------|----------|------------|-----------
Utsang| .42| .69  |.59 | 1.0|
Kham| .31 | .64 |.47 | .91
Amdo| .30| .64|.25|.55

You can see that the 'mixed' model outperforms the 'single' model except with respect to the Amdo dialect material.

In order to achieve the generalized performance of the 'mixed' model, as well as the superior single dialect performance of the 'single' model, ordinarily one would further finetune one model or the other to try to improve its performance.

## Adding Dialects With Balanced Finetuning

In **Fine-Tuning a Multi-Dialect Speech Recognition Model for Tibetan Languages**, a model that was previously trained for the Utsang dialect was finetuned on data from the Amdo and Kham dialects. The model's performance improved on the new dialects but worsened significantly on the the Utsang dialct.

One way of attempting to avoid this outcome is to finetune the 'single' model with a balanced mix of additional training data. I finetuned the 'single' model described above on the balanced set of 15,000 samples that was previously used to train the 'mixed' model. The results are shown in the table below. I have re-presented the original values for the 'single' model alongside the values for the finetuned ('FT') model.

Dialect | Single CER | Single WER| FT CER | FT WER
--------|-----------|----------|------------|-----------
Utsang|.59 | 1.0| .41 | .64
Kham| .47 | .91| .29|.60
Amdo| .25|.55 | .24|.51

These results show that the model now outperforms the 'single' model with respect to not only the added dialects, but has also improved slightly on the Amdo material.

## Improving Single Dialect Performance With Finetuning

If we have a balanced model, like the 'mixed' model above of the successfully finetuned model described in the previous section, we may still want to improve the performance of that model for a particular dialect. However, finetuning on a single dialect results in the problematic loss of generalized performance of the kind seen in **Fine-Tuning a Multi-Dialect Speech Recognition Model for Tibetan Languages**.

I finetuned the 'mixed' model described above using the 15,000 Amdo only training samples. You can see the evaluation results in the table below. I've re-presented the original 'mixed' model results as well as the finetuned ('FT') results.

Dialect | Mixed CER | Mixed WER| FT CER | FT WER
--------|-----------|----------|------------|-----------
Utsang| .42| .69  |.51|.86
Kham| .31 | .64 |.38|.79
Amdo| .30| .64|.22|.44
 

You can see that the model has improved with respect to the Amdo material, but that performance has worsened significantly for the other two dialects.

## Improving Single Dialect Performance With LoRA Finetuning

### A Brief Introduction to Low Rank Adaptation

**Low-Rank Adaptation (LoRA)** is a way to fine-tune large models more efficiently. Instead of changing the model’s full weight matrix, LoRA keeps it frozen and adds two small trainable matrices to learn an update

This greatly reduces training cost and memory use while keeping performance high.

When the model used, LoRA can be loaded or not. If used, it modifies the model's behavior; if not, the original model runs unchanged. This makes LoRA easy to swap in or out.

This means that one could train a LoRA for each dialect while preserving the performance of the base model. Each LoRA trains more quickly and with fewer compute resources than a full model. Thus, using LoRAs provides the benefits of finetuned models without loss of performance from the underlying model and for a lower cost than producing three separate full models.

### LoRA Performance Results

In order to improve performance on a single dialect, without losing performance on other dialects, a model can be finetuned user Low Rank Adaptation.

I finetuned the 'mixed' model using the same 15,000 Amdo only training samples as the previous example, but used LoRA. The results are shown in the table below.

Dialect | Mixed CER | Mixed WER| LoRA CER | LoRA WER
--------|-----------|----------|------------|-----------
Utsang| .42| .69  |.43|.71
Kham| .31 | .64 |.32|.68
Amdo| .30| .64|.28|.61

You can see that, as before, Amdo performance has improved while performance on the other two dialects has worsened. Both of these effects are lessened by LoRA, but additional finetuning could be performed to better approximate the non-LoRA results.