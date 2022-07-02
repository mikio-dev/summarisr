from sumy.nlp.stemmers import Stemmer
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.utils import get_stop_words


class Summarise:
    """
    The class Summarise is a wrapper around the Python library Sumy
    """

    def __init__(self, language: str = "english", sentences_count: int = 3):
        self.language = language
        self.sentences_count = sentences_count

    def summarise(self, text: str) -> str:
        """
        This function summarises the text specified by the text parameter using
        the Python library Sumy (https://pypi.org/project/sumy/).

        :param text: The text to summarise.
        :param language: The language of the text.
        :param sentences_count: The number of sentences to summarise.
        :return: The summarised text.
        """
        parser = PlaintextParser.from_string(text, Tokenizer(self.language))

        stemmer = Stemmer(self.language)

        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(self.language)
        summary_sentence_list = [
            str(s) for s in summarizer(parser.document, self.sentences_count)
        ]
        return " ".join(summary_sentence_list)
