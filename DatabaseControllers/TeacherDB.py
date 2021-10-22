from FirebaseConfig import db

emptyTeacher = {
    "name":"",
    "email":"",
    "listOfQuestID":["test"]
}

teacher = {
    "name":"hu soon",
    "email":"husoon98@email.com",
    "listOfQuestID":[]
}


class TeacherDB:
    def add_teacher(self, teacher):
        db.child("teachers").push(teacher)

    def get_teacher(self):
        teacherList = db.child("teachers").get()
        return teacherList.val()

    def update_teacher(self, key, newTeacher):
        db.child("teachers").child(key).update(newTeacher)

    def delete_teacher(self, key):
        db.child("teachers").child(key).remove()

    def get_single_teacher(self, teacherID):
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

teacherDB = TeacherDB()
teacherDB.add_teacher(teacher)

