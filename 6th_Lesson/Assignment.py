# class Name:
#     def __init__(self, name, age):
#            self.name = name
#            self.age = age
#     def intro(self):
#             print(f"Hi, my name is {self.name}, and my age is {self.age}")
    
# info1 = Name("idk", 18)
# info1.intro()

# class Car:
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed
#     def accel(self):
#         self.speed += 10
#         print(f"current speed: {self.speed}")
    
# car1 = Car("TIDK", 100)
# car1.accel()
# car1.accel()
# car1.accel()

class char:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.vaild = True
    def atk(self):
        print(f"{self.name} has attacked")
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
        print(f"{self.name} healed {dmg} points of hp, and has {self.hp}hp left")
        


char1 = char("idk", 100)
char1.atk()
char1.dmg(80)
char1.heal(50)
char1.stats()
char1.dmg(80)
char1.stats()
char1.heal(50)
char1.stats()

# class bank:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"{amount} has been added and current balance is {self.balance}")
#     def withdraw(self, amount):
#         self.balance -= amount
#         print(f"{amount} has been withdrawn and current balance is {self.balance}")


# bank1 = bank("idk", 100)
# bank1.deposit(500)
# bank1.withdraw(80)