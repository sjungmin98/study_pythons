# function만 사용 시 제한 극복 -> class
def attack(damage, health):
    health = health - damage
    return health

# First enemy
name = "first"
health_first = 120
damage = 0
attack = 5

# Second enemy
name = "second"
health_second= 200
damage = 0
attack = 10

class Enemy:
    def __init__(self, name, health) :    # 생성자
        self.name = name
        self.health = health
        self.damage = 0
        pass

    def attack(self, damage) :
        self.health = self.health - damage
        return self.health    
   
    def function_name(self) :   # self 키워드 필요(class 소속 확인용)
        pass
        return 0
   
first_enemy = Enemy('first', 150)    # 자신 자원(functions과 varables) 확인
second_enemy = Enemy('second', 300)
pass
