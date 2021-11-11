from DatabaseControllers.FirebaseConfig import db
# import FirebaseConfig

# db = FirebaseConfig.db

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
    def add_question(self,subject,level,question):
        db.child("questions").child(subject).child(level).push(question)

    def get_questions(self, subject, level):
        questionList = db.child("questions").child(subject).child(level).get()
        return questionList.val()

    # db.child("users").child("Morty").update({"name": "Mortiest Morty"})
    def update_questions(self, subject, level, questionID, newQuestion):
        db.child("questions").child(subject).child(
            level).child(questionID).update(newQuestion)

    def delete_questions(self, questionID):
        db.child("questions").child(questionID).remove()


if __name__ == "__main__":


    data = {
    "subject": "algebra",
    "level": "level 1",
    "questionText": "2+1+2+8+1-11=x",
    "optionA": "2",
    "optionB": "3",
    "optionC": "5",
    "optionD": "14",
    "correctAnswer": "2",
}
    
    test = QuestionDB()
    print(test.add_question("algebra","level 1",data))
