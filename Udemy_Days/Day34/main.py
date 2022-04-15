from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# takes from the data the question and the answer and make a list of them
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


#call the to main classes the quizbrain whitch requires the list of questions
quiz = QuizBrain(question_bank)
#the ui class tha requires the quiz variable with the values of Quizbrain Class
quiz_ui = QuizInterface(quiz)

