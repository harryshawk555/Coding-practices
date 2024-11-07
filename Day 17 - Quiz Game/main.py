from data import question_data,new_questions
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []

#for q in question_data:
#    question_bank.append(Question(q["text"],q["answer"]))

for q in new_questions:
    question_bank.append(Question(q["question"],q["correct_answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_questions():
    quiz.next_question()
quiz.results()