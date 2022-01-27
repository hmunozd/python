import mysql.connector
from mysql.connector import errorcode
import abc
from typing import Text, TypeVar, Generic

class Conexion(object):

    def conectarse(self):
        try:
            self.con = mysql.connector.connect(
                user='sql10467211',
                password='QwDGRuN5zW',
                host='localhost',
                database='sql10467211',
            )
            print("Conexión exitosa con la base de datos 'sql10467211'")
            self.mensaje = "Conexión exitosa con la base de datos 'sql10467211'."
            self.error = False
        except mysql.connector.Error as err:
            self.error = True
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("El nombre de usuario o la contraseña son incorrectos")
                self.mensaje = "El nombre de usuario o la contraseña son incorrectos"
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("La base de datos no existe")
                self.mensaje = "La base de datos no existe"
            else:
                print(err)
                self.mensaje = err
    def cerrar_con(self):
        self.con.close()

class Dao(abc.ABC):
    @abc.abstractmethod
    def conectarse(self):
        ...

    @abc.abstractmethod
    def createTabla(self):
        ...

    @abc.abstractmethod
    def getAll(self):
        ...

    @abc.abstractmethod
    def getRegistro(self, numero:int):
        ...

    @abc.abstractmethod
    def setUpdate(self, reg:object):
        ...

    @abc.abstractmethod
    def setDelete(self, numero:int):
        ...

    @abc.abstractmethod
    def setCreate(self, reg:object):
        ...
