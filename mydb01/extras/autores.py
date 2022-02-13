from __future__ import annotations

from .database import Conexion, Dao
from mydb01.extras.tutoriales import Tutorial

class Autores:

    def __init__(self, nombre:str= '', apellido:str = '', celular:str = '', email:str = '', id:int = 0):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular
        self.email = email

class AutoresDao(Dao):
    def conectarse(self):
        try:
            self.db = Conexion()
            self.db.conectarse()
            self.cur = self.db.con.cursor()
            self.db_autores: list['Autores'] = []

            self.db.mensaje = 'Conexión a la base de datos: EXITOSA'
            self.db.error = False
        except Exception as ex:
            self.db.mensaje = f'Conexión a la base de datos desde TutorialDao: FALLO. {ex}'
            self.db.error = True

    def createTabla(self):
        try:
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS autores("
                + "ID INT AUTO_INCREMENT PRIMARY KEY,"
                + "NOMBRE VARCHAR(100) NOT NULL,"
                + "APELLIDO VARCHAR(40) NOT NULL,"
                + "CELULAR VARCHAR(40) NOT NULL,"
                + "EMAIL VARCHAR(40) NOT NULL)"
            )
            self.db.mensaje = "Tabla autores creada con exito en la base de datos"
            self.db.error = False
        except Exception as ex:
            self.db.mensaje = "Tabla autores no se pudo crear en la base de datos"
            self.db.error = False

    def getAll(self):
        try:
            sqlSelect = "SELECT * FROM autores"
            self.cur.execute(sqlSelect)
            resultado = self.cur.fetchall()
            pre = []
            # Reg es una tupla
            for reg in resultado:
                # Pasamos los parametros de la tupla en autor
                autor = Autores(reg[1], reg[2], reg[3], reg[4])
                autor.id = reg[0]
                pre.append(autor)

            self.db_autores = pre
            self.db.mensaje = "Autores obtenidos con exito"
            self.db.error = False

        except Exception as ex:
            self.db.mensaje = f"Ocurrio un error al obtener los autores {ex}"
            self.db.error = False

    def getRegistro(self, numero:int):
        try:
            sqlInsert = "SELECT * FROM autores WHERE id = %s"
            self.cur.execute(sqlInsert, (numero,))
            resultado = self.cur.fetchall()
            id, nombre, apellido, celular, email = resultado[0]
            autor = Autores(nombre, apellido, celular, email)
            autor.id = id
            self.db.mensaje = f"Registro consultado correctamente, EXITOSO: {resultado[0]}"
            self.db.error = False
            print(resultado[0])
            return autor
        except Exception as ex:
            self.db.mensaje = f"Falló al buscar: FALLÓ. {ex}"
            self.db.error = True
            return 'FALLO'

    def setUpdate(self, reg:object):
        try:
            sqlInsert = "UPDATE autores SET nombre=%s, apellido=%s, celular=%s, email=%s WHERE id= %s"
            autor = (reg.nombre, reg.apellido, reg.celular, reg.email, reg.id)
            self.cur.execute(sqlInsert, autor)
            self.db.con.commit()
            self.db.mensaje = f"Valores modificados: {autor}"
            self.db.error = False
        except Exception as ex:
            self.db.mensaje = f"Falló al modificar los valores: FALLO. {ex}"
            self.db.error = True

    def setDelete(self, numero:int):
        try:
            sqlInsert = "DELETE FROM autores WHERE id = %s"
            self.cur.execute(sqlInsert, (numero,))
            self.db.con.commit()
            self.db.mensaje = f"Dato eliminado correctamente, ID: {numero}"
            self.db.error = False
        except Exception as ex:
            self.db.mensaje = f"Falló al Eliminar: FALLÓ. {ex}"
            self.db.error = True

    def setCreate(self, reg:object):
        try:
            sqlInsert = "INSERT INTO autores (nombre, apellido, celular, email) VALUES (%s, %s, %s, %s)"
            autor = (reg.nombre, reg.apellido, reg.celular, reg.email)
            self.cur.execute(sqlInsert, autor)
            self.db.con.commit()
            self.db.mensaje = f"Valores insertados: {autor}"
            self.db.error = False
        except Exception as ex:
            self.db.mensaje = f"Falló al insertar los valores: {autor}"
            self.db.error = True

    def mis_tutoriales(self, numero:int):
        try:
            sqlInsert = '''SELECT tutoriales.id AS id,
            tutoriales.titulo AS titulo,
            tutoriales.creado as creado
            FROM tutoriales
            INNER JOIN autores ON tutoriales.autorid = autores.id AND autores.id = %s'''
            self.cur.execute(sqlInsert, (numero,))
            resultado = self.cur.fetchall()
            pre = []
            for reg in resultado:
                tutorial = Tutorial(reg[1], numero, reg[2])
                tutorial.id = reg[0]
                pre.append(tutorial)
            self.db.mensaje = f"INNER JOIN autores ON tutoriales, EXITOSO"
            self.db.error = False
            print(resultado[0])
            return pre
        except Exception as ex:
            self.db.mensaje = f"Falló el INNER: FALLÓ. {ex}"
            self.db.error = True
            return 'FALLO'
