# Toward a Cleaner Translation Dataset
*Nov 2024*
## Introduction
While performing topic modeling on the translation dataset 'openpecha/cleaned_MT_v1.0.2' it was discovered that some elements ('sentence pairs') of the dataset may present problems for model training. There are 3 primary issues:

1. Some elements have Tibetan text in the target output. This can lead to poor results from models trained on the dataset and is undesirable. 
2. Some elements contain emojis in either the source or target text.
3. Some elements appear to consist entirely of numerals and punctuation. 

Samples were extracted programmatically for this analysis. Entries in the dataset as downloaded from Hugging Face are Python dictionary with the structure of the following example:

> {'Source': 'ཐུབ་པས་རྟག་ཏུ་དེ་བཞིན་སྤྱད།།',
 'Target': 'The aspirant should move in such a way at all times.',
 'File_Name': 'TM2382',
 'Machine Aligned': True}

Notably, the dictionaries lack an 'id' entry. This makes reproducibility less reliable. It is recommended that 'id' numbers be added for future versions.

## Tibetan in the Target Text

Tibetan text is in the Unicode block (U+0F00-0FFF). We can find elements of the dataset that have Tibetan in the target output by searching for dictionaries where characters in the 'Target' entry fall within that Unicode range, record the index of that dictionary (i.e. texts[0], texts[785], etc.) and then pull those dictionaries from the over all dataset.

Sentence pairs that include Tibetan text in the target ouput were extracted using the following python code:

```python
from datasets import load_dataset

texts = load_dataset('openpecha/cleaned_MT_v1.0.2', split="train")

tibetan_range = range(0x0F00, 0x0FFF + 1)
locs = []

for i in range(len(texts)):
    for char in texts[i]['Target']:
            if ord(char) in tibetan_range:
                locs.append(i)
                break
```

This was repeated with the test set as well.

### Train Split

TThere are 2423 such elements in the train split. These elements in the train split fall roughly into three categories.

1. Some have Tibetan characters occur as part of an English sentence, largely as examples from language learning textbooks like so:

>*'Further, when an action being done is one of “no apparent agentother”, for example in ཛ་མཁན་གྱི་འཁོར་ལོ་འཁོར་རོ། “the potter’s wheel turning”, initially there is སྐོར་བྱེད་གཞན་ a turner and an other from it but once the wheel འཁོར་བཞིན་པའི་ is turning, that is, when it is just turning of itself without turner who is other, given that the situation has a non-separate action and agent, it is not expressed with “བསྐོར་” but expressed with “འཁོར་”. Further, when agent-other is not actually apparent, for example in སྐྱེས་བུ་ཞིག་གི་མདུན་དུ་ལྕགས་ཤིག་རང་བཞིན་གྱིས་གསེར་དུ་གྱུར་པ་ “right before a person iron turned to gold by itself” the merit of that person is indeed the agent-other nonetheless that merit is not actually apparent and given that change occurs by the iron itself acting38 this is not expressed as iron turned into gold with “བསྒྱུར་” but with “གྱུར་”. Moreover, when this is analysed very closely, from the stance of the self-character of each thing involved, “something of itself to itself” transgresses action-agent but generally, from the stance of a rough take on it, merely in convention there is no transgression.'*

2. Some seem to be mistakes in the machine alignment of the dataset like so:

>*'བས་འདི་ མས་ཚིག་གསལ་ལས་ག ངས་པ་ མས་ཀྱི་ནང་ ནས་ཀྱང་ཤིན་ ་ ོགས་དཀའ་བར་ ང་བས་ཚིག་གསལ་གྱི་ཚིག་ ངས་ཏེ་བཤད་ན། ཇི་ ད་ ། ཅི་ ེ་ཇི་ ར་ ་མི་ ག་ཅེས་ ་ བ་ལ་ཆོས་དང་ཆོས་ཅན་གཉིས་ ི་ཉིད་བ ང་བ་ཡིན་གྱི་ཁྱད་ པར་ནི་མ་ཡིན་ཏེ། ཁྱད་པར་འཛིན་ན་ནི་ ེས་ ་དཔག་པ་དང་ ེས་ ་དཔག་པར་ ་བའི་ཐ་ ད་མེད་པར་འ ར་རོ། ། འདི་ ར་གལ་ཏེ་འ ང་བ་ཆེན་པོ་བཞི་ལས་ ར་པའི་ ་འཛིན་ན་ནི་ དེ་ཕ་རོལ་པོ་ལ་མ་ བ་བོ། ། འོན་ཏེ་ནམ་མཁའི་ཡོན་ཏན་འཛིན་ ན་ནི་དེ་རང་ཉིད་སངས་ ས་པ་ལ་མ་ བ་པ་ཡིན་ནོ། ། དེ་ བཞིན་ ་ ེ་ ག་པ་ ་མི་ ག་པར་དམ་འཆའ་བ་ནའང་ ས་ པའི་ ་འཛིན་ན་དེ་གཞན་ལ་མ་ བ་བོ། ། འོན་ཏེ་མངོན་པར་ གསལ་བར་ ་བ་ཡིན་ན་ནི་དེ་རང་ལ་མ་ བ་པ་ཡིན་ནོ། ། དེ་ བཞིན་ ་ཅི་རིགས་པར་འཇིག་པའང་གལ་ཏེ་ ་དང་བཅས་པ་ ཡིན་ན་ནི་དེ་སངས་ ས་པ་རང་ལ་མ་ བ་པ་ཡིན་ལ། འོན་ཏེ་ ་ Difficult Points in the Opposite of the Consequences, 633.2) identifies the other party as a Dīpaka.'*

>*'IV.56, sde dge 9a.2: {IV.56} དངོས་པོ་བ ོད་ ་མེད་པ་ལ། །ཉམས་པ་དང་ནི་འཕེལ་མི་ ང༌། ། ོམ་ཞེས་ ་བའི་ལམ་གྱིས་ནི། །ཅི་ཞིག་ཉམས་ཤིང་ཅི་ཞིག་ཐོབ། ། 2# Response [to the objection about efficacy] (IV.5758){2 parts} This has two parts: actual response and dispelling an objection to that response.'*

3. Others seem to be trivial inclusions either by accident or as seed syllables in an otherwise useful piece of English text like so:

>*'THE LIMB OF OFFERINGྲ For this limb visualize incalculable beautiful and captivating offering goddesses who are capable of engendering bliss to both the eyes and the mind of the beholder.'*

>*'One day when Hall was having a bath, he began to sing. ་The bathroom was small and had a stone floor, so his song was very beautiful, he thought. ‘'*


### Test Split

There are only five relevant samples in the test split. They are shown below:

```
{'Source': 'ལེགས་པར་བཤད་པ་(ཆུའི་བསྟན་བཅོས་)',
  'Target': 'A Treatise on Water🔽 ( 🔽དོན་འགྱུར་ཙམ་རེད་འདུག)',
  'File_Name': 'TM4707',
  'Machine Aligned': True},
 {'Source': 'ལོ་མང་པོ་ན་ལུས་དེ་ཉིད་ཀྱིས་མཁའ་སྤྱོད་དུ་གཤེགས་སོ།། གུརུབྷིཀྵན་པཱའི་ལོ་རྒྱུས་རྫོགས་སོ།།།།🔽',
  'Target': '༼༦༢༽  After many years, he went in this very body to the realm of the Dakas.🔽',
  'File_Name': 'TM0770',
  'Machine Aligned': True},
 {'Source': '(མྱ་ངམ་དགོན་པ་སྣོད་བྱས་ནས་ཐར་བར་བྱས་པ་ལས་གཞན་ཐབས་མེད་དོ་སྙམ་ནས་སྣ་ལག་པ་བསྒྲེང་བ་ལྟར་བརྐྱངས་དཔག་ཚད་དུ་མ་ཡོད་པ་འདི་ལས་ཇི་ལྟར་བསྒྲལ། ད་ནི་ངའི་ཤ་འདི་ལམ་རྒྱགས་དང་། རྒྱུ་མའི་ཆུ་ཏེ་སྨྲས་པ། ) It hardly makes sense, plz check it!',
  'Target': '(How can they cross this remote wasteland many leagues across? There is no way for them to escape other than for them to use my flesh as provisions for their journey and to use my entrails as water bags."He lifted his trunk to point and told them,) དབྱིན་བོད་གཉིས་མ་དཔེ་དང་བསྡུར་ནས་བལྟ་དགོས་འདུག་སྙམ།',
  'File_Name': 'TM4707',
  'Machine Aligned': True},
 {'Source': 'འཁོར་དྲུག་བརྒྱ་དང་བཅས་མཁའ་སྤྱོད་དུ་གཤེགས་སོ།། གུརུཀིརཔཱལའི་ལོ་རྒྱུས་རྫོགས་སོ།།།།🔽',
  'Target': '༼༧༤༽  With a circle of six hundred, he went to the realm of the Dakas.🔽',
  'File_Name': 'TM0770',
  'Machine Aligned': True},
 {'Source': 'མཐར་འཁོར་དྲུག་བརྒྱ་དང་བཅས་ནས་མཁའ་སྤྱོད་དུ་གཤེགས་སོ།། གུརུཀཔཱལའི་ལོ་རྒྱུས་རྫོགས་སོ།།།།🔽',
  'Target': '༼༧༣༽  Then, with a circle of six hundred, he went to the realm of the Dakas.🔽',
  'File_Name': 'TM0770',
  'Machine Aligned': True}
```

Note that in addition to including Tibetan script in the target output, one example also has English in the source text.

### Suggestions

I suggest the following actions, using the category numbering used in the Train Split section above:

For texts of type 1 (Tibetan characters occur as part of an English sentence), I recommend removing these samples from the dataset entirely.

For texts of type 2 (Large portion of Tibetan script occur prior to the English), I recommend that these entires be checked by a competent speaker to ensure that the English text is correctly related to the associated source text. If so, the Tibetan script could be manually cleaned.

For texts of type 3 (Negligible or small portion of Tibetan script), I recommend that the Tibetan script simply be removed from the target text, with no additional alterations.

## Emojis

The dataset was then searched for emojis in the target outputs. Again, the train and test sets were both searched. The following code was used:

```python
emoji_locs = []

for i in range(len(texts)):
    for char in texts[i]['Target']:
        char_code = ord(char)
        if any(start <= char_code <= end for start, end in emoji_ranges):
            emoji_locs.append(i)
            break
```

### Train Split

There were 0 elements in the Train Split with emojis in the target output. There are also 0 elements with emojis in the source text.

### Test Split

The test split contains 8436 elements with emojis in the target output. Not all of these include emojis in both the source and target texts. 5593 of them contain the 'Down Arrow' emoji: 🔽. None of these emojis, at first glance, appear to meaningfully alter the text.

### Suggestions

I recommend that the emojis simply be removed with no additional alterations to the texts.

## Numeric Strings

Some elements of the dataset appear to have target outputs that consist only of numerals and punctuation. These are likely to be section headers in the original source.

Elements meeting this description were extracted with the following code:

```python
short_locs = []

for i in range(len(texts)):
    if len(texts[i]['Target'].split(' ')) == 1:
                short_locs.append(i)

short_texts = [texts[elt] for elt in short_locs]

num_range = range(48, 58)
num_locs = []

for i in range(len(texts)):
    for char in texts[i]['Target']:
            if ord(char) in num_range:
                num_locs.append(i)
                break
```

### Train Split

There are 7571 elements which match this description in the train split. Some samples are shown below:

{'Source': 'གསུམ་པ་ནི།',
 'Target': '162.',
 'File_Name': 'TM1117',
 'Machine Aligned': True}

{'Source': 'ཞེས་པས་བསྟན།',
 'Target': '2.2.2.1.1.6.2.3.1.1.2.3.3.2.2.2.1.3.',
 'File_Name': 'TM3004',
 'Machine Aligned': True}

{'Source': 'གཉིས་པ་ནི།',
 'Target': '3.2.5.2.1.2.1.2.',
 'File_Name': 'TM0581',
 'Machine Aligned': True}

### Test Split

There are only 5 elements which match the description in the test split. They are shown below:

```
[{'Source': 'གཉིས་པ་ལ།',
  'Target': '2.',
  'File_Name': 'TM0767',
  'Machine Aligned': True},
 {'Source': '🔽',
  'Target': '26.🔽',
  'File_Name': 'TM4793',
  'Machine Aligned': True},
 {'Source': '🔽',
  'Target': '25.🔽',
  'File_Name': 'TM4793',
  'Machine Aligned': True},
 {'Source': 'རྟག་པ་དང་།🔽',
  'Target': '3.permanence,🔽',
  'File_Name': 'TM0757',
  'Machine Aligned': True},
 {'Source': '🔽',
  'Target': '29.🔽',
  'File_Name': 'TM4793',
  'Machine Aligned': True}]
```

These are more clearly problematic than those from train split. Note that 4 of the 5 also include an emoji. More troublingly, 3 of the 5 have only an emoji in the source text but have a numeric string as the target output.

### Suggestions

The elements in the test split appear irredeemable and should be removed entirely. The elements in the training set may be useful. There are certainly cases in the Tibetan corpus where lengthy numeric strings are used as section headers. It may be valuable for the translation model to be able to handle them effectively.

## Conclusion

There are some relatively straightforward ways to improve the dataset for translation model training. I recommend that the suggestions here be discussed by those working on the machine translation model and decisions be made about how best to produce a cleaner  'openpecha/cleaned_MT_v1.0.3'