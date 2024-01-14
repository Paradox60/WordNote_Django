class Question_card:
    def __init__(self, question_word, correct_answer, incorrect_answer1, incorrect_answer2, incorrect_answer3, base_id):
        self.question_word = question_word
        self.correct_answer = correct_answer
        self.incorrect_answer1 = incorrect_answer1
        self.incorrect_answer2 = incorrect_answer2
        self.incorrect_answer3 = incorrect_answer3
        self.base_id = base_id

    def __str__(self):
        return f'{self.question_word} - {self.correct_answer} - {self.incorrect_answer1} - {self.incorrect_answer2} - {self.incorrect_answer3} - {self.base_id}'

class Library_card:
    def __init__(self, word, translate, progress, time, base_id):
        self.word = word
        self.translate = translate
        self.progress = progress
        self.time = time
        self.base_id = base_id

    def __str__(self):
        return f'{self.word} - {self.translate} - {self.progress} - {self.time} - {self.base_id}'