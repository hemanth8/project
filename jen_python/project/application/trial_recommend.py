import json
import pickle
import sklearn
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import cosine_similarity


class TFIDF_MODEL:

    def __init__(self, num_features=5000, mat_label="tf_matrix.pk", feats_label="tf_feats.json"):
        self.data = pd.read_csv(r"C:\Users\Fission Labs\Downloads\processed_data.csv")
        self.num_features = num_features
        self.mat_label = mat_label
        self.feats_label = feats_label

    def data_preperation(self):
        self.data['processed_question'] = self.data['processed_question'].apply(lambda x: str(x))
        self.data['processed_title'] = self.data['processed_title'].apply(lambda x: str(x))
        self.data = self.data.sort_values(by='id')

    def build_matrix(self):
        self.data_preperation()
        tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english',
                             max_features=self.num_features)
        tfidf_matrix = tf.fit_transform(self.data['processed_title'])
        vocab = tf.get_feature_names()
        self.write_data(tfidf_matrix, vocab)
        return True

    def load_data(self):
        # self.build_matrix()
        with open(self.mat_label, 'rb') as fp:
            tfidf_mat = pickle.load(fp)

        with open(self.feats_label, 'r') as fp:
            vocab = json.load(fp)

        return tfidf_mat, vocab

    def predict_obs(self, obs):
        tfidf_mat, vocab = self.load_data()
        tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english', max_features=5000,
                             vocabulary=vocab)
        val = tf.fit_transform([obs])
        close_indexes = cosine_similarity(val, tfidf_mat).argsort().flatten()[::-1][:10]
        # for ind in close_indexes:
        #     print(self.data.iloc[ind])
        return close_indexes

    def write_data(self, tfidf_mat, vocab):
        with open(self.mat_label, 'wb') as fp:
            pickle.dump(tfidf_mat, fp)

        with open(self.feats_label, 'w') as fp:
            json.dump(vocab, fp)
