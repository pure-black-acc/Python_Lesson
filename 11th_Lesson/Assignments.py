class BurgerStore:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu
    def show_menu(self):
        print(f"Our signiture menu is {self.menu}")
    def cook(self):
        print(f"{self.menu} order has been detected")
    
class KoreaStore(BurgerStore):
    def __init__(self, name):
        super().__init__(name, "불고기버거")
        self.name = name
    def cook(self):
        print(f"Cooking korean style {self.menu}")

class JapanStore(BurgerStore):
    def __init__(self, name,):
        super().__init__(name, "데리야끼버거")
        self.name = name
    def cook(self):
        print(f"Cooking Japan style {self.menu}")

class USAStore(BurgerStore):
    def __init__(self, name):
        super().__init__(name, "치즈버거")
        self.name = name
    def cook(self):
        super().cook()
        print(f"Cooking usa style {self.menu}")


k = KoreaStore("맥도날드 한국")
j = JapanStore("맥도날드 일본")
u = USAStore("맥도날드 미국")
k.show_menu()
k.cook()
j.show_menu()
j.cook()
u.show_menu()
u.cook()

