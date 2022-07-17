from clases import Person, Informatic, TecnicoRedes
print("\n\t\t ############ Clase Persona ############")
persona = Person()
persona.setName("Dokken")
persona.setSurname("Lee")
print(f"Persona: {persona.getName()} {persona.getSurname()}")

print("\n\t\t ########## Clase Informatico ##########")
informatico = Informatic("Milton", "Ponce", 1.70, 22, "PHP, JS, Python", 5)
print(f"\n{informatico.getInfo()}")
print(f"\n{informatico.walk()}")

print("\n\t\t ######### Clase Tecnico Redes #########")
tecnico = TecnicoRedes()
tecnico.setName("Hector")
print(tecnico.auditarRedes, tecnico.getName())
print(f"\n{tecnico.getInfo()}")