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
        print("...")

    def getDevises(self):
        #listeDevises = []
        with sqlite3.connect("devises.db") as connection:
            cursor = connection.cursor()
            listeDevises = linesValuesToDeviseObjects( cursor.execute(
                "SELECT * FROM devise").fetchall())  # or .fetchone()

        print(">>> listeDevises=", listeDevises)
        return listeDevises;

    def getDeviseById(self , id ):
        return None;

    def createDevise(self , dev: Devise):
        key = dev.code;


    def updateDevise(self, dev: Devise):
        key = dev.code;


    def saveDevise(self , dev : Devise ):
        print("ok")

    def deleteDeviseById(self, id):
        return None