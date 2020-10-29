import pdb

import pytest

import unittest

from utils.api_helper import ApiHelper
from utils.teststatus import TestStatus
from utils.read_data import *

@pytest.mark.usefixtures("oneTimeEveryClassSetup")
class LibraryValidation(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.ts = TestStatus(None)
        self.api=ApiHelper()
        self.endpoint = getYamlData(self.lib_testdata_file, 'end_points')

    def test_reading_book_details(self):
        print("inside lib_test test_reading_book_details method")
        params={}
        test_data=getYamlData(self.lib_testdata_file)
        params.__setitem__('AuthorName',test_data['author'])
        url = test_data['base_url'] + self.endpoint['read_api']
        response=self.api.get(url,params)
        res=response.json()
        exp_result={k:v for k,v in test_data.items() if k!='author' and k!='base_url'}
        results= exp_result in res
        self.ts.markFinal('test_reading_book_details',results,"book details does not match")

