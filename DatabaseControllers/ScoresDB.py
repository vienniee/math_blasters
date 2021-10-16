from FirebaseConfig import db

emptyScore = {
    "studentID":"",
    "minigame":"",
    "level":"",
    "TotalScore":0
}

class ScoreDB():
    def add_score(score):
        db.child("scores").push(score)

    def get_score():
        scoreList = db.child("scores").get()
        return scoreList.val()

    def update_score(key,newscore):
        db.child("scores").child(key).update(newscore)

    def delete_score(key):
        db.child("scores").child(key).remove()