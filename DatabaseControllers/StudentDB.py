
from DatabaseControllers.FirebaseConfig import db
# import firebase as firebase

# db = firebase.database()

student = {
    "name":"",
    "email":"",
    "class":"",
    "character":"",
    "progress":{
        "math":{
            "minigame1":0,
            "minigame2": 0
        },
        "science": {
            "minigame1": 0,
            "minigame2": 0
        },
    },
    "achievements":{
        "choose your character": {
            "achievementDescription":"",
            "achievement criteria":"",
            "completed":False
        }
    }
    ,
    "Quests":[]
}

#Changed to static implementation

class StudentDB:

    def add_student(key,studentData):
        db.child("students").child(key).set(studentData)

    def get_student(key):
        return db.child("students").child(key).get().val()
    
    def get_all_students():
        return db.child("students").get().val()

    def update_student(key, newStudent):
        db.child("students").child(key).update(newStudent)

    def delete_student(key):
        db.child("students").child(key).remove()

    


if __name__ == "__main__":

    student = {
        "name": "kelvin",
        "email": "kelv",
        "class": "qweqwe",
        "character": "qweqwewq",
        "progress": {
            "math": {
                "minigame1": 0,
                "minigame2": 0
            },
            "science": {
                "minigame1": 0,
                "minigame2": 0
            },
        },
        "achievements": {
            "choose your character": {
                "achievementDescription": "qweqwe",
                "achievement criteria": "qweqwe",
                "completed": False
            }
        },
        "Quests": []
}


    student_Controller = StudentDB()

    # student_Controller.add_student(student)
    # print(student_Controller.get_student().key())
    for user in student_Controller.get_student().each():
        print(user.key())  # Morty
        print(user.val())
