from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QPushButton

from .widgets.mainWindow import MainWindow
from .dataPreparation import get_allKeys, get_ansAsKanas, get_ansAsKangi, get_ansAsTranslate



def showMeKards(dataKey, keyBound, PATH_TO_STUDIED_KEYS):

    app = QApplication([])
    app.setStyle('Fusion')

    allKeys = get_allKeys()
    if keyBound != None:
        allKeys = allKeys[:keyBound]

    if   dataKey == 0:
        mainWindow = MainWindow(get_ansAsKangi,     allKeys, PATH_TO_STUDIED_KEYS)
    elif dataKey == 1:
        mainWindow = MainWindow(get_ansAsKanas,     allKeys, PATH_TO_STUDIED_KEYS)
    elif dataKey == 2:
        mainWindow = MainWindow(get_ansAsTranslate, allKeys, PATH_TO_STUDIED_KEYS)
    else:
        assert False, ValueError("Cur data key maintains [0 - kangi, 1 - hiragana, 2 - translate]")

    mainWindow.setFixedSize(1500, 600)
    mainWindow.show()

    app.exec()
    return