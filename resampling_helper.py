
from imblearn.over_sampling import BorderlineSMOTE
from sklearn.model_selection import StratifiedKFold
from imblearn.pipeline import Pipeline, make_pipeline
from sklearn.model_selection import cross_val_score
import numpy as np

def resampling(ratio,X_train,y_train):
    oversample = BorderlineSMOTE(sampling_strategy=ratio,random_state=42)
    X, y = oversample.fit_resample(X_train, y_train)
    return X,y


def pipeline_for_sampling(X, y,sampling_strategy,model,scoring = "f1"):
    imba_pipeline = make_pipeline(BorderlineSMOTE(sampling_strategy=sampling_strategy,random_state=42), 
                              model)
    skfold=StratifiedKFold(n_splits=5)
    scores = cross_val_score(imba_pipeline, X, y, cv=skfold,scoring=scoring)
    return np.mean(scores)
