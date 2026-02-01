def sumar_dos():
  while True:
    a=input("numero 1: ")
    b=input("numero 2: ")
    
    try:#intenta lo de abajo
      resultado = int(a)+int(b)
    except Exception as e:#en caso de
      print("Te pedi un numero, no te detengas")
      print(f"Error: {e}")
    else:#se ejecuta si no hay errores
      break
    finally:#Se ejecuta sin importar lo que pase
      print("Esto siempre se ejecuta")
    
  return resultado

print(sumar_dos())