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

    def get_quest_by_subject_studentID(self,subject,studentID):
        result = []

        questList = db.child("quests").get()
        for quest in questList.each():
            if quest.val()["subject"] == subject:

                for student in quest.val()["listofStudentID"]:
                    if student == studentID:
                        quest.val()["questID"] = quest.key()
                        result.append(quest.val())

        return result

    def get_single_quest(self,questID):
        questList = db.child("quests").get()
        for quest in questList.each():
            if(quest.key() == questID):
                return quest.val()

        return -1

    def add_questionID(self,questID,questionID):
        # quest = self.get_single_quest(questID)

        # questionList = quest["listofQuestionID"]
        # questionList.append(questionID)
        # db.child("quests").child(questID).update({"listofQuestionID":questionList})

        db.child("quests").child(questID).child(
            "listofQuestionID").push(questionID)

        # questionList = quest["listofQuestionID"]
        # questionList.append(questionID)
        # db.child("quests").child(questID).update({"listofQuestionID":questionList})

        #db.child("quests").child(questID).child("listofQuestionID").push(questionID)

    def add_studentID(self,questID,studentID):
        db.child("quests").child(questID).child("listofStudentID").child(studentID).set(0)

    def update_quest_score(self,questID, StudentID, score):
        db.child("quests").child(questID).child("listofStudentID").child(StudentID).set(score)


if __name__ == "__main__":
    emptyQuest = {
        "listofQuestionID":["test2"],
        "listofStudentID":["test1"],
        "subject": "math",
        "createdBy":"Ms Eng"
    }
    emptyQuest = {
        "listofQuestionID":["test3"],
        "listofStudentID":["test1"],
        "subject": "math",
        "createdBy":"Mr chua"
    }
    questdb = QuestDB()
    # questdb.add_questionID(questID="-MoCiI66M8xDFvM-ThOJ",questionID= "-MoDE0mqW3ulxILVN1Ao")
    emptyQuest = {
        "listofQuestionID": [],
        "listofStudentID": [],
        "subject": "algebra",
        "createdBy": "kelvin"
    }
    questdb.add_questionID("-MoNDiN_4yQxF0_G1Bkq", "-MoDE0mqW3ulxILVN1Ao")



