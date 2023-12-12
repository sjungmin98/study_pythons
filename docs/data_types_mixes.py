# list 안에서 dictionary 구성

# key(str) : value(여러 변수 종류 가능
dict_carinfo_mustang = {
"brand": "Ford",
"model": "Mustang",
"year": 1964,
"price": 30000
}

dict_carinfo_sonata = {
"brand": "Hyundai",
"model": "Sonata",
"year": 2020,
"color": "Black",
"price": 30000
}

list_carinfo = [dict_carinfo_mustang, dict_carinfo_sonata]

# list_carinfo = [
#     {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964,
#     "price": 30000
#     },
#     {
#     "brand": "Hyundai",
#     "model": "Sonata",
#     "year": 2020,
#     "color": "Black",
#     "price": 30000
#     } 
# ]

# list_carinfo.append(
#     {
#     "brand": "Kia",
#     "model": "K5",
#     "year": 2021,
#     "color": "White",
#     "price": 28000
#     }
# )

pass
dict_carinfo_k5 = {
        "brand": "Kia",
        "model": "K5",
        "year": 2021,
        "color": "White",
        "price": 28000
    }

list_carinfo.append(dict_carinfo_k5)

# list_carinfo 안에 있는 index[0]에 있는 "model": "mustang" 접근 방법
dict_carinfo_index_first = list_carinfo[0]
dict_carinfo_index_first['model']
pass
list_carinfo[0]['model']
pass

#for로 각 dict 정보 출력 
for dict_carinfo in list_carinfo :
    brand = dict_carinfo['brand']
    model = dict_carinfo['model']
    print("브랜드 : {}, 모델 : {}".format(brand, model))
    pass