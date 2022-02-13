from __future__ import annotations
from .database import Conexion, Dao
import datetime

class Tutorial:

    def __init__(self, titulo:str= '', autor:str = '', creado:datetime = '', id:int = 0):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.creado = creado

class TutorialDao(Dao):
    def conectarse(self):
        try:
            self.db = Conexion()
            self.db.conectarse()
            self.cur = self.db.con.cursor()
            self.db_tutoriales: list['Tutorial'] = []

            self.db.mensaje = 'Conexión a la base de datos: EXITOSA'
            self.db.error = False
        except Exception as ex:
            self.db.mensaje = f'Conexión a la base de datos desde TutorialDao: FALLO. {ex}'
            self.db.error = True

    def createTabla(self):
        try:
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS tutoriales("
                + "ID INT AUTO_INCREMENT PRIMARY KEY,"
                + "TITULO VARCHAR(100) NOT NULL,"
                + "AUTORID INT NOT NULL,"
                + "CREADO DATE,"
                + "FOREIGN KEY (AUTORID) REFERENCES autores(id))"
            )
            self.db.mensaje = "Tabla tutoriales creada con exito en la base de datos"
            self.db.error = False
        except Exception as ex:
            self.db.mensaje = "Tabla tutoriales no se pudo crear en la base de datos"
            self.db.error = False

    def getAll(self):
        try:
            sqlSelect = "SELECT * FROM tutoriales"
            self.cur.execute(sqlSelect)
            resultado = self.cur.fetchall()
            pre = []
            # Reg es una tupla
            for reg in resultado:
                # Pasamos los parametros de la tupla en tutorial
                tutorial = Tutorial(reg[1], reg[2], reg[3])
                tutorial.id = reg[0]
                pre.append(tutorial)

            self.db_tutoriales = pre
            self.db.mensaje = "Autores obtenidos con exito"
            self.db.error = False

        except Exception as ex:
            self.db.mensaje = f"Ocurrio un error al obtener los autores {ex}"
            self.db.error = False

    def getRegistro(self, numero:int):
        try:
            sqlInsert = "SELECT * FROM tutoriales WHERE id = %s"
            self.cur.execute(sqlInsert, (numero,))
            resultado = self.cur.fetchall()
            id, titulo, creado, autor = resultado[0]
            tutorial = Tutorial(titulo, autor, creado)
            tutorial.id = id
            self.db.mensaje = f"Registro consultado correctamente, EXITOSO: {resultado[0]}"
            self.db.error = False
            print(resultado[0])
            return tutorial
        except Exception as ex:
            self.db.mensaje = f"Falló al buscar: FALLÓ. {ex}"
            self.db.error = True
            return 'FALLO'

    def setUpdate(self, reg:object):
        try:
            sqlInsert = "UPDATE tutoriales SET titulo=%s, autorid=%s, creado=%s WHERE id= %s"
            tutorial = (reg.titulo, reg.autor, reg.creado, reg.id)
            self.cur.execute(sqlInsert, tutorial)
            self.db.con.commit()
            self.db.mensaje = f"Valores modificados: {tutorial}"
            self.db.error = False
        except Exception as ex:
            self.db.mensaje = f"Falló al modificar los valores: FALLO. {ex}"
            self.db.error = True

    def setDelete(self, numero:int):
        try:
            sqlInsert = "DELETE FROM tutoriales WHERE id = %s"
            self.cur.execute(sqlInsert, (numero,))
            self.db.con.commit()
            self.db.mensaje = f"Dato eliminado correctamente, ID: {numero}"
            self.db.error = False
        except Exception as ex:
            self.db.mensaje = f"Falló al Eliminar: FALLÓ. {ex}"
            self.db.error = True

    def setCreate(self, reg:object):
        try:
            sqlInsert = "INSERT INTO tutoriales (titulo, autorid, creado) VALUES (%s, %s, %s)"
            tutorial = (reg.titulo, reg.autor, reg.creado)
            self.cur.execute(sqlInsert, tutorial)
            self.db.con.commit()
            self.db.mensaje = f"Valores insertados: {tutorial}"
            self.db.error = False
        except Exception as ex:
            self.db.mensaje = f"Falló al insertar los valores: {tutorial}"
            self.db.error = True
