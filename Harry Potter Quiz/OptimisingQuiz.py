class QuizQuestions:
    def __init__(self, questions, choices, answers, num_correct, question_number) -> None:
        # quiz basics
        self.questions = questions
        self.choices = choices
        self.answers = answers
        self.num_correct = num_correct
        self.question_number = question_number

    
    def runQuiz(self):
        # quiz body
        for index in range(-1, len(self.questions) - 1):
            # print Q&A and take input
            print(index)
            print(f"Question: {self.question_number}")
            print(f'{self.questions[index]}')
            userAnswer = input(f'{self.choices[index]} \n')

            # check to see if the answer that is input is correct
            if userAnswer.lower() == self.choices[index][self.answers[index]].lower():
                print("You are Correct!")
                self.num_correct += 1
            else:
                print("Sorry, you are incorrect.")
            print(f"Quiz Result: {self.num_correct / self.question_number * 100}%\n")
            self.question_number += 1
        return self.num_correct, self.question_number


questions = ['I dont think you should be an Auror, Harry... ... The Aurors are part of the ___', 'Oh hello Harry, did you know one of your eyebrows is bright ___', 'Which of the following shops CANNOT be found in Diagon Alley',
'First name of the barman who works at the Leaky Cauldron', 'Enter, stranger, but take heed...', 'Harry met his first fellow Hogwarts student at Madam Malkins Robes, who was it?',
'What was the name of the pygmy puff Ginny bought from Weasleys Wizard Wheezes', 'In ootp what three things are scattered on the floor of The Knight Bus when Harry, Ron, and Hermione are heading back to Hogwarts',
'What are the name of Severus Snapes parents','Who is the author of Unfogging The Future', 'What is Harry\'s date of birth']
choices = [['humdinger league','rotfang conspiracy','durmstrang plot','mugwump scheme'], ['purple', 'yellow','red','green'],['Weasleys Wizard Wheezes','Eyelops Owl Emporium','honeydukes','ollivanders'],
['tom','aberforth','greg', 'theo'],['the verse you should take time to read', 'take only what you dearly need', 'we know of every darkest deed', 'of what awaits the sin of greed'],['draco','hermione', 'ronald', 'terry'],
['hugo', 'arnold', 'barry','craig'],['egg shells, digestives, and bat wings', 'cat hair, feathers, and cat litter', 'frogspawn, cockroaches, and custard creams', 'beetle dung, dead wassps, and a mug of tea'],
['Theodore Snape and Ethel Prince','Tripp Snape and Eliane Prince','Toby Snape and Ellen Prince','Tobias Snape and Eileen Prince'],['Selina Sapworthy', 'Cassandra Vablatsky','Greta Catchlove', 'Galatea Merrythought'],
['1980', '1990', '1981','1991']]
answers = [1, 1, 2, 0, 3, 0, 1, 2, 3, 1]

questions2 = ['In which book did Harry Potter first meet Luna Lovegod?', 'In which book does Harry Potter meet Rufus Scrimgeour?', 'In which book is Sirius black first mentioned?',
'In which book did Harry Potter first meet Horace Slughorn?', 'In which book did Harry Potter first meet Cho Chang?', 'In which book did Harry Potter first meet Charlie Weasley?',
'In which book did Harry Potter first meet Narcissa Malfoy?', 'In which book did Harry Potter first meet Zacharias Smith?']
choices2 = [["Order of The Pheonix", "Half Blood Prince", "Philosopher's Stone", "Prisoner of Azkaban", "Goblet of Fire"]] * len(questions2)
answers2 = [0, 1, 2, 1, 3, 4, 4, 0]

if __name__ == "__main__":
    hpQuiz = QuizQuestions(questions, choices, answers, 0, 1)
    num_correct_quiz, question_num_quiz = hpQuiz.runQuiz()
    hpQuizP2 = QuizQuestions(questions2, choices2, answers2, num_correct_quiz, question_num_quiz)
    hpQuizP2.runQuiz()