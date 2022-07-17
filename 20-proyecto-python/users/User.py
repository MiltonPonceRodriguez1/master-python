import datetime
import hashlib
import users.Conection as Conection

connect = Conection.connectDB()
database = connect[0]
cursor = connect[1]

class User:
    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password

    def toRegister(self):
        fecha = datetime.datetime.now()

        # Cifrar contraseña
        encryption = hashlib.sha256()
        encryption.update(self.password.encode('utf8'))

        sql = "INSERT INTO users VALUES(NULL, %s, %s, %s, %s, %s)"
        user = (self.name, self.surname, self.email, encryption.hexdigest() , fecha)
        
        try:
            cursor.execute(sql, user)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result

    def toLogin(self):
        # Consulta para comprobar si existe el usuario
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"

        # Cifrar contraseña
        encryption = hashlib.sha256()
        encryption.update(self.password.encode('utf8'))

        # Datos para la consulta
        user = (self.email, encryption.hexdigest())

        cursor.execute(sql, user)
        result = cursor.fetchone()

        return result