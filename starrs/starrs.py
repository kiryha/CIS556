import os
import sqlite3
import smtplib
from datetime import date
from PySide import QtGui
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
        self.description = application_tuple[20]


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

    # Tuple to object conversion
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

    # CURDs
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

    def add_application(self, application_tuple):

        application = Application(application_tuple)
        print application_tuple
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

    def set_status(self, user_id, status):
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

    def get_pending_applicants(self):
        """
        Get and return list of user IDs who applied to university, their data was entered, but decision was not made
        """

        pending_applicants = []

        user_ids = self.get_users_with_transcripts()

        if not user_ids:
            return

        for user_id in user_ids:
            if self.get_recommendations(user_id):
                pending_applicants.append(user_id)

        return pending_applicants

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


# STARRS Application
class STARRS(QtGui.QMainWindow, ui_main.Ui_STARRS):
    def __init__(self, parent=None):
        super(STARRS, self).__init__(parent=parent)

        # SETUP UI
        self.setupUi(self)

        # Database
        self.sql_file_path = '{0}/data/database.db'.format(scripts_root)
        if not os.path.exists(self.sql_file_path):
            self.init_database()

        # Starrs data
        self.starrs_data = None

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
        self.btnSetTranscripts.pressed.connect(self.add_transcripts)
        self.btnSetRecomendations.pressed.connect(self.add_recommendations)
        self.btnGetPendingApplicants.pressed.connect(self.get_pending_applicants)
        self.btnMadeDecision.pressed.connect(self.set_status)

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

        self.comDegreeSought.addItems(['MS', 'MSE'])
        self.comAdmissionTerm.addItems(['Summer 2022', 'Fall 2022', 'Winter 2023', 'Summer 2023', 'Fall 2023'])
        self.comDescision.addItems(['Admitted With Aid', 'Admitted', 'Rejected'])
        scores = ['95-100', '85-94', '70-84', '0-70']
        self.comRecomendationScore_1.addItems(scores)
        self.comRecomendationScore_2.addItems(scores)
        self.comRecomendationScore_3.addItems(scores)

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
            '']

        return user_tuple, application_tuple

    def init_database(self):
        """
        Create empty database tables
        """

        init_database(self.sql_file_path)

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

        self.statusBar().showMessage('>> Applicant {0} recommendations submitted!'.format(user_id))

    def get_pending_applicants(self):

        pending_applicants = self.starrs_data.get_pending_applicants()

        if not pending_applicants:
            return

        self.comPendingApplicants.clear()
        self.comPendingApplicants.addItems(pending_applicants)

    def set_status(self):
        """
        Admit/reject applicant by GS
        """

        user_id = self.comPendingApplicants.currentText()
        status = self.comDescision.currentText()

        self.starrs_data.set_status(user_id, status)
        self.statusBar().showMessage('>> Applicant {0} decision submitted!'.format(user_id))


if __name__ == "__main__":
    app = QtGui.QApplication([])
    starrs = STARRS()
    starrs.show()
    app.exec_()
