import Sign 
from pick import pick

option = ["Войти", "Регистрация","Выход"]

option, index = pick(option, "Добро пожаловать в Subway")

match(index):
    case 0:
       Sign.In()
    case 1:
        Sign.Up()
    case 2:
        exit()

