from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score

def cross_validation_imbalanced_df(model,X_train,y_train,scoring):
    cv = StratifiedKFold(n_splits=5, random_state=1, shuffle=True)
    scores = cross_val_score(model,X_train,y_train, scoring=scoring, cv=cv, n_jobs=-1)
    return scores