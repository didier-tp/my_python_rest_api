from devise import Devise
import sqlite3
from singleton import Singleton

#version simulee sans base de données , simple map/dictionnary en memoire

def columnsValuesToDeviseObject(listeValeursDeColonne):
    return Devise( listeValeursDeColonne[0] , listeValeursDeColonne[1]  , listeValeursDeColonne[2] );

def linesValuesToDeviseObjects(listeValeursDeLigne):
    devises=[]
    for elt in listeValeursDeLigne:
        devises.append(columnsValuesToDeviseObject(elt))
    return devises;


class DeviseService(metaclass=Singleton):
    def __init__(self):
        print("DeviseService via/with sqlLite")

    def getDevises(self):
        with sqlite3.connect("devises.db") as connection:
            cursor = connection.cursor()
            listeDevises = linesValuesToDeviseObjects( cursor.execute(
                "SELECT * FROM devise").fetchall())  # or .fetchone()
        print(">>> listeDevises=", listeDevises)
        return listeDevises;

    def getDeviseById(self , id ):
        with sqlite3.connect("devises.db") as connection:
            cursor = connection.cursor()
            devise = columnsValuesToDeviseObject(cursor.execute(
                "SELECT * FROM devise WHERE code='"+id+"'").fetchone())
        print(">>> devise for id=" ,id , "=", devise)
        return devise

    def createDevise(self , dev: Devise):
        key = dev.code;
        reqSql= "INSERT INTO devise(code, name, change) VALUES('" + dev.code + "', '" + dev.name + "'," + str(dev.change) + ")"
        print(">>> createDevise sql=", reqSql)
        with sqlite3.connect("devises.db") as connection:
            cursor = connection.cursor()
            cursor.execute(reqSql)


    def updateDevise(self, dev: Devise):
        key = dev.code;
        reqSql = "UPDATE devise SET name='" + dev.name + "' , change=" + str(dev.change) + "  WHERE code='" + key + "'"
        print(">>> updateDevise sql=", reqSql)
        with sqlite3.connect("devises.db") as connection:
            cursor = connection.cursor()
            cursor.execute(reqSql)


    def deleteDeviseById(self, id):
        deletedDevise = self.getDeviseById(id);
        reqSql = "DELETE FROM devise WHERE code='" + id + "'"
        print(">>> deleteDeviseById sql=", reqSql)
        with sqlite3.connect("devises.db") as connection:
            cursor = connection.cursor()
            cursor.execute(reqSql)
        return deletedDevise;