from DatabaseControllers.FirebaseConfig import db
#import FirebaseConfig 

#db = FirebaseConfig.db


class ScoreDB:
    def add_or_update_score(self,studentID,subject,level,score):
        db.child("scores").child(studentID).child(subject).child(level).set(score)

    def get_all_score(self):
        scoreList = db.child("scores").get()
        return scoreList.val()

    def get_single_score(self,studentID):
        scoreList = db.child("scores").child(studentID).get()
        return scoreList.val()

    def delete_score(self, studentID):
        db.child("scores").child(studentID).remove()


#if __name__ == "__main__":

    #test = ScoreDB()
    #print(test.add_or_update_score(
        #"-MluIlic4pAOT7Dk8Fuq", "fraction", "level 1", 10))


