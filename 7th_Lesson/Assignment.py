# class anim:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def speak(self, bark):
#         print(f"{self.name} and {bark}")

# dog = anim("dog", 3)
# cat = anim("cat", 5)

# dog.speak("bark")
# cat.speak("meow")


class char:
    def __init__(self, name, hp, atk, maxhp):
        self.name = name
        self.hp = hp
        self.att = atk
        self.maxhp = maxhp
        self.vaild = True

    def atk(self, target):
        #target.name = target
        print(f"{self.name} has attacked to {target.name}")
        if self.hp <= 0:
            print("Cannot perform Action! No Dmg applied")
            pass
        else:
            target.dmg(self.att)
        
        

    def dmg(self, dmg):
        self.hp -= dmg
        if self.hp<= 0:
            self.hp = 0
            self.vaild = False
        print(f"{self.name} took {dmg} points of dmg, and has {self.hp}hp left")
       

    def stats(self):
        print(f"has {self.hp}hp left")
        if self.vaild == False:
            print(f"cannot Atk!")

    def heal(self, dmg):
        if self.hp<= 0:
            self.vaild = True
        self.hp += dmg
        if self.hp >= 100:
            self.hp = 100

        print(f"{self.name} healed {dmg} points of hp, and has {self.hp}hp total")
        


char1 = char("idk", 100, 480, 100)
char2 = char("boss", 1000, 50, 1000)

char2.atk(char1)
char1.atk(char2)
char2.atk(char1)
char1.atk(char2)
char1.heal(1000)
char1.atk(char2)

