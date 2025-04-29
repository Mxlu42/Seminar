from pymongo import MongoClient
import sys
import os

class Create_Data():
    def __init__(self):
        with open('blueprint.txt', 'r', encoding='utf-8') as file:
            inhalt = file.read()
            print(inhalt)

cs = Create_Data()

cs()