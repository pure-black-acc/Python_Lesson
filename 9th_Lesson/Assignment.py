import time
class phone:
    def __init__(self, model, max_bat, cur_bat, on):
        self.model = model
        self.max = max_bat
        self.cur = cur_bat      
        self.on = on

    def use_bat(self, amount):
        if self.on == False:
            print(f"Charge before using the phone")
            return

        elif self.cur - amount < 0:
            print(f"Cannot use Battery, requested amount is too large. current: {self.cur}%")
            pass

        elif self.cur - amount == 0:
            self.cur = 0
            print(f"Battery Out, turned off")
            self.on = False
            pass

        else:
            self.cur -= amount
            print(f"Battery used. Current Battery: {self.cur}%")
    
    def charge(self, which):
        if self.on == False:
            print(f"Turning on the phone.")
            self.on = True
        needed = which.get_info(self)
        print(f"calculated. needed {needed}%")
        a = 0
        while a < needed:
            time.sleep(1)
            self.cur += 10
            which.total -= 10
            print(f"charging... {self.cur}%")
            a += 10
        if self.cur > self.max:
            self.cur = self.max
        print(f"using {which.charge_model} for charging.")
        print(f"Phone charged, now {self.cur}%")
        print(f"current charger left: {which.total}")
    
    def stat(self):
        print(f"Current Model: {self.model}, Current percentages: {self.cur}%")

class charger:
    def __init__(self, model, power, total, max):
        self.charge_model = model
        self.power = power
        self.total = total
        self.max = max
        pass

    def get_info(self, phone):
        print(f"Current need battery = {phone.max - phone.cur}")
        return phone.max - phone.cur
    
    def charge_charger(self):
        while self.total < self.max:
            time.sleep(1)
            self.total += 10
            print(f"charging... {self.total}%")
a = phone("nokia", 100, 60, True)
b = charger("Charger A", 40, 50000, 50000)

a.stat()
a.use_bat(20)
a.use_bat(100)
a.use_bat(40)
a.use_bat(20)
a.charge(b)
a.use_bat(20)
a.stat()    
b.get_info(a)    
b.charge_charger()
