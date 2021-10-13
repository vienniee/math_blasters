from FirebaseConfig import db

emptyTeacher = {
    "name":"",
    "email":"",
    "listOfQuestID":[test]
}


class TeacherDB:
    def add_teacher(teacher):
        db.child("teachers").push(teacher)

    def get_teacher():
        teacherList = db.child("teachers").get()
        return teacherList.val()

    def update_teacher(key,newTeacher):
        db.child("teachers").child(key).update(newTeacher)

    def delete_teacher(key):
        db.child("teachers").child(key).remove()

    def get_single_teacher(self,teacherID):
        teacherList = db.child("teachers").get()
        for teacher in teacherList.each():
            if(teacher.key() == teacherID):
                return teacher.val()
        return -1

    def add_questID(self,teacherID,questID):
        teacher = self.get_single_teacher(teacherID)
        questList = teacher["listOfQuestID"]
        questList.append(questID)
        db.child("teachers").child(teacherID).update({"listOfQuestID":questList})

