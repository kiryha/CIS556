# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created: Wed Jun  1 16:09:42 2022
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_STARRS(object):
    def setupUi(self, STARRS):
        STARRS.setObjectName("STARRS")
        STARRS.resize(563, 878)
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
        self.tabWidget = QtGui.QTabWidget(self.tab_1)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtGui.QSplitter(self.tab)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_3 = QtGui.QLabel(self.splitter)
        self.label_3.setMinimumSize(QtCore.QSize(200, 0))
        self.label_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_3.setObjectName("label_3")
        self.linStudentFirstName = QtGui.QLineEdit(self.splitter)
        self.linStudentFirstName.setMaximumSize(QtCore.QSize(16777215, 20))
        self.linStudentFirstName.setObjectName("linStudentFirstName")
        self.linStudentMidName = QtGui.QLineEdit(self.splitter)
        self.linStudentMidName.setMaximumSize(QtCore.QSize(16777215, 20))
        self.linStudentMidName.setObjectName("linStudentMidName")
        self.linStudentLastName = QtGui.QLineEdit(self.splitter)
        self.linStudentLastName.setMaximumSize(QtCore.QSize(16777215, 20))
        self.linStudentLastName.setObjectName("linStudentLastName")
        self.verticalLayout_3.addWidget(self.splitter)
        self.splitter_7 = QtGui.QSplitter(self.tab)
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setObjectName("splitter_7")
        self.label_9 = QtGui.QLabel(self.splitter_7)
        self.label_9.setMinimumSize(QtCore.QSize(200, 0))
        self.label_9.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_9.setObjectName("label_9")
        self.linGREVErbal = QtGui.QLineEdit(self.splitter_7)
        self.linGREVErbal.setObjectName("linGREVErbal")
        self.linGREVQuant = QtGui.QLineEdit(self.splitter_7)
        self.linGREVQuant.setObjectName("linGREVQuant")
        self.linGREVAnalitical = QtGui.QLineEdit(self.splitter_7)
        self.linGREVAnalitical.setObjectName("linGREVAnalitical")
        self.verticalLayout_3.addWidget(self.splitter_7)
        self.splitter_9 = QtGui.QSplitter(self.tab)
        self.splitter_9.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_9.setObjectName("splitter_9")
        self.label_11 = QtGui.QLabel(self.splitter_9)
        self.label_11.setMinimumSize(QtCore.QSize(200, 0))
        self.label_11.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_11.setObjectName("label_11")
        self.linApplicantEmail = QtGui.QLineEdit(self.splitter_9)
        self.linApplicantEmail.setObjectName("linApplicantEmail")
        self.verticalLayout_3.addWidget(self.splitter_9)
        self.splitter_11 = QtGui.QSplitter(self.tab)
        self.splitter_11.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_11.setObjectName("splitter_11")
        self.label_14 = QtGui.QLabel(self.splitter_11)
        self.label_14.setMinimumSize(QtCore.QSize(200, 0))
        self.label_14.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_14.setObjectName("label_14")
        self.linApplicantPhone = QtGui.QLineEdit(self.splitter_11)
        self.linApplicantPhone.setObjectName("linApplicantPhone")
        self.verticalLayout_3.addWidget(self.splitter_11)
        self.splitter_10 = QtGui.QSplitter(self.tab)
        self.splitter_10.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_10.setObjectName("splitter_10")
        self.label_12 = QtGui.QLabel(self.splitter_10)
        self.label_12.setMinimumSize(QtCore.QSize(200, 0))
        self.label_12.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_12.setObjectName("label_12")
        self.linAddressZip = QtGui.QLineEdit(self.splitter_10)
        self.linAddressZip.setObjectName("linAddressZip")
        self.linAddressState = QtGui.QLineEdit(self.splitter_10)
        self.linAddressState.setObjectName("linAddressState")
        self.linAddressCity = QtGui.QLineEdit(self.splitter_10)
        self.linAddressCity.setObjectName("linAddressCity")
        self.linAddressStreet = QtGui.QLineEdit(self.splitter_10)
        self.linAddressStreet.setObjectName("linAddressStreet")
        self.verticalLayout_3.addWidget(self.splitter_10)
        self.splitter_2 = QtGui.QSplitter(self.tab)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_4 = QtGui.QLabel(self.splitter_2)
        self.label_4.setMinimumSize(QtCore.QSize(200, 0))
        self.label_4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_4.setObjectName("label_4")
        self.linWorkExpirience = QtGui.QLineEdit(self.splitter_2)
        self.linWorkExpirience.setObjectName("linWorkExpirience")
        self.verticalLayout_3.addWidget(self.splitter_2)
        self.splitter_5 = QtGui.QSplitter(self.tab)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.label_7 = QtGui.QLabel(self.splitter_5)
        self.label_7.setMinimumSize(QtCore.QSize(200, 0))
        self.label_7.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_7.setObjectName("label_7")
        self.linPriorDegree1 = QtGui.QLineEdit(self.splitter_5)
        self.linPriorDegree1.setObjectName("linPriorDegree1")
        self.linPriorYear1 = QtGui.QLineEdit(self.splitter_5)
        self.linPriorYear1.setObjectName("linPriorYear1")
        self.linPriorGPA1 = QtGui.QLineEdit(self.splitter_5)
        self.linPriorGPA1.setObjectName("linPriorGPA1")
        self.linPriorUniversity1 = QtGui.QLineEdit(self.splitter_5)
        self.linPriorUniversity1.setObjectName("linPriorUniversity1")
        self.verticalLayout_3.addWidget(self.splitter_5)
        self.splitter_6 = QtGui.QSplitter(self.tab)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.label_8 = QtGui.QLabel(self.splitter_6)
        self.label_8.setMinimumSize(QtCore.QSize(200, 0))
        self.label_8.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_8.setObjectName("label_8")
        self.linPriorDegree2 = QtGui.QLineEdit(self.splitter_6)
        self.linPriorDegree2.setObjectName("linPriorDegree2")
        self.linPriorYear2 = QtGui.QLineEdit(self.splitter_6)
        self.linPriorYear2.setObjectName("linPriorYear2")
        self.linPriorGPA2 = QtGui.QLineEdit(self.splitter_6)
        self.linPriorGPA2.setObjectName("linPriorGPA2")
        self.linPriorUniversity2 = QtGui.QLineEdit(self.splitter_6)
        self.linPriorUniversity2.setObjectName("linPriorUniversity2")
        self.verticalLayout_3.addWidget(self.splitter_6)
        self.splitter_3 = QtGui.QSplitter(self.tab)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_5 = QtGui.QLabel(self.splitter_3)
        self.label_5.setObjectName("label_5")
        self.comAdmissionTerm = QtGui.QComboBox(self.splitter_3)
        self.comAdmissionTerm.setMaximumSize(QtCore.QSize(120, 16777215))
        self.comAdmissionTerm.setObjectName("comAdmissionTerm")
        self.verticalLayout_3.addWidget(self.splitter_3)
        self.splitter_4 = QtGui.QSplitter(self.tab)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_6 = QtGui.QLabel(self.splitter_4)
        self.label_6.setObjectName("label_6")
        self.comDegreeSought = QtGui.QComboBox(self.splitter_4)
        self.comDegreeSought.setMaximumSize(QtCore.QSize(120, 16777215))
        self.comDegreeSought.setObjectName("comDegreeSought")
        self.verticalLayout_3.addWidget(self.splitter_4)
        self.btnSubmitApplication = QtGui.QPushButton(self.tab)
        self.btnSubmitApplication.setMinimumSize(QtCore.QSize(0, 45))
        self.btnSubmitApplication.setObjectName("btnSubmitApplication")
        self.verticalLayout_3.addWidget(self.btnSubmitApplication)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.tabWidget.addTab(self.tab, "")
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.splitter_8 = QtGui.QSplitter(self.tab_5)
        self.splitter_8.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_8.setObjectName("splitter_8")
        self.label_10 = QtGui.QLabel(self.splitter_8)
        self.label_10.setObjectName("label_10")
        self.lineStudentID = QtGui.QLineEdit(self.splitter_8)
        self.lineStudentID.setObjectName("lineStudentID")
        self.verticalLayout_5.addWidget(self.splitter_8)
        self.btnCheckApplicationStatus = QtGui.QPushButton(self.tab_5)
        self.btnCheckApplicationStatus.setMinimumSize(QtCore.QSize(0, 45))
        self.btnCheckApplicationStatus.setObjectName("btnCheckApplicationStatus")
        self.verticalLayout_5.addWidget(self.btnCheckApplicationStatus)
        self.splitter_27 = QtGui.QSplitter(self.tab_5)
        self.splitter_27.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_27.setObjectName("splitter_27")
        self.labApplicationStatus = QtGui.QLabel(self.splitter_27)
        self.labApplicationStatus.setMaximumSize(QtCore.QSize(120, 16777215))
        self.labApplicationStatus.setObjectName("labApplicationStatus")
        self.linApplicationStatus = QtGui.QLineEdit(self.splitter_27)
        self.linApplicationStatus.setEnabled(False)
        self.linApplicationStatus.setObjectName("linApplicationStatus")
        self.verticalLayout_5.addWidget(self.splitter_27)
        self.line = QtGui.QFrame(self.tab_5)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.btnEnroll = QtGui.QPushButton(self.tab_5)
        self.btnEnroll.setMinimumSize(QtCore.QSize(0, 45))
        self.btnEnroll.setObjectName("btnEnroll")
        self.verticalLayout_5.addWidget(self.btnEnroll)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab_5, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.tabSections.addTab(self.tab_1, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox = QtGui.QGroupBox(self.tab_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.splitter_12 = QtGui.QSplitter(self.groupBox)
        self.splitter_12.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_12.setObjectName("splitter_12")
        self.label_15 = QtGui.QLabel(self.splitter_12)
        self.label_15.setMinimumSize(QtCore.QSize(200, 0))
        self.label_15.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_15.setObjectName("label_15")
        self.linStudentIDAdmission = QtGui.QLineEdit(self.splitter_12)
        self.linStudentIDAdmission.setObjectName("linStudentIDAdmission")
        self.verticalLayout_10.addWidget(self.splitter_12)
        self.splitter_13 = QtGui.QSplitter(self.groupBox)
        self.splitter_13.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_13.setObjectName("splitter_13")
        self.label = QtGui.QLabel(self.splitter_13)
        self.label.setMinimumSize(QtCore.QSize(200, 0))
        self.label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label.setObjectName("label")
        self.linTranscript = QtGui.QLineEdit(self.splitter_13)
        self.linTranscript.setObjectName("linTranscript")
        self.linRecommendation = QtGui.QLineEdit(self.splitter_13)
        self.linRecommendation.setObjectName("linRecommendation")
        self.verticalLayout_10.addWidget(self.splitter_13)
        self.line_3 = QtGui.QFrame(self.groupBox)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_10.addWidget(self.line_3)
        self.btnAddStudentData = QtGui.QPushButton(self.groupBox)
        self.btnAddStudentData.setMinimumSize(QtCore.QSize(0, 45))
        self.btnAddStudentData.setObjectName("btnAddStudentData")
        self.verticalLayout_10.addWidget(self.btnAddStudentData)
        self.verticalLayout_6.addWidget(self.groupBox)
        self.groupBox_4 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.btnGetPendingApplicants = QtGui.QPushButton(self.groupBox_4)
        self.btnGetPendingApplicants.setMinimumSize(QtCore.QSize(0, 45))
        self.btnGetPendingApplicants.setObjectName("btnGetPendingApplicants")
        self.verticalLayout_11.addWidget(self.btnGetPendingApplicants)
        self.splitter_26 = QtGui.QSplitter(self.groupBox_4)
        self.splitter_26.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_26.setObjectName("splitter_26")
        self.label_27 = QtGui.QLabel(self.splitter_26)
        self.label_27.setMinimumSize(QtCore.QSize(200, 0))
        self.label_27.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_27.setObjectName("label_27")
        self.comPendingApplicants = QtGui.QComboBox(self.splitter_26)
        self.comPendingApplicants.setObjectName("comPendingApplicants")
        self.verticalLayout_11.addWidget(self.splitter_26)
        self.splitter_14 = QtGui.QSplitter(self.groupBox_4)
        self.splitter_14.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_14.setObjectName("splitter_14")
        self.label_2 = QtGui.QLabel(self.splitter_14)
        self.label_2.setMinimumSize(QtCore.QSize(200, 0))
        self.label_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_2.setObjectName("label_2")
        self.comDescision = QtGui.QComboBox(self.splitter_14)
        self.comDescision.setObjectName("comDescision")
        self.verticalLayout_11.addWidget(self.splitter_14)
        self.btnMadeDecision = QtGui.QPushButton(self.groupBox_4)
        self.btnMadeDecision.setMinimumSize(QtCore.QSize(0, 45))
        self.btnMadeDecision.setObjectName("btnMadeDecision")
        self.verticalLayout_11.addWidget(self.btnMadeDecision)
        self.verticalLayout_6.addWidget(self.groupBox_4)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
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
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(STARRS)

    def retranslateUi(self, STARRS):
        STARRS.setWindowTitle(QtGui.QApplication.translate("STARRS", "S T A R R S", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("STARRS", "Firs Name | Midle Name | Last Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("STARRS", "GRE: Verbal | Quantitative | Analitical", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("STARRS", "Applicant email", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("STARRS", "Cell Number", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("STARRS", "Zip | State | City | Street", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("STARRS", "Prior Work Expirience:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("STARRS", "1 Prior Degree | Year | GPA | University ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("STARRS", "2 Prior Degree | Year | GPA | University ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("STARRS", "Admission Term:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("STARRS", "Apply for Degree", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSubmitApplication.setText(QtGui.QApplication.translate("STARRS", "Submit Application", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("STARRS", "Apply for Degree", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("STARRS", "Enter student ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCheckApplicationStatus.setText(QtGui.QApplication.translate("STARRS", "Check Application Status", None, QtGui.QApplication.UnicodeUTF8))
        self.labApplicationStatus.setText(QtGui.QApplication.translate("STARRS", "Application status:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEnroll.setText(QtGui.QApplication.translate("STARRS", "Enroll to Database University", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtGui.QApplication.translate("STARRS", "Check Application Status", None, QtGui.QApplication.UnicodeUTF8))
        self.tabSections.setTabText(self.tabSections.indexOf(self.tab_1), QtGui.QApplication.translate("STARRS", "Online Application Process", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("STARRS", "Submit Student Data", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("STARRS", "Enter student ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("STARRS", "Transcripts | Recomendations:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAddStudentData.setText(QtGui.QApplication.translate("STARRS", "Add Student Transcripts and Recomendations", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("STARRS", "Make Decision", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGetPendingApplicants.setText(QtGui.QApplication.translate("STARRS", "Get List of Decision Pending Applicants", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("STARRS", "List of Decision Pending Applicants", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("STARRS", "Select applicant destiny", None, QtGui.QApplication.UnicodeUTF8))
        self.btnMadeDecision.setText(QtGui.QApplication.translate("STARRS", "Submit Applicant Status", None, QtGui.QApplication.UnicodeUTF8))
        self.tabSections.setTabText(self.tabSections.indexOf(self.tab_2), QtGui.QApplication.translate("STARRS", "Admissions Process", None, QtGui.QApplication.UnicodeUTF8))
        self.tabSections.setTabText(self.tabSections.indexOf(self.tab_3), QtGui.QApplication.translate("STARRS", "Online Registration", None, QtGui.QApplication.UnicodeUTF8))
        self.tabSections.setTabText(self.tabSections.indexOf(self.tab_4), QtGui.QApplication.translate("STARRS", "Graduation Process", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("STARRS", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.actInitDatabase.setText(QtGui.QApplication.translate("STARRS", "Init Database", None, QtGui.QApplication.UnicodeUTF8))

