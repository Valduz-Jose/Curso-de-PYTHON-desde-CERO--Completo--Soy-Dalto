nombres = ["Lucas","Matias","Jose","Pedro","roberto"]
apellidos = ["dalto","zing","Robletes","tarado","Valduz"]

#registrar en un txt d forma optima

with open("archivos_problemas_resueltos\\nombres_y_apellidos.txt","w") as arch:
  arch.writelines("los datos son:\n")
  [arch.writelines(f"Nombre: {n}\nApellido: {a}\n----------------\n") for n,a in zip(nombres,apellidos)]
  
