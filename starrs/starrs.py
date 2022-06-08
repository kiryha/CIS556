import os
import sqlite3
import smtplib
from datetime import date
from PySide import QtGui, QtCore
from ui import ui_main

scripts_root = os.path.dirname(__file__).replace('\\', '/')


# Database
def init_database(sql_file_path):
    """
    Create database tables
    """

    connection = sqlite3.connect(sql_file_path)
    cursor = connection.cursor()

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
                    date_received text,
                    transcripts integer,
                    gre_verbal text,
                    gre_quantitative text,
                    gre_analytical text,
                    experience text,
                    interest text,
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
                    ranking text,
                    comments text,
                    description text,
                    FOREIGN KEY(user_id) REFERENCES user(id)
                    )''')

    cursor.execute('''CREATE TABLE recommendation (
                    id integer primary key autoincrement,
                    user_id integer,
                    name text,
                    email text,
                    title text,
                    affiliation text,
                    score text,
                    description text,
                    FOREIGN KEY(user_id) REFERENCES user(id)
                    )''')

    cursor.execute('''CREATE TABLE student (
                    id integer primary key autoincrement,
                    user_id integer,
                    description text,
                    FOREIGN KEY(user_id) REFERENCES user(id)
                    )''')

    connection.commit()
    connection.close()


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


class Application:
    def __init__(self, application_tuple):
        self.id = None
        self.user_id = None
        self.date_received = ''
        self.transcripts = None
        self.gre_verbal = ''
        self.gre_quantitative = ''
        self.gre_analytical = ''
        self.experience = ''
        self.interest = ''
        self.admission_term = ''
        self.degree_sought = ''
        self.prior1_major = ''
        self.prior1_year = ''
        self.prior1_gpa = ''
        self.prior1_university = ''
        self.prior2_major = ''
        self.prior2_year = ''
        self.prior2_gpa = ''
        self.prior2_university = ''
        self.status = ''
        self.ranking = ''
        self.comments = ''
        self.description = ''

        self.init(application_tuple)

    def init(self, application_tuple):

        self.id = application_tuple[0]
        self.user_id = application_tuple[1]
        self.date_received = application_tuple[2]
        self.transcripts = application_tuple[3]
        self.gre_verbal = application_tuple[4]
        self.gre_quantitative = application_tuple[5]
        self.gre_analytical = application_tuple[6]
        self.experience = application_tuple[7]
        self.interest = application_tuple[8]
        self.admission_term = application_tuple[9]
        self.degree_sought = application_tuple[10]
        self.prior1_major = application_tuple[11]
        self.prior1_year = application_tuple[12]
        self.prior1_gpa = application_tuple[13]
        self.prior1_university = application_tuple[14]
        self.prior2_major = application_tuple[15]
        self.prior2_year = application_tuple[16]
        self.prior2_gpa = application_tuple[17]
        self.prior2_university = application_tuple[18]
        self.status = application_tuple[19]
        self.ranking = application_tuple[20]
        self.comments = application_tuple[21]
        self.description = application_tuple[22]


class Recommendation:
    def __init__(self, recommendation_tuple):
        self.id = None
        self.user_id = None
        self.name = None
        self.email = None
        self.title = None
        self.affiliation = None
        self.score = None
        self.description = None

        self.init(recommendation_tuple)

    def init(self, recommendation_tuple):

        self.id = recommendation_tuple[0]
        self.user_id = recommendation_tuple[1]
        self.name = recommendation_tuple[2]
        self.email = recommendation_tuple[3]
        self.title = recommendation_tuple[4]
        self.affiliation = recommendation_tuple[5]
        self.score = recommendation_tuple[6]
        self.description = recommendation_tuple[7]


class Student:
    def __init__(self, student_tuple):
        self.id = None
        self.user_id = None
        self.description = None

        self.init(student_tuple)

    def init(self, student_tuple):

        self.id = student_tuple[0]
        self.user_id = student_tuple[1]
        self.description = student_tuple[2]


# Database manipulations
class StarrsData:
    def __init__(self, sql_file_path):
        self.sql_file_path = sql_file_path

        # Processed data
        self.pending_users = []
        self.pending_applications = []

        self.init_starrs_data()

    # Data init
    def init_starrs_data(self):

        self.get_pending_applicants()

    # Tuple to object conversion
    def convert_to_user(self, user_tuples):

        users = []

        for user_tuple in user_tuples:
            user = User(user_tuple)
            users.append(user)

        return users

    def convert_to_application(self, application_tuples):

        applications = []

        for application_tuple in application_tuples:
            application = Application(application_tuple)
            applications.append(application)

        return applications

    def convert_to_recommendation(self, recommendation_tuples):

        recommendations = []

        for recommendation_tuple in recommendation_tuples:
            recommendation = Recommendation(recommendation_tuple)
            recommendations.append(recommendation)

        return recommendations

    # Basic CURDs
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
        return user

    def get_user(self, user_id):

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM user WHERE id=:id",
                       {'id': user_id})

        user_tuple = cursor.fetchone()

        connection.close()

        if user_tuple:
            return self.convert_to_user([user_tuple])[0]

    def get_user_by_name(self, last_name):

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM user WHERE last_name=:last_name",
                       {'last_name': last_name})

        user_tuples = cursor.fetchall()
        connection.close()

        if user_tuples:
            return self.convert_to_user(user_tuples)

    def add_application(self, application_tuple):

        application = Application(application_tuple)

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        # Add object to DB
        cursor.execute("INSERT INTO application VALUES ("
                       ":id,"
                       ":user_id,"
                       ":date_received,"
                       ":transcripts,"
                       ":gre_verbal,"
                       ":gre_quantitative,"
                       ":gre_analytical,"
                       ":experience,"
                       ":interest,"
                       ":admission_term,"
                       ":degree_sought,"
                       ":prior1_major,"
                       ":prior1_year,"
                       ":prior1_gpa,"
                       ":prior1_university," 
                       ":prior2_major,"
                       ":prior2_year,"
                       ":prior2_gpa,"
                       ":prior2_university,"
                       ":status,"
                       ":ranking,"
                       ":comments,"
                       ":description)",

                       {'id': cursor.lastrowid,
                        'user_id': application.user_id,
                        'date_received': application.date_received,
                        'transcripts': application.transcripts,
                        'gre_verbal': application.gre_verbal,
                        'gre_quantitative': application.gre_quantitative,
                        'gre_analytical': application.gre_analytical,
                        'experience': application.experience,
                        'interest': application.interest,
                        'admission_term': application.admission_term,
                        'degree_sought': application.degree_sought,
                        'prior1_major': application.prior1_major,
                        'prior1_year': application.prior1_year,
                        'prior1_gpa': application.prior1_gpa,
                        'prior1_university': application.prior1_university,
                        'prior2_major': application.prior2_major,
                        'prior2_year': application.prior2_year,
                        'prior2_gpa': application.prior2_gpa,
                        'prior2_university': application.prior2_university,
                        'status': application.status,
                        'ranking': application.status,
                        'comments': application.status,
                        'description': application.description})

        connection.commit()
        application.id = cursor.lastrowid  # Add database ID to the object
        connection.close()

        print 'Application for user {} added!'.format(application.user_id)

    def get_application(self, user_id):

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM application WHERE user_id=:user_id",
                       {'user_id': user_id})

        application_tuple = cursor.fetchone()

        connection.close()

        if application_tuple:
            return self.convert_to_application([application_tuple])[0]

    def add_transcripts(self, user_id, transcripts):
        """
        GS enters transcripts
        """

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("UPDATE application SET "
                       "transcripts=:transcripts "

                       "WHERE user_id=:user_id",

                       {'user_id': user_id,
                        'transcripts': transcripts})

        connection.commit()
        connection.close()

    def add_recommendation(self, recommendation_tuple):
        """
        GS enters recommendation
        """

        recommendation = Recommendation(recommendation_tuple)

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("INSERT INTO recommendation VALUES ("
                       ":id,"
                       ":user_id,"
                       ":name,"
                       ":email,"
                       ":title,"
                       ":affiliation,"
                       ":score,"
                       ":description)",

                       {'id': cursor.lastrowid,
                        'user_id': recommendation.user_id,
                        'name': recommendation.name,
                        'email': recommendation.email,
                        'title': recommendation.title,
                        'affiliation': recommendation.affiliation,
                        'score': recommendation.score,
                        'description': recommendation.description})

        connection.commit()
        recommendation.id = cursor.lastrowid  # Add database ID to the object
        connection.close()

        return recommendation

    def get_recommendations(self, user_id):

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM recommendation WHERE user_id=:user_id",
                       {'user_id': user_id})

        recommendation_tuples = cursor.fetchall()

        connection.close()

        if recommendation_tuples:
            return self.convert_to_recommendation(recommendation_tuples)

    def update_status(self, user_id, status):
        """
        Set applicant status
        """

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("UPDATE application SET "
                       "status=:status "

                       "WHERE user_id=:user_id",

                       {'user_id': user_id,
                        'status': status
                        })

        connection.commit()
        connection.close()

        # Update pending applicant data
        self.update_pending_applications(user_id)

    def get_users_with_transcripts(self):
        """
        Get list of student ids for all students with transcripts submitted by GS
        """

        user_ids = []

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM application WHERE "
                       "transcripts IS 1 "
                       "AND status IS NULL")

        application_tuples = cursor.fetchall()
        connection.close()

        for application_tuple in application_tuples:
            user_ids.append(str(application_tuple[1]))

        return user_ids

    def add_student(self, student_tuple):

        student = Student(student_tuple)

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        # Add object to DB
        cursor.execute("INSERT INTO student VALUES ("
                       ":id,"
                       ":user_id,"
                       ":description)",

                       {'id': cursor.lastrowid,
                        'user_id': student.user_id,
                        'description': student.description})

        connection.commit()
        student.id = cursor.lastrowid  # Add database ID to the object
        connection.close()

        print 'Student {0} added!'.format(student.user_id)
        return student

    def update_comments(self, user_id, comments):

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("UPDATE application SET "
                       "comments=:comments "

                       "WHERE user_id=:user_id",

                       {'user_id': user_id,
                        'comments': comments})

        connection.commit()
        connection.close()

        # Update STARRS data
        self.update_pending_applications(user_id)

    def update_ranking(self, user_id, ranking):

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("UPDATE application SET "
                       "ranking=:ranking "

                       "WHERE user_id=:user_id",

                       {'user_id': user_id,
                        'ranking': ranking})

        connection.commit()
        connection.close()

        # Update STARRS data
        self.update_pending_applications(user_id)

    def update_pending_applications(self, user_id):
        for application in self.pending_applications:
            if application.user_id == user_id:
                index = self.pending_applications.index(application)
                self.pending_applications[index] = self.get_application(user_id)

    # Multi step actions
    def get_pending_applicants(self):
        """
        Get and return list of user IDs who applied to university, their data was entered, but decision was not made
        """

        # Get pending applicants isd
        pending_applicants_ids = []

        user_ids = self.get_users_with_transcripts()

        if not user_ids:
            del self.pending_users[:]
            del self.pending_applications[:]
            return

        for user_id in user_ids:
            if self.get_recommendations(user_id):
                pending_applicants_ids.append(user_id)

        # Get pending applicants object and update class variables
        del self.pending_users[:]
        del self.pending_applications[:]

        for user_id in pending_applicants_ids:
            self.pending_users.append(self.get_user(user_id))
            self.pending_applications.append(self.get_application(user_id))

        return pending_applicants_ids


# STARRS Application
class AlignDelegate(QtGui.QItemDelegate):
    def paint(self, painter, option, index):
        option.displayAlignment = QtCore.Qt.AlignCenter
        QtGui.QItemDelegate.paint(self, painter, option, index)


class DropdownDelegate(QtGui.QItemDelegate):
    def __init__(self, data, parent=None):
        QtGui.QItemDelegate.__init__(self, parent)
        self._data = data

    def createEditor(self, parent, option, index):
        model_value = index.model().data(index, QtCore.Qt.DisplayRole)

        editor = QtGui.QComboBox(parent)
        editor.addItems(self._data)

        return editor

    def setEditorData(self, editor, index):

        model_value = index.model().data(index, QtCore.Qt.EditRole)

        # editor.setEditText(model_value)
        current_index = editor.findText(model_value)
        if current_index > 0:
            editor.setCurrentIndex(current_index)

    def setModelData(self, editor, model, index):
        editor_value = editor.currentText()
        model.setData(index, editor_value, QtCore.Qt.EditRole)
        # ModelDataSet(editorValue)


class ApplicantModel(QtCore.QAbstractTableModel):
    def __init__(self, starrs_data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)

        self.starrs_data = starrs_data
        self.header = ['  Id  ', ' Email ', '  Verbal ', '      Ranking      ', '  Comments  ', '  Status  ']

    # Build-in functions
    def flags(self, index):

        column = index.column()
        if column in [3, 4, 5]:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable
        else:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def headerData(self, col, orientation, role):

        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[col]

    def rowCount(self, parent):

        return len(self.starrs_data.pending_users)

    def columnCount(self, parent):

        return len(self.header)

    def data(self, index, role):

        if not index.isValid():
            return

        row = index.row()
        column = index.column()

        if role == QtCore.Qt.DisplayRole:  # Fill table data to DISPLAY
            if column == 0:
                return self.starrs_data.pending_users[row].id

            if column == 1:
                return self.starrs_data.pending_users[row].email

            if column == 2:
                return self.starrs_data.pending_applications[row].gre_verbal

            if column == 3:
                return self.starrs_data.pending_applications[row].ranking

            if column == 4:
                return self.starrs_data.pending_applications[row].comments

            if column == 5:
                return self.starrs_data.pending_applications[row].status

    def setData(self, index, cell_data, role=QtCore.Qt.EditRole):
        """
        When table cell is edited
        """

        row = index.row()
        column = index.column()
        user_id = self.starrs_data.pending_users[row].id

        if role == QtCore.Qt.EditRole:

            if column == 3:
                self.starrs_data.update_ranking(user_id, cell_data)
                print '>> Ranking updated: {}'.format(cell_data)

            if column == 4:
                self.starrs_data.update_comments(user_id, cell_data)
                print '>> Comment updated: {}'.format(cell_data)

            if column == 5:
                self.starrs_data.update_status(user_id, cell_data)
                print '>> Status updated: {}'.format(cell_data)

            return True


class FoundApplicantModel(QtCore.QAbstractTableModel):
    def __init__(self, users, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)

        self.users = users
        self.header = ['  Id  ', ' Email ', '  First Name ', '  Last Name  ', '  Phone  ']

    def flags(self, index):

        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def headerData(self, col, orientation, role):

        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[col]

    def rowCount(self, parent):

        return len(self.users)

    def columnCount(self, parent):

        return len(self.header)

    def data(self, index, role):

        if not index.isValid():
            return

        row = index.row()
        column = index.column()

        if role == QtCore.Qt.DisplayRole:  # Fill table data to DISPLAY
            if column == 0:
                return self.users[row].id

            if column == 1:
                return self.users[row].email

            if column == 2:
                return self.users[row].first_name

            if column == 3:
                return self.users[row].last_name

            if column == 4:
                return self.users[row].phone


class STARRS(QtGui.QMainWindow, ui_main.Ui_STARRS):
    def __init__(self, parent=None):
        super(STARRS, self).__init__(parent=parent)

        # SETUP UI
        self.setupUi(self)

        # Constants
        self.rankings = ['Reject', 'Border Line', 'Admit', 'Admit With Aid']
        self.decisions = ['Admitted With Aid', 'Admitted', 'Rejected']
        self.terms = ['Summer 2022', 'Fall 2022', 'Winter 2023', 'Summer 2023', 'Fall 2023']
        self.degrees = ['MS', 'MSE']
        self.scores = ['95-100', '85-94', '70-84', '0-70']

        # Database
        self.sql_file_path = '{0}/data/database.db'.format(scripts_root)
        if not os.path.exists(self.sql_file_path):
            self.init_database()

        # Starrs data
        self.starrs_data = None
        self.applicant_model = None

        # Init UI data
        self.init_ui()
        self.init_data()

        # UI functionality
        self.actInitDatabase.triggered.connect(self.init_database)

        # 1)
        self.btnSubmitApplication.pressed.connect(self.submit_application)
        self.btnCheckApplicationStatus.pressed.connect(self.check_application_status)
        self.btnEnroll.pressed.connect(self.enroll)
        # 2)
        self.btnFindApplicant.pressed.connect(self.find_applicant)
        self.btnSetTranscripts.pressed.connect(self.add_transcripts)
        self.btnSetRecomendations.pressed.connect(self.add_recommendations)
        self.btnUpdatePendingApplicants.pressed.connect(self.update_applicants)

    # Data and UI setup
    def init_ui(self):

        # Temp fill forms
        # Application
        self.linStudentFirstName.setText('Kiryha')
        self.linStudentLastName.setText('Krysko')
        self.linGREVErbal.setText('170')
        self.linGREVQuant.setText('170')
        self.linGREVAnalitical.setText('6')
        self.linApplicantEmail.setText('coder@umich.edu')
        self.linApplicantPhone.setText('734-780-0123')
        self.linAddressZip.setText('48067')
        self.linAddressState.setText('MI')
        self.linAddressCity.setText('Royal Oak')
        self.linAddressStreet.setText('W 6th st')
        self.linWorkExpirience.setText('I was working as developer at Google. In my dreams.')
        self.linAreaOfInterest.setText('Computer Graphics')
        self.linPriorDegree1.setText('Bachelor')
        self.linPriorYear1.setText('1998')
        self.linPriorGPA1.setText('3.2')
        self.linPriorUniversity1.setText('KTILP')
        self.linPriorDegree2.setText('Master')
        self.linPriorYear2.setText('1999')
        self.linPriorGPA2.setText('3.6')
        self.linPriorUniversity2.setText('KTILP')
        self.linRecomendation1Name.setText('Richard Feynman')
        self.linRecomendation1Email.setText('rick@alamos.net')
        self.linRecomendation1Title.setText('physicist')
        self.linRecomendation1Affiliation.setText('what is it?')
        # Admission
        self.linRecomendationName_1.setText('Richard Feynman')
        self.linRecomendationEmail_1.setText('rick@alamos.net')
        self.linRecomendationTitle_1.setText('physicist')
        self.linRecomendationAffiliation_1.setText('The best!')
        self.linRecomendationName_2.setText('Hubert J Farnsworth')
        self.linRecomendationEmail_2.setText('express@futurama.com')
        self.linRecomendationTitle_2.setText('professor')
        self.linRecomendationAffiliation_2.setText('Cords')

        # UI controls
        self.comDegreeSought.addItems(self.degrees)
        self.comAdmissionTerm.addItems(self.terms)
        self.comRecomendationScore_1.addItems(self.scores)
        self.comRecomendationScore_2.addItems(self.scores)
        self.comRecomendationScore_3.addItems(self.scores)

        # Tables
        self.setup_table(self.tabApplicantData)
        self.setup_table(self.tabFoundApplicants)

    def init_data(self):

        self.starrs_data = StarrsData(self.sql_file_path)
        self.applicant_model = ApplicantModel(self.starrs_data)
        self.tabApplicantData.setModel(self.applicant_model)

        ranking = DropdownDelegate(self.rankings, self.tabApplicantData)
        decision = DropdownDelegate(self.decisions, self.tabApplicantData)
        self.tabApplicantData.setItemDelegateForColumn(3, ranking)
        self.tabApplicantData.setItemDelegateForColumn(5, decision)

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

        application_tuple = [
            None,  # id
            None,  # user_id
            date.today().strftime('%Y/%m/%d'),  # date received
            0,  # transcripts
            self.linGREVErbal.text(),
            self.linGREVQuant.text(),
            self.linGREVAnalitical.text(),
            self.linWorkExpirience.text(),
            self.linAreaOfInterest.text(),
            self.comAdmissionTerm.currentText(),
            self.comDegreeSought.currentText(),
            self.linPriorDegree1.text(),
            self.linPriorYear1.text(),
            self.linPriorGPA1.text(),
            self.linPriorUniversity1.text(),
            self.linPriorDegree2.text(),
            self.linPriorYear2.text(),
            self.linPriorGPA2.text(),
            self.linPriorUniversity2.text(),
            None,  # status
            '',  # reviewer ranking
            '',  # reviewer comments
            '']

        return user_tuple, application_tuple

    def init_database(self):
        """
        Create empty database tables
        """

        init_database(self.sql_file_path)

    def setup_table(self, table):

        table.verticalHeader().hide()
        table.verticalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        table.horizontalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        table.horizontalHeader().setStretchLastSection(True)
        table.setItemDelegate(AlignDelegate())

    def init_applicants(self):

        ranking = DropdownDelegate(self.rankings, self.tabApplicantData)
        decision = DropdownDelegate(self.decisions, self.tabApplicantData)
        self.tabApplicantData.setItemDelegateForColumn(3, ranking)
        self.tabApplicantData.setItemDelegateForColumn(5, decision)

    def update_applicants(self):

        self.applicant_model.layoutAboutToBeChanged.emit()
        self.starrs_data.get_pending_applicants()
        self.applicant_model.layoutChanged.emit()

    # Common
    def send_email(self, email, user_name, user_id):

        # Authenticate
        login = "random.t4@outlook.com"
        password = 'starrs1234'
        session = smtplib.SMTP('smtp-mail.outlook.com', 587)
        session.starttls()
        session.login(login, password)

        # Compose email
        subject = 'Welcome to STARRS!'
        text = 'Hello {0}, \nYour id/password is {1}.'.format(user_name, user_id)
        message = 'Subject: {0}\n\n{1}'.format(subject, text)

        # Send email
        session.sendmail(login, email, message)
        session.quit()

    # 1) Online Application
    def submit_application(self):

        # Add user
        user_tuple, application_tuple = self.get_ui_apply()
        user = self.starrs_data.add_user(user_tuple)

        # Sent password
        self.statusBar().showMessage('>> Password is: >{0}<'.format(user.id))

        # Add application
        application_tuple[1] = user.id
        self.starrs_data.add_application(application_tuple)

    def check_application_status(self):
        """
        The status is:
            Application Materials Missing
            Application Received and Decision Pending
            Admission Decision: Accepted
            Admission Decision: Rejected
        """

        # Get user application
        user_id = self.linStudentID.text()
        application = self.starrs_data.get_application(user_id)

        if not application:
            self.linApplicationStatus.setText('Application Was Not Submitted!')
            return

        if application.status:
            self.linApplicationStatus.setText('Admission Decision: {}'.format(application.status))

        else:
            # Get recommendations
            recommendations = self.starrs_data.get_recommendations(user_id)

            if application.transcripts and recommendations:
                self.linApplicationStatus.setText('Application Received and Decision Pending')
            else:
                missing = ''
                if not application.transcripts:
                    missing = 'transcripts'
                if not recommendations:
                    if not application.transcripts:
                        missing += ' and recommendations'
                    else:
                        missing = ' recommendations'
                        
                self.linApplicationStatus.setText('Application Materials Missing: {}'.format(missing))

    def enroll(self):
        """
        Enroll admitted student to Database University
        """

        user_id = self.linStudentID.text()

        if user_id == '':
            self.statusBar().showMessage('>> Please, enter the user id!')
            return

        # Check if user was admitted
        application = self.starrs_data.get_application(user_id)

        if not application:
            return

        if application.status in ['Admitted With Aid', 'Admitted'] :

            student_tuple = [None, user_id, 'I accept']
            self.starrs_data.add_student(student_tuple)

    def find_applicant(self):

        user_id = self.linSearchApplicantID.text()
        last_name = self.linSearchApplicantLastname.text()

        users = None

        if user_id != '':
            users = [self.starrs_data.get_user(user_id)]
        elif last_name != '':
            users = self.starrs_data.get_user_by_name(last_name)
        else:
            self.tabFoundApplicants.setModel(FoundApplicantModel([]))
            self.statusBar().showMessage('>> Enter applicant ID or Last Name!')

        if users:
            self.tabFoundApplicants.setModel(FoundApplicantModel(users))

    # 2) Admission process
    def add_transcripts(self):
        """
        Add transcripts by GS
        """

        user_id = self.linStudentIDAdmission.text()
        if user_id == '':
            self.statusBar().showMessage('>> Please, enter the user id!')
            return

        if self.chbTranscripts.isChecked():
            transcripts = 1
        else:
            transcripts = 0

        self.starrs_data.add_transcripts(user_id, transcripts)
        self.statusBar().showMessage('>> Applicant {0} transcripts submitted!'.format(user_id))

    def add_recommendations(self):
        """
        Add recommendations by GS
        """

        # TODO: check existing recommendations, should not be more than 3 in total

        user_id = self.linStudentIDAdmission.text()
        if user_id == '':
            self.statusBar().showMessage('>> Please, enter the user id!')
            return

        if self.chbDoRecommendation_1.isChecked():

            recommendation_tuple = [
                None,
                user_id,
                self.linRecomendationName_1.text(),
                self.linRecomendationEmail_1.text(),
                self.linRecomendationTitle_1.text(),
                self.linRecomendationAffiliation_1.text(),
                self.comRecomendationScore_1.currentText(),
                'For Student {}'.format(user_id)]
            self.starrs_data.add_recommendation(recommendation_tuple)

        if self.chbDoRecommendation_2.isChecked():

            recommendation_tuple = [
                None,
                user_id,
                self.linRecomendationName_2.text(),
                self.linRecomendationEmail_2.text(),
                self.linRecomendationTitle_2.text(),
                self.linRecomendationAffiliation_2.text(),
                self.comRecomendationScore_2.currentText(),
                'For Student {}'.format(user_id)]

            self.starrs_data.add_recommendation(recommendation_tuple)

        if self.chbDoRecommendation_3.isChecked():

            recommendation_tuple = [
                None,
                user_id,
                self.linRecomendationName_3.text(),
                self.linRecomendationEmail_3.text(),
                self.linRecomendationTitle_3.text(),
                self.linRecomendationAffiliation_3.text(),
                self.comRecomendationScore_3.currentText(),
                'For Student {}'.format(user_id)]

            self.starrs_data.add_recommendation(recommendation_tuple)

        self.statusBar().showMessage('>> Applicant {0} recommendations submitted!'.format(user_id))


if __name__ == "__main__":
    app = QtGui.QApplication([])
    starrs = STARRS()
    starrs.show()
    app.exec_()
