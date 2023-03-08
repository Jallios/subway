import Sign
from pick import pick

option = ["Войти", "Регистрация","Выход"]

option, index = pick(option, "Добро пожаловать в Subway")

match(index):
    case 0:
       print(2)
    case 1:
        Sign.Up()
    case 2:
        print(2)

