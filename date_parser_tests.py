import unittest
import datetime
from date_parser import DateParser

class TestDateParser(unittest.TestCase):

    def test_is_an_instance_of_date_parser(self):
        result = DateParser("2020-04-11")
        self.assertTrue(isinstance(result, DateParser))

    def test_can_parse_yyyy_mm_dd_as_dash(self):
        parser = DateParser("2020-04-11")
        result = parser.parse()
        expected = datetime.datetime(2020, 04, 11, 0, 0)

        self.assertEqual(expected, result)

    def test_can_parse_yyyy_mm_dd_as_underscore(self):
        parser = DateParser("2020_04_11")
        result = parser.parse()
        expected = datetime.datetime(2020, 04, 11, 0, 0)

        self.assertEqual(expected, result)

    def test_can_parse_yyyy_mm_dd_as_forward_slash(self):
        parser = DateParser("2020/04/11")
        result = parser.parse()
        expected = datetime.datetime(2020, 04, 11, 0, 0)

        self.assertEqual(expected, result)
    
    def test_can_parse_mm_dd_yyyy_as_forward_slash(self):
        parser = DateParser("04/11/2020")
        result = parser.parse()
        expected = datetime.datetime(2020, 04, 11, 0, 0)

        self.assertEqual(expected, result)

    def test_can_parse_mm_dd_yyyy_as_dash(self):
        parser = DateParser("04-11-2020")
        result = parser.parse()
        expected = datetime.datetime(2020, 04, 11, 0, 0)

        self.assertEqual(expected, result)
    
    def test_can_parse_mm_dd_yyyy_as_underscore(self):
        parser = DateParser("04_11_2020")
        result = parser.parse()
        expected = datetime.datetime(2020, 04, 11, 0, 0)

        self.assertEqual(expected, result)
   
    def test_invalid_date_string_raises_value_error(self):
        with self.assertRaises(ValueError):
            parser = DateParser("this is not a date")
            parser.parse()


if __name__ == '__main__':
    unittest.main()
