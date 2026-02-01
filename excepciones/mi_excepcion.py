#Creando mi propia excepcion personalizada
class MiExcepcion(Exception):
  def __init__(self, err):
    print(f"Impresionante, cometiste el siguiente error: {err}")
  
#Lanzando mi propia excepcion
# raise MiExcepcion("Jajajaja Persona poco culta")
    
#manejandola
try:
  raise MiExcepcion("Jajajaja Persona poco culta")
except:
  print("como vas a cometer ese error")
