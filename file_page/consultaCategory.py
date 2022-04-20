#print(int("00254652"))
from asyncio.proactor_events import _ProactorBaseWritePipeTransport
import mysql.connector 
from mysql.connector import errorcode


arq = "00254652"
arq = int(arq)
arq = str(arq)

print(arq)
print(type(arq))


try:
    db_connection = mysql.connector.connect(host="127.0.0.1", user ="root",  password="admin", database = "paneiro")
   
    print(db_connection)
    print("Database Connect Made!")
    #db_connection.close()
except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exist")
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("User name or password is wrong")
    else:
        print(error)
else:
    cursor = db_connection.cursor()



def lerCategory():
    
    arrayfile = []
    cursor.execute("SELECT idcategory, cdcategory FROM `pan_categoria` ")
    result = cursor.fetchall()
    arquivo = open("./arqtxt/categoria.txt", "a")
    for x in result:
        print(x, "\n")
        arrayfile.append( ' {}, \n'.format(x))
        arquivo.writelines(arrayfile)
    print("resultados:",cursor.rowcount)
                
    arquivo.close()    


lerCategory()




#print("usuarios",cursor.rowcount) #mostra quantas linhas foram retornadas com exito
