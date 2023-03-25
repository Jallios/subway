import BD
import datetime
import Main
import os
import tabulate
import random
import calendar


from pick import pick

def Select():
    select = BD.DBExecute("Product","select",[])
    print(tabulate.tabulate(select, headers=["Номер","Продукт","Количество","Цена","Категория"]))
    a = input("Для продолжения нажмите Enter")
    os.system("cls")
    MenuUser()

def BalanceCheck():
    for user in BD.DBExecute("User","selectID",[Main.ID]):
        print(f"Баланс = {user[3]}")
    
def AddBalance():
    
    BalanceCheck()

    Balance = int(input("Введите сумму: "))

    halva = random.randint(0, 10)

    if(halva == 7):
        print("Вы везунчик +20% к вашему счёту!!!")
        a = input("Для продолжения нажмите Enter")
        Balance += Balance/100 * 20
    
    if(100 < Balance < 500):
        for user in BD.DBExecute("User","selectID",[Main.ID]):
            BD.DBExecute("User","updateBalance",[user[3]+Balance,Main.ID])
    else:
        print("Меньше 100 нельзя, больше 500 нельзя")
    os.system("cls")
    MenuUser()

def AddOrder():

    BalanceCheck()

    count = int(input("Введите какое количество слоёв вы хотите: "))
    if(count <= 0):
        print("Нормально введи!!")
        a = input("Для продолжения нажмите Enter")
        os.system("cls")
        MenuUser()
    i = 0
    cost = 0

    select = BD.DBExecute("Product","selectProduct",[])
    print(tabulate.tabulate(select, headers=["Номер","Продукт","Количество","Цена","Категория"]))

    while(i != count):
        component = int(input("Введите номер продукта: "))
        if(component <= 0):
            print("Нормально введи!!")
            a = input("Для продолжения нажмите Enter")
            os.system("cls")
            MenuUser()
        for product in BD.DBExecute("Product","selectID",[component]):
            cost += product[3] + 5
            BD.DBExecute("Product","update",[product[2]-1,component])
        i += 1
   
    option = ["Да", "Нет","Выйти"]

    option, index = pick(option, "Хотите доваить топинг?")

    match(index):
        case 0:
            select = BD.DBExecute("Product","selectToping",[])
            print(tabulate.tabulate(select, headers=["Номер","Продукт","Количество","Цена","Категория"]))
            count = int(input("Введите какое количество слоёв вы хотите: "))
            if(count <= 0):
                print("Нормально введи!!")
                a = input("Для продолжения нажмите Enter")
                os.system("cls")
                MenuUser()
            i = 0
            while(i != count):
                component = int(input("Введите номер продукта: "))
                if(component <= 0):
                    print("Нормально введи!!")
                    a = input("Для продолжения нажмите Enter")
                    os.system("cls")
                    MenuUser()
                for product in BD.DBExecute("Product","selectID",[component]):
                    cost += product[3] + 5
                    BD.DBExecute("Product","update",[product[2]-1,component])
                i += 1
            for user in BD.DBExecute("User","selectID",[Main.ID]):
                if user[3] >= cost:
                    if(user[5] == 2):
                        cost -= cost/100 * 5
                    if(user[5] == 3):
                        cost -= cost/100 * 10
                    if(user[5] == 4):
                        cost -= cost/100 * 20
                    bone = random.randint(0, 10)
                    if(bone == 1):
                        print("В мясе обнаружена кость скидка 20%!!!")
                        a = input("Для продолжения нажмите Enter")
                        cost -= cost/100 * 20
                    BD.DBExecute("User","updateBalance",[user[3]-cost,Main.ID])
                    for admin in BD.DBExecute("User","selectID",[1]):
                        BD.DBExecute("User","updateBalance",[admin[3]+cost,1])
                    BD.DBExecute("Order","insert",[cost,datetime.datetime.now(),Main.ID])
                else:
                    print("Недостаточно средств!!!")
                    a = input("Для продолжения нажмите Enter")
                    MenuUser()
        case 1:
            for user in BD.DBExecute("User","selectID",[Main.ID]):
                if user[3] >= cost:
                    if(user[5] == 2):
                        cost -= cost/100 * 5
                    if(user[5] == 3):
                        cost -= cost/100 * 10
                    if(user[5] == 4):
                        cost -= cost/100 * 20
                    bone = random.randint(0, 10)
                    if(bone == 1):
                        print("В мясе обнаружена кость скидка 20%!!!")
                        a = input("Для продолжения нажмите Enter")
                        cost -= cost/100 * 20
                    BD.DBExecute("User","updateBalance",[user[3]-cost,Main.ID])
                    for admin in BD.DBExecute("User","selectID",[1]):
                        BD.DBExecute("User","updateBalance",[admin[3]+cost,1])
                    BD.DBExecute("Order","insert",[cost,datetime.datetime.now(),Main.ID])
                else:
                    print("Недостаточно средств!!!")
                    a = input("Для продолжения нажмите Enter")
                    MenuUser()
        case 2:
            os.system("cls")
            MenuUser()
    for user in BD.DBExecute("Order","selectUser",[Main.ID]):
        if(user[0] >= 5000):
            print("Вы совершили покупки на 5000 рублей Subway предоставляет вам бранзовую скидочную карту (скидка 5%)!!!")
            a = input("Для продолжения нажмите Enter")
            BD.DBExecute("User","updateCard",[2,Main.ID])
        if(user[0] >= 15000):
            print("Вы совершили покупки на 15000 рублей Subway предоставляет вам бранзовую скидочную карту (скидка 10%)!!!")
            a = input("Для продолжения нажмите Enter")
            BD.DBExecute("User","updateCard",[3,Main.ID])
        if(user[0] >= 25000):
            print("Вы совершили покупки на 5000 рублей Subway предоставляет вам бранзовую скидочную карту (скидка 20%)!!!")
            a = input("Для продолжения нажмите Enter")
            BD.DBExecute("User","updateCard",[4,Main.ID])

    os.system("cls")
    MenuUser()
    
def MenuUser():
    
    option = ["Посмотреть позиции", "Сделать заказ","Пополнить баланс","Выйти"]

    option, index = pick(option, "Добро пожаловать")

    match(index):
        case 0:
            Select()
        case 1:
            AddOrder()
        case 2:
            AddBalance()
        case 3:
            exit()
