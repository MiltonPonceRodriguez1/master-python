from cgitb import reset
import datetime
import users.Conection as Conection

connect = Conection.connectDB()
database = connect[0]
cursor = connect[1]

class Note:
    def __init__(self, user_id, title = "", description = ""):
        self.user_id = user_id
        self.title = title
        self.description = description

    def store(self):
        # Fecha actual
        date = datetime.datetime.now()

        # Consulta a la base de datos
        
        sql = "INSERT INTO notes VALUES(NULL, %s, %s, %s, %s)"
        #sql = "INSERT INTO notes VALUES(NULL, %s, %s, %s, NOW())"
        
        # Valores de la nota
        note = (self.user_id, self.title, self.description, date)

        try:
            cursor.execute(sql, note)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result

    def show(self):
        sql = f"SELECT * FROM notes WHERE user_id = {self.user_id}"

        cursor.execute(sql)
        result = cursor.fetchall()

        return result

    def delete(self):
        print(f"Vamos a eliminar la nota xD")
        sql = f"DELETE FROM notes WHERE user_id = {self.user_id} AND title LIKE '%{self.title}%'"

        cursor.execute(sql)
        database.commit()

        return [cursor.rowcount, self]


