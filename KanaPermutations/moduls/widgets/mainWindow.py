from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QMainWindow, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QFontDatabase

from random import *
import copy
import enum

import os

STUDIED_WORD_PROPABILITY = 0.4 # than we show random card we can use studied word instead of

class QType(enum.Enum):
    UNIQUE  = 0
    STUDIED = 1
    RANDOM  = 2
    UNDEFINED = -1


class MainWindow(QMainWindow):
    def __init__(self, getQuestFunc, allKeys, PATH_TO_STUDIED_KEYS):
        super(MainWindow, self).__init__()
        self.getQuestFunc = getQuestFunc
        self.allKeys = allKeys
        self.PATH_TO_STUDIED_KEYS = PATH_TO_STUDIED_KEYS
        self.qText, self.qAns = "UNDEFINED", "UNDEFINED" # текстовое представления полей вопроса и ответа
        self.qKey = "" # текущий ключ вопроса
        self.qType = QType.UNDEFINED
        self.readCurStudiesWords()
        self.initUI()
        self.retranslateUI()
        self.reinitUniqueKeys()

        self.i_stage = 0
        self.updateToNextState()

    def readCurStudiesWords(self):
        self.studiedWords = {}
        if os.path.isfile(self.PATH_TO_STUDIED_KEYS) == False:
            self.__rewriteStudiedWordsInFile()
        with open(self.PATH_TO_STUDIED_KEYS, "rt", encoding='utf8') as f:
            self.studiedWords = set(f.read().splitlines())

    def deleteStudiedWordsFromFile(self):
        self.__rewriteStudiedWordsInFile()

    def __rewriteStudiedWordsInFile(self):
        try:
            with open(self.PATH_TO_STUDIED_KEYS, "wt", encoding='utf8') as f:
                allWords = "\n".join(list(self.studiedWords))
                f.write(allWords)
        except Exception as e:
            print("")

    def initUI(self):
        l = QVBoxLayout()
        w_centr = QWidget()
        w_centr.setLayout(l)
        self.setCentralWidget(w_centr)
        self.l_question  = QLabel(self)
        self.l_answer    = QLabel(self)
        f = QFont("Meiryo", 70)
        self.l_question.setFont(f)
        f = QFont("Arial", 26)
        self.l_answer.setFont(f)
        l.setAlignment(Qt.AlignHCenter)
        self.l_question.setAlignment(Qt.AlignHCenter)
        l.addWidget(self.l_question)
        l.addWidget(self.l_answer)
        return


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.updateToNextState()
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.markCurrentCardAsStudied()
        event.accept()

    def markCurrentCardAsStudied(self):
        self.studiedWords.add(self.qKey)
        reply = QMessageBox().question(self, "Studied deleting", f"Do you studied '{self.qKey}'?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.deleteStudiedWordsFromFile()
        else:
            pass

    def updateToNextState(self):
        if self.i_stage % 2 == 1:
            self.showMeAnswer()
        else:
            self.getNextKard()

    def getCurTypeColor(self):
        if self.qType == QType.STUDIED:
            colorName = "blue"
        else:
            colorName = "black"
        return colorName

    def updateAnswer(self):
        colorName = self.getCurTypeColor()
        self.l_answer.setStyleSheet(f"QLabel {{ color : {colorName} }}")
        self.l_answer.setText(self.qAns)

    def updateQuestion(self):
        colorName = self.getCurTypeColor()
        self.l_question.setStyleSheet(f"QLabel {{ color : {colorName} }}")
        self.l_question.setText(self.qText)
        self.l_answer.setText("")

    def getNextKard(self):
        self.qKey, self.qType = self.getNextKey()
        self.qText, self.qAns = self.getQuestFunc(self.qKey)
        self.updateQuestion()
        self.i_stage += 1

    def showMeAnswer(self):
        self.updateAnswer()
        self.i_stage += 1

    def isTimeToUnique(self):
        # We mean self.i_stage have +2 increment
        if int((self.i_stage - (self.i_stage % 2))/2) % 2 == 0:
            return True
        return False

    def timeToRepeatStudied(self):
        return random() < STUDIED_WORD_PROPABILITY

    def reinitUniqueKeys(self):
        self.uniqueKeys = set(copy.deepcopy(self.allKeys))

    def getNextKey(self):
        unstudiedSet = self.uniqueKeys.difference(self.studiedWords)
        unstudiedPostFix = f" Unstudied {len(unstudiedSet)}"
        if self.isTimeToUnique():
            if len(unstudiedSet) == 0:
                self.reinitUniqueKeys()
                print("We had finished all unique.")
            qKey = choice(list(unstudiedSet))
            qType = QType.UNIQUE
            self.uniqueKeys.remove(qKey)
            self.setWindowTitle(f"unique {unstudiedPostFix}")
        else:
            if self.timeToRepeatStudied():
                qKey  = choice(list(self.studiedWords))
                qType = QType.STUDIED
                self.setWindowTitle(f"studied {unstudiedPostFix}")
            else:
                qKey  = choice(list(set(self.allKeys).difference(self.studiedWords)))
                qType = QType.RANDOM
                self.setWindowTitle(f"random {unstudiedPostFix}")
        return qKey, qType

    def retranslateUI(self):
        return

    pass