from DatabaseControllers.QuestionDB import QuestionDB

def Questionfilter(topic,level):
    difficulty = level
    subject = topic
    # load question list
    # questions with 4 options, last is answer
    qn_db = QuestionDB()
    qlist1 = qn_db.get_questions()
    qlist2 = []
    for i in qlist1:
        qlist2.append(str(qlist1[i]))  # converting into list
    qlist3 = list(qlist2)
    print(qlist3)
    qlist4 = []
    for i in range(len(qlist3)):
        a = qlist3[i].replace("{'correctAnswer': ", "")
        b = a.replace("'level': ", "")
        c = b.replace("'optionA': ", "")
        d = c.replace("'optionB': ", "")
        e = d.replace("'optionC': ", "")
        f = e.replace("'optionD': ", "")
        g = f.replace("'questionText': ", "")
        k = g.replace("'subject': ", "")
        j = k.replace("'", "")
        h = j.replace("}", "")
        i = h.replace(" ", "")
        qlist4.append(i)
    qlist5 = []
    order = [1, 7, 6, 2, 3, 4, 5, 0]
    for i in range(len(qlist4)):
        output = qlist4[i].split(",")
        output1 = [output[x] for x in order]
        if output1[0] != "":
            qlist5.append(output1)
    qlist6 = []
    print(qlist5)
    for i in range(len(qlist5)):
        if qlist5[i][0] == difficulty:
            print(qlist5[i][1])
            print(subject)
            if qlist5[i][1] == subject:
                print("pass")
                qlist6.append(qlist5[i][2:8])
    print(qlist6)
    question_list = qlist6
    return question_list