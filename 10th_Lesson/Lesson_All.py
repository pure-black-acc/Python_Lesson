class animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("idk")

class dog(animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def wag(self):
        print("tail moving")

    def speak(self):
        print("bark xD")

# thing about overriding:
# if there are 2 same named methods, child class will be used with priority
# 1. class defined -> function called
# 2. python will try to find the child function first
# 3. if found -> execute it
# 4. else execute the parent function

class cat(animal):
    def speak(self):
        print("meow")

dog1 = dog("puppy", 2)
cat1 = cat("kitten")
print(dog1.name)
print(dog1.age)
dog1.speak()
cat1.speak()

