# Creating openpecha/cleaned_MT_v1.0.3
*Dec 2024*

The cleaner version of the machine translation dataset **openpecha/cleaned_MT_v1.0.3** was created by cleaning **openpecha/cleaned_MT_v1.0.2** with the steps listed below. Each step is accompanied by the code that was used to perform it.

This cleaning is intended as an iteration on the cleaning process, and should not be taken to be definitive.

As a result of this cleaning, **133,757 sentence pairs were removed from the training set** and **52 sentence pairs were removed from the test set**. This leaves a **training set of 1,429,192 sentence pairs** and a **test set of 9,066 sentence pairs**.

Note that the dataset must first be turned into a Pandas dataframe. Each code block assumes that this has already been performed.

## Remove Any Pairs With Tibetan in the Target Text

```python
# Regular expression to match Tibetan script
tibetan_pattern = re.compile(r'[\u0F00-\u0FFF]')

# Remove rows where 'target' contains Tibetan script
train_df = train_df[~train_df['Target'].str.contains(tibetan_pattern, na=False)]
test_df = test_df[~test_df['Target'].str.contains(tibetan_pattern, na=False)]
```

## Remove Emojis From Source and Target

```python
# Regular expression to match emojis
emoji_pattern = re.compile(
    "[\U0001F600-\U0001F64F"  # Emoticons
    "\U0001F300-\U0001F5FF"  # Symbols & Pictographs
    "\U0001F680-\U0001F6FF"  # Transport & Map Symbols
    "\U0001F1E0-\U0001F1FF"  # Flags (iOS)
    "]+", 
    flags=re.UNICODE
)

# Remove emojis from both 'source' and 'target' columns
train_df['Source'] = train_df['Source'].str.replace(emoji_pattern, '', regex=True)
train_df['Target'] = train_df['Target'].str.replace(emoji_pattern, '', regex=True)

test_df['Source'] = test_df['Source'].str.replace(emoji_pattern, '', regex=True)
test_df['Target'] = test_df['Target'].str.replace(emoji_pattern, '', regex=True)
```

## Remove Pairs Whose Target is Just Numbers And/Or Punctuation

```python
# Regular expression to match rows with only numbers and punctuation
train_df = train_df[~train_df['Target'].str.fullmatch(r'[0-9\W]+', na=False)]
test_df = test_df[~test_df['Target'].str.fullmatch(r'[0-9\W]+', na=False)]
```

## Remove Pairs Where Target is Just Roman Numerals

```python
roman_numeral_pattern = r'^(?=[MDCLXVI])M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})\.?$'

# Remove rows where 'target' matches the pattern
train_df = train_df[~train_df['Target'].str.fullmatch(roman_numeral_pattern, na=False)]
test_df = test_df[~test_df['Target'].str.fullmatch(roman_numeral_pattern, na=False)]
```

## Remove Any Pairs Where Either Source or Target Are Empty

```python
train_df = train_df[(train_df['Source'] != '') & (train_df['Target'] != '')]
test_df = test_df[(test_df['Source'] != '') & (test_df['Target'] != '')]
```

## De-duplicate Sentence Pairs

```python
# Drop duplicate values in either column, keeping the first occurrence
train_df = train_df.drop_duplicates(subset='Source', keep='first')
train_df = train_df.drop_duplicates(subset='Target', keep='first')

test_df = test_df.drop_duplicates(subset='Source', keep='first')
test_df = test_df.drop_duplicates(subset='Target', keep='first')
```