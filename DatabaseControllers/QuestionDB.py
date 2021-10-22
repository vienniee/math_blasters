from DatabaseControllers.FirebaseConfig import db


emptyQuestion = {
    "minigame":"",
    "level":"",
    "questionText":"",
    "optionA":"",
    "optionB":"",
    "optionC":"",
    "optionD":"",
    "correctAnswer":"",
}

# newQuestion = {
#     "minigame":"test",
#     "level":"test",
#     "questionText":"tes",
#     "optionA":"1",
#     "optionB":"2",
#     "optionC":"3",
#     "optionD":"4",
#     "correctAnswer":"1",
# }


class QuestionDB():
    def add_questions(question):
        db.child("questions").push(question)

    def get_questions():
        questionList = db.child("questions").get()
        return questionList.val()

    def update_questions(key,newQuestion):
        db.child("questions").child(key).update(newQuestion)

    def delete_questions(key):
        db.child("questions").child(key).remove()

QuestionDB.add_questions(emptyQuestion)
# result = get_questions()
# print(result['-MluRa7WuoXOOWc0gPGe'])
# update_questions("-MluRa7WuoXOOWc0gPGe",newQuestion)
# delete_questions("-MluQizsvARWcyLAlbqp")