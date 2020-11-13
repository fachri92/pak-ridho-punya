class Hero:
    count = 0
    heroes = []
    # block = 20
    battle_round = 1

    def __init__(self, hero_name):
        # instance variable
        self.name = hero_name
        if self.name == 'Saitama':    
            self.hp = 5000
            self.atk = 5000
            Hero.count += 1
            Hero.heroes.append(hero_name)
            self.id = Hero.count
            self.defence = 300
        elif self.name == 'Genos':    
            self.hp = 5000
            self.atk = 2000
            Hero.count += 1
            Hero.heroes.append(hero_name)
            self.id = Hero.count
            self.defence = 150
        elif self.name == 'Atomic Samurai':    
            self.hp = 5000
            self.atk = 3000
            Hero.count += 1
            Hero.heroes.append(hero_name)
            self.id = Hero.count
            self.defence = 175 

    # void function, method tanpa return
    def introduce(self):
        print('My name is', self.name, 'I am a Hero!')

    # method with argumen:
    # def healthUp(self, up):
    #     self.hp += up

    # method with return
    def getHealth(self):
        return self.hp

    #          hero2        hero1
    def attack(self, opponent):
        # print(self.name, 'hit', opponent.name)
        #        hero1.attcked(hero2)
        damage = opponent.attacked(self, self.atk)
        batrep = Hero.battle_report(self, opponent, damage)
        return batrep
        # print(f"{self.name}'s HP is {self.hp} left")
        # print(f"{opponent.name}'s HP is {opponent.hp} left")

    def attacked(self, opponent, atk_opponent):
        # print(self.name, 'hitted by', opponent.name)
        damage = int(atk_opponent/self.defence)
        self.hp -= damage
        return damage

    @classmethod
    def battle_report(cls, attacker, opponent, damage):
        batrep = {
            'Round' : Hero.battle_round,
            'Attacker' : attacker.name,
            'Opponent' : opponent.name,
            'Damage' : damage,
            'Attacker HP Left': attacker.hp,
            'Opponent HP Left': opponent.hp
        }
        Hero.battle_round+=1
        return batrep

# instaciating
play_again = 'y'

while play_again == 'y':
    Hero.battle_round = 1
    print("### Welcome to One Punch Man 1v1 ###")
    print('Hero Available: (1) Saitama; (2) Genos; (3) Atomic Samurai')
    hero1 = int(input('Choose Your First Hero!: '))
    while hero1 > 3:
        print("Can't find hero!")
        print('Hero Available: (1) Saitama; (2) Genos; (3) Atomic Samurai')
        hero1 = int(input('Choose Your First Hero!: '))

    hero2 = int(input('Choose Your Second Hero!: '))
    while hero2 > 3 or hero2 == hero1:
        print("You either choose the same hero as Player 1 nor, you choose not existed hero. Choose another one!")
        print('Hero Available: (1) Saitama; (2) Genos; (3) Atomic Samurai')
        hero2 = int(input('Choose Your Second Hero!: '))
    
    if hero1 == 1:
        hero1 = Hero('Saitama')
    elif hero1 == 2:
        hero1 = Hero('Genos')
    elif hero1 == 3:
        hero1 = Hero('Atomic Samurai')

    if hero2 == 1:
        hero2 = Hero('Saitama')
    elif hero2 == 2:
        hero2 = Hero('Genos')
    elif hero2 == 3:
        hero2 = Hero('Atomic Samurai')

    hero1.introduce()
    hero2.introduce()

    print(f'{hero1.name}: {hero1.hp}')
    print()
    print('VS')
    print()
    print(f'{hero2.name}: {hero2.hp}')

    game_round = []
    while hero1.hp > 0 and hero2.hp > 0:
        game_round.append(hero2.attack(hero1))
        if hero1.hp > 0 and hero2.hp > 0:
            game_round.append(hero1.attack(hero2))
        else:
            break

    if hero1.hp > 0:
        print(f'{hero1.name}, WIN! After {len(game_round)} Rounds')
    else:
        print(f'{hero2.name}, WIN! After {len(game_round)} Rounds')


    see_bat_rep = 'y'
    while see_bat_rep == 'y':
        which_round = int(input('Which round do you want to see the report?: '))
        if which_round < 1 or which_round > len(game_round):
            print('Round Invalid')
        else:
            print(game_round[which_round-1])
            see_bat_rep = input('Do you want to see another report?(y/n): ').lower()
            if see_bat_rep != 'y':
                play_again = input('Do you want to play again?(y/n): ').lower()

# print(Hero.heroes)

# print(Hero.__dict__)

# Private Variable







