class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        print(F"{self.num1+self.num2}")  
        print(f"추가 계산 완료.") 

# c = Calculator(10, 5)
# c.add()


class AdvanvedCalculator(Calculator):
    def __init__(self, num1):
        super().__init__(num1, num2 = 10)
        super().add()  #when function is in here. when new object is defined(line 21) the function in here is automatically executed

    def mul(self):
        print(F"{self.num1*self.num2}")  
    
c = AdvanvedCalculator(5)

c.mul()
