import notes.Note as Model
from users import User

class Actions:
    
    def store(self, user):
        print(f"\nOk {user[1]}!! Vamos a crear una nueva nota ...")
        
        title = input("Introduce el titulo de tu nota: ")
        description = input("Introduce la descripción de tu nota: ")

        note = Model.Note(user[0], title, description)
        save = note.store()

        if save[0] >= 1:
            print(f"\nPerfecto, has guardado la nota: {save[1].title}")
        else:
            print(f"\nNo se ha guardado la nota, lo siento {user[1]} ")
        
    def show(self, user):
        print(f"\n Vale {user[1]}!! Aquí tienes tus notas: ")

        note = Model.Note(user[0])
        notes = note.show()

        for note in notes:
            print(f"\n****************  {note[4]}  ****************")
            print(note[2])
            print(note[3])
            print(f"**********************************************")

    def delete(self, user: User):
        print(f"\nOk {user[1]}!! Vamos a eliminar notas")
        title = input("Introduce el titulo de la nota a eliminar: ")
        
        note = Model.Note(user[0], title)
        result = note.delete()

        if result[0] >= 1:
            print(f"\nSe elimino correctamente la nota {result[1].title}")
        else:
            print(f"\nNo se pudo eliminar la nota!! Intentalo mas tarde ...")