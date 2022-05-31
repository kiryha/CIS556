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


class STARRS(QtGui.QMainWindow, ui_main.Ui_STARRS):
    def __init__(self, parent=None):
        super(STARRS, self).__init__(parent=parent)

        # SETUP UI
        self.setupUi(self)
        # Temp
        self.tabStudents.hide()
        self.btnAddStudent.hide()

        # # Data
        # self.students_model = None
        # self.students_data = None
        #
        # # Load students
        # self.init_students()

        self.sql_file_path = '{0}/data/database.db'.format(scripts_root)

        self.init_ui()

        # UI functionality
        self.actInitDatabase.triggered.connect(self.init_database)
        # Students
        self.btnAddStudent.clicked.connect(self.add_student)

    def init_ui(self):

        self.comDegreeSought.addItems(['MS', 'MSE'])
        self.comAdmissionTerm.addItems(['S2022', 'F2022', 'W2023', 'S2023', 'F2023'])

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


if __name__ == "__main__":
    app = QtGui.QApplication([])
    starrs = STARRS()
    starrs.show()
    app.exec_()
