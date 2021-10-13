from FirebaseConfig import db

emptyQuest = {
    "ListofQuestionID":[],
    "listofStudentID":[]
}


def add_quest(quest):
    db.child("quests").push(quest)

def get_quest():
    questList = db.child("quests").get()
    return questList

def update_quest(key,newQuest):
    db.child("quests").child(key).update(newQuest)

def delete_quest(key):
    db.child("quests").child(key).remove()

