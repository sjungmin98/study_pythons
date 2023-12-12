# mixed_questions = [
#     {
#         "question": "Python이라는 언어는 어떤 특징을 가지고 있나요?",
#         "answer": ["고급 프로그래밍 언어로 간결하고 읽기 쉬운 문법을 가짐", "HTML과 같은 마크업 언어", "하드웨어를 직접 제어할 수 있는 저급 언어", "한 줄씩 소스 코드를 해석해서 실행하지 않는 언어"],
#         "correct_index": 0,
#         "score": 10
#     },
#     {
#         "question": "Python에서 'for' 반복문을 어떻게 사용하나요?",
#         "answer": ["시퀀스나 다른 반복 가능한 객체의 원소들을 순회", "'for'는 Python에 존재하지 않는 키워드임", "'for' 키워드를 사용하여 조건이 참인 동안 반복", "'for' 키워드를 사용하여 특정 횟수만큼 반복"],
#         "correct_index": 0,
#         "score": 10
#     },
#     {
#         "question": "Python에서 클래스를 어떻게 정의하고 사용하나요?",
#         "answer": ["'class' 키워드를 사용하여 정의", "'object' 키워드를 사용하여 정의", "'cls' 키워드를 사용하여 정의", "'new' 키워드를 사용하여 정의"],
#         "correct_index": 0,
#         "score": 10
#     }]

def get_mixed_questions():
    
    list_mixed_questions = []

    # input 기능 추가
    for inputs in range(3):
        question = input("question : ")

        list_mixed_answers = []
        
        answer = input("answer : ")
        list_mixed_answers.append(answer)
        correct_index = input("correct_index : ")
        score = input("score : ")

        # 입력값을 딕셔너리로 저장
        dict_mixed_questions = {
            'question': question,
            'answer': list_mixed_answers,
            'correct_index': correct_index,
            'score': score
        }
        list_mixed_questions.append(dict_mixed_questions)

    return list_mixed_questions


def print_mixed_questions(list_mixed_questions):
    
    # 입력값 출력
    for mixed_questions in list_mixed_questions:
        print("\"question\" : {}".format(mixed_questions['question']))
        print("\"answer\" : {}".format(mixed_questions['answer']))
        print("\"correct_index\" : {}".format(mixed_questions['correct_index']))
        print("\"score\" : {}".format(mixed_questions['score']))

# 함수 호출
mixed_questions_data = get_mixed_questions()
print_mixed_questions(mixed_questions_data)