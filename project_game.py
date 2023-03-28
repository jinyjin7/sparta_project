import random 

print( " ")
print("-------------------------------------------")
print("안녕하세요 지금부터 게임을 시작하겠습니다.\nYes or Yes")
print("-------------------------------------------")
print( " ")


class Character:
    # 모든 캐릭터의 모체가 되는 클래스
    def __init__(self, name, hp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power

    

    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"\n{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"\n{other.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f"{self.name}의 HP : {self.hp}/{self.max_hp}")

     
        # 플레이어 클레스
class Player1(Character):            
    def __init__(self, name, hp, power, ma_power,mp):
        super().__init__(name, hp, power)
        # 마법 공격
        self.name = input("\033[33m플레이어 이름을 입력하세요:\033[0m\n ")
        self.magic_power = ma_power
        self.magic_mp = mp
        self.max_mp = mp


    # 플레이어의 공격    
    def attack(self, other):
        # 공격 선택
            attack_choice = input("공격을 숫자로 입력하세요 : \n1. 일반공격, 2. 마법공격\n")
        # 일반 공격할 경우
            if attack_choice == "1":
                damage = random.randint(self.power - 2, self.power + 2)
                other.hp = max(other.hp - damage, 0)
                print(f"\n{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
                if other.hp == 0:
                    print(f"\t{other.name}이(가) 쓰러졌습니다.")


         # 마법 공격할 경우
            elif attack_choice == "2":
                # 마나가 충분한지 확인하기
                if self.magic_mp >= 10:
                    #공격시 마나가 닳도록 설정
                    self.magic_mp -= 10
                    damage = random.randint(self.magic_power - 1, self.magic_power + 5)
                    other.hp = max(other.hp - damage, 0)
                    print(f"\n{self.name}의 마법공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
                    if other.hp == 0:
                        print(f"\n{other.name}이(가) 쓰러졌습니다.")
                else :
                    #마나가 부족한 경우
                    print("\n마나가 부족합니다. 일반공격으로 대체합니다.")
                    damage = random.randint(self.power - 2, self.power + 2)
                    other.hp = max(other.hp - damage, 0)
                    print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
                    if other.hp == 0:
                        print(f"{other.name}이(가) 쓰러졌습니다.")

            elif attack_choice.isdigit() == False:
                print("\033[33m숫자로만 입력해주세요.\n공격을 안하고 한턴 넘어갑니다.\033[0m\n")

            elif int(attack_choice) < 1 or int(attack_choice) > 2:
                print("\033[33m1 또는 2 중에서 선택해주세요.\n공격을 안하고 한턴 넘어갑니다.\033[0m\n")

        
            else :
                print("정상적인 접근이 아닙니다. 다시 시도해주세요")
                return attack_choice


                                

    def show_status(self):
        super().show_status()
        print(f"{self.name}의 MP : {self.magic_mp}/{self.max_mp}")
                

# 몬스터 클레스
class FireMonster(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)
        self.hp = hp
                
    def attack(self, other):
        super().attack(other)
            
    def show_status(self):
        super().show_status()

class IceMonster(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)
        self.hp = hp
                
    def attack(self, other):
        super().attack(other)
            
    def show_status(self):
        super().show_status()

class ThunderMonster(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)
        self.hp = hp
                
    def attack(self, other):
        super().attack(other)
            
    def show_status(self):
        super().show_status()
                


# 게임 진행하기
player1 = Player1(name=input(),hp=200, power=10, ma_power=15, mp=50)
fire_monster = FireMonster(name="파이어", hp=100, power=6)
Ice_monster = IceMonster(name="프리저", hp=110, power=15)
Thu_monster = ThunderMonster(name="썬더", hp=100, power=20)

monsters = [fire_monster, Ice_monster, Thu_monster]

# 랜덤한 몬스터 선택하기
selected_monster = random.choice(monsters)

# 선택된 몬스터 출력하기
print("\n야생의", selected_monster.name, "가 나타났다!")

turn = random.randrange(0, 2) # 홀, 짝으로 턴 변경 

#공격 반복문
while True:

    player1.attack(selected_monster)
    selected_monster.show_status()

    selected_monster.attack(player1)
    player1.show_status()
    
    if player1.hp == 0:
        print(f"{player1.name}이(가) 패배")
        break
    
    elif selected_monster.hp == 0:
        print(f"{player1.name}이(가) 승리")
        break

    else: 
        print ("게임을 계속합니다.\n")

