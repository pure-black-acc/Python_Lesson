class BankAcc:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def depos(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Current total is {self.balance}")
    
    def withd(self, amount):
        if self.balance - amount <= 0:
            print("Cannot withdraw! Insufficient Amount.")
        else:
            self.balance -= amount
            print(f"Withdrawed {amount}. Current total is {self.balance}")
    def stat(self):
        print(f"Account Owner: {self.owner}, Current Balnance: {self.balance}")


a = BankAcc("idk", 5000)
a.depos(500)
a.withd(6000)
a.withd(4000)
a.stat()


class movie:
    def __init__(self, title, tot_se, reserv):
        self.title = title
        self.total = tot_se
        self.reserved = reserv

    def reserve(self, reserve):
        if self.total - reserve > 0:
            self.reserved += reserve
            self.total -= reserve
            print("reserved successfully.")
        else:
            print("Cannot reserve, Insufficient Seats")
    
    def cancel(self, seat):
        if self.reserved - seat > 0:
            self.total += seat
            self.reserved -= seat
            print("reserved canceled successfully.")
        else:
            print("Cannot cancel reserve, Invaild amount")
    
    def stats(self):
        print(f"Title: {self.title}, Seats left: {self.total}, Seats reserved: {self.reserved}")

a = movie("Heh", 500, 0)
a.reserve(50)
a.reserve(600)
a.cancel(30)
a.cancel(500)
a.reserve(400)
a.stats()

class libraryBook:
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.aval = available

    def borrow(self):
        if self.aval == True:
            self.aval = False
            print("Successfully borrowed")
        else:
            print("Cannot borrow!")
    def return_book(self):
        if self.aval == False:
            self.aval = True
            print("Successfully Returned")
        else:
            print("Error, tried to return book that hasn't been borrowed")
    def status(self):
        print(f"Title: {self.title}, Author: {self.author}, Is it avaible for borrowing? {self.aval}")
    
a = libraryBook("idk", "Him", True)
a.borrow()
a.borrow()
a.return_book()
a.return_book()
a.borrow()
a.status()


