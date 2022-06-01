import os
import sqlite3
from PySide import QtGui
from PySide import QtCore
from ui import ui_main

scripts_root = os.path.dirname(__file__).replace('\\', '/')


# Database
def init_database(sql_file_path):
    """
    Create database tables
    """

    connection = sqlite3.connect(sql_file_path)
    cursor = connection.cursor()

    # OLD
    cursor.execute('''CREATE TABLE student (
                    id integer primary key autoincrement,
                    first_name text,
                    last_name text,
                    description text
                    )''')

    # User
    cursor.execute('''CREATE TABLE user (
                    id integer primary key autoincrement,
                    first_name text,
                    middle_name text,
                    last_name text,
                    email text,
                    address text,
                    phone text,
                    description text
                    )''')

    # Student application
    cursor.execute('''CREATE TABLE application (
                    id integer primary key autoincrement,
                    user_id integer,
                    gre_verbal text,
                    gre_quantitative text,
                    gre_analytical text,
                    date_received text,
                    experience text,
                    admission_term text,
                    degree_sought text,
                    prior1_major text,
                    prior1_year text,
                    prior1_gpa text,
                    prior1_university text,
                    prior2_major text,
                    prior2_year text,
                    prior2_gpa text,
                    prior2_university text,
                    status text,
                    description text,
                    FOREIGN KEY(user_id) REFERENCES user(id)
                    )''')

    connection.commit()
    connection.close()


class Student:
    def __init__(self, student_tuple):
        self.id = None
        self.first_name = ''
        self.last_name = ''
        self.description = ''

        self.init(student_tuple)

    def init(self, student_tuple):

        self.id = student_tuple[0]
        self.first_name = student_tuple[1]
        self.last_name = student_tuple[2]
        self.description = student_tuple[3]


class User:
    def __init__(self, user_tuple):
        self.id = None
        self.first_name = ''
        self.middle_name = ''
        self.last_name = ''
        self.email = ''
        self.address = ''
        self.phone = ''
        self.description = ''

        self.init(user_tuple)

    def init(self, user_tuple):

        self.id = user_tuple[0]
        self.first_name = user_tuple[1]
        self.middle_name = user_tuple[2]
        self.last_name = user_tuple[3]
        self.email = user_tuple[4]
        self.address = user_tuple[5]
        self.phone = user_tuple[6]
        self.description = user_tuple[7]


# Data models
class AlignDelegate(QtGui.QItemDelegate):
    def paint(self, painter, option, index):
        option.displayAlignment = QtCore.Qt.AlignCenter
        QtGui.QItemDelegate.paint(self, painter, option, index)


class Students:
    def __init__(self, sql_file_path):
        self.sql_file_path = sql_file_path
        self.list_students = []

    def convert_to_students(self, student_tuples):

        students = []

        for student_tuple in student_tuples:
            student = Student(student_tuple)
            students.append(student)

        return students

    def add_student(self, student_tuple):

        # Create student object
        student = Student(student_tuple)

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        # Add object to DB
        cursor.execute("INSERT INTO student VALUES ("
                       ":id,"
                       ":first_name,"
                       ":last_name,"
                       ":description)",

                       {'id': cursor.lastrowid,
                        'first_name': student.first_name,
                        'last_name': student.last_name,
                        'description': student.description})

        connection.commit()
        student.id = cursor.lastrowid  # Add database ID to the object
        connection.close()

        # Add student to data instance
        self.list_students.append(student)

    def get_students(self):

        connection = sqlite3.connect(self.sql_file_path)

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM student")
        student_tuples = cursor.fetchall()
        connection.close()

        if student_tuples:
            student_objects = self.convert_to_students(student_tuples)
            self.list_students.extend(student_objects)


class StudentsModel(QtCore.QAbstractTableModel):
    def __init__(self, students, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)

        self.students = students
        self.header = ['  Id  ', '  First Name ', '  Last Name ', '  Description  ']

    # Build-in functions
    def flags(self, index):

        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[col]

    def rowCount(self, parent):

        if not self.students.list_students:
            return 0

        return len(self.students.list_students)

    def columnCount(self, parent):

        return len(self.header)

    def data(self, index, role):

        if not index.isValid():
            return

        row = index.row()
        column = index.column()
        student = self.students.list_students[row]

        if role == QtCore.Qt.DisplayRole:  # Fill table data to DISPLAY
            if column == 0:
                return student.id

            if column == 1:
                return student.first_name

            if column == 2:
                return student.last_name

            if column == 3:
                return student.description


class StarrsData:
    def __init__(self, sql_file_path):
        self.sql_file_path = sql_file_path

    def add_user(self, user_tuple):

        user = User(user_tuple)

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        # Add object to DB
        cursor.execute("INSERT INTO user VALUES ("
                       ":id,"
                       ":first_name,"
                       ":middle_name,"
                       ":last_name,"
                       ":email,"
                       ":address,"
                       ":phone,"
                       ":description)",

                       {'id': cursor.lastrowid,
                        'first_name': user.first_name,
                        'middle_name': user.middle_name,
                        'last_name': user.last_name,
                        'email': user.email,
                        'address': user.address,
                        'phone': user.phone,
                        'description': user.description})

        connection.commit()
        user.id = cursor.lastrowid  # Add database ID to the object
        connection.close()

        print 'User {0} {1} added!'.format(user.first_name, user.last_name)


class STARRS(QtGui.QMainWindow, ui_main.Ui_STARRS):
    def __init__(self, parent=None):
        super(STARRS, self).__init__(parent=parent)

        # SETUP UI
        self.setupUi(self)
        # self.tabStudents.hide()

        # # Data
        # self.students_model = None
        # self.students_data = None
        #
        # # Load students
        # self.init_students()
        # self.btnAddStudent.clicked.connect(self.add_student)

        self.sql_file_path = '{0}/data/database.db'.format(scripts_root)
        self.starrs_data = None

        self.init_ui()
        self.init_data()

        # UI functionality
        self.actInitDatabase.triggered.connect(self.init_database)

        self.btnSubmitApplication.pressed.connect(self.submit_application)

    def init_ui(self):

        # Temp fill forms
        self.linStudentFirstName.setText('Sara')
        self.linStudentLastName.setText('Connor')
        self.linGREVErbal.setText('170')
        self.linGREVQuant.setText('170')
        self.linGREVAnalitical.setText('6')
        self.linApplicantEmail.setText('connor@umich.edu')
        self.linApplicantPhone.setText('734-780-0123')
        self.linAddressZip.setText('48067')
        self.linAddressState.setText('MI')
        self.linAddressCity.setText('Royal Oak')
        self.linAddressStreet.setText('W 6th st')
        self.linWorkExpirience.setText('I was working as developer at Google')
        self.linPriorDegree1.setText('Bachelor')
        self.linPriorYear1.setText('1998')
        self.linPriorGPA1.setText('3.2')
        self.linPriorUniversity1.setText('KTILP')
        self.linPriorDegree2.setText('Master')
        self.linPriorYear2.setText('1999')
        self.linPriorGPA2.setText('3.6')
        self.linPriorUniversity2.setText('KTILP')

        self.comDegreeSought.addItems(['MS', 'MSE'])
        self.comAdmissionTerm.addItems(['S2022', 'F2022', 'W2023', 'S2023', 'F2023'])

    def init_data(self):

        self.starrs_data = StarrsData(self.sql_file_path)

    def get_ui_apply(self):

        user_tuple = [
                        None,
                        self.linStudentFirstName.text(),
                        self.linStudentMidName.text(),
                        self.linStudentLastName.text(),
                        self.linApplicantEmail.text(),
                        '{0}, {1}, {2}, {3}'.format(self.linAddressZip.text(),
                                                    self.linAddressState.text(),
                                                    self.linAddressCity.text(),
                                                    self.linAddressStreet.text()),
                        self.linApplicantPhone.text(),
                        '']

        self.linGREVErbal.text()
        self.linGREVQuant.text()
        self.linGREVAnalitical.text()

        self.linWorkExpirience.text()
        self.comDegreeSought.currentText()
        self.comAdmissionTerm.currentText()
        self.linPriorDegree1.text()
        self.linPriorYear1.text()
        self.linPriorGPA1.text()
        self.linPriorUniversity1.text()
        self.linPriorDegree2.text()
        self.linPriorYear2.text()
        self.linPriorGPA2.text()
        self.linPriorUniversity2.text()

        return user_tuple

    def setup_table(self, table):

        table.verticalHeader().hide()
        table.verticalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        table.horizontalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        table.horizontalHeader().setStretchLastSection(True)
        table.setItemDelegate(AlignDelegate())

    def init_students(self):

        self.setup_table(self.tabStudents)

        self.students_data = Students(self.sql_file_path)
        self.students_data.get_students()

        self.students_model = StudentsModel(self.students_data)
        self.tabStudents.setModel(self.students_model)

    def init_database(self):
        """
        Create empty database tables
        """

        init_database(self.sql_file_path)

    def add_student(self):

        first_name = self.linStudentFirstName.text()
        last_name = self.linStudentLastName.text()
        description = self.linStudentDescription.text()
        student_tuple = [None, first_name, last_name, description]

        self.students_model.layoutAboutToBeChanged.emit()
        self.students_data.add_student(student_tuple)
        self.students_model.layoutChanged.emit()

    # 1) Online Application
    def submit_application(self):

        user_tuple = self.get_ui_apply()
        self.starrs_data.add_user(user_tuple)


if __name__ == "__main__":
    app = QtGui.QApplication([])
    starrs = STARRS()
    starrs.show()
    app.exec_()
