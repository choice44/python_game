import random
import os


class Character:
    """
    부모 클래스
    """

    def __init__(self, name, hp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")


class Player(Character):
    """
    플레이어 클래스
    """

    def __init__(self, name, hp, mp, power):
        super().__init__(name, hp, power)
        self.max_mp = mp
        self.mp = mp
        self.magicpower = 20

    def attack(self, other, attack_type):
        # 공격 타입 선택에서 일반공격 입력 시
        if attack_type == "일반공격":
            damage = random.randint(self.power * 0.8, self.power * 1.2)
            other.hp = max(other.hp - damage, 0)
            print(f"\n{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
            if other.hp == 0:
                print(f"\n{other.name}이(가) 쓰러졌습니다.")
        # 공격 타입 선택에서 마법공격 입력 시
        elif attack_type == "마법공격":
            if self.mp < 10:
                print("마나가 부족합니다.")
                return False

            damage = random.randint(
                self.magicpower * 0.8, self.magicpower * 1.2)
            other.hp = max(other.hp - damage, 0)
            print(f"\n{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
            self.mp -= 10

            if other.hp == 0:
                print(f"\n{other.name}이(가) 쓰러졌습니다.")
        # 일반공격 마법공격 이외의 입력을 할 시
        else:
            print("잘못된 입력입니다.")
            return False

        return damage

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp} MP {self.mp}/{self.max_mp}")


class Monster(Character):
    """
    몬스터 클래스
    """

    def attack(self, other):
        damage = random.randint(self.power * 0.8, self.power * 1.2)
        other.hp = max(other.hp - damage, 0)
        print(f"\n{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"\n{other.name}이(가) 쓰러졌습니다.")
            print(f"{other.name}의 패배 ㅜ")


os.system('clear')
# 플레이어 이름 입력
player_name = input("플레이어의 이름을 입력하십시오: ")
player = Player(player_name, 100, 30, 10)
# 몬스터 리스트 생성
monsters = [
    Monster("붉은여우", 50, 5),
    Monster("회색늑대", 70, 10),
    Monster("말코손바닥사슴", 100, 8),
    Monster("침팬지", 100, 10),
    Monster("갈색곰", 200, 20)
]
# 몬스터 리스트에서 랜덤으로 몬스터 선택 후 몬스터 출력
monster = random.choice(monsters)
print(f"\n몬스터 {monster.name}이(가) 출현했습니다.")

# 플레이어 몬스터 모두 체력이 0 초과일 경우 반복
while player.hp > 0 and monster.hp > 0:
    # 현재상태 출력
    print("\n=== 현재상태 === ")
    player.show_status()
    monster.show_status()
    # 공격 타입 선택
    while True:
        attack_type = input("\n공격 타입을 선택하십시오[ 일반공격 / 마법공격]: ")
        os.system('clear')
        attack = player.attack(monster, attack_type)
        if attack:
            break
    # 몬스터 체력이 0이하일 경우 몬스터 공격하지 못하게 브렠
    if monster.hp <= 0:
        print(f"{player.name}의 승리!")
        break

    monster.attack(player)
