import BD
import MainAdministrator
import MainUser
ID = 0

def Up():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    BD.DBExecute("User","insert",[login,password,0,1,1])

def In():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    for i in BD.DBExecute("User","select",[login,password]):
        if login == i[1] and password == i[2]:
            global ID 
            ID = i[0]
            if i[4] == 2:
                MainAdministrator.Main()
            else: 
                ID = i[0]
                MainUser.Main()
                