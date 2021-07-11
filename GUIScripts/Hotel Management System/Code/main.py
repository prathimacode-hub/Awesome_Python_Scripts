import os
import pickle

print(
    "///////////////****************//////////////*****************/////////////////*****************///////////////////******************//////////")
print(
    "----------------------------------------------------- 5 STAR HOTEL AND RESORTS -----------------------------------------------------------------")
print(
    "//////////////****************///////////////*****************/////////////////*****************///////////////////******************//////////")

u = list()
Delux = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
Semi_Delux = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25)
General = (26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45)
Joint_Room = (46, 47, 48, 49, 50, 46, 47, 48, 49, 50)
m = [9]
G = []


def chk_name():
    while True:
        print("\n")
        name = input("ENTER GUEST NAME:")
        a = name.isdigit()
        if len(name) != 0 and a != True:
            return name

            break
        else:
            print("invalid input please input a valid name")
            print(" ")


def chk_add():
    while True:
        print("\n")
        address = input("ENTER GUEST ADDRESS:")
        a = address.isdigit()
        if len(address) != 0 and a != True:
            return address
            break

        else:
            print("invalid input ")
        print(" ")


def chk_mo():
    while True:
        print("\n")
        mobile_no = input("ENTER MOBILE/PNOHE NO.:")
        if mobile_no.isdigit() == True and len(mobile_no) != 0 and len(mobile_no) == 10:
            return mobile_no
            break
        else:
            print("invalid input ")
        print(" ")


def chk_day():
    while True:
        print("\n")
        no_of_days = input("ENTER NO. OF DAYS GUEST WANT TO STAY:")
        a = no_of_days.isdigit()
        if a == True and len(no_of_days) != 0:
            return no_of_days
            break
        else:
            print("invalid input ")


def chk_pay():
    while True:
        print("\n")
        op = input("Enter guest's choice:")
        a = op.isdigit()
        if len(op) != 0 and a == True and (op == "1" or op == "2"):
            op = int(op)
            return op
            break
        else:
            print("invalid input ")


class save:
    price = 0
    room = "0"

    def __init__(self):
        self.price = 0
        self.name = " "
        self.address = " "
        self.no_of_days = 0
        self.room = "0"

    def enter(self):
        self.name = chk_name()
        self.address = chk_add()
        self.mobile_no = chk_mo()
        self.no_of_days = int(chk_day())

    def tor(self):
        print("1. Delux")
        print("2. Semi-Delux")
        print("3. General")
        print("4. Joint Room")
        while True:
            ch = input("Enter guest's choice:")
            a = ch.isdigit()
            if len(ch) != 0 and a == True and (ch == "1" or ch == "2" or ch == "3" or ch == "4"):
                break
            else:
                print("invalid input ")
        ch = int(ch)
        if ch == 1:
            self.price = self.price + (2000 * self.no_of_days)
            m[0] = 1
        elif ch == 2:
            self.price = self.price + (1500 * self.no_of_days)
            m[0] = 2
        elif ch == 3:
            self.price = self.price + (1000 * self.no_of_days)
            m[0] = 3
        elif ch == 4:
            self.price = self.price + (1700 * self.no_of_days)
            m[0] = 4
        else:
            print("invalid choice")

    def payment_option(self):
        print("1. By cash")
        print("2. By credit/debit card")
        op = chk_pay()
        if op == 1:
            print("No discount.")
        elif op == 2:
            self.price = self.price - ((self.price * 10) / 100)
            print("Discount of 10%.")
        else:
            print("Invalid option.")

    def bill(self):
        print("\n")
        print("@@@@@@@@@  5 STAR HOTEL AND RESORTS  @@@@@@@@@@@@@@@@")
        print("@@@@@@@@@@@@ HAUS KHAZ,  NEW DELHI @@@@@@@@@@@@@@@@@@")
        print("@@@@@@@@@@ SERVING    GUEST   SINCE @@@@@@@@@@@@@@@@@")
        print("@@@@@@@@@@@@@@@    ###1950###       @@@@@@@@@@@@@@@@@")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("NAME-", self.name)
        print("\n")
        print("ADDRESS-", self.address)
        print("\n")
        print("MOBILE NO.-", self.mobile_no)
        print("\n")
        print("YOUR TOTAL BILL IS Rs.", self.price)
        print("\n")
        if m[0] == 1:
            a = Delux
        elif m[0] == 2:

            a = Semi_Delux
        elif m[0] == 3:
            a = General
        elif m[0] == 4:
            a = Joint_Room

        G = []
        f2 = open("hotel.dat", "rb")
        try:
            while True:
                s = pickle.load(f2)
                k = s.room
                G.append(k)
                continue
        except EOFError:
            pass

        for r in a:
            if r not in G:
                print(self.name, " - room", r, "is alloted to you")
                self.room = r
                break
            else:
                continue
        self.room = r
        print("\n")
        print("@@@@@@@@@@@@@@@@@@@@ THANK YOU  @@@@@@@@@@@@@@@@@@@@@@")
        print("@@@@@@@@ HOPE YOU WOULD ENJOY OUR SERVICE @@@@@@@@@@@@")


# main




while True:
    print("\n")
    print("1.Check in")
    print("2.SHOW GUEST LIST")
    print("3.Check out")
    print("4.get info of any guest")
    print("5.EXIT")
    k = input("Enter choice:")





    if k == "1":
        a = GUEST()
        f = open("hotel.dat", "ab")
        a.enter()
        a.tor()
        a.payment_option()
        a.bill()
        pickle.dump(a, f,protocol=2)
        f.close()






    elif k == "2":
        f1 = open("hotel.dat", "rb")
        print("NAME", "\t", "\t", "ROOM NO.")
        try:
            while True:
                s = pickle.load(f1)
                print(s.name, "\t", "\t", s.room)
        except EOFError:
            pass
        f1.close()






    elif k == "3":
        print("\n")
        while True:
            a = input("ENTER ROOM NO.")
            if len(a) != 0:
                break
            else:
                print("no input found")
                continue
            v = int(a)
        v = int(a)
        f = open("hotel.dat", "rb")
        f1 = open("hote.dat", "ab")
        n = 0
        try:
            while True:
                s = pickle.load(f)
                if s.room == v:
                    n = 1
                    name1=s.name

                    print(" ")
                else:
                    pickle.dump(s, f1)
        except EOFError:
            if n == 0:
                print("NO GUEST IN ROOM ", v)
            elif n == 1:

                print("THANK YOU",name1,"2 FOR VISTING US")
                print("HOPE YOU LIKE OUR SERVICE")
                print("\n")
            pass
        f.close()
        f1.close()
        os.remove("hotel.dat")
        os.rename("hote.dat", "hotel.dat")




    elif k == "4":
        f2 = open("hotel.dat", "rb")
        while True:
            v = input("ENTER ROOM NO.")
            if len(v) != 0:
                break
            else:
                print("no input found")
                continue
        v = int(v)
        try:
            n = 0
            while True:
                s = pickle.load(f2)
                a = s.room
                if v == a:
                    n = 1
                    print("NAME-", "\t", "\t", s.name)
                    print("\n")
                    print("ADDRESS-", "\t", s.address)
                    print("\n")
                    print("MOBILE NO.-", "  ", s.mobile_no)
                    print("\n")
                    print("HIS TOTAL BILL IS Rs.", s.price)
                elif EOFError:
                    if n == 0:
                        print("NO GUEST IN ROOM ", v)
                else:
                    n = 0
                    continue
        except EOFError:
            pass
        f2.close()





    elif k == "5":
        break


    else:
        print("invalid choice")
        continue


