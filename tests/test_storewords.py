import unittest
from storewords.storewords import StoreWords

class StoreWordsTestCase(unittest.TestCase):

    def test_folderpath(self):
        storeWords = StoreWords('/Users/hujiabao/books/english/en/words/')
        print(storeWords.folderPath)
        self.assertEqual(storeWords.folderPath,'/Users/hujiabao/books/english/en/words/')

unittest.main