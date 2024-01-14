import pickle

import sklearn

import warnings

from sklearn.exceptions import InconsistentVersionlarning

# Catch the InconsistentVersionWarning and print the original scikit-learn version 
warnings.simplefilter("error", InconsistentVersionlarning)

try:
    model = pickle.load(open('saved_model.pk1', 'rb'))

except InconsistentVersionWarning as w:
    print(w.original_sklearn_version)