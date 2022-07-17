import users.User as UserModule
import notes.Actions

class Actions:

    def register(self):
        print("\nOk!! Vamos a registrarte en el sistema...")

        name = input("¿Cuál es tu nombre?: ")
        surname = input("¿Cuales son tus apellidos?: ")
        email = input("¿Introduce tu email?: ")
        password = input("¿Introduce tu contraseña?: ")

        user = UserModule.User(name, surname, email, password)
        registration = user.toRegister()

        if registration[0] >= 1:
            print(f"\nPerfecto {registration[1].name} te has registrado con el email {registration[1].email}")
        else:
            print("\nNo te has registrado corectamente !!!")

    def login(self):
        print("\nVale!! Identificate en el sistema...")
        try:
            email = input("¿Introduce tu email?: ")
            password = input("¿Introduce tu contraseña?: ")

            user = UserModule.User(None, None, email, password)
            login = user.toLogin()

            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.nextActions(login)

        except Exception as e:
            # print(type(e))
            # print(type(e).__name__)
            print(f"\nLogin incorrecto!!, Intentalo más tarde")
        
    def nextActions(self, user):
        print("""
            Acciones disponibles:
                -[1] Crear nota
                -[2] Mostrar tus notas
                -[3] Eliminar nota
                -[4] Salir
        """)

        action = int(input("¿Que quieres hacer?: "))
        doThe = notes.Actions.Actions()

        if action == 1:
            print("Vamos a crear una nota")
            doThe.store(user)
        elif action == 2:
            doThe.show(user)
        elif action == 3:
            doThe.delete(user)
        elif action == 4:
            print(f"Ok {user[1]}, hasta pronto!!!")
            exit()
        self.nextActions(user)