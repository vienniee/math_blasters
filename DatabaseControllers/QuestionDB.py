# from DatabaseControllers.FirebaseConfig import db
import FirebaseConfig

db = FirebaseConfig.db

emptyQuestion = {
    "subject":"",
    "level":"",
    "questionText":"",
    "optionA":"",
    "optionB":"",
    "optionC":"",
    "optionD":"",
    "correctAnswer":"",
}

class QuestionDB:
    def add_questions(self,question):
        db.child("questions").push(question)

    def get_questions(self):
        questionList = db.child("questions").get()
        return questionList.val()

    # db.child("users").child("Morty").update({"name": "Mortiest Morty"})
    def update_questions(self,questionID,newQuestion):
        db.child("questions").child(questionID).update(newQuestion)

    def delete_questions(self, questionID):
        db.child("questions").child(questionID).remove()

# QuestionDB.add_questions(emptyQuestion)


if __name__ == "__main__":


    data = {
    "subject": "algebra",
    "level": "1",
    "questionText": "2-2+8+2-2+2+1-3=x",
    "optionA": "1",
    "optionB": "7",
    "optionC": "8",
    "optionD": "10",
    "correctAnswer": "8",
}
    
    test = QuestionDB()
    print(test.add_questions(data))
