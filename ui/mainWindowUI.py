# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Mon Oct 20 12:45:12 2014
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
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.listSessions = QtGui.QListWidget(self.centralwidget)
        self.listSessions.setObjectName(_fromUtf8("listSessions"))
        self.gridLayout.addWidget(self.listSessions, 1, 0, 1, 1)
        self.tableLog = QtGui.QTableWidget(self.centralwidget)
        self.tableLog.setObjectName(_fromUtf8("tableLog"))
        self.tableLog.setColumnCount(2)
        self.tableLog.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableLog.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableLog.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.tableLog, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNewSession = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("list-add"))
        self.actionNewSession.setIcon(icon)
        self.actionNewSession.setObjectName(_fromUtf8("actionNewSession"))
        self.actionRemoveSession = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("list-remove"))
        self.actionRemoveSession.setIcon(icon)
        self.actionRemoveSession.setObjectName(_fromUtf8("actionRemoveSession"))
        self.actionModifySession = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-properties"))
        self.actionModifySession.setIcon(icon)
        self.actionModifySession.setObjectName(_fromUtf8("actionModifySession"))
        self.actionPlay = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("media-playback-start"))
        self.actionPlay.setIcon(icon)
        self.actionPlay.setObjectName(_fromUtf8("actionPlay"))
        self.actionStop = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("media-playback-stop"))
        self.actionStop.setIcon(icon)
        self.actionStop.setObjectName(_fromUtf8("actionStop"))
        self.actionPause = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("media-playback-pause"))
        self.actionPause.setIcon(icon)
        self.actionPause.setObjectName(_fromUtf8("actionPause"))
        self.actionConfigure = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("applications-system"))
        self.actionConfigure.setIcon(icon)
        self.actionConfigure.setObjectName(_fromUtf8("actionConfigure"))
        self.actionQuit = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("application-exit"))
        self.actionQuit.setIcon(icon)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.toolBar.addAction(self.actionNewSession)
        self.toolBar.addAction(self.actionRemoveSession)
        self.toolBar.addAction(self.actionModifySession)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPlay)
        self.toolBar.addAction(self.actionPause)
        self.toolBar.addAction(self.actionStop)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionConfigure)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "TimbreGest - IES Almudeyne", None))
        self.label.setText(_translate("MainWindow", "Sesiones", None))
        self.label_2.setText(_translate("MainWindow", "Información de registro", None))
        item = self.tableLog.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Hora", None))
        item = self.tableLog.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Descripción", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionNewSession.setText(_translate("MainWindow", "Nueva sesión", None))
        self.actionNewSession.setToolTip(_translate("MainWindow", "<html><head/><body><p>Crea una <span style=\" font-weight:600;\">sesión</span> (conjunto de alarmas que suenan secuencialmente a una hora concreta) y que se repite automáticamente en unos días de la semana.</p></body></html>", None))
        self.actionRemoveSession.setText(_translate("MainWindow", "Eliminar sesión", None))
        self.actionRemoveSession.setToolTip(_translate("MainWindow", "<html><head/><body><p>Elimina la <span style=\" font-weight:600;\">sesión actual</span>.</p></body></html>", None))
        self.actionModifySession.setText(_translate("MainWindow", "Modificar sesión", None))
        self.actionModifySession.setToolTip(_translate("MainWindow", "<html><head/><body><p>Modifica la sesión actual.</p></body></html>", None))
        self.actionPlay.setText(_translate("MainWindow", "Reproducir sesión", None))
        self.actionPlay.setToolTip(_translate("MainWindow", "<html><head/><body><p>Reproduce la sesión seleccionada.</p></body></html>", None))
        self.actionStop.setText(_translate("MainWindow", "Parar reproducción", None))
        self.actionStop.setToolTip(_translate("MainWindow", "<html><head/><body><p>Para la reproducción en curso.</p></body></html>", None))
        self.actionPause.setText(_translate("MainWindow", "Pausa", None))
        self.actionPause.setToolTip(_translate("MainWindow", "<html><head/><body><p>Pausa la reproducción actual.</p></body></html>", None))
        self.actionConfigure.setText(_translate("MainWindow", "Configuración", None))
        self.actionConfigure.setToolTip(_translate("MainWindow", "<html><head/><body><p>Configura la aplicación.</p></body></html>", None))
        self.actionQuit.setText(_translate("MainWindow", "Salir", None))
        self.actionQuit.setToolTip(_translate("MainWindow", "<html><head/><body><p>Cierra la aplicación.</p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

