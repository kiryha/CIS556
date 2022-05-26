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

    # PROJECT MANAGER ITEMS
    cursor.execute('''CREATE TABLE student (
                    id integer primary key autoincrement,
                    first_name text,
                    last_name text,
                    description text
                    )''')

    connection.commit()
    connection.close()


class Student:
    def __init__(self):
        self.id = None
        self.first_name = ''
        self.last_name = ''
        self.description = ''


# Data models
class AlignDelegate(QtGui.QItemDelegate):
    def paint(self, painter, option, index):
        option.displayAlignment = QtCore.Qt.AlignCenter
        QtGui.QItemDelegate.paint(self, painter, option, index)


class Students:
    def __init__(self):
        self.list_students = []

    def get_students(self):

        student = Student()
        student.first_name = 'Kiryha'
        student.last_name = 'Krysko'

        self.list_students.append(student)


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

        return 4

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
        # self.resize(1920, 1000)

        self.sql_file_path = '{0}/data/database.db'.format(scripts_root)

        # Load students
        self.init_students()

        # UI functionality
        self.actInitDatabase.triggered.connect(self.init_database)

    def setup_table(self, table):

        table.verticalHeader().hide()
        table.verticalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        table.horizontalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        table.horizontalHeader().setStretchLastSection(True)
        table.setItemDelegate(AlignDelegate())

    def init_students(self):

        self.setup_table(self.tabStudents)

        students_data = Students()
        students_data.get_students()

        students_model = StudentsModel(students_data)
        self.tabStudents.setModel(students_model)

    def init_database(self):
        """
        Create empty database tables
        """

        init_database(self.sql_file_path)


if __name__ == "__main__":
    app = QtGui.QApplication([])
    starrs = STARRS()
    starrs.show()
    app.exec_()
