# list로 어떤 data를 access 할 때는 주로 dictionary 활용. (list의 index 변화가 일어났을 때 내가 원하는 값 도출하지 못할 수도 있기 때문)
# Class 초기화 방법
dict_initial = {} #empty
dict_initial = dict() #class 이름이 dict

list_car_info = ['Ford', 'Mustang', 1964]      # 종류가 다른 datatype을 묶음. # 유지보수가 힘듦(각 값의 정보를 식별하기 어려움). # 

# key : value
# ""  : str, int, list, dictionary, ...
dict_car_info = {
  "brand": "Ford",  
  "model": "Mustang",
  "year": 1964,
  "items" : list_car_info
}
model=dict_car_info["model"]
print("dict_car_info의 model name : {}".format(model))

# key를 이용해서 값 변경
dict_car_info["year"]=1970
# dict_car_info={'brand': 'Ford', 'model': 'Mustang', 'year': 1970, 'items': ['Ford', 'Mustang', 1964]}

# key 추가 = 변수 생성과 같음
dict_car_info['color'] = "red"
# dict_car_info={'brand': 'Ford', 'model': 'Mustang', 'year': 1970, 'items': ['Ford', 'Mustang', 1964], 'color': 'red'}

# key value 변경
dict_car_info["color"]=["red", "yellow", "brown"]
# dict_car_info={'brand': 'Ford', 'model': 'Mustang', 'year': 1970, 'items': ['Ford', 'Mustang', 1964], 'color': ['red', 'yellow', 'brown']}
pass

# key remove = pop()
dict_car_info.pop("items")
# dict_car_info={'brand': 'Ford', 'model': 'Mustang', 'year': 1970, 'color': ['red', 'yellow', 'brown']}


