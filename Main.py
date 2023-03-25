from pick import pick
import BD
import MainAdministrator, MainUser
import os

ID = 0

def Up():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    BD.DBExecute("User","insert",[login,password,0,1,1])
    os.system("cls")
    Menu()

def In():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    for i in BD.DBExecute("User","select",[login,password]):
        if login == i[1] and password == i[2]:
            global ID 
            ID = i[0]
            if i[4] == 2:
                MainAdministrator.MenuAdmin()
                os.system("cls")
            else: 
                ID = i[0]
                MainUser.MenuUser()
                os.system("cls")
                
def Menu():
    option = ["Войти", "Регистрация","Выход"]

    option, index = pick(option, "Добро пожаловать в Subway")

    match(index):
        case 0:
            In()
        case 1:
            Up()
        case 2:
            exit()

Menu()