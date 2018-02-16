from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = r'C:\Users\Utilisateur\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Utilisateur\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'

setup(
    name = "MondoClean",
    version = "0",
    description = "Data Cleaner permettant le pre traitement/conditionnement de larges donnees Excel",
    options = {'build.exe':{'packages': ['pandas', 'tkinter', 'openpyxl', 'PIL', 'secrets', 'numpy',  'numpy.core._methods'],
                            'include_files': ["tcl86t.dll", "tk86t.dll"]}},
    executables = [Executable('UI.py')],
)
