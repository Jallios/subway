import BD
import Sign

from pick import pick

def Select():
    select = BD.DBExecute("Product","select",[])
    for row in select:
        print('row = %r' % (row,))

def Insert():
    Product = input("Введите продукт: ")
    Cost_TP = input("Введите цену: ")
    BD.DBExecute("Product","insert",[Product,0,Cost_TP])
    Select()

def Update():
    Select()
    ID_Product = int(input("Введите ID: "))
    Product = input("Введите продукт: ")
    Quality = int(input("Введите кол-во: "))   
    Cost_TP = int(input("Введите цену: "))
    for i in BD.DBExecute("User","selectID",[Sign.ID]):
        if i[3]>= Quality*Cost_TP:
            BD.DBExecute("Product","update",[Product,Quality,Cost_TP,ID_Product])
            BD.DBExecute("User","update",[i[1],i[2],i[3]-Quality*Cost_TP,i[4],i[5],i[0]])
        else:
            print("Недостаточно средств")

def Delete():
    Select()
    ID_Product = int(input("Введите ID"))
    BD.DBExecute("Product","delete",[ID_Product])

def Main():

    print(Sign.ID)

    option = ["Выборка", "Добавить","Редактировать","Удалить","Выйти"]

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
