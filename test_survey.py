import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):


    def test_store_single_response(self):
        question = "What language do you first learn to speak ?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('Python')
        self.assertIn('Python', my_survey.responses)

    def test_store_few_responses(self):
        question = "What language do you first learn to speak ?"
        my_survey = AnonymousSurvey(question)
        responses = ['Python','Ruby',"C#"]

        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
    unittest.main
