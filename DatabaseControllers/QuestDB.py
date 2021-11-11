from FirebaseConfig import db


emptyQuest = {
    "listofQuestionID":["test1"],
    "listofStudentID":["test1"],
    "subject": "",
    "createdBy":""
}

class QuestDB:
    def add_quest(self,quest):
        db.child("quests").push(quest)

    def get_quest(self):
        questList = db.child("quests").get()
        return questList.val()

    def update_quest(self,key,newQuest):
        db.child("quests").child(key).update(newQuest)

    def delete_quest(self,key):
        db.child("quests").child(key).remove()

    def get_single_quest(self,questID):
        questList = db.child("quests").get()
        for quest in questList.each():
            if(quest.key() == questID):
                return quest.val()

        return -1

    def add_questionID(self,questID,questionID):
        quest = self.get_single_quest(self,questID)
        questionList = quest["listofQuestionID"]
        questionList.append(questionID)
        db.child("quests").child(questID).update({"listofQuestionID":questionList})

    def add_studentID(self,questID,studentID):
        quest = self.get_single_quest(QuestDB,questID)
        studentList = quest["listofStudentID"]
        studentList.append(studentID)
        db.child("quests").child(questID).update({"listofQuestionID":studentList})


emptyQuest = {
    "listofQuestionID":["test1"],
    "listofStudentID":["test1"],
    "subject": "math",
    "createdBy":"Ms Tan"
}

questdb = QuestDB()
questdb.add_quest(emptyQuest)
# get_single_quest()





