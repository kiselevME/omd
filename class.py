# from typing import Iterable
from math import log
from feature_extraction import CountVectorizer


class TFIDF_Transformer:
    @staticmethod
    def tf_transform(count):
        tf_count = [[item / sum(doc) for item in doc]
                    for doc in count]
        return tf_count

    @staticmethod
    def idf_transform(count):
        docs_count = len(count)
        corpus_len = len(count[0])
        # считаем документы, в которых встречается слово
        idf_count = [sum([1 if count[j][i] else 0 for j in range(docs_count)])
                     for i in range(corpus_len)]
        # применяем формулу IDF
        idf_count = [log((docs_count + 1) / (idf + 1)) + 1
                     for idf in idf_count]
        return idf_count

    def fit_transform(self, count_corpus):
        tf_corp = self.tf_transform(count_corpus)
        idf_corp = self.idf_transform(count_corpus)
        # print(tf_corp)
        # print(idf_corp)
        tf_idf = [[round(tf*idf, 3) for tf, idf in zip(tf_line, idf_corp)]
                  for tf_line in tf_corp]
        return tf_idf


class TFIDF_Vectorizer(CountVectorizer):
    def __init__(self):
        super().__init__()
        self.transformer = TFIDF_Transformer()

    def fit_transform(self, corpus):
        count_matrix = super().fit_transform(corpus)
        return self.transformer.fit_transform(count_matrix)


if __name__ == '__main__':
    corpus1 = ['Crock Pot Pasta Never boil pasta again',
               'Pasta Pomodoro Fresh ingredients Parmesan to taste']

    corpus2 = ['Crock Pot Pasta Never boil pasta again',
               'Pasta Pomodoro Fresh ingredients Parmesan to taste',
               'asd Isdvisdjv ds]fj sdflks jdf']

    tf_idf = TFIDF_Vectorizer()
    print(tf_idf.fit_transform(corpus1))
