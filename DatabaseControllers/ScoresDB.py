from DatabaseControllers.FirebaseConfig import db

emptyScore = {
    "studentID":"",
    "minigame":"",
    "level":"",
    "TotalScore":0
}

class ScoreDB:
    def add_score(self,score):
        db.child("scores").push(score)

    def get_score(self):
        scoreList = db.child("scores").get()
        return scoreList.val()

    def update_score(self, key, newscore):
        db.child("scores").child(key).update(newscore)

    def delete_score(self, key):
        db.child("scores").child(key).remove()
