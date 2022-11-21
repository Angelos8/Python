from pickle import TRUE
from typing import Text


class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        #the above expression returns true or false
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        player_answer = input(f'Q.{self.question_number}: {current_question.text} (True/False): ')
        self.check_answer(player_answer, current_question.answer)

  
    def check_answer(self,player_answer,correct_answer):
        if player_answer.lower() ==  correct_answer.lower():
            self.score += 1
            print("You are right!")
        else:
            print("You are wrong!")
        print(f"Score: {self.score}/{self.question_number}\n")