import sys
import time
from search import *
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.comboBox.setCurrentIndex(0)
        self.ui.comboBox.addItems((str(i) for i in range(3, 15)))
        self.ui.statusbar.showMessage('Moskalyuk Andriy, 2017')

        self.ui.pushButton.clicked.connect(self.start1)
        self.ui.pushButton_2.clicked.connect(self.save_to_file)

        self.writeFile = open("text.txt", 'w', encoding='utf-8')
        self.writeFile.close()

    created = False

    def save_to_file(self):
        s = self.ui.plainTextEdit.toPlainText()
        f = open('text.txt', 'a')
        f.write(s)
        f.write('\n\n')
        f.close()

    def start1(self):
        self.ui.pushButton.setEnabled(False)
        self.ui.plainTextEdit.clear()
        self.lenth_of_word = int(self.ui.comboBox.currentText())
        self.letters = self.ui.lineEdit.text()

        self.word(self.letters, self.lenth_of_word)

    def word(self, letters, lenth_of_word):

        self.cancelled = False

        self.t1 = time.time()
        self.resArr = []
        self.init = set(letters)
        self.res = ["", "", "", ""]
        print(lenth_of_word)
        for s in open("dict.txt", 'r', encoding='utf-8'):
            if (len(s) == lenth_of_word) and (self.init <= set(s)):
                self.resArr.append(s)

        self.str = "Find match: " + str(len(self.resArr)) + "\n" + ' '.join(self.resArr) + "\n" + "It took: " + str(
            time.time() - self.t1) + " с."
        self.ui.plainTextEdit.appendPlainText(self.str)


        self.ui.pushButton.setEnabled(True)

    def wordFive(self, letters):

        self.cancelled = False

        self.t1 = time.time()
        self.c = 0
        self.resArr = []
        self.init = letters
        self.res = ["", "", "", "", ""]
        self.r = open("dict.txt", 'r', encoding='utf-8')
        self.fileRead = self.r.read()
        self.fileSplit = [i for i in self.fileRead.split() if len(i) == 4]
        self.r.close()

        self.progress = QtWidgets.QProgressDialog("Searching...", "Stop", 0, len(self.init), self.ui.lineEdit)
        self.progress.setWindowModality(QtCore.Qt.WindowModal)
        self.progress.setMinimumDuration(1000)

        for self.i in range(0, len(self.init)):
            self.res[0] = self.init[self.i]

            self.progress.setValue(self.i)
            if self.progress.wasCanceled():
                self.cancelled = True
                self.ui.pushButton.setEnabled(True)
                return

            for self.q in range(0, len(self.init)):
                if (self.q != self.i):
                    self.res[1] = self.init[self.q]

                    for self.p in range(0, len(self.init)):
                        if (self.p != self.i) and (self.p != self.q):
                            self.res[2] = self.init[self.p]

                            for self.pp in range(0, len(self.init)):
                                if (self.pp != self.i) and (self.pp != self.q) and (self.pp != self.p):
                                    self.res[3] = self.init[self.pp]

                                    for self.qq in range(0, len(self.init)):
                                        if (self.qq != self.i) and (self.qq != self.q) and (self.qq != self.p) and (
                                            self.qq != self.pp):
                                            self.res[4] = self.init[self.qq]

                                            self.wordFve = self.res[0] + self.res[1] + self.res[2] + self.res[3] + \
                                                           self.res[4]
                                            if self.wordFve in self.fileSplit:
                                                if self.wordFve not in self.resArr:
                                                    self.resArr.append(self.wordFve)

                                            self.c += 1

        self.str = "Найдено совпадений: " + str(len(self.resArr)) + "\n" + self.arrOutput(self.resArr) + "\n" + str(
            self.c) + " комбинаций проверено\nВремя исполнения: " + str(time.time() - self.t1) + " с."
        self.ui.plainTextEdit.appendPlainText(self.str)
        self.progress.deleteLater()
        self.ui.pushButton.setEnabled(True)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())