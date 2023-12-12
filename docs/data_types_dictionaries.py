# Class 초기화 방법
dict_initial = {}    # empty
dict_initial = dict() # empty

list_car_info = ['Ford', 'Mustang', 1964 , 2500]

# key(str) : value(여러 변수 종류 가능, 변수 범위 무제한(dictionary, class 같은거 가능))
dict_carinfo = {
"brand": "Ford",
"model": "Mustang",
"year": 1964,
"items": []
}
model = dict_carinfo["model"]   #list에선 인덱스 번호로 찾았지만 이건 key로 찾음
print("dict_carinfo에 있는 model name : {}".format(model))

# key 로 인한 값 변경
dict_carinfo['year'] = 1970
# 새로운 key와 값 정의
dict_carinfo['color'] = "red"
dict_carinfo['color'] = ["red", "yellow", "brown"]
pass