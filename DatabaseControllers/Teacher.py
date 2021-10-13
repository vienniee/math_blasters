from FirebaseConfig import db

emptyTeacher = {
    "name":"",
    "email":""
}


def add_teacher(teacher):
    db.child("teachers").push(teacher)

def get_teacher():
    teacherList = db.child("teachers").get()
    return teacherList

def update_teacher(key,newTeacher):
    db.child("teachers").child(key).update(newTeacher)

def delete_teacher(key):
    db.child("teachers").child(key).remove()

