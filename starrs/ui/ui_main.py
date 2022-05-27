# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\projects\master\CIS556\dev\starrs\ui\ui_main.ui'
#
# Created: Fri May 27 13:45:20 2022
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_STARRS(object):
    def setupUi(self, STARRS):
        STARRS.setObjectName("STARRS")
        STARRS.resize(563, 877)
        self.centralwidget = QtGui.QWidget(STARRS)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabSections = QtGui.QTabWidget(self.centralwidget)
        self.tabSections.setObjectName("tabSections")
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabStudents = QtGui.QTableView(self.tab_1)
        self.tabStudents.setObjectName("tabStudents")
        self.verticalLayout_2.addWidget(self.tabStudents)
        self.splitter_2 = QtGui.QSplitter(self.tab_1)
        self.splitter_2.setMaximumSize(QtCore.QSize(16777215, 55))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setMaximumSize(QtCore.QSize(16777215, 20))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.linStudentFirstName = QtGui.QLineEdit(self.splitter)
        self.linStudentFirstName.setMaximumSize(QtCore.QSize(16777215, 20))
        self.linStudentFirstName.setObjectName("linStudentFirstName")
        self.linStudentLastName = QtGui.QLineEdit(self.splitter)
        self.linStudentLastName.setMaximumSize(QtCore.QSize(16777215, 20))
        self.linStudentLastName.setObjectName("linStudentLastName")
        self.linStudentDescription = QtGui.QLineEdit(self.splitter)
        self.linStudentDescription.setMaximumSize(QtCore.QSize(16777215, 20))
        self.linStudentDescription.setObjectName("linStudentDescription")
        self.btnAddStudent = QtGui.QPushButton(self.splitter_2)
        self.btnAddStudent.setMaximumSize(QtCore.QSize(16777215, 30))
        self.btnAddStudent.setObjectName("btnAddStudent")
        self.verticalLayout_2.addWidget(self.splitter_2)
        self.tabSections.addTab(self.tab_1, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabSections.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabSections.addTab(self.tab_3, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabSections.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.tabSections)
        STARRS.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(STARRS)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 563, 21))
        self.menubar.setObjectName("menubar")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        STARRS.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(STARRS)
        self.statusbar.setObjectName("statusbar")
        STARRS.setStatusBar(self.statusbar)
        self.actInitDatabase = QtGui.QAction(STARRS)
        self.actInitDatabase.setObjectName("actInitDatabase")
        self.menuEdit.addAction(self.actInitDatabase)
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(STARRS)
        self.tabSections.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(STARRS)

    def retranslateUi(self, STARRS):
        STARRS.setWindowTitle(QtGui.QApplication.translate("STARRS", "S T A R R S", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAddStudent.setText(QtGui.QApplication.translate("STARRS", "Add Student", None, QtGui.QApplication.UnicodeUTF8))
        self.tabSections.setTabText(self.tabSections.indexOf(self.tab_1), QtGui.QApplication.translate("STARRS", "Online Application Process", None, QtGui.QApplication.UnicodeUTF8))
        self.tabSections.setTabText(self.tabSections.indexOf(self.tab_2), QtGui.QApplication.translate("STARRS", "Admissions Process", None, QtGui.QApplication.UnicodeUTF8))
        self.tabSections.setTabText(self.tabSections.indexOf(self.tab_3), QtGui.QApplication.translate("STARRS", "Online Registration", None, QtGui.QApplication.UnicodeUTF8))
        self.tabSections.setTabText(self.tabSections.indexOf(self.tab_4), QtGui.QApplication.translate("STARRS", "Graduation Process", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("STARRS", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.actInitDatabase.setText(QtGui.QApplication.translate("STARRS", "Init Database", None, QtGui.QApplication.UnicodeUTF8))

