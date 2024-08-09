# MLotsawa

This project is an attempt at creating user-friendly translation software to be used for translating from Classical Tibetan to English. The objective is to produce a tool which can assist (not replace!) human translators in the process of creating English language versions of the texts. 

Data for this project was taken from [Lotsawa House](lotsawahouse.org). The pre-trained model architecure used is Google's T5.

## Introduction

**TO DO!**

## Data

The dataset for this project can be found here: 
https://www.kaggle.com/datasets/billingsmoore/classical-tibetan-to-english-translation-dataset/data

This dataset used for architecture selection consists of 100,000 pairs of sentences or phrases. The first member of each pair is a sentence or phrase in Classical Tibetan. The second member is the English translation of the first.

The pairs are pulled from texts sourced from Lotsawa House (lotsawahouse.org) and are offered under the same license as the original texts they provided.

The data is provided as a pickled pandas data frame which consists of a single column, 'translation'. Entries in that column are a python dictionary of the structure: {'bo': 'Tibetan text', 'en': 'English text'}.

The purpose of this structure is to mimic the OPUS books dataset which is popular in machine translation tutorials and therefore be easily usable with code that was originally intended to work with that dataset.

### Reference Text

For the sake of intuitive qualititative assessments of models, I will use an excerpt, specifically the opening 'Refuge' section from 'A Brief Amitabha Sleeping Practice' by Jamyang Khyentse Chökyi Lodrö. 

This text was selected because the translation does not preserve any Tibetan terms (which is sometimes intentionally done by translators for the sake of technical or philosophical specificity) but does include a handful of Sanksrit words (i.e. Buddha, Dharma) which have been adopted into English and are extremely common in the corpus. Additionally, it is not considered a restricted, or secret, text which is sometimes the case with important texts within the tradition.

The original Tibetan version of this text, transliterated into Latin script, reads:

***sangye chö dang tsok kyi chok nam la***

***changchub bardu dak ni kyab su chi***

***dak gi jin sok gyipé sönam kyi***

***dro la pen chir sangye drubpar shok***

which Adam Pearcey translates as:

***In the Buddha, the Dharma and the Supreme Assembly***

***I take refuge until I attain enlightenment.***

***Through the merit of practising generosity and so on,***

***May I attain buddhahood for the benefit of all beings.***


## [Architecture Selection]()

Multiple typical model architectures have been tested for this project. First, a proof of concept model was produced using the architecture used in the Keras translation tutorial (henceforth, the 'Keras model'). Second, Facebook's No Language Left Behind model was tested and finetuned. Third, two larger models were tried and finetuned: Google's T5 and Facebook's Llama 2. In the architecture selection process, only the smallest version of each architecture was tested. Model translation results at this stage were assessed qualitatively. Each model was used to translate a sample text to assess general translation quality.

Ultimately, the T5 model was found to produce the most satisfactory results.

The best results from each model are show in the table below. Note that the original line breaks are preserved.

| Model Name              | Translation |
| ----------------------- | ----------- |
| Original Translation    | ***In the Buddha, the Dharma and the Supreme Assembly***<br>***I take refuge until I attain enlightenment.***<br>***Through the merit of practising generosity and so on,***<br>***May I attain buddhahood for the benefit of all beings.***
| Keras Model             | ***the most powerful and abundant invoking the handsome<br>my own mind now i have arrived in their transferred before us after<br>the auspicious opportunity recalling the enlightened ladys rage and abundant and the<br>the outer and inner benefit to all other offerings***
| No Language Left Behind | ***[*See longer report in 'docs/ArchitectureSelection.md']***
|  T5                     | ***the buddhas and bodhisattvas the dharma dharma and the supreme assembly***<br>***i take refuge in the bodhisattva bodhisattva***<br>***i offer to all my buddhas and bodhisattvas and so on***<br>***and grant us the buddhahood of all buddhas the attainment of buddhahood***
| Llama 2                 | ***I pray to you, the supreme deity***<br>***I am a disciple of the great Vajradhara and I have been entrusted with the Dharma by my guru***<br>***I am a dak gi jin sok gyip snam kyi***<br>***I rejoice in the glorious deeds of my guru***

## Size Selection

For this project, three model sizes were tried: small, base, and large. Each was trained for three epochs. The metric used for evaluation of these models was the BLEU score as implemented by sacreBLEU. Additionally, each model was used to produce a sample translation of the sample text previously used in the architecture selection process.

The results significantly favor the use of the 'large' model size.

Below is a summary table:

|Size     |Parameters  |BLEU  |Translation|
|---------|------------|------|-----------|
|Reference| n/a        |n/a   | ***In the Buddha, the Dharma and the Supreme Assembly***<br>***I take refuge until I attain enlightenment.***<br>***Through the merit of practising generosity and so on,***<br>***May I attain buddhahood for the benefit of all beings.***|
|Small    |60 million  |17.982| ***buddd ch the dchochochoknam the buddddu d the dchochochoque***<br>***i take refuge until until changchub bardu c c chub bdudu to my i***<br>***through the dak dr dak jinsme lords and the rest***<br>***attain attain attainmentmentment attain attainmentmentment in the spontaneous attainment***|
|Base     |220 million |29.165|***in the presence of the buddha the dharma and the supreme assembly<br>until i reach enlightenment i take refuge in you<br>through the merit of practising generosity and so on<br>for the benefit of beings i will accomplish buddhahood for the sake of all beings***|
|Large    |770 million |56.14 |***all of these buddhas dharmas and supreme saghas including the buddha the dharma and<br>i take refuge until enlightenment is realized<br>through the merit of practising generosity and so on<br>for the benefit of all beings i shall attain buddhahood***|
