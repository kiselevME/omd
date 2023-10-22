from typing import Iterable
from math import log


class CountVectorizer:
    """Convert a collection of text documents to a matrix of token counts.

    Args:
        lowercase (bool, optional): Convert all characters to lowercase before
        tokenizing. Defaults to True.
    """

    def __init__(self, lowercase: bool = True) -> None:
        self.lowercase = lowercase

    def _preprocessing(self, raw_documents: Iterable) -> list:
        """Preprocessing of the input corpus of texts."""
        for i, doc in enumerate(raw_documents):
            if not isinstance(doc, str):
                ValueError("object in raw_documents is not a string")
            if self.lowercase:
                raw_documents[i] = doc.lower()
        return raw_documents

    def _create_vocabulary(self, raw_documents: Iterable) -> None:
        """Сreates a vocabulary from corpus words."""
        # использую словарь, т.к. его ключи упорядочены
        voc = {}
        for doc in raw_documents:
            for word in doc.split(" "):
                voc[word] = voc.get(word, "")
        self._vocabulary = list(voc.keys())

    def _create_token_matrix(self, raw_documents: Iterable) -> None:
        """Creates and returns a token matrix. Before using this function,
        you need to call _create_vocabulary."""
        self._token_matrix = []
        for doc in raw_documents:
            # подсчитываю количество каждого элемента в строке
            count_words = {k: 0 for k in self._vocabulary}
            for word in doc.split(" "):
                count_words[word] += 1
            # в следующей строке пользуюсь упорядоченностью словаря
            self._token_matrix.append(list(count_words.values()))

    def _check_vocabulary(self) -> None:
        """Check if vocabulary is empty or missing (not fitted)."""
        if not hasattr(self, "_vocabulary"):
            raise AttributeError("Vocabulary not fitted or provided")

    def fit_transform(self, raw_documents: Iterable) -> list:
        """Creates and returns a matrix of token counts.

        Args:
            raw_documents (Iterable): Collection of text documents
            (documents must be in the str format)

        Returns:
            list: Matrix of token counts
        """

        if isinstance(raw_documents, str):
            raise ValueError(
                "Iterable over raw text documents expected, \
                              string object received"
            )
        if not isinstance(raw_documents, Iterable):
            raise ValueError("raw_documents is not an iterable object")
        # предобработка начального корпуса
        raw_documents = self._preprocessing(raw_documents)
        # создание словаря и матрицы токенов
        self._create_vocabulary(raw_documents)
        self._create_token_matrix(raw_documents)
        return self._token_matrix

    def get_feature_names(self) -> list:
        """Get output feature names for transformation.

        Returns:
            list: Transformed feature names.
        """
        self._check_vocabulary()
        return self._vocabulary


class TfidfTransformer:
    """Performs term frequency, inverse document frequency and
    TF-IDF counting functions
    """

    @staticmethod
    def tf_transform(count_matrix: Iterable) -> list:
        """Converts the count matrix to term frequency

        Args:
            count_matrix (Iterable): Matrix, where the rows are documents,
            the columns are words from the vocabulary,
            and the cells are the number of word in the document

        Returns:
            list: term frequency matrix
        """
        tf = [[item / sum(doc) for item in doc] for doc in count_matrix]
        return tf

    @staticmethod
    def idf_transform(count_matrix: Iterable) -> list:
        """Сonverts the count matrix to inverse document frequency

        Args:
            count_matrix (Iterable): Matrix, where the rows are documents,
            the columns are words from the vocabulary,
            and the cells are the number of word in the document

        Returns:
            list: inverse document frequency list
        """
        docs_total = len(count_matrix)
        voc_size = len(count_matrix[0])
        # Документы со словом
        docs_with_word = [
            sum([1 if count_matrix[i][j] > 0 else 0
                 for i in range(docs_total)])
            for j in range(voc_size)
        ]
        # Применяем формулу для IDF
        idf = [log((docs_total + 1) / (cnt + 1)) + 1 for cnt in docs_with_word]
        return idf

    def fit_transform(self, count_matrix: Iterable) -> list:
        """Converts the count matrix to TF-IDF matrix
        Args:
            count_matrix (Iterable): Matrix, where the rows are documents,
            the columns are words from the vocabulary,
            and the cells are the number of word in the document

        Returns:
            list: TF-IDF matrix
        """
        tf_corp = self.tf_transform(count_matrix)
        idf_corp = self.idf_transform(count_matrix)
        tf_idf = [
            [round(tf * idf, 3) for tf, idf in zip(tf_line, idf_corp)]
            for tf_line in tf_corp
        ]
        return tf_idf


class TfidfVectorizer(CountVectorizer):
    """Vectorizes a corpus of documents into a count matrix
    Performs term frequency, inverse document frequency and TF-IDF counting
    functions
    """

    def __init__(self) -> None:
        super().__init__()
        self.transformer = TfidfTransformer()

    def fit_transform(self, corpus: Iterable) -> list:
        """Calculates the TF-IDF matrix based on the corpus of documents

        Args:
            corpus (Iterable): corpus of documents

        Returns:
            list: TF-IDF matrix
        """
        count_matrix = super().fit_transform(corpus)
        return self.transformer.fit_transform(count_matrix)
