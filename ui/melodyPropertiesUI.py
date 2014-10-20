# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'melodyProperties.ui'
#
# Created: Mon Oct 20 12:47:15 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(483, 244)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.editFile = QtGui.QLineEdit(self.centralwidget)
        self.editFile.setObjectName(_fromUtf8("editFile"))
        self.horizontalLayout.addWidget(self.editFile)
        self.btnLoadFile = QtGui.QToolButton(self.centralwidget)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-open"))
        self.btnLoadFile.setIcon(icon)
        self.btnLoadFile.setObjectName(_fromUtf8("btnLoadFile"))
        self.horizontalLayout.addWidget(self.btnLoadFile)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.sliderInit = QtGui.QSlider(self.centralwidget)
        self.sliderInit.setOrientation(QtCore.Qt.Horizontal)
        self.sliderInit.setObjectName(_fromUtf8("sliderInit"))
        self.horizontalLayout_2.addWidget(self.sliderInit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.sliderLength = QtGui.QSlider(self.centralwidget)
        self.sliderLength.setOrientation(QtCore.Qt.Horizontal)
        self.sliderLength.setObjectName(_fromUtf8("sliderLength"))
        self.horizontalLayout_3.addWidget(self.sliderLength)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.dialVolume = QtGui.QDial(self.centralwidget)
        self.dialVolume.setObjectName(_fromUtf8("dialVolume"))
        self.horizontalLayout_4.addWidget(self.dialVolume)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSave = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-save"))
        self.actionSave.setIcon(icon)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionDiscard = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-revert"))
        self.actionDiscard.setIcon(icon)
        self.actionDiscard.setObjectName(_fromUtf8("actionDiscard"))
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionDiscard)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "TimbreGest - IES Almudeyne [Propiedades de timbre]", None))
        self.label.setText(_translate("MainWindow", "Archivo", None))
        self.btnLoadFile.setText(_translate("MainWindow", "...", None))
        self.label_2.setText(_translate("MainWindow", "Inicio", None))
        self.label_3.setText(_translate("MainWindow", "Duración", None))
        self.label_4.setText(_translate("MainWindow", "Volumen", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionSave.setText(_translate("MainWindow", "Guardar cambios", None))
        self.actionSave.setToolTip(_translate("MainWindow", "<html><head/><body><p>Guarda los cambios realizados.</p></body></html>", None))
        self.actionDiscard.setText(_translate("MainWindow", "Descartar cambios", None))
        self.actionDiscard.setToolTip(_translate("MainWindow", "<html><head/><body><p>Descarta los cambios realizados.</p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

