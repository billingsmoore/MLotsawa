# Phonetic Tibetan to English Translation

The purpose of this file is to document the process of creating the model ['billingsmoore/phonetic-tibetan-to-english-translation'](https://huggingface.co/billingsmoore/phonetic-tibetan-to-english-translation).

The full model card, including instructions for both primary usage and downstream usage can be found at the link above. However, this model has been superceded by the model ['billingsmoore/tibetan-to-english-translation'](https://huggingface.co/billingsmoore/tibetan-to-english-translation) and it is recommended that you use that model rather than this one.

The section titles below can be clicked to see the associated Jupyter notebook.


## Table of Contents
1. [Introduction](#introduction)
2. [Architecture Selection](#architecture-selection-1)
3. [Size Selection](#size-selection-1)
4. [Hyperparameter Tuning](#hyperparameter-tuning-1)
5. [Final Model Training](#final-model-training-1)


## Introduction

This project is an attempt at creating user-friendly translation software to be used for translating from Classical Tibetan to English. The objective is to produce a tool which can assist (not replace!) human translators in the process of creating English language versions of the texts. 

The intended use case for this project is to be used locally on a reasonably priced computer of the kind that might be used by a non-specialist. The intended specifications for this imagined machine are 8 GB of RAM with no dedicated GPU but a CPU capable of the ONNX runtime. For example, an ideal product would be usable on a reasonably new MacBook Air or mid-price HP laptop.

Data for this project was taken from [Lotsawa House](lotsawahouse.org). The pre-trained model architecure used is Google's t5-large.

Each section below provides a brief explanation of the decisions made for data usage, architecture selection, and size selection. The heading for each section also links to a longer explanation for that phase of the project.

### [Data](https://huggingface.co/datasets/billingsmoore/phonetic-tibetan-to-english-translation-pairs)

[The dataset for this project can be found here.](https://huggingface.co/datasets/billingsmoore/phonetic-tibetan-to-english-translation-pairs)

This dataset used for this project consists of pairs of sentences or phrases. The first member of each pair is a sentence or phrase in Classical Tibetan. The second member is the English translation of the first.

The pairs are pulled from texts sourced from [Lotsawa House](lotsawahouse.org). There was an initial set of over 15 million pairs.

The architecture selection process utilized a random subset of 100,000 pairs. A randomized 20,000 of which were used for evaluation.

The model size selection process utilized a larger random subset of 1 million pairs and a separate set of 100,000 pairs for evaluation.

The hyperparameter tuning process utilized a random subset of 10 million pairs and a seperate subset of 100,000 pairs for evaluation.

##### Reference Text

For the sake of intuitive qualititative assessments of models, I use an excerpt, specifically the opening 'Refuge' section, from 'A Brief Amitabha Sleeping Practice' by Jamyang Khyentse Chökyi Lodrö. 

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


### [Architecture Selection](#architecture-selection-1)

Multiple typical model architectures have been tested for this project. First, a proof of concept model was produced using the architecture used in the Keras translation tutorial (henceforth, the 'Keras model'). Second, Facebook's No Language Left Behind model was tested and finetuned. Third, two larger models were tried and finetuned: Google's T5 and Facebook's Llama 2. In the architecture selection process, only the smallest version of each architecture was tested. Model translation results at this stage were assessed qualitatively. Each model was used to translate a sample text to assess general translation quality.

Ultimately, the T5 model was found to produce the most satisfactory results.

The best results from each model are show in the table below. Note that the original line breaks are preserved.

| Model Name              | Translation |
| ----------------------- | ----------- |
| Reference Translation    | ***In the Buddha, the Dharma and the Supreme Assembly***<br>***I take refuge until I attain enlightenment.***<br>***Through the merit of practising generosity and so on,***<br>***May I attain buddhahood for the benefit of all beings.***
| Keras Model             | ***the most powerful and abundant invoking the handsome<br>my own mind now i have arrived in their transferred before us after<br>the auspicious opportunity recalling the enlightened ladys rage and abundant and the<br>the outer and inner benefit to all other offerings***
| No Language Left Behind | ***[*See longer report in 'Docs/ArchitectureSelection.md']***
|  T5                     | ***the buddhas and bodhisattvas the dharma dharma and the supreme assembly***<br>***i take refuge in the bodhisattva bodhisattva***<br>***i offer to all my buddhas and bodhisattvas and so on***<br>***and grant us the buddhahood of all buddhas the attainment of buddhahood***
| Llama 2                 | ***I pray to you, the supreme deity***<br>***I am a disciple of the great Vajradhara and I have been entrusted with the Dharma by my guru***<br>***I am a dak gi jin sok gyip snam kyi***<br>***I rejoice in the glorious deeds of my guru***

### [Size Selection](#size-selection-1)

For this project, three model sizes were tried: small, base, and large. Each was trained for three epochs. The metric used for evaluation of these models was the BLEU score as implemented by sacreBLEU. Additionally, each model was used to produce a sample translation of the sample text previously used in the architecture selection process.

The results significantly favor the use of the 'large' model size.

Below is a summary table:

|Size     |Parameters  |BLEU  |Translation|
|---------|------------|------|-----------|
|Reference Translation| n/a        |n/a   | ***In the Buddha, the Dharma and the Supreme Assembly***<br>***I take refuge until I attain enlightenment.***<br>***Through the merit of practising generosity and so on,***<br>***May I attain buddhahood for the benefit of all beings.***|
|Small    |60 million  |17.982| ***buddd ch the dchochochoknam the buddddu d the dchochochoque***<br>***i take refuge until until changchub bardu c c chub bdudu to my i***<br>***through the dak dr dak jinsme lords and the rest***<br>***attain attain attainmentmentment attain attainmentmentment in the spontaneous attainment***|
|Base     |220 million |29.165|***in the presence of the buddha the dharma and the supreme assembly<br>until i reach enlightenment i take refuge in you<br>through the merit of practising generosity and so on<br>for the benefit of beings i will accomplish buddhahood for the sake of all beings***|
|Large    |770 million |56.14 |***all of these buddhas dharmas and supreme saghas including the buddha the dharma and<br>i take refuge until enlightenment is realized<br>through the merit of practising generosity and so on<br>for the benefit of all beings i shall attain buddhahood***|


### Hyperparameter Tuning

For this project, only a small number of hyperparameters are relevant. Batch sizes both for training and evaluation were automated using the Transformers library in order to optimize for memory usage.

Of note are the optimizer, learning rate, and learning rate scheduling.

The optimizer used was [Adafactor](https://paperswithcode.com/method/adafactor), which provides its own learning rate scheduling. This leaves only the initial learning rate to be decided upon.

Learning rate substantially impacted the initial training loss of the model with smaller rates producing smaller initial loss. However, the best initial values also seemed to increase rather than decrease over time, potentially because they begin in a local minimum that they cannot escape. 

Conversely, high learning rates have very poor initial losses, higher than the final loss from the last training epoch but decrease over time, suggesting they have careened out of the minimum discovered by previous training and are making their way back to it. 

Ultimately, the 3e-4 learning rate was chosen for final training.

### Final Model Training

This model was trained for 6 epochs on a set of 1 million sentence pairs, with an additional set of 100,000 sentence pairs used for evaluation. It was then trained for 1 additional epoch on a set of 10 million sentence pairs with a separate set of 100,000 sentence pairs for evaluation.

## Architecture Selection

Multiple typical model architectures have been tested for this project. First, a proof of concept model was produced using the architecture used in the Keras translation tutorial (henceforth, the 'Keras model'). Second, Facebook's No Language Left Behind model was tested and finetuned. Third, two larger models were tried and finetuned: Google's T5 and Facebook's Llama 2. In the architecture selection process, only the smallest version of each architecture was tested.

Ultimately, the T5 model was found to produce the most satisfactory results. In fact, it was the only architecture which produced something like a usable translation.

The notebooks used to train/fine-tune and test each model can be found in the 'notebooks' folder of this repository. Each set of notebooks is in the folder named for the architecture used. 

Model translation results at this stage were assessed qualitatively. That is, no specific quantitative metric was used to assess model performance. Instead, each model was used to translate a sample text to assess general translation quality. During training, the evaluation metrics built in to the associated libraries or suggested by the mentioned tutorials/cookbooks were used, but these metrics did not impact the final selection of an architecture.

The reason for this approach is that translation metrics are often based on a sort of 'similarity' between two strings of texts. That is, if a generated translation is identical to the provided translation it gets the best score, and if it is entirely different it get the worst score. This approach is well-suited to corpi of texts where phrasings and nomenclature are well established and uniform (i.e. legal documents, textbooks). However, the Tibetan Buddhist corpus as it exists in English is not like this.

Translators of Tibetan texts are often working from the perspective of a particular interpretive tradition and are basing their translations not on established jargon but instead on English phrasings that best approximate the meaning of the Tibetan as they (or their teacher) understand it. This depiction is not meant to be derogatory! Religious texts, especially those from a tradition like Tibetan Buddhism which is diverse both in its texts but also in its interpretations of those texts, can not be translated in any other way! Translators of this tradition frequently preface their work with an explanation of this state of affairs and go out of their way to make clear what sorts of decisions they have made in making their translations and why they made those decisions the way that they did.

However, this presents a real obstacle to machine translation. The English corpus is replete with idiosyncratic translation, preservation of Tibetan technical terms, preservation of Sanskrit technical terms, intentional rephrasings, etc. which make straightforward similarity and immensely poor means of comparing translations. Thus, there is no good solution, at this point, other than simply having a human look at a sample translation and determine if it makes sense semantically, something the machine can not do on its own.

The best results from each model are show in the table below. Note that the original line breaks are preserved.

| Model Name              | Translation |
| ----------------------- | ----------- |
| Original Translation    | ***In the Buddha, the Dharma and the Supreme Assembly***<br>***I take refuge until I attain enlightenment.***<br>***Through the merit of practising generosity and so on,***<br>***May I attain buddhahood for the benefit of all beings.***
| Keras Model             | ***the most powerful and abundant invoking the handsome<br>my own mind now i have arrived in their transferred before us after<br>the auspicious opportunity recalling the enlightened ladys rage and abundant and the<br>the outer and inner benefit to all other offerings***
| No Language Left Behind | ***[*See below]***
|  T5                     | ***the buddhas and bodhisattvas the dharma dharma and the supreme assembly***<br>***i take refuge in the bodhisattva bodhisattva***<br>***i offer to all my buddhas and bodhisattvas and so on***<br>***and grant us the buddhahood of all buddhas the attainment of buddhahood***
| Llama 2                 | ***I pray to you, the supreme deity***<br>***I am a disciple of the great Vajradhara and I have been entrusted with the Dharma by my guru***<br>***I am a dak gi jin sok gyip snam kyi***<br>***I rejoice in the glorious deeds of my guru***

### [Keras Model](/Notebooks/Models/PhoneticTibetanToEnglishTranslation/arch-selection/keras/proof-of-concept-modeling.ipynb)

 The proof of concept model was produced following using the architecture used in the Keras translation tutorial. This architecture is similar to that suggested by Phillip Koehn in 'Neural Machine Translation', his 2020 textbook on the subject. A full description of this model is below:

![Keras Model Architecture](readme-assets/phonetic/keras-arch.png?raw=true "Keras Model Architecture")

Training this model produced the following results where 'Loss' is the Sparse Categorical Entropy loss function:

![Keras Model Results](readme-assets/phonetic/keras-results.png?raw=true "Keras Model Results")

Unfortunately, when tested on the 'Amitabha' text, it produces the following nonsense translation:

***咀 ngen barch la iu sol 咀 om 《 kyewa gyalp khyer***

***咀 嚼 《 kyewa denpa 》r sa ap***

***咀 嚼 《 kyewa denpa 》r sa ap***

**咀 嚼 《 kyewa denpa 》r sa ap**

This is not ideal. However, 100,000 samples is an extremely small sample for training from scratch. Another iteration of this model trained on some 15 million data samples (less well documented, but still sourced from Lotsawa House) produced the following translation:

***the most powerful and abundant invoking the handsome***

***my own mind now i have arrived in their transferred before us  after***

***the auspicious opportunity recalling the enlightened ladys rage and abundant   and the***

***the outer and inner benefit to all other offerings***

This is still unacceptably poor, but is at least recognizably English. Thus, the proof-of-concept model has done its job.

### [No Language Left Behind](/Notebooks/Models/PhoneticTibetanToEnglishTranslation/arch-selection/nllb/nllb-finetuning.ipynb)

#### Pretrained Translations

Classical Tibetan is a low resource language. No Language Left Behind is a translation model that Facebook created to cater to low resource languages, and it supports Tibetan out of the box! This seems like it should be an easy giant step forward.

Unfortunately, at the time of writing, NLLB seems to be out of step with it's own documentation and it seems like functional translation is not viable at present. However, in previous testing, I was able to use it, following the approach used by [Digital Tibetan](https://digitaltibetan.github.io/DigitalTibetan/docs/tibetan_machine_translation.html), to work with a section of the Longchen Nyingtik Ngondro liturgy entitled "The Excellent Path to Omniscience The Preliminary Practice of the Heart-Essence of the Vast Expanse (Longchen Nyingtik) from the Great Perfection" arranged by Dodrupchen Jikme Trinle Özer. The full text is available at [Lotsawa House here](https://www.lotsawahouse.org/tibetan-masters/dodrupchen-I/longchen-nyingtik-ngondro). However, it is important to note that within the tradition, the full text is not to be read without the supervision or advice of a teacher.

##### Single Line Translation

I first tested a single line of this text.

In the Tibetan script:

***འོད་འཕྲོས་རྒྱལ་བ་སྲས་བཅས་མཆོད་པས་མཉེས། །***

Transliterated:

***ö trö gyalwa sé ché chöpé nyé***

Translated:

***Light streams out, making offerings to the buddhas and bodhisattvas, and pleasing them.***

NLLB translates the Tibetan script as:

***The Son of Man, the Son of the Light, is pleased with sacrifice.***

which is semantically similar to the original but obviously quite poor. The reference to "buddhas and bodhisattvas" is changed to "The Son of Man, the Son of the Light", perhaps a result of another set of religious texts in the training set. The reference to "offerings" in the original is changed to a reference to a "sacrifice" and problematic substitution to say the least.

If we use the transliterated version, NLLB returns the following:

***I'm very happy with the way it turned out.***

which is straightforwardly poor.


##### Longer Text Translation

It's possible that the translations improve which greater context. To test this I've provided below larger samples for translation. These samples come from the same portion of the same text but I've used the entire section, entitled "The Blessing of the Speech".

The section of text is as follows:

Tibetan:

***ཨོཾ་ཨཱཿཧཱུྂ། ལྕེ་དབང་རྂ་ཡིག་ལས་བྱུང་མེས་བསྲེགས་ནས། །***

***འོད་དམར་རྣམ་པའི་རྡོ་རྗེ་རྩེ་གསུམ་སྦུབས། །***

***ཨཱ་ལི་ཀཱ་ལིའི་མཐའ་སྐོར་རྟེན་འབྲེལ་སྙིང་། །***

***མུ་ཏིག་ཕྲེང་བ་ལྟ་བུའི་ཡིག་འབྲུ་ལས། །***

***འོད་འཕྲོས་རྒྱལ་བ་སྲས་བཅས་མཆོད་པས་མཉེས། །***

***སླར་འདུས་ངག་སྒྲིབ་དག་ནས་གསུང་རྡོ་རྗེའི། །***

***བྱིན་རླབས་དངོས་གྲུབ་ཐམས་ཅད་ཐོབ་པར་འགྱུར། །***

Transliterated:

***om ah hung ché wang ram yik lé jung mé sek né***

***ö mar nampé dorjé tsesum bub***

***ali kali takor tendrel nying***

***mutik trengwa tabü yikdru lé***

***ö trö gyalwa sé ché chöpé nyé***

***lar dü ngak drib dak né sung dorjé***

***jinlab ngödrub tamché tobpar gyur***

Translated:

***Oṃ āḥ hūṃ! From the syllable raṃ (in my speech centre) arises fire, consuming my tongue,***

***Which is transformed into a three-spoked vajra of red light.***

***In its centre are the vowels and consonants, and around them the mantra of ‘The Essence of Interdependent Origination’***

***Their syllables are like strings of pearls. From them,***

***Light streams out, making offerings to the buddhas and bodhisattvas, and pleasing them.***

***As it converges back, all the obscurations of my speech are purified, and***

***I obtain all the blessings and siddhis of vajra speech.***


The Tibetan script is translated as:

***"The letter O'Bohemian was burned with fire, burned with red-colored stones, burned with the heart of the Alkali siege, and the letter like the Book of Mormon was read with joy, and the Son of Light and Victory was delighted with the sacrifice."***

The transliteration is translated as:

***'The name of the child is called the "trengwa tabü yikdru" by the name of the child is called the "chewable" by the name of the child, the "drub" by the name of the child.'***



We can see that neither translation appears to have improved. However, there is a point of interest in the translation from the Tibetan script. Note the reference to the Book of Mormon, which may give us a clue to the training set for this model. It is likely that Meta had access to a variety of training materials that are commonly translated into a huge number of languages, among which is undoubtedly a sizeable portion of materials from the LDS Church, which evangelized globally. This presents a particular concern, because we want to avoid translations that bring with themselves a great deal of conceptual, particularly theological, baggage (i.e. the substitution of 'sacrifice' for 'offering' above).

Below, I've translated the passage in Tibetan script line by line. Note that the translation changes significantly. The first line is notably messy and the Book of Mormon is no longer mentioned, but there is still a lot of room for improvement.


 ***'Oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, what the word of the word of the word of the word of the word of the word of the word of the word of the word of the word of the word of the word of the word of the word of the word of the word of the word of the word of the word of the word of the word of the word of the word of the word of the word of the word of the word of the word of the word of the word of the word of the word is.***

 ***Three corners of a bright red-colored stone were lit.***
 
 ***The siege of Alicante was celebrated in the heart of the city.***

 ***Letters like the letter "m" are:***

 ***The light of the world is pleased with sacrifices, even the son of the conqueror.***

 ***Again, the words of the silent silent stone were heard.***

 ***Blessings will be given to all that is accomplished.***

 Still, we are getting results that are semantically relevant to the source text in a way that the Keras model was unable to achieve so there is hope for finetuning this model.

 #### Finetuning Results

 Unfortunately, substantial improvements were not made. Loss, once again Sparse Categorical Cross Entropy, only improved for two epochs of training, even with the larger dataset mentioned above.  
 
 The longer text translated above is translated again below:

***with***

***although the king and ministers had already been seated on the lotus***

***the sun is transformed into a dazzling vajra and his consort dissolves into***

***in its centre are the vowels and consonants and around them the mantra of the essence***

***their syllables are like strings of pearls on which are***

***hungry hungry victorious ones sweetheart***

***once again i arise in the form of the vajra speech the obscuring nails and***

***i obtain all the blessings of accomplishment and the twofold accumulation***

There is clear improvement in this translation, but not enough to make this a viable model. Additionally, these results are not representative of actual performance because the larger dataset, again, poorly documented, almost certainly contains the exact text we are translating here. Thus, it seems necessary to look to a larger model.

### [T5](/Notebooks/Models/PhoneticTibetanToEnglishTranslation/arch-selection/t5/t5-small-finetuning.ipynb)

According to the Hugging Face model card for the T5 model:

>"With T5, we propose reframing all NLP tasks into a unified text-to-text-format where the input and output are always text strings, in contrast to BERT-style models that can only output either a class label or a span of the input. Our text-to-text framework allows us to use the same model, loss function, and hyperparameters on any NLP task."

An admirable goal! The smallest T5 model, and the one initially used here, is T5-small with 60 million parameters. The same size as the NLLB model used above.

T5 has a disadvantage against NLLB, it does not, to my knowledge, support Tibetan out of the box. However, it was purpose built to be finetuned for translation tasks!

#### Finetuning

This model was finetuned using the 100,000 pair dataset for 30 epochs. This time evaluation was done by calculating the BLEU score of the predicted translations. 

 BLEU (BiLingual Evaluation Understudy) is a standard (if not uncontroversial) metric in machine translation. BLEU gives each prediction a score between 0 and 1, where 0 means the model's predicted translation is nothing like the correct translation and 1 means the predicited translation is identical to the correct one. [You can read more about the specifics here.](https://en.wikipedia.org/wiki/BLEU)

The training loss is plotted below.

![T5 Small Model Results](readme-assets/phonetic/t5-small-loss.png?raw=true "T5 Small Model Results")

You can see that loss drops substantially then levels off just before 20,000 training steps, which is just before reaching epoch 20.

We can see this by returning to our original assessment text. As a reminder:

Transliterated Tibetan:

***sangye ch dang tsok kyi chok nam la***

***changchub bardu dak ni kyab su chi***

***dak gi jin sok gyip snam kyi***

***dro la pen chir sangye drubpar shok***

English:

***In the Buddha the Dharma and the Supreme Assembly***

***I take refuge until I attain enlightenment***

***Through the merit of practising generosity and so on***

***May I attain buddhahood for the benefit of all beings***

Below are the translations after 10, 20, and 30 training epochs.

##### Epoch 10

***the buddhis dharma dharma and dharma kyichok nam la***

***i offer to you i pray***

***i offer to all my buddhas and bodhisattvas and so on***

***grant us the buddhahood of all our wishes and wishes so that we may attain buddhahood***

##### Epoch 20

***the buddhas and bodhisattvas the dharma dharma and the supreme assembly***

***i take refuge in the bodhisattva bodhisattva***

***i offer to all my buddhas and bodhisattvas and so on***

***and grant us the buddhahood of all buddhas the attainment of buddhahood***


##### Epoch 30

***the buddhas dharma dharma dharma and tsok kyichok nam la***

***i take refuge in the bodhisattva bodhisattva***

***i offer to you the buddhas and their heirs and so on***

***and grant us the buddhahood to accomplish enlightenment***

#### Assessment

Clearly, the quality of the results peaked at epoch 20. This translation does still leave something to be desired but is an extremely exciting result! With the small dataset of 100k samples, for only 20 training epochs, using the smallest model (!), T5 substantially outperforms the other models.

### [Llama 2](/Notebooks/Models/PhoneticTibetanToEnglishTranslation/arch-selection/llama2/llama2-finetuning.ipynb)

Llama 2 is a large language model developed by Facebook. It is the second Llama model that they have produced. The smallest size and the size used here is the 7B version, which has 7 billion trainable parameters, far, far more than the other models thus far tested. This places Llama 2 into a unique position. It is possible that the additional parameters will make it substantially more performant but it is certain that it will make training a much longer and more computationally expensive process. Additionally, the model is too large to be usable on many low or mid-tier commercial computers limiting its usefulness to many translators. As such, the bar is high for this to be the model that we proceed with.

To facilitate training such a large model, the QLoRA technique was used. [You can read more about how this works here.](https://github.com/artidoro/qlora)

Working with Llama (or any other LLM) also introduces an additional variable: prompt selection. The input to a model which is prepared to accept and follow instructions should include an instruction. What the exact format of that instruction should be is not obvious. I have tested two possibilities: 

The "T5 prompt": "Translate from Tibetan to English: \<Tibetan text\> \n \<English text\> [found here.](https://huggingface.co/learn/nlp-course/chapter7/4?fw=pt)

The "Reddit prompt": "Tibetan: \<Tibetan Text\> English: \<English text\>" [found here.](https://www.reddit.com/r/LocalLLaMA/comments/169ae0e/comment/jz1c51y/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)

The "Reddit prompt" asserts that this prompt was found to be the most effective for training LLM's for translation but I have not been able to find a citation for this claim thus far. A responder suggests the source to be [Yamada (2023)](https://arxiv.org/abs/2308.01391) but this is not correct. Yamada instead explores the use of larger contexts for translation tasks on models that already provide at least somewhat effective translation, which is not the case for us.

To select a prompt structure for further training, I first trained the model for a single epoch on the "T5 prompt" and the "Reddit prompt". You can see the results below.

I've restated our sample text for reference:

Transliterated Tibetan:

***sangye ch dang tsok kyi chok nam la***

***changchub bardu dak ni kyab su chi***

***dak gi jin sok gyip snam kyi***

***dro la pen chir sangye drubpar shok***

English:

***In the Buddha the Dharma and the Supreme Assembly***

***I take refuge until I attain enlightenment***

***Through the merit of practising generosity and so on***

***May I attain buddhahood for the benefit of all beings***

You can see in the chart below that it seems like training loss is substantially better using the "T5 prompt" than when using the "Reddit Prompt"

![Llama Single Epoch Model Results](readme-assets/phonetic/llama-prompt-comparison.png?raw=true "Llama Single Epoch Model Results")

However, as we will see below, this does not necessarily mean a better translation model.


#### T5 Prompt Model Epoch 1

The model trained for a single epoch using the "T5 prompt" produces the following translation:

***nobody can be your refuge like your own mind***

***nobody is more kind than you***

***trp tsal tnpa dang yerm shokpar gyur chik tu solwa debpa dang rgyal po yi kyi gsal***

***nobody can do it for you  You have to do it yourself***

This is, of course, not a very good translation, being essentially unrelated to the correct translation. The third line is not even recognizably Engish.

#### Reddit Prompt Model Epoch 1

The model trained for a single epoch using the "Reddit prompt" produces the following translation:

***I pray to you, the supreme deity***

***I am a disciple of the great Vajradhara and I have been entrusted with the Dharma by my guru***

***I am a dak gi jin sok gyip snam kyi***

***I rejoice in the glorious deeds of my guru***

This translation is somewhat better, although interestingly, the third line still seems to be causing problems. The decision was made to use the "Reddit prompt" moving forward.

#### Reddit Prompt Model Epoch 3

In the chart below, you can see that training loss continues to improve with additional training, but what we've seen so far should lead us to be skeptical of that as a meaningful metric.

![Llama Three Epoch Model Results](readme-assets/phonetic/llama-3-epochs.png?raw=true "Llama Three Epoch Model Results")

The model trained for additional epochs using the "Reddit prompt" produces the following translation:

***May all your prayers be fulfilled***

***The vajra masters are my guardians***

***Awakening***

***I take refuge in the Buddha***

This is not much better. The third line is now in English but does not approximate the correct translation.

Note that the Llama model was trained for far fewer epochs than the T5 model. This is somewhat unfair, however, the amount of time taken to train Llama was substantially longer. Each epoch for Llama took approximately 24 hours, compared to the total training time of the T5 model being only about 8 hours.

The additional time taken to train the Llama model for additional epochs does not at this point seem justifiable.

## [Size Selection](/Notebooks/Models/PhoneticTibetanToEnglishTranslation/size-selection/t5-sizes-finetuning.ipynb)

### Introduction

An important decision for this project was to select the size of model to be trained for the final product. The size of the model is determined by the number of parameters in the model and effects the amount of memory necessary to run the model as well as how long it takes for the model to produce its output.

Larger models can be more effective at learning from large scale datasets and, in general, can be expected to be 'better' than smaller models for a given use case. However, larger models can also be more prone to 'overfitting', learning the 'accidental' patterns in data that are not useful for prediction.

The T5 model family come in five sizes: small, base, large, XL, and XXL. XL and XXL were previous known as 3B and 11B respectively, for the number of parameters in the model. The full details of the model can be found on [Huggingface](https://huggingface.co/docs/transformers/model_doc/t5).

For this project, only three sizes were tried: small, base, and large. The reason for this is that the intended usage of this model is to be run locally on mid-range commodity hardware by non-technical translators. Therefore, models must be relatively small.

To select the size of model to be trained for the final product, each size of model was trained for three epochs. The metric used for evaluation of these models was the BLEU score as implemented by sacreBLEU. Additionally, each model was used to produce a sample translation of the sample text previously used in the architecture selection process.

### Dataset

To account for the possibility that the larger sizes of model may quickly overfit to a relatively small dataset, a larger sample was used than in the architecture selection process. 

For this phase, a random sample of 1 million text pairs was selected from the full dataset. Additionally, a seperate set of 100 thousand pairs were sampled to be used for evaluation.

### Training Results

Graphs results of training can be seen below:


![Training Loss](readme-assets/phonetic/size-select-train-loss.png?raw=true "Training Loss")

![Eval Loss](readme-assets/phonetic/size-select-eval-loss.png?raw=true "Eval Loss")

![Eval BLEU](readme-assets/phonetic/size-select-eval-bleu.png?raw=true "Eval BLEU")

You can see that each model follows a similar trajectory over the course of training. As expected, the large models quantitatively outperform their smaller counterparts by a significant amount. 

Below is a summary table which includes final BLEU scores as well as training parameters and a sample translation:

|Size     |Parameters  |BLEU  |Translation|
|---------|------------|------|-----------|
|Reference| n/a        |n/a   | ***In the Buddha, the Dharma and the Supreme Assembly***<br>***I take refuge until I attain enlightenment.***<br>***Through the merit of practising generosity and so on,***<br>***May I attain buddhahood for the benefit of all beings.***|
|Small    |60 million  |17.982| ***buddd ch the dchochochoknam the buddddu d the dchochochoque***<br>***i take refuge until until changchub bardu c c chub bdudu to my i***<br>***through the dak dr dak jinsme lords and the rest***<br>***attain attain attainmentmentment attain attainmentmentment in the spontaneous attainment***|
|Base     |220 million |29.165|***in the presence of the buddha the dharma and the supreme assembly<br>until i reach enlightenment i take refuge in you<br>through the merit of practising generosity and so on<br>for the benefit of beings i will accomplish buddhahood for the sake of all beings***|
|Large    |770 million |56.14 |***all of these buddhas dharmas and supreme saghas including the buddha the dharma and<br>i take refuge until enlightenment is realized<br>through the merit of practising generosity and so on<br>for the benefit of all beings i shall attain buddhahood***|

Again, we can see that the larger models both dramatically outperform the 'small' model. However, the difference between the 'large' and 'base' sizes is not straightforwardly substantial.

## Hyperparameter Tuning

For this project, only a small number of hyperparameters are relevant. Batch sizes both for training and evaluation were automated using the Transformers library in order to optimize for memory usage.

Of note are the optimizer, learning rate, and learning rate scheduling.

### Optimizer

The optimizer used was [Adafactor](https://paperswithcode.com/method/adafactor). Adafactor substantially reduces memory usage compared to the more popular Adam optimizer, which was essential for local training, and was designed and optimized specifically for translation tasks. Adafactor is also the optimizer that was used for the original training of the T5 model. Further information can be found in the source below.

[Anil, R., Gupta, V., Koren, T., & Singer, Y. (2019, September 11). Memory-efficient adaptive optimization. arXiv.org. https://doi.org/10.48550/arXiv.1901.11150 ](https://arxiv.org/abs/1901.11150)



### Learning Rate

8 different learning rates were tested for 10,000 training steps. The learning rate that was selected for further training was 3e-4. The reason for this decision and the sources for the tested rates are explained below.

The T5 model card suggests a learning rate of either 1e-4 or 3e-4, higher than the default learning rate of the Transformers Trainer class, 5e-5. The Huggingface Translation tutorial uses a learning rate of 2e-5.

For thoroughness, 5e-5 and 2e-2 were tested as extremes. Then, 3e-3 and 4e-4 were tested as small adjustments to the 3e-4 suggestion, whose performance was in the middle of the two extremes.

The results of these tests can be seen below.

![Learning Rate Loss](readme-assets/phonetic/lr-results.png?raw=true "Learning Rate Loss")

Learning rate substantially impacted the initial training loss of the model with smaller rates producing smaller initial loss. However, the best initial values also seemed to increase rather than decrease over time, potentially because they begin in a local minimum that they cannot escape. 

Conversely, high learning rates have very poor initial losses, higher than the final loss from the last training epoch but decrease over time, suggesting they have careened out of the minimum discovered by previous training and are making their way back to it. 

Ultimately, the 3e-4 learning rate was chosen for final training.

## [Final Model Training](/Notebooks/Models/PhoneticTibetanToEnglishTranslation/final-phonetic-model-training/t5-finetuning.ipynb)

The architecture that was used for model training was Google's T5. The size used was the 'Large' model with 770 million parameters. The original model can be found on Huggingface as google-t5/t5-large.

This model was trained for 6 epochs on a set of 1 million sentence pairs, with an additional set of 100,000 sentence pairs used for evaluation. It was then trained for 1 additional epoch on a set of 10 million sentence pairs with a separate set of 100,000 sentence pairs for evaluation.

### Training Results

The final BLEU score achieved was 83.4374. The full results of training can be seen below.

![Loss](readme-assets/phonetic/final-losses.png?raw=true "Loss")

![BLEU](readme-assets/phonetic/final-bleu.png?raw=true "BLEU")



### Example Translations

#### 'A Brief Amitabha Sleeping Practive

For an example translation, we can use again 'A Brief Amitabha Sleeping Practice' by Jamyang Khyentse Chökyi Lodrö. However, this time, I've provided a full translation of the text side by side with Adam Pearcey's original translation.

| Pearcey | MLotsawa |
|---------|----------|
|***In the Buddha the Dharma and the Supreme Assembly<br>I take refuge until I attain enlightenment<br>Through the merit of practising generosity and so on<br>May I attain buddhahood for the benefit of all beings***|***in the buddha the dharma and the supreme assembly<br>i take refuge till enlightenment is realized<br>through the merit of practising generosity and so on<br>may i attain buddhahood for the benefit of all beings***|
|***You are the protectors of all beings every single one<br>You are the deities who remorselessly destroy the mras and their forces<br>You who know all things just as they are in their true nature<br>Enlightened ones with your retinues come now to this place***|***you are the protector of all beings without exception<br>are the deities who remorselessly destroy the mras and their forces<br>you who know all things just as they are in their true nature<br>i pray that the buddhas with their retinues come now to this place***|
|***To all the buddhas the lions of the human race<br>In all directions of the universe through past and present and future<br>To every single one of you I bow in homage<br>Devotion fills my body speech and mind***|***to all the buddhas the lions of the human race<br>in all directions of the universe through past and present and future<br>in as many worlds as there are in the ten directions<br>devotion fills my body speech and mind***|
|***Through the power of this prayer aspiring to Good Action<br>All the victorious ones appear vivid here before my mind<br>And I multiply my body as many times as atoms in the universe<br>Each one bowing in prostration to all the buddhas***|***all triumphant buddhas rise vividly to mind<br>all the victorious ones appear vivid here before my mind<br>and i multiply my body as many times as atoms in the universe<br>each one bowing in prostration to all the buddhas***|
|***In every atom preside as many buddhas as there are atoms<br>And around them all their bodhisattva heirs<br>And so I imagine them filling<br>Completely the entire space of reality***|***in every atom preside as many buddhas as there are atoms<br>and around them all their bodhisattva heirs<br>and so i imagine them filling<br>of the infinite womb of all things***|
|***Saluting them with an endless ocean of praise<br>With the sounds of an ocean of different melodies<br>I sing of the buddhas noble qualities<br>And praise all those who have gone to perfect bliss***|***saluting them with an endless ocean of praise<br>with the sounds of an ocean of different melodies<br>i sing of the buddhas noble qualities<br>and praise all those who have gone to perfect bliss***|
|***To every buddha I make offerings<br>Of the loveliest flowers of beautiful garlands<br>Of music and perfumed ointments the best of parasols<br>The brightest lamps and finest incense***|***to every buddha i make offerings<br>of the loveliest flowers of beautiful garlands<br>the best lamps and sacred incense<br>arranged in perfect symmetry***|
|***To every buddha I make offerings<br>Exquisite garments and the most fragrant scents<br>Powdered incense heaped as high as Mount Meru<br>Arranged in perfect symmetry***|***to every buddha i make offerings<br>exquisite garments and the most fragrant scents<br>all these in special exquisite arrays<br>arranged in perfect symmetry***|
|***Then the vast and unsurpassable offerings<br>Inspired by my devotion to all the buddhas and<br>Moved by the power of my faith in Good Actions<br>I prostrate and offer to all you victorious ones***|***then the vast and unsurpassable offerings<br>inspired by my devotion to all the buddhas and<br>moved by the power of my faith in good actions<br>i prostrate and offer to all you victorious ones***|
|***Whatever negative acts I have committed<br>While driven by desire hatred and ignorance<br>With my body my speech and also with my mind<br>Before you I confess and purify each and every one***|***whatever negative acts i have committed<br>while driven by desire hatred and ignorance<br>with my body my speech and also with my mind<br>before you i confess and purify each and every one***|
|***With a heart full of delight I rejoice at all the merits<br>Of buddhas and bodhisattvas<br>Pratyekabuddhas those in training and the arhats beyond training<br>And every living being throughout the entire universe***|***with a heart full of delight i rejoice at all the merits<br>of buddhas and bodhisattvas<br>the goodness of those on paths of training or the path of no further training<br>and every living being throughout the entire universe***|
|***You who are like beacons of light shining through the worlds<br>Who passed through the stages of enlightenment to attain buddhahood freedom from all attachment<br>I exhort you all of you protectors<br>Turn the unsurpassable wheel of Dharma***|***you who are like beacons of light shining through the worlds<br>then gradually gained enlightenment free from attachment<br>i exhort you all of you protectors<br>i ask you to set in motion the wheel of the highest doctrine***|
|***Joining my palms together I pray<br>To you who intend to pass into nirvana<br>Remain for aeons as many as the atoms in this world<br>And bring wellbeing and happiness to all living beings***|***joining my palms together i pray<br>to you who intend to pass into nirva<br>remain for aeons as many as the atoms in this world<br>and bring wellbeing and happiness to all living beings***|
|***What little virtue I have gathered through my homage<br>Through offering confession and rejoicing<br>Through exhortation and prayer all of it<br>I dedicate to the enlightenment of all beings<br>Bhagavn tathgata arhat complete and perfect buddha Amitbha to you I pay homage In you I take refuge***|***what little virtue i have gathered through my homage<br>through offering confession and rejoicing<br>through exhortation and prayerall of it<br>i dedicate towards all enlightenment<br>transcendent accomplished victor thusgone one foe destroyer<br>then beneath the bodhi tree you put the sages to flight<br>bhagavn tathgata arhat complete and perfect buddha protector amithba buddha of***|
|***The Buddha Amitbha Limitless Light is before me<br>From the syllable Hrih at his heart a second syllable emerges<br>Passes through his right nostril and enters my left nostril<br>From where it descends to the centre of my heart<br>It radiates light and rays of light<br>Which purify my misdeeds obscurations and habitual patterns<br>Then together with my exhalation of breath<br>It passes through my right nostril to enter<br>The conquerors left nostril and dissolve back into the Hrih<br>My own mind and the victorious ones wisdom mind<br>Merge indivisibly and I rest in a state beyond the ordinary mind***|***before me is amitbha<br>in his heart centre is<br>it passes through his right nostril<br>from where it descends to the centre of my heart<br>it radiates boundless light rays<br>which purify my misdeeds obscurations and habits<br>then together with my exhalation of breath<br>it emerges from my right nostril<br>entering the blessed one through his left nostril dissolves back into<br>the victors wisdom mind and my own mind are indivisible<br>i let be within this thoughtfree state***|