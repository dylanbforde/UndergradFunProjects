
class Quiz():
    def __init__(self, prompt, choices, topic):
        self._prompt = prompt
        self._choices = choices
        self._topic = topic
    
    def getQuestions(self):
        return self._prompt
    def setQuestions(self, newPrompt):
        self._prompt = newPrompt
    questions = property(getQuestions, setQuestions)
    
    def getChoices(self):
        return self._choices
    def setChoices(self, newChoices):
        self._choices = newChoices
    choices = property(getChoices, setChoices)

    def getAnswers(self):
        return self._answers
    def setAnswers(self, newAnswers):
        self._answers = newAnswers
    answers = property(getAnswers, setAnswers)

    def runQuiz(self):
        print(f'the ultimate {self._topic} quiz\n')
        score = 0

        for num in len(prompt):
            answer = input(f'{self._prompt[num]}\n{self._choices}')
        if answer.lower() == self._answers[num]:
            score += 1
            print('You are correct!')
        else:
            print('Unfortunately, you are not correct.')
        
Quiz(Questions_multiple_choice, multiple_choice_answers, 'Harry Potter')

if __name__ == '__main__':
    print(Quiz.getQuestions)



        

        