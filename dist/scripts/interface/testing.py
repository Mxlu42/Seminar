import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dbhelp import *

db = DBHelp()
noten = db.get_noten_faecher(['Mathe'], [1, 2])