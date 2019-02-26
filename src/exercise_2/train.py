from src.exercise_2.utils import load_reviews, extract_texts_and_labels
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer


def train_model():
    reviews = load_reviews('./data/review_100_samples.json')
    texts, labels = extract_texts_and_labels(reviews)

    data_train, data_val, labels_train, labels_val = train_test_split(texts, labels, random_state=0)
    text_clf = Pipeline([('vect', CountVectorizer()),
                         ('tfidf', TfidfTransformer()),
                         ('clf', RandomForestClassifier())])
    text_clf = text_clf.fit(data_train, labels_train)

    return text_clf, data_val, labels_val

if __name__ == '__main__':
    text_clf, data_val, labels_val = train_model()
    # serialize model
