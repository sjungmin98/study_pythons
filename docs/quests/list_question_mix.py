
def mixed_questions() :
    mixed_questions = [
        {
        "question": "",
        "answer": [],
        "correct_index": 0,
        "score": 0
        },
            {
        "question": "",
        "answer": [],
        "correct_index": 0,
        "score": 0
        },
            {
        "question": "",
        "answer": [],
        "correct_index": 0,
        "score": 0
        }
    ]
    pass
    for dict_loop in range(len(mixed_questions)) :
        mixed_questions[dict_loop]["question"]=input("quest : ")
        for answer_loop in range(4) :
            mixed_questions[dict_loop]["answer"].append(input("answer : "))
        mixed_questions[dict_loop]["correct_index"]=input("correct_index : ")
        mixed_questions[dict_loop]["score"]=input("score : ")
    print(mixed_questions)
mixed_questions()
