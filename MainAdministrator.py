import BD
import Main
from pick import pick
import tabulate
import os


def Select():
    select = BD.DBExecute("Product","select",[])
    print(tabulate.tabulate(select, headers=["Номер","Продукт","Количество","Цена","Категория"]))
    a = input("Для продолжения нажмите Enter")
    os.system("cls")
    MenuAdmin()

def BalanceCheck():
    for user in BD.DBExecute("User","selectID",[Main.ID]):
        print(f"Баланс = {user[3]}")

def Insert():
    Product = input("Введите продукт: ")
    Cost_TP = input("Введите цену: ")

    option = ["Продукт", "Топинг"]

    option, index = pick(option, "Выберите категорию продукта")

    match(index):
        case 0:
            BD.DBExecute("Product","insert",[Product,0,Cost_TP,1])
        case 1:
            BD.DBExecute("Product","insert",[Product,0,Cost_TP,2])
    Select()

def Update():
    BalanceCheck()
    select = BD.DBExecute("Product","select",[])
    print(tabulate.tabulate(select, headers=["Номер","Продукт","Количество","Цена","Категория"]))
    ID_Product = int(input("Введите номер продукта: "))
    Quality = int(input("Введите кол-во: "))   
    for user in BD.DBExecute("User","selectID",[Main.ID]):
        for product in BD.DBExecute("Product","selectID",[ID_Product]):
            if user[3] >= Quality*product[3]:
                BD.DBExecute("Product","update",[Quality,ID_Product])
                BD.DBExecute("User","updateBalance",[user[3]-Quality*product[3],Main.ID])
            else:
                print("Недостаточно средств")
    Select()

def Delete():
    select = BD.DBExecute("Product","select",[])
    print(tabulate.tabulate(select, headers=["Номер","Продукт","Количество","Цена"]))
    ID_Product = int(input("Введите ID: "))
    BD.DBExecute("Product","delete",[ID_Product])
    Select()

def MenuAdmin():

    option = ["Выборка всех позиций", "Добавить позицию","Заказать позицию","Удалить позицию","Выйти"]

    option, index = pick(option, "Добро пожаловать в Администратор")

    match(index):
        case 0:
            Select()
        case 1:
            Insert()
        case 2:
            Update()
        case 3:
            Delete()
        case 4:
            exit()