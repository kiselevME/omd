from unittest import TestCase
from unittest.mock import patch
from what_is_year_now import what_is_year_now


class TestWhatIsYear(TestCase):
    @patch('what_is_year_now.json.load')
    @patch('what_is_year_now.urllib.request.urlopen')
    def test_what_is_year_now_1(self, mock_urlib, mock_json_load):
        mock_json_load.return_value = dict({'currentDateTime': '2019-03-01'})
        self.assertEqual(what_is_year_now(), 2019)

    @patch('what_is_year_now.json.load')
    @patch('what_is_year_now.urllib.request.urlopen')
    def test_what_is_year_now_2(self, mock_urlib, mock_json_load):
        mock_json_load.return_value = dict({'currentDateTime': '01.03.2019'})
        self.assertEqual(what_is_year_now(), 2019)

    @patch('what_is_year_now.json.load')
    @patch('what_is_year_now.urllib.request.urlopen')
    def test_what_is_year_now_raise_1(self, mock_urlib, mock_json_load):
        mock_json_load.return_value = dict({'currentDateTime': 'abobaaboba'})
        with self.assertRaises(ValueError):
            what_is_year_now()
