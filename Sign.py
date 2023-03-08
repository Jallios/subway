import BD

def Up():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    BD.DBExecute("User","insert",[login,password,0,1,1])

