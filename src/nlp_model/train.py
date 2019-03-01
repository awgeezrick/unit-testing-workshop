from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split

def train_model(texts, labels):
    data_train, data_val, labels_train, labels_val = train_test_split(texts, labels, random_state=0)

    text_clf = Pipeline([('vect', CountVectorizer()),
                        ('tfidf', TfidfTransformer()),
                        ('clf', RandomForestClassifier())
                        ])
    text_clf = text_clf.fit(data_train, labels_train)

    return text_clf, data_val, labels_val