# MLotsawa

This project is an attempt at creating user-friendly translation software to be used for translating 
from Classical Tibetan to English. 

## Introduction

## Data

The dataset for this project can be found here: 
https://www.kaggle.com/datasets/billingsmoore/classical-tibetan-to-english-translation-dataset/data

This dataset consists of 100,000 pairs of sentences or phrases. The first member of each pair is a sentence or phrase in Classical Tibetan. The second member is the English translation of the first.

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


## Architectures Tested

Multiple typical model architectures have been tested. First, a proof of concept model was produced following using the architecture used in the Keras translation tutorial (henceforth, the 'Keras model'). Second, Facebook's No Language Left Behind model was tested and finetuned. Third, two larger models were tried and finetuned: Google's T5 and Facebook's Llama 2.

### Keras Model

 The proof of concept model was produced following using the architecture used in the Keras translation tutorial. This architecture is similar to that suggested by Phillip Koehn in 'Neural Machine Translation', his 2020 textbook on the subject. A full description of this model is below:

![Keras Model Architecture](/readme-assets/keras-arch.png?raw=true "Keras Model Architecture")

Training this model produced the following results where 'Loss' is the Sparse Categorical Entropy loss function:

![Keras Model Results](/readme-assets/keras-results.png?raw=true "Keras Model Results")

Unfortunately, when tested on the 'Amitabha' text, it produces the following nonsense translation:

***咀 ngen barch la iu sol 咀 om 《 kyewa gyalp khyer***

***咀 嚼 《 kyewa denpa 》r sa ap***

***咀 嚼 《 kyewa denpa 》r sa ap***

**咀 嚼 《 kyewa denpa 》r sa ap**

This is not ideal. However, 100,000 samples is an extremely small sample for training from scratch. Another iteration of this model trained on some 15 million data samples (less well documented, but still sourced from Lotsawa House) produced the following translation:

***the most powerful and abundant    invoking the handsome***

***my own mind now i have arrived in their transferred before us  after***

***the auspicious opportunity recalling the enlightened ladys rage and abundant   and the***

***the outer and inner benefit to all other offerings***

This is still unacceptably poor, but is at least recognizably English. Thus, the proof-of-concept model has done its job.

### No Language Left Behind

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

### T5

According to the Hugging Face model card for the T5 model:

>"With T5, we propose reframing all NLP tasks into a unified text-to-text-format where the input and output are always text strings, in contrast to BERT-style models that can only output either a class label or a span of the input. Our text-to-text framework allows us to use the same model, loss function, and hyperparameters on any NLP task."

An admirable goal! The smallest T5 model, and the one initially used here, is T5-small with 60 million parameters. The same size as the NLLB model used above.

T5 has a disadvantage against NLLB, it does not, to my knowledge, support Tibetan out of the box. However, it was purpose built to be finetuned for translation tasks!

#### Finetuning

This model was finetuned using the 100,000 pair dataset for 30 epochs. This time evaluation was done by calculating the BLEU score of the predicted translations. 

 BLEU (BiLingual Evaluation Understudy) is a standard (if not uncontroversial) metric in machine translation. BLEU gives each prediction a score between 0 and 1, where 0 means the model's predicted translation is nothing like the correct translation and 1 means the predicited translation is identical to the correct one. [You can read more about the specifics here.](https://en.wikipedia.org/wiki/BLEU)

The training loss is plotted below.

![T5 Small Model Results](/readme-assets/t5-small-loss.png?raw=true "T5 Small Model Results")

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

### Llama 2

# TODO