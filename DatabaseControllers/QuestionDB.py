
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

    def get_all_questions(self):

        temp ={}

        questionList = db.child("questions").get()
        questiondb =  questionList.val()

        for subject in questiondb:
            #print(subject)
            for level in questiondb[subject]:
                #print(level)
                for question_id in questiondb[subject][level]:
                    #print(question_id)
                    temp[question_id] = questiondb[subject][level][question_id]

        return temp

    def get_single_question(self,questionID):
        db = QuestionDB()
        temp = db.get_all_questions()

        return temp[f'{questionID}']


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
    "questionText": "2+1+2+8+1-1=x",
    "optionA": "2",
    "optionB": "3",
    "optionC": "5",
    "optionD": "14",
    "correctAnswer": "2",
}
    
    test = QuestionDB()
    print(test.get_single_question("-MoI_Crd-AGYfoiRcifX"))
