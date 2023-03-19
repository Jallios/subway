import BD
import Sign

import datetime
import random

from pick import pick

def Select():
    select = BD.DBExecute("Product","select",[])
    for row in select:
        print('%r' % (row,))

def Insert():
    i = int(input("Введите количество слоёв которое хотите: "))
    a = 0
    order = []
    cost = 0
    dt_now = datetime.datetime.now()
    Select()
    while(i-1 >= a):
        sloy = int(input("Введите продукт: "))
        for s in BD.DBExecute("Product","selectID",[sloy]):
            if(s[2]>0):
                BD.DBExecute("Product","update",[s[2]-1,sloy])
                cost += s[3]
                order.append(s[1])
            else:
                print("Нет в наличии")
        a += 1    
    user_input = input('Хотите топинг (yes/no): ')

    yes_choices = ['да', 'y']
    no_choices = ['нет', 'n']

    if user_input.lower() in yes_choices:
        Select()
        i = int(input("Введите количество слоёв которое хотите: "))
        a = 0
        while(i-1 >= a):
            sloy = int(input("Введите продукт: "))
            if(s[2]>0):
                BD.DBExecute("Product","update",[s[2]-1,sloy])
                cost += s[3]
                order.append(s[1])
            else:
                print("Нет в наличии")
            a += 1    
            for i in BD.DBExecute("User","selectID",[Sign.ID]):
                if i[3]>= cost:
                    if i[5] == 2:
                        cost/100*5
                    if i[5] == 3:
                        cost/100*10
                    if i[5] == 4:
                        cost/100*20
                    if random.random() == 1:
                        BD.DBExecute("Order","insert",[cost,dt_now,Sign.ID])
                        BD.DBExecute("User","updateBalance",[i[3]-cost,Sign.ID])
                        for s in BD.DBExecute("User","selectID",[1]):
                            BD.DBExecute("User","updateBalance",[s[3]+cost,s[0]])
                    else:
                        print("В мясе обнаружена кость скидка -20%")
                        BD.DBExecute("Order","insert",[cost/100*20,dt_now,Sign.ID])
                        BD.DBExecute("User","updateBalance",[i[3]-cost/100*20,Sign.ID])
                        for s in BD.DBExecute("User","selectID",[1]):
                            BD.DBExecute("User","updateBalance",[s[3]+cost/100*20,s[0]])
                else:
                    print("Недостаточно средств")
    elif user_input.lower() in no_choices:
         for i in BD.DBExecute("User","selectID",[Sign.ID]):
            if i[3]>= cost:
                if random.random() == 1:
                    BD.DBExecute("Order","insert",[cost,dt_now,Sign.ID])
                    BD.DBExecute("User","updateBalance",[i[3]-cost,Sign.ID])
                    for s in BD.DBExecute("User","selectID",[1]):
                        BD.DBExecute("User","updateBalance",[i[3]+cost,i[0]])
                else:
                    print("В мясе обнаружена кость скидка -20%")
                    BD.DBExecute("Order","insert",[cost/100*20,dt_now,Sign.ID])
                    BD.DBExecute("User","updateBalance",[i[3]-cost/100*20,Sign.ID])
                    for s in BD.DBExecute("User","selectID",[1]):
                        BD.DBExecute("User","updateBalance",[s[3]+cost/100*20,s[0]])
            else:
                print("Недостаточно средств")
    
def AddBalance():
    Select()
    ID_User = Sign.ID
    Balance = int(input("Введите сумму: "))
    if(100 < Balance < 500):
        BD.DBExecute("User","updateBalance",[Balance,ID_User])
    else:
        print("Меньше 100 нельзя, больше 500 нельзя")


def Delete():
    Select()
    ID_Product = int(input("Введите ID"))
    BD.DBExecute("Product","delete",[ID_Product])

def Main():
    
    for s in BD.DBExecute("User","selectID",[Sign.ID]):
        if len(s) == 5:
            BD.DBExecute("User","updateCard",[2,Sign.ID])
        if len(s) == 10:
            BD.DBExecute("User","updateCard",[3,Sign.ID])
        if len(s) == 20:
            BD.DBExecute("User","updateCard",[4,Sign.ID])
            
        

    print(Sign.ID)

    option = ["Посмотреть компоненты", "Сделать заказ","Пополнить","Выйти"]

    option, index = pick(option, "Добро пожаловать в Администратор")

    match(index):
        case 0:
            Select()
        case 1:
            Insert()
        case 2:
            AddBalance()
        case 3:
            Delete()
        case 4:
            exit()
