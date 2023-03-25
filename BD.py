import pyodbc
def DBExecute(table,command,values): 
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                        "Server=LAPTOP-7NUBAMDH\SQLEXPRESS;"
                        "Database=Subway;"
                        "Trusted_Connection=yes;")

    cursor = cnxn.cursor()
    match(table):
        case "User":
            if(command == "insert"):
                cursor.execute('insert into [dbo].[User] ([Login_User],[Password_User],[Balance],[Role_ID],[Card_ID]) values (?,?,?,?,?)',(values[0],values[1],values[2],values[3],values[4]))
                cursor.commit()
            elif(command == "updateBalance"):
                cursor.execute('UPDATE [dbo].[User] SET [Balance] = ? WHERE [ID_User] = ?',(values[0],values[1]))
                cursor.commit()
            elif(command == "updateCard"):
                cursor.execute('UPDATE [dbo].[User] SET [Card_ID] = ? WHERE [ID_User] = ?',(values[0],values[1]))
                cursor.commit()
            elif(command == "select"):
                return cursor.execute(f'select * from [dbo].[User]').fetchall()
            elif(command == "selectID"):
                return cursor.execute(f'select * from [dbo].[User] WHERE [ID_User] = ?',[values[0]]).fetchall()
        case "Product":
            if(command == "insert"):
                cursor.execute('insert into [dbo].[Product] ([Product],[Quality],[Cost_TP], [PC_ID]) values (?,?,?,?)',(values[0],values[1],values[2],values[3]))
                cursor.commit()
            elif(command == "delete"):
                cursor.execute('Delete from [dbo].[Product] where [ID_Product] = ?',[values[0]])
                cursor.commit()
            elif(command == "update"):
                cursor.execute('UPDATE [dbo].[Product] SET [Quality] = ? WHERE [ID_Product] = ?',(values[0],values[1]))
                cursor.commit()
            elif(command == "select"):
                product = cursor.execute(f'select * from [dbo].[Product]').fetchall()
                return product
            elif(command == "selectProduct"):
                product = cursor.execute(f'select * from [dbo].[Product] WHERE [PC_ID] = 1').fetchall()
                return product
            elif(command == "selectToping"):
                product = cursor.execute(f'select * from [dbo].[Product] WHERE [PC_ID] = 2').fetchall()
                return product
            elif(command == "selectID"):
                product = cursor.execute(f'select * from [dbo].[Product] WHERE [ID_Product] = ?',[values[0]]).fetchall()
                return product
        case "Order":
            if(command == "insert"):
                cursor.execute('insert into [dbo].[Order] ([Cost_Order],[DateTime_Order],[User_ID]) values (?,?,?)',(values[0],values[1],values[2]))
                cursor.commit()
            elif(command == "selectUser"):
                order = cursor.execute(f'select SUM([Cost_Order]) from [dbo].[Order] WHERE [User_ID] = ?',[values[0]]).fetchall()
                return order