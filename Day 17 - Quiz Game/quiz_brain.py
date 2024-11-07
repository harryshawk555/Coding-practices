class QuizBrain:

    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.no_questions = len(questions)
        self.correct_answers = 0

    def next_question(self):
        print("Q"+str(self.question_number+1)+". "+
              self.question_list[self.question_number].text)
        self.check_question()
        self.question_number += 1
        
    def still_questions(self):
        if self.question_number < self.no_questions:
            return True
        else:
            return False

    def check_question(self):
        answer = input("Answer: ")
        if answer.lower() == self.question_list[self.question_number].answer.lower():
            print("Correct!!!")
            self.correct_answers += 1
        else:
            print("Wrong!!!\n The correct answer was: "+self.question_list[self.question_number].answer)

    def results(self):
        if self.correct_answers == self.no_questions:
            print("Well Done. You got "+ str(self.correct_answers)+"/"+str(self.no_questions))
        else:
            print("You got "+ str(self.correct_answers)+"/"+str(self.no_questions)+". Better luck next time!")

