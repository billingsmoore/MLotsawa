Pickle files named with 'dict' are dictionaries of either texts by index. They are formatted like so:

Each dictionary consists of keys, labels which are domain tags, and values, lists of indexes in the original dataset. Thus,
a dictionary with the entry dictionary['Cats'] = [1,2,3] means that elements 1, 2, and 3, in the original dataset should be tagged with
the label 'Cats'.

buddhist-labels-idx-dict.pkl is a dictionary of this kind for Buddhist material in the dataset.
non-buddhist-labels-idx-dict.pkl is a dictionary of this kind for non-Buddhist material in the dataset.

buddhist-or-no-idx-dict.pkl is a dictionary of this kind whose labels are just 'Buddhist' or 'non-Buddhist'.

The file uncat-idx-list.pk is just a Python list of indexes in the original dataset which have not yet been tagged at all.

