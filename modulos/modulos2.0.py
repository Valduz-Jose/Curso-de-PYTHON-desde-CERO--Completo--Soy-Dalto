#si el modulo esta en una carpeta en la misma ruta que el script que lo importa
# import funciones_buenas.saludar as m_saludar
# print(m_saludar.saludar("Luis"))

#python prioriza los modulos nativos sobre los creados por el usuario
import sys
sys.path.append("c:\\Users\\Alejandro\\Documents\\Curso de Python DALTO\\funciones_buenas")
import saludar as modulo_saludar
print(modulo_saludar.saludar("Luis"))


# import sys
# from pathlib import Path

# # Ruta más confiable y legible
# ruta = Path(r"c:\Users\Alejandro\Documents\Curso de Python DALTO\funciones_buenas")
# sys.path.append(str(ruta))

# try:
#     import saludar as modulo_saludar
#     print(modulo_saludar.saludar("Luis"))
# except ModuleNotFoundError as e:
#     print("No se encuentra el módulo 'saludar'")
#     print("Ruta agregada:", ruta)
#     print("Contenido de la carpeta:", list(ruta.glob("*.py")))
# except AttributeError:
#     print("El módulo saludar existe, pero NO tiene la función 'saludar()'")