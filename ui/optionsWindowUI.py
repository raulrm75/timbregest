# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optionsWindow.ui'
#
# Created: Mon Oct 20 12:46:57 2014
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
        MainWindow.resize(438, 356)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabPowerOff = QtGui.QTabWidget(self.centralwidget)
        self.tabPowerOff.setObjectName(_fromUtf8("tabPowerOff"))
        self.tabAlarms = QtGui.QWidget()
        self.tabAlarms.setObjectName(_fromUtf8("tabAlarms"))
        self.formLayout = QtGui.QFormLayout(self.tabAlarms)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.tabAlarms)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.tabAlarms)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.toolButton = QtGui.QToolButton(self.tabAlarms)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout.addWidget(self.toolButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.tabAlarms)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(self.tabAlarms)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.toolButton_2 = QtGui.QToolButton(self.tabAlarms)
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.horizontalLayout_2.addWidget(self.toolButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.formLayout.setLayout(0, QtGui.QFormLayout.LabelRole, self.verticalLayout_2)
        self.tabPowerOff.addTab(self.tabAlarms, _fromUtf8(""))
        self.tabFreeDays = QtGui.QWidget()
        self.tabFreeDays.setObjectName(_fromUtf8("tabFreeDays"))
        self.layoutWidget = QtGui.QWidget(self.tabFreeDays)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 298, 217))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.tableWidget = QtGui.QTableWidget(self.layoutWidget)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_3.addWidget(self.tableWidget)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.toolButton_3 = QtGui.QToolButton(self.layoutWidget)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("list-add"))
        self.toolButton_3.setIcon(icon)
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.verticalLayout_3.addWidget(self.toolButton_3)
        self.toolButton_4 = QtGui.QToolButton(self.layoutWidget)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("list-remove"))
        self.toolButton_4.setIcon(icon)
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))
        self.verticalLayout_3.addWidget(self.toolButton_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.tabPowerOff.addTab(self.tabFreeDays, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.layoutWidget1 = QtGui.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 254, 56))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.checkBox = QtGui.QCheckBox(self.layoutWidget1)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout_5.addWidget(self.checkBox)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.timeEdit = QtGui.QTimeEdit(self.layoutWidget1)
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.horizontalLayout_4.addWidget(self.timeEdit)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.tabPowerOff.addTab(self.tab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabPowerOff)
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
        self.tabPowerOff.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "TimbreGest - IES Almudeyne [Opciones]", None))
        self.label.setText(_translate("MainWindow", "Alarma inicial", None))
        self.toolButton.setText(_translate("MainWindow", "...", None))
        self.label_2.setText(_translate("MainWindow", "Alarma final", None))
        self.toolButton_2.setText(_translate("MainWindow", "...", None))
        self.tabPowerOff.setTabText(self.tabPowerOff.indexOf(self.tabAlarms), _translate("MainWindow", "Alarmas", None))
        self.label_3.setText(_translate("MainWindow", "Días libres", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Descripción", None))
        self.toolButton_3.setText(_translate("MainWindow", "...", None))
        self.toolButton_4.setText(_translate("MainWindow", "...", None))
        self.tabPowerOff.setTabText(self.tabPowerOff.indexOf(self.tabFreeDays), _translate("MainWindow", "Festivos", None))
        self.checkBox.setText(_translate("MainWindow", "Habilitar apagado automático", None))
        self.label_4.setText(_translate("MainWindow", "Hora de apagado automático", None))
        self.tabPowerOff.setTabText(self.tabPowerOff.indexOf(self.tab), _translate("MainWindow", "Apagado automático", None))
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
