from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_blank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_blank.append(new_question)

quiz = QuizBrain(question_blank)
quiz.next_question()
