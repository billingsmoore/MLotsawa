# Architecture Selection

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

## Keras Model

 The proof of concept model was produced following using the architecture used in the Keras translation tutorial. This architecture is similar to that suggested by Phillip Koehn in 'Neural Machine Translation', his 2020 textbook on the subject. A full description of this model is below:

![Keras Model Architecture](../readme-assets/keras-arch.png?raw=true "Keras Model Architecture")

Training this model produced the following results where 'Loss' is the Sparse Categorical Entropy loss function:

![Keras Model Results](../readme-assets/keras-results.png?raw=true "Keras Model Results")

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

## No Language Left Behind

### Pretrained Translations

Classical Tibetan is a low resource language. No Language Left Behind is a translation model that Facebook created to cater to low resource languages, and it supports Tibetan out of the box! This seems like it should be an easy giant step forward.

Unfortunately, at the time of writing, NLLB seems to be out of step with it's own documentation and it seems like functional translation is not viable at present. However, in previous testing, I was able to use it, following the approach used by [Digital Tibetan](https://digitaltibetan.github.io/DigitalTibetan/docs/tibetan_machine_translation.html), to work with a section of the Longchen Nyingtik Ngondro liturgy entitled "The Excellent Path to Omniscience The Preliminary Practice of the Heart-Essence of the Vast Expanse (Longchen Nyingtik) from the Great Perfection" arranged by Dodrupchen Jikme Trinle Özer. The full text is available at [Lotsawa House here](https://www.lotsawahouse.org/tibetan-masters/dodrupchen-I/longchen-nyingtik-ngondro). However, it is important to note that within the tradition, the full text is not to be read without the supervision or advice of a teacher.

#### Single Line Translation

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


#### Longer Text Translation

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

 ### Finetuning Results

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

## T5

According to the Hugging Face model card for the T5 model:

>"With T5, we propose reframing all NLP tasks into a unified text-to-text-format where the input and output are always text strings, in contrast to BERT-style models that can only output either a class label or a span of the input. Our text-to-text framework allows us to use the same model, loss function, and hyperparameters on any NLP task."

An admirable goal! The smallest T5 model, and the one initially used here, is T5-small with 60 million parameters. The same size as the NLLB model used above.

T5 has a disadvantage against NLLB, it does not, to my knowledge, support Tibetan out of the box. However, it was purpose built to be finetuned for translation tasks!

### Finetuning

This model was finetuned using the 100,000 pair dataset for 30 epochs. This time evaluation was done by calculating the BLEU score of the predicted translations. 

 BLEU (BiLingual Evaluation Understudy) is a standard (if not uncontroversial) metric in machine translation. BLEU gives each prediction a score between 0 and 1, where 0 means the model's predicted translation is nothing like the correct translation and 1 means the predicited translation is identical to the correct one. [You can read more about the specifics here.](https://en.wikipedia.org/wiki/BLEU)

The training loss is plotted below.

![T5 Small Model Results](../readme-assets/t5-small-loss.png?raw=true "T5 Small Model Results")

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

#### Epoch 10

***the buddhis dharma dharma and dharma kyichok nam la***

***i offer to you i pray***

***i offer to all my buddhas and bodhisattvas and so on***

***grant us the buddhahood of all our wishes and wishes so that we may attain buddhahood***

#### Epoch 20

***the buddhas and bodhisattvas the dharma dharma and the supreme assembly***

***i take refuge in the bodhisattva bodhisattva***

***i offer to all my buddhas and bodhisattvas and so on***

***and grant us the buddhahood of all buddhas the attainment of buddhahood***


#### Epoch 30

***the buddhas dharma dharma dharma and tsok kyichok nam la***

***i take refuge in the bodhisattva bodhisattva***

***i offer to you the buddhas and their heirs and so on***

***and grant us the buddhahood to accomplish enlightenment***

### Assessment

Clearly, the quality of the results peaked at epoch 20. This translation does still leave something to be desired but is an extremely exciting result! With the small dataset of 100k samples, for only 20 training epochs, using the smallest model (!), T5 substantially outperforms the other models.

## Llama 2

Llama 2 is a large language model developed by Facebook. It is the second Llama model that they have produced. The smallest size and the size used here is the 7B version, which has 7 billion trainable parameters, far, far more than the other models thus far tested. This places Llama 2 into a unique position. It is possible that the additional parameters will make it substantially more performant but it is certain that it will make training a much longer and more computationally expensive process. Additionally, the model is too large to be usable on many low or mid-tier commercial computers limiting its usefulness to many translators. As such, the bar is high for this to be the model that we proceed with.

To facilitate training such a large model, the QLoRA technique was used. [You can read more about how this works here.](https://github.com/artidoro/qlora)

Working with Llama (or any other LLM) also introduces an additional variable: prompt selection. The input to a model which is prepared to accept and follow instructions should include an instruction. What the exact format of that instruction should be is not obvious. I have tested two possibilities: 

The "T5 prompt": "Translate from Tibetan to English: <Tibetan text> \n <English text> found here: https://huggingface.co/learn/nlp-course/chapter7/4?fw=pt

The "Reddit prompt": "Tibetan: <Tibetan Text> English: <English text> found here: https://www.reddit.com/r/LocalLLaMA/comments/169ae0e/comment/jz1c51y/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

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

![Llama Single Epoch Model Results](../readme-assets/llama-prompt-comparison.png?raw=true "Llama Single Epoch Model Results")

However, as we will see below, this does not necessarily mean a better translation model.


### T5 Prompt Model Epoch 1

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

### Reddit Prompt Model Epoch 3

In the chart below, you can see that training loss continues to improve with additional training, but what we've seen so far should lead us to be skeptical of that as a meaningful metric.

![Llama Three Epoch Model Results](../readme-assets/llama-3-epochs.png?raw=true "Llama Three Epoch Model Results")

The model trained for additional epochs using the "Reddit prompt" produces the following translation:

***May all your prayers be fulfilled***

***The vajra masters are my guardians***

***Awakening***

***I take refuge in the Buddha***

This is not much better. The third line is now in English but does not approximate the correct translation.

Note that the Llama model was trained for far fewer epochs than the T5 model. This is somewhat unfair, however, the amount of time taken to train Llama was substantially longer. Each epoch for Llama took approximately 24 hours, compared to the total training time of the T5 model being only about 8 hours.

The additional time taken to train the Llama model for additional epochs does not at this point seem justifiable.