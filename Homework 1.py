__author__ = 'Dark-Knight'


def menu():

    while True:
        print("1. input employee first name")
        print("2. input employee last name ")
        print("3. input employee date of birth")
        print("4. input employee social security")
        print("5. input employee street address")
        print("6. input employee city")
        print("7. input employee zip code")
        print("8. input employee information")
        print("9. quit")
        userchoice = input("Please input your choice of 1,2,3,4,5,6,7,8,9: ")
        if userchoice == "1"or userchoice == "2"or userchoice == "3" or userchoice == "4"\
            or userchoice == "5" or userchoice == "6" or userchoice == "7" or userchoice == "8" \
            or userchoice == "9":
            return userchoice
        else:
            print("you must choose 1,2,3,4,,5,6,,7,8 or 9")
x = menu()


def dochoice(x):
        if x == "1":
            print(input("employee first name:").title())
        elif x == "2":
            print(input("employee last name:").title())
        elif x == "3":
            print(input("employee date of birth:").title())
        elif x == "4":
            print(input("employee social security:").title())
        elif x == "5":
            print(input("employee street address").title())
        elif x == "6":
            print(input("employee city:").title())
        elif x == "7":
            print(input("employee zip code:").title())
        elif x == "8":
            print(input("employee information:").title())
        elif x == "9":
            print(input("Quit:"))
        else:
            print(input("invalid choice"))


def firstname():
    s = input("Enter first name").strip().title()
    return s


def lastname():
    t = input("Enter last name name").strip().title()
    return t


def dob():
    m = int(input("month").strip())
    if m >= 1 or m <= 12:
        print(m)
    else:
        print("invalid input")

    d = int(input("day").strip())
    if d >= 1 or d <= 31:
        print(d)
    else:
        print("you must input 1-31")
    y = int(input("year").strip())
    if y >= 1900 or y <= 2014:
        print(y)
    else:
        print("invalid input")
    return str(m) + '/' + str(d)+'/'+str(y)


def ss():
    ms = input("input a number between 0-999").strip()
    m = int(ms)
    if m >= 0 or m <= 999:
        print(m)
    else:
        print("invalid input")
    rs = input("input a number between 0-99").strip()
    r = int(rs)
    if r >= 0 or r <= 99:
        print(r)
    else:
        print("invalid input")
    ts = input("input a number between 0-9999").strip()
    t = int(ts)
    if t >= 0 or t <= 9999:
        print(t)
    else:
        print("invalid input")
    return str(ms)+"-"+str(rs)+"-"+str(ts)


def street():

    numb = input("input a street number between 0-9999").strip()
    w = int(numb)
    if w >= 0 or w <= 9999:
        print(w)
    else:
        print("invalid input")
    address = input("please enter the name of your street").strip()
    print(address)
    return str(w)+" "+str(address)


def city():

    place = input("please enter the name of your city").strip()
    return place


def fivem():

    zipcode = input("please input a five digit number").strip()
    n = int(zipcode)
    return zipcode


name = firstname()
lname = lastname()
date = dob()
ss = ss()
street = street()
city = city()
zipco = fivem()


def printemployee():
    print(name)
    print(lname)
    print(date)
    print(ss)
    print(street)
    print(city)
    print(zipco)
