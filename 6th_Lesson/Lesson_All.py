# class cal:
#     pass

# a = cal()
# print(f"a : {a}")


class cal2:
    def setdata(self, fir, sec): #how does this works? by setdata, the variable get assigned numbers in fir, and sec
        self.fir = fir             #and add(self) will add fir, and sec, and send out the result of the addition.
        self.sec = sec
    def setdata(self, fir, sec): #how does this works? by setdata, the variable get assigned numbers in fir, and sec
        self.fir = fir             #and add(self) will add fir, and sec, and send out the result of the addition.
        self.sec = sec
    def add(self):
        result = self.fir+self.sec
        return result

cal1 = cal2()
cal12 = cal2()

cal1.setdata(4,2)
cal12.setdata(3,5)

print(f"{cal1.add()}")
print(f"{cal12.add()}")


class Cal_Init:
    def __init__(self):
        self.fir = 100         
        self.sec = 200
    def setdata(self, fir, sec):
        self.fir = fir             
        self.sec = sec
    def add(self):
        result = self.fir+self.sec
        return result

cal1 = Cal_Init()
print(f"{cal1.add()}")
cal1.setdata(4,2)
print(f"{cal1.add()}")