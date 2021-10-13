from FirebaseConfig import db


emptyQuestion = {
    "minigame":"",
    "level":"",
    "questionText":"",
    "optionA":"",
    "optionB":"",
    "optionC":"",
    "optionD":"",
    "correctAnswer":"",
}


def add_questions(question):
    db.child("/Questions").push(question)

def get_questions():
    questionList = db.child("/Questions").get()
    return questionList

add_questions(emptyQuestion)