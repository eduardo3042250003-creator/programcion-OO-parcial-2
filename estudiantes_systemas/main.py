from conexion import conexion
from estudiantes import estudiantesBD

class app():
    def __init__(self):
        self.main()
    def esperaTecla (self):
        input("....OPRIMA CUALQUIER TECLA PARA CONTINUAR....")
    def borrarPantalla (self):
        print("\033c")
    def terminar(self):
        input("....gracias por usar el sisitema ")
    def opcInvalida(self):
         input ("...opcion invalida....\npresiona enter para continuar")
    def menuAcciones(self,tipo):
        print(f"\t\t...::::menu de tipo {tipo} :::.... ")
        opcion = input("\n\t1.- agregar  \n\t2.- Borrar \n\t3.- modificar \n\t4.- mostrar \n\t5.-regresar \n\t...seleciona una opcion...." ).strip()
        return opcion
    def respuesta_sql(self,respuesta):
        if respuesta:
            input("\t\t:::accion exitosa:::")
        else:
            input("\t\t:::!camarada al chile no jalo!:::")
    def pedirDatos(self,tipo):
        self.borrarPantalla()
        print(f"\t\t ::: REGISTRAR NUEVO {tipo.upper()} :::")
        marca = input("Ingrese el nombre: ").upper().strip()
        color = input("Ingrese la notas: ")
        regresar = (marca,color)
        return regresar

    """
    def datos_estudiante(self,tipo):
        self.borrarPantalla()
        print(f"\n\tIngresar los datos del {tipo}")
        estudiantito={}
        estudiantito['nombre']=input("Nombre: ").upper().strip()
        estudiantito['nota']=input("Nota: ").upper().strip()
        return estudiantito
    """
    def menu_estudiantes(self):
        opc = True
        while opc:
            self.borrarPantalla()
            opc = self.menuAcciones('estudiantes')

            match opc:
                case '1':
                    datosCoche = self.pedirDatos("estudiantes")
                    estudiante1 = estudiantesBD.Estudiantes(*datosCoche)
                    respuesta = estudiante1.insertar()
                    self.respuesta_sql(respuesta)
                    del estudiante1
                case '2':
                    self.borrarPantalla()
                    id = int(input("ingrese el id del estudiante que desea eliminar....."))
                    respuesta = estudiantesBD.Estudiantes.eliminar(id)
                    self.respuesta_sql(respuesta)
                    self.esperaTecla()

                case '3':
                    self.borrarPantalla()
                    id =int( input("ingrese el id del coche que desea actualizar......"))
                    datosCoche = self.pedirDatos("coches")
                    estudiante1 = estudiantesBD.Estudiantes(*datosCoche)
                    respuesta = estudiante1.actualizar(id)
                    self.respuesta_sql(respuesta)
                    self.esperaTecla()
                    del estudiante1
                case '4':
                    registros = estudiantesBD.Estudiantes.consultar()
                    if len(registros) > 0:
                        numCoches = 1
                        print(f"\n\tcoche # {numCoches}\n\tID:\tnombre:\t\tnotas:")
                        for fila in registros:
                            print(f"\t{fila[0]} \t {fila[1]}\t\t {fila[2]}") 
                    else:
                        print("no se encontro informacion en la base de datos")
                    self.esperaTecla()
                case '5':
                    opc = False
                case _:
                    self.opcInvalida()
    def main(self):
            opcion = True
            while opcion:
                self.borrarPantalla()
                opcion = input("\t\t ::::menu principal:::::\n\t1- estudiantes\n\t2- salir\n\t elige una opcion....").lower().strip()
                match opcion:
                    case '1':
                        self.borrarPantalla()
                        self.menu_estudiantes()
                        self.esperaTecla()
                    case '2':
                        self.borrarPantalla()
                        self.terminar()
                        opcion = False
                    case _:
                        self.borrarPantalla()
                        self.opcInvalida()

if __name__ == "__main__":
    app()

##metodos estaticos
##tema decoradores
##investigar que se puede hacer para que el metodo set y get se utilizen directamente con el atibuto