import os
import sqlite3
from datetime import date
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

    # User
    cursor.execute('''CREATE TABLE user (
                    id integer primary key autoincrement,
                    first_name text,
                    middle_name text,
                    last_name text,
                    email text,
                    address text,
                    home_phone text,
                    work_phone text,
                    mobile_phone text,
                    description text
                    )''')

    # Student application
    cursor.execute('''CREATE TABLE application (
                    id integer primary key autoincrement,
                    user_id integer,
                    date_received text,
                    status text,
                    transcripts text,
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
                    description text,
                    FOREIGN KEY(user_id) REFERENCES user(id) 
                    ON DELETE CASCADE
                    ON UPDATE NO ACTION
                    )''')

    # Recommendation letters
    cursor.execute('''CREATE TABLE recommendationletter (
                    recommendation_no integer,
                    application_id integer,
                    user_id integer
                    name text,
                    affiliation text,
                    email text,
                    title text,
                    score text,                   
                    FOREIGN KEY(application_id, user_id) REFERENCES application(application_id, user_id) 
                    ON DELETE CASCADE
                    ON UPDATE NO ACTION
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
        self.home_phone = ''
        self.work_phone = ''
        self.mobile_phone = ''
        self.description = ''

        self.init(user_tuple)

    def init(self, user_tuple):

        self.id = user_tuple[0]
        self.first_name = user_tuple[1]
        self.middle_name = user_tuple[2]
        self.last_name = user_tuple[3]
        self.email = user_tuple[4]
        self.address = user_tuple[5]
        self.home_phone = user_tuple[6]
        self.work_phone = user_tuple[7]
        self.mobile_phone = user_tuple[8]
        self.description = user_tuple[9]


class Application:
    def __init__(self, application_tuple):
        self.id = None
        self.user_id = None
        self.date_received = ''
        self.status = ''
        self.transcripts = ''
        self.recommendations = ''
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
        self.description = ''
        self.init(application_tuple)

    def init(self, application_tuple):

        self.id = application_tuple[0]
        self.user_id = application_tuple[1]
        self.date_received = application_tuple[2]
        self.status = application_tuple[3]
        self.transcripts = application_tuple[4]
        self.gre_verbal = application_tuple[5]
        self.gre_quantitative = application_tuple[6]
        self.gre_analytical = application_tuple[7]
        self.experience = application_tuple[8]
        self.interest = application_tuple[9]
        self.admission_term = application_tuple[10]
        self.degree_sought = application_tuple[11]
        self.prior1_major = application_tuple[12]
        self.prior1_year = application_tuple[13]
        self.prior1_gpa = application_tuple[14]
        self.prior1_university = application_tuple[15]
        self.prior2_major = application_tuple[16]
        self.prior2_year = application_tuple[17]
        self.prior2_gpa = application_tuple[18]
        self.prior2_university = application_tuple[19]
        self.description = application_tuple[20]

class Recommendation:
    def __init__(self, recommendation_tuple):
        self.title = ''
        self.name = ''
        self.email = ''
        self.affiliation = ''
        self.init(recommendation_tuple)

    def init(self, recommendation_tuple):

        self.title = recommendation_tuple[0]
        self.name = recommendation_tuple[1]
        self.email = recommendation_tuple[2]
        self.affiliation = recommendation_tuple[3]      

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
                       ":home_phone,"
                       ":work_phone,"
                       ":mobile_phone,"
                       ":description)",

                       {'id': cursor.lastrowid,
                        'first_name': user.first_name,
                        'middle_name': user.middle_name,
                        'last_name': user.last_name,
                        'email': user.email,
                        'address': user.address,
                        'home_phone': user.home_phone,
                        'work_phone': user.work_phone,
                        'mobile_phone': user.mobile_phone,
                        'description': user.description})

        connection.commit()
        user.id = cursor.lastrowid  # Add database ID to the object
        connection.close()

        print 'User {0} {1} added!'.format(user.first_name, user.last_name)
        return user

    def add_application(self, application_tuple, recommendations_tuple):

        application = Application(application_tuple)

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        # Add object to DB
        cursor.execute("INSERT INTO application VALUES ("
                       ":id,"
                       ":user_id,"
                       ":date_received,"
                       ":status,"
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
                       ":description)",

                       {'id': cursor.lastrowid,
                        'user_id': application.user_id,
                        'date_received': application.date_received,
                        'status': application.status,
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
                        'description': application.description})

        connection.commit()
        application.id = cursor.lastrowid  # Add database ID to the object

        recommendation_no=0;

        for recommendation_tuple in recommendations_tuple:
                recommendation_no+=1
                # Add object to DB
                cursor.execute("INSERT INTO recommendationletter VALUES ("
                       ":recommendation_no,"
                       ":application_id,"
                       ":user_id,"
                       ":affiliation,"
                       ":email,"
                       ":title,"
                       ":score)",

                       {'recommendation_no': recommendation_no,
                        'application_id': application.id,
                        'user_id': application.user_id,
                        'title': str(recommendation_tuple[0]),
                        'email': str(recommendation_tuple[1]),
                        'affiliation': str(recommendation_tuple[2]),
                        'score': None})

                connection.commit()
        
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

    def add_student_data(self, user_id, transcripts, scores):
        """
        GS enters transcripts and recommendations
        """

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("UPDATE application SET "
                       "transcripts=:transcripts "
                       "WHERE user_id=:user_id",

                       {'user_id': user_id,
                        'transcripts': transcripts
                        })

        connection.commit()

        recommendation_no=0;

        for score in scores:
            recommendation_no+=1
            cursor.execute("UPDATE recommendationletter SET "
                       "score=:score "
                       "WHERE user_id=:user_id AND recommendation_no = :recommendation_no",

                       {'user_id': user_id,
                        'score': score,
                        'recommendation_no': recommendation_no
                        })
            connection.commit()

        connection.close()



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

    def get_pending_applicants(self):
        """
        Get and return list of user IDs who applied to university, their data was entered, but decision was not made
        """

        pending_applicants = []

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()
        
        cursor.execute("SELECT application.* FROM application INNER JOIN recommendationLetter ON application.id = recommendationLetter.application_id WHERE application.transcripts != 0 AND application.transcripts IS NOT NULL GROUP BY application.user_id")

        application_tuples = cursor.fetchall()

        connection.close()

        for application_tuple in application_tuples:
            pending_applicants.append(str(application_tuple[0]))

        return pending_applicants


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
        # 2)
        self.btnSearchApplicant.pressed.connect(self.search_applicant)
        self.btnAddStudentData.pressed.connect(self.add_student_data)
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
        self.linApplicantHomePhone.setText('734-780-0122')
        self.linApplicantWorkPhone.setText('734-780-0123')
        self.linApplicantMobilePhone.setText('734-780-0124')
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
        # Admission
        # self.linTranscript.setText('Transcripts')
        # self.linRecommendation.setText('Recommendations')
        self.comRecommScore1.addItems(['','top 5%', '85-94%', '70-84%', 'below 70%'])
        self.comRecommScore2.addItems(['','top 5%', '85-94%', '70-84%', 'below 70%'])
        self.comRecommScore3.addItems(['','top 5%', '85-94%', '70-84%', 'below 70%'])

        self.comDegreeSought.addItems(['MS', 'MSE'])
        self.comAdmissionTerm.addItems(['Summer 2022', 'Fall 2022', 'Winter 2023', 'Summer 2023', 'Fall 2023'])
        self.comDescision.addItems(['Admitted With Aid', 'Admitted', 'Rejected'])

        self.comTitle1.addItems(['','Mr', 'Ms', 'Dr'])
        self.comTitle2.addItems(['','Mr', 'Ms', 'Dr'])
        self.comTitle3.addItems(['','Mr', 'Ms', 'Dr'])

        self.comRecommRelation1.addItems(['','Professor', 'Coworker', 'Friend'])
        self.comRecommRelation2.addItems(['','Professor', 'Coworker', 'Friend'])
        self.comRecommRelation3.addItems(['','Professor', 'Coworker', 'Friend'])

        self.comTitle1.setCurrentIndex(3)
        self.linRecommName1.setText('Thomas Steiner')
        self.linRecommEmail1.setText('Thomas.Steiner@umich.edu')
        self.comRecommRelation1.setCurrentIndex(1)

        self.comTitle2.setCurrentIndex(2)
        self.linRecommName2.setText('Gerardo Mitsuy')
        self.linRecommEmail2.setText('mitsuy@gmail.com')
        self.comRecommRelation2.setCurrentIndex(3)
        

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
            self.linApplicantHomePhone.text(),
            self.linApplicantWorkPhone.text(),
            self.linApplicantMobilePhone.text(),
            '']

        application_tuple = [
            None,  # id
            None,  # user_id
            date.today().strftime('%d/%m/%Y'),  # date received
            None,  # status
            None,  # transcripts
            None,  # recommendations
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
            'description']

        recommendation_tuple1 = [
            self.comTitle1.currentText(),
            self.linRecommName1.text(),
            self.linRecommEmail1.text(),
            self.comRecommRelation1.currentText()
         ]

        recommendation_tuple2 = [
            self.comTitle2.currentText(),
            self.linRecommName2.text(),
            self.linRecommEmail2.text(),
            self.comRecommRelation2.currentText()
         ]

        recommendation_tuple3 = [
            self.comTitle3.currentText(),
            self.linRecommName3.text(),
            self.linRecommEmail3.text(),
            self.comRecommRelation3.currentText()
         ]


        recommendations_tuple = []

        if recommendation_tuple1[1]:
            recommendations_tuple.append(recommendation_tuple1)

        if recommendation_tuple2[1]:
            recommendations_tuple.append(recommendation_tuple2)

        if recommendation_tuple3[1]:
            recommendations_tuple.append(recommendation_tuple2)

        return user_tuple, application_tuple, recommendations_tuple

    def init_database(self):
        """
        Create empty database tables
        """

        init_database(self.sql_file_path)

    # 1) Online Application
    def submit_application(self):

        # Add user
        user_tuple, application_tuple, recommendations_tuple = self.get_ui_apply()

        user = self.starrs_data.add_user(user_tuple)

        # Sent password
        self.statusBar().showMessage('>> Password is: >{0}<'.format(user.id))

        # Add application
        application_tuple[1] = user.id
        self.starrs_data.add_application(application_tuple, recommendations_tuple)

    def check_application_status(self):
        """
        The status is:
            Application Materials Missing
            Application Received and Decision Pending
            Admission Decision: Accepted
            Admission Decision: Rejected
        """

        # Get user application
        user_id = self.lineStudentID.text()

        application = self.starrs_data.get_application(user_id)

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM recommendationletter WHERE user_id=:user_id",
                       {'user_id': user_id})

        recommendationCount = cursor.fetchall()[0][0]

        connection.close()

        if not application:
            self.linApplicationStatus.setText('Application Was Not Submitted!')
            return

        if application.status:
            self.linApplicationStatus.setText('Admission Decision: {}'.format(application.status))

        else:
            if application.transcripts and recommendationCount > 0:
                self.linApplicationStatus.setText('Application Received and Decision Pending')
            else:
                missing = ''
                if not application.transcripts:
                    missing += ' | transcripts |'
                if recommendationCount == 0:
                    missing += ' | recommendations |'

                self.linApplicationStatus.setText('Application Materials Missing: {}'.format(missing))

    def convert_score_to_index(self, score):
        if (score == 'top 5%'):
            return 1
        elif (score == 'top 5%'):
                return 2;
        elif (score == '85-94%'):
                return 2;
        elif (score == '70-84%'):
                return 3;
        elif (score == 'below 70%'):
                return 4;
        else:
            return 0


    # 2) Admission process
    def search_applicant(self):
        """
        Applicant could have up to 3 recommendation letters.
        Button is to show if there is transcript received and enable how many recommendation scores textboxes
        """

        user_id = self.linStudentIDAdmission.text()

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM recommendationletter WHERE user_id=:user_id",
                       {'user_id': user_id})

        recommendationCount = cursor.fetchall()[0][0]

        cursor.execute("SELECT transcripts FROM application WHERE user_id=:user_id",
                       {'user_id': user_id})

        transcript = cursor.fetchall()[0][0]


        
        cursor.execute("SELECT score FROM recommendationletter WHERE user_id=:user_id",
                       {'user_id': user_id})

        scores = cursor.fetchall()

        if scores:
            if len(scores)>0 :
                self.comRecommScore1.setCurrentIndex(self.convert_score_to_index(scores[0][0]))
            else:
                self.comRecommScore1.setCurrentIndex(0)
            if len(scores)>1 :
                self.comRecommScore2.setCurrentIndex(self.convert_score_to_index(scores[1][0]))
            else:
                self.comRecommScore2.setCurrentIndex(0)                
            if len(scores)>2 :
                self.comRecommScore3.setCurrentIndex(self.convert_score_to_index(scores[2][0]))
            else:
                self.comRecommScore3.setCurrentIndex(0)   

        if (transcript == '1') :
            self.checkTranscriptReceived.setChecked(True)
            self.checkTranscriptReceived.show();
            
        else:
            self.checkTranscriptReceived.setChecked(False)
        
        
        if (recommendationCount == 0) :
            self.labelRL1.setDisabled(True)
            self.comRecommScore1.setDisabled(True)

            self.labelRL2.setDisabled(True)
            self.comRecommScore2.setDisabled(True)

            self.labelRL3.setDisabled(True)
            self.comRecommScore3.setDisabled(True)

        if (recommendationCount == 1) :
            self.labelRL1.setDisabled(False)
            self.comRecommScore1.setDisabled(False)

            self.labelRL2.setDisabled(True)
            self.comRecommScore2.setDisabled(True)

            self.labelRL3.setDisabled(True)
            self.comRecommScore3.setDisabled(True)    

        if (recommendationCount == 2) :
            self.labelRL1.setDisabled(False)
            self.comRecommScore1.setDisabled(False)

            self.labelRL2.setDisabled(False)
            self.comRecommScore2.setDisabled(False)

            self.labelRL3.setDisabled(True)
            self.comRecommScore3.setDisabled(True)  

        if (recommendationCount == 3) :
            self.labelRL1.setDisabled(False)
            self.comRecommScore1.setDisabled(False)

            self.labelRL2.setDisabled(False)
            self.comRecommScore2.setDisabled(False)

            self.labelRL3.setDisabled(False)
            self.comRecommScore3.setDisabled(False)             


    def add_student_data(self):
        """
        Add transcripts and recommendations by GS
        """

        user_id = self.linStudentIDAdmission.text()
        transcripts = self.checkTranscriptReceived.isChecked()

        score1 = self.comRecommScore1.currentText()
        score2 = self.comRecommScore2.currentText()
        score3 = self.comRecommScore3.currentText()

        scores = []

        if score1:
            scores.append(score1)

        if score2:
            scores.append(score2)

        if score3:
            scores.append(score3)

        self.starrs_data.add_student_data(user_id, transcripts, scores)
        self.statusBar().showMessage('>> Applicant {0} data submitted!'.format(user_id))

    def get_pending_applicants(self):

        pending_applicants = self.starrs_data.get_pending_applicants()

        self.comPendingApplicants.clear()
        self.comPendingApplicants.addItems(pending_applicants)

    def set_status(self):
        """
        Admit/reject applicant by GS
        """

        user_id = self.comPendingApplicants.currentText()
        status = self.comDescision.currentText()

        self.starrs_data.set_status(user_id, status)


if __name__ == "__main__":
    app = QtGui.QApplication([])
    starrs = STARRS()
    starrs.show()
    app.exec_()
