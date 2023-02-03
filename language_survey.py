from survey import AnonymousSurvey

question = 'What language do you like the most ?'
my_survey = AnonymousSurvey(question)

my_survey.show_questions()
print('Enter "q" at any time to Quit.\n')
while True:
    response = input('Language: ')
    if response == 'q':
        break
    else:
        my_survey.store_response(response)

print("Thank you everyone to participate in the survey")
my_survey.show_results()