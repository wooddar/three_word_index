import logging
import pandas as pd

from word_index.word_index import WordIndexFilter
from word_index.word_index import WordIndex

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    twi = WordIndex(10)
    logger.info(twi.generate_word_index())
    word_filter = WordIndexFilter().set_max_length(5).set_min_length(1)
    twi = WordIndex(5,word_count=2,word_filter=word_filter)
    logger.info(twi.generate_word_index())