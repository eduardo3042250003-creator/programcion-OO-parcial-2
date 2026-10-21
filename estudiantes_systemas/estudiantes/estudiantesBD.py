from conexion import conexion,cursor
class Estudiantes():
    def __init__(self,nombre,notas):
       self._nombre = nombre
       self._notas = notas

    @property
    def nombre(self):
        return self._nombre 
    @nombre.setter
    def nombre (self,nombre):
        self._nombre = nombre
    @property
    def notas (self):
        return self._notas
    @notas.setter
    def notas(self,notas):
        self._notas = notas



    def insertar(self):
        try:
            sql = "INSERT INTO estudiantes VALUES (null, %s, %s )"
            valores = (self._nombre, self._notas)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error detallado en SQL: {e}") 
            return False
    @staticmethod
    def consultar():
        try:
            sql = "select * from estudiantes"
            cursor.execute(sql,)
            return cursor.fetchall()
        except:
            return []
    @staticmethod
    def eliminar(id: int):
        try:
            sql = "delete from estudiantes where id= %s "
            valores =  (id,)
            cursor.execute(sql,valores)
            conexion.commit()
            return True
        except:
            return False
    def actualizar(self, id):
        try:
            
            sql = "UPDATE estudiantes SET nombre = %s, nota = %s WHERE id = %s"
            valores = (self._nombre, self._notas, id)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False



    