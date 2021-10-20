import unittest
from validSentences import (
    sentence_validator, validate_first_character, validate_ending, validate_quotations, validate_full_stops, validate_numerals
)

class TestCaseScenarios(unittest.TestCase):

    def test_success_scenarios(self):
        self.assertTrue(sentence_validator('The quick brown fox said "hello Mr lazy dog".'))
        self.assertTrue(sentence_validator('The quick brown fox said hello Mr lazy dog.'))
        self.assertTrue(sentence_validator('One lazy dog is too few, 13 is too many.'))
        self.assertTrue(sentence_validator('One lazy dog is too few, thirteen is too many.'))
        self.assertTrue(sentence_validator('How many "lazy dogs" are there?'))

    def test_invalid_scenarios(self):
        self.assertFalse(sentence_validator('The quick brown fox said "hello Mr. lazy dog".'))
        self.assertFalse(sentence_validator('the quick brown fox said "hello Mr lazy dog".'))
        self.assertFalse(sentence_validator('"The quick brown fox said "hello Mr lazy dog."'))
        self.assertFalse(sentence_validator('One lazy dog is too few, 12 is too many.'))
        self.assertFalse(sentence_validator('Are there 11, 12, or 13 lazy dogs?'))
        self.assertFalse(sentence_validator('There is no punctuation in this sentence'))

    def test_validate_first_character(self):
        self.assertFalse(validate_first_character(''))
        self.assertFalse(validate_first_character('ciaran'))
        self.assertTrue(validate_first_character('Ciaran'))
        self.assertFalse(validate_first_character('ciCran'))
        
    def test_validate_ending(self):
        self.assertFalse(validate_ending(''))
        self.assertFalse(validate_ending('ciaran'))
        self.assertTrue(validate_ending('ciaran?'))
        self.assertTrue(validate_ending('ciaran.'))
        self.assertTrue(validate_ending('.'))

    def test_validate_quotations(self):
        self.assertFalse(validate_quotations('"""'))
        self.assertFalse(validate_quotations('"'))
        self.assertFalse(validate_quotations(''))

    def test_validate_full_stops(self):
        self.assertFalse(validate_full_stops('ci.ar.an'))
        self.assertFalse(validate_full_stops('Mr. ciaran.'))
        self.assertTrue(validate_full_stops('Mr ciaran.'))

    def test_validate_numerals(self):
        self.assertFalse(validate_numerals('I am 1'))
        self.assertFalse(validate_numerals('I am either 1,2,3 or 4 5 6 or 7,8,9,10,11'))
        self.assertTrue(validate_numerals('I am One'))

if __name__ == '__main__':
    unittest.main()