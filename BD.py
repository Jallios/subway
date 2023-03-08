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
                
            elif(command == "delete"):
                cursor.execute('Delete from '+table+' where ID_User = ?',[values])
               
            elif(command == "update"):
                cursor.execute('UPDATE '+table+' SET Login_User = ?, Password_User = ?, Balance = ?, Role_ID = ?, Card_ID = ?',(values[0],values[1],values[2],values[3],values[4]))
                
            elif(command == "select"):
                cursor.execute('select * from ' + table)
                