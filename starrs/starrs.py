import os
import sqlite3
import smtplib
from datetime import date
from PySide import QtGui, QtCore
from ui import ui_main

scripts_root = os.path.dirname(__file__).replace('\\', '/')


# Database
init_data = {
    'users': [
        {'id': 1,
         'first_name': 'Alexander',
         'middle_name': 'S',
         'last_name': 'Copper',
         'email': 'acopper@umich.edu',
         'address': '48067, MI, Royal Oak, W 6th st, 310',
         'phone': '734-780-0001',
         'role': 'GS'},

        {'id': 2,
         'first_name': 'Sumanth',
         'middle_name': 'Shiva',
         'last_name': 'Pracah',
         'email': 'sshiva@umich.edu',
         'address': '48226, MI, Detroit, Woodward ave, 1435',
         'phone': '734-780-0002',
         'role': 'Reviewer'},

        {'id': 3,
         'first_name': 'Kimberly',
         'middle_name': 'La',
         'last_name': 'Praire',
         'email': 'kim@umich.edu',
         'address': '48226, MI, Detroit, 555 Brush St, 2530',
         'phone': '734-780-0003',
         'role': 'Adviser'},

        {'id': 4,
         'first_name': 'Thomas',
         'middle_name': '',
         'last_name': 'Steiner',
         'email': 'tstain@umich.edu',
         'address': '48120, MI, Dearborn, W Warren Ave, 1440',
         'phone': '734-780-0004',
         'role': 'Instructor'}
    ],

    'departments': [{'id': 1, 'name': 'CIS'}, {'id': 2, 'name': 'ECE'}],

    'courses': [
        {'id': 1,
         'name': 'Database Systems',
         'number': '556',
         'department_id': 1,
         'credit_hours': 3,
         'instructor_id': 4},

        {'id': 2,
         'name': 'Software Engineering',
         'number': '553',
         'department_id': 1,
         'credit_hours': 3,
         'instructor_id': 4},

        {'id': 3,
         'name': 'Embedded Systems',
         'number': '554',
         'department_id': 2,
         'credit_hours': 3,
         'instructor_id': 4}],

    'sections': [
        {'id': 1,
         'course_id': 1,
         'number': '001',
         'admission_term': 'Summer 2022',
         'instructor_id': 4}
    ]
}


def init_database(sql_file_path):
    """
    Create database tables
    """

    connection = sqlite3.connect(sql_file_path)
    cursor = connection.cursor()

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

    cursor.execute('''CREATE TABLE role (
                    id integer primary key autoincrement,
                    user_id integer,
                    name text,
                    description text,
                    FOREIGN KEY(user_id) REFERENCES user(id)
                    )''')

    cursor.execute('''CREATE TABLE application (
                    id integer primary key autoincrement,
                    user_id integer,
                    date_received text,
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
                    rec1_name text,
                    rec1_email text,
                    rec1_title text,
                    rec1_affiliation text,
                    rec1_score text,
                    rec2_name text,
                    rec2_email text,
                    rec2_title text,
                    rec2_affiliation text,
                    rec2_score text,
                    rec3_name text,
                    rec3_email text,
                    rec3_title text,
                    rec3_affiliation text,
                    rec3_score text,
                    transcripts integer,
                    status text,
                    ranking text,
                    comments text,
                    description text,
                    FOREIGN KEY(user_id) REFERENCES user(id)
                    )''')

    cursor.execute('''CREATE TABLE academic (
                    id integer primary key autoincrement,
                    user_id integer,
                    course_id integer,
                    section_id integer, 
                    grade text,
                    description text,
                    FOREIGN KEY(user_id) REFERENCES user(id)
                    FOREIGN KEY(course_id) REFERENCES course(id)
                    FOREIGN KEY(section_id) REFERENCES section(id)
                    )''')

    cursor.execute('''CREATE TABLE course (
                    id integer primary key autoincrement,
                    name text,
                    number integer,
                    department_id integer,
                    credit_hours integer,
                    description text, 
                    FOREIGN KEY(department_id) REFERENCES department(id)
                    )''')

    cursor.execute('''CREATE TABLE department (
                    id integer primary key autoincrement,
                    name text,
                    description text
                    )''')

    cursor.execute('''CREATE TABLE section (
                    id integer primary key autoincrement,
                    course_id integer,
                    number text,
                    admission_term text,
                    instructor_id integer,
                    description text,
                    FOREIGN KEY(course_id) REFERENCES course(id)
                    FOREIGN KEY(instructor_id) REFERENCES user(id)
                    )''')

    connection.commit()
    connection.close()


def populate_database(sql_file_path):
    """
    Add data to the database: users
    """

    for user_data in init_data['users']:

        connection = sqlite3.connect(sql_file_path)
        cursor = connection.cursor()

        cursor.execute("INSERT INTO user VALUES ("
                       ":id,"
                       ":first_name,"
                       ":middle_name,"
                       ":last_name,"
                       ":email,"
                       ":address,"
                       ":phone,"
                       ":description)",

                       {'id': user_data['id'],
                        'first_name': user_data['first_name'],
                        'middle_name': user_data['middle_name'],
                        'last_name': user_data['last_name'],
                        'email': user_data['email'],
                        'address': user_data['address'],
                        'phone': user_data['phone'],
                        'description': ''})

        connection.commit()

        cursor.execute("INSERT INTO role VALUES ("
                       ":id,"
                       ":user_id,"
                       ":name,"
                       ":description)",

                       {'id': cursor.lastrowid,
                        'user_id': user_data['id'],
                        'name': user_data['role'],
                        'description': ''})

        connection.commit()
        connection.close()

    for department_data in init_data['departments']:

        connection = sqlite3.connect(sql_file_path)
        cursor = connection.cursor()

        cursor.execute("INSERT INTO department VALUES ("
                       ":id,"
                       ":name,"
                       ":description)",

                       {'id': department_data['id'],
                        'name': department_data['name'],
                        'description': ''})

        connection.commit()
        connection.close()

    for course_data in init_data['courses']:

        connection = sqlite3.connect(sql_file_path)
        cursor = connection.cursor()

        cursor.execute("INSERT INTO course VALUES ("
                       ":id,"
                       ":name,"
                       ":number,"
                       ":department_id,"
                       ":credit_hours,"
                       ":description)",

                       {'id': course_data['id'],
                        'name': course_data['name'],
                        'number': course_data['number'],
                        'department_id': course_data['department_id'],
                        'credit_hours': course_data['credit_hours'],
                        'description': ''})

        connection.commit()
        connection.close()

    for section_data in init_data['sections']:

        connection = sqlite3.connect(sql_file_path)
        cursor = connection.cursor()

        cursor.execute("INSERT INTO section VALUES ("
                       ":id,"
                       ":course_id,"
                       ":number,"
                       ":admission_term,"
                       ":instructor_id,"
                       ":description)",

                       {'id': section_data['id'],
                        'course_id': section_data['course_id'],
                        'number': section_data['number'],
                        'admission_term': section_data['admission_term'],
                        'instructor_id': section_data['instructor_id'],
                        'description': ''})

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


class Role:
    def __init__(self, role_tuple):
        self.id = None
        self.user_id = None
        self.name = ''
        self.description = ''

        self.init(role_tuple)

    def init(self, role_tuple):

        self.id = role_tuple[0]
        self.user_id = role_tuple[1]
        self.name = role_tuple[2]
        self.description = role_tuple[3]


class Application:
    def __init__(self, application_tuple):
        self.id = None
        self.user_id = None
        self.date_received = ''
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
        self.rec1_name = ''
        self.rec1_email = ''
        self.rec1_title = ''
        self.rec1_affiliation = ''
        self.rec1_score = ''
        self.rec2_name = ''
        self.rec2_email = ''
        self.rec2_title = ''
        self.rec2_affiliation = ''
        self.rec2_score = ''
        self.rec3_name = ''
        self.rec3_email = ''
        self.rec3_title = ''
        self.rec3_affiliation = ''
        self.rec3_score = ''
        self.transcripts = None
        self.status = ''
        self.ranking = ''
        self.comments = ''
        self.description = ''

        self.init(application_tuple)

    def init(self, application_tuple):

        self.id = application_tuple[0]
        self.user_id = application_tuple[1]
        self.date_received = application_tuple[2]
        self.gre_verbal = application_tuple[3]
        self.gre_quantitative = application_tuple[4]
        self.gre_analytical = application_tuple[5]
        self.experience = application_tuple[6]
        self.interest = application_tuple[7]
        self.admission_term = application_tuple[8]
        self.degree_sought = application_tuple[9]
        self.prior1_major = application_tuple[10]
        self.prior1_year = application_tuple[11]
        self.prior1_gpa = application_tuple[12]
        self.prior1_university = application_tuple[13]
        self.prior2_major = application_tuple[14]
        self.prior2_year = application_tuple[15]
        self.prior2_gpa = application_tuple[16]
        self.prior2_university = application_tuple[17]
        self.rec1_name = application_tuple[18]
        self.rec1_email = application_tuple[19]
        self.rec1_title = application_tuple[20]
        self.rec1_affiliation = application_tuple[21]
        self.rec1_score = application_tuple[22]
        self.rec2_name = application_tuple[23]
        self.rec2_email = application_tuple[24]
        self.rec2_title = application_tuple[24]
        self.rec2_affiliation = application_tuple[26]
        self.rec2_score = application_tuple[27]
        self.rec3_name = application_tuple[28]
        self.rec3_email = application_tuple[29]
        self.rec3_title = application_tuple[30]
        self.rec3_affiliation = application_tuple[31]
        self.rec3_score = application_tuple[32]
        self.transcripts = application_tuple[33]
        self.status = application_tuple[34]
        self.ranking = application_tuple[35]
        self.comments = application_tuple[36]
        self.description = application_tuple[37]


# Database manipulations
class StarrsData:
    def __init__(self, sql_file_path):
        self.sql_file_path = sql_file_path

        # Processed data
        self.pending_users = []
        self.pending_applications = []
        self.edit_user = None
        self.edit_application = None
        self.display_users = []
        self.display_applications = []

    # Init data
    def clear_data(self):

        del self.pending_users[:]
        del self.pending_applications[:]
        self.edit_user = None
        self.edit_application = None
        del self.display_users[:]
        del self.display_applications[:]

    # Tuple to object conversion
    def convert_to_user(self, user_tuples):

        users = []

        for user_tuple in user_tuples:
            user = User(user_tuple)
            users.append(user)

        return users

    def convert_to_role(self, role_tuples):

        roles = []

        for role_tuple in role_tuples:
            role = Role(role_tuple)
            roles.append(role)

        return roles

    def convert_to_application(self, application_tuples):

        applications = []

        for application_tuple in application_tuples:
            application = Application(application_tuple)
            applications.append(application)

        return applications

    # Basic CURDs
    # User
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

    def get_users_by_name(self, last_name):

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM user WHERE last_name=:last_name",
                       {'last_name': last_name})

        user_tuples = cursor.fetchall()
        connection.close()

        if user_tuples:
            return self.convert_to_user(user_tuples)

    def update_user_attribute(self, attribute_name, user_id, attribute_value):

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("UPDATE user SET {0}=:{0} WHERE id=:id".format(attribute_name),

                       {'id': user_id,
                        '{0}'.format(attribute_name): attribute_value})

        connection.commit()
        connection.close()

        # Update root data
        self.edit_user = self.get_user(user_id)

    # Role
    def add_role(self, role_tuple):

        role = Role(role_tuple)

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        # Add object to DB
        cursor.execute("INSERT INTO role VALUES ("
                       ":id,"
                       ":user_id,"
                       ":name,"
                       ":description)",

                       {'id': cursor.lastrowid,
                        'user_id': role.user_id,
                        'name': role.name,
                        'description': role.description})

        connection.commit()
        role.id = cursor.lastrowid  # Add database ID to the object
        connection.close()

    def get_user_roles(self, user_id):

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM role WHERE user_id=:user_id",
                       {'user_id': user_id})

        role_tuples = cursor.fetchall()

        connection.close()

        if role_tuples:
            return self.convert_to_role(role_tuples)

    # Application
    def add_application(self, application_tuple):

        application = Application(application_tuple)

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        # Add object to DB
        cursor.execute("INSERT INTO application VALUES ("
                       ":id,"
                       ":user_id,"
                       ":date_received,"
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
                       ":rec1_name,"
                       ":rec1_email,"
                       ":rec1_title,"
                       ":rec1_affiliation,"
                       ":rec1_score,"
                       ":rec2_name,"
                       ":rec2_email,"
                       ":rec2_title,"
                       ":rec2_affiliation,"
                       ":rec2_score,"  
                       ":rec3_name,"
                       ":rec3_email,"
                       ":rec3_title,"
                       ":rec3_affiliation,"
                       ":rec3_score,"
                       ":transcripts,"
                       ":status,"
                       ":ranking,"
                       ":comments,"
                       ":description)",

                       {'id': cursor.lastrowid,
                        'user_id': application.user_id,
                        'date_received': application.date_received,
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
                        'rec1_name': application.rec1_name,
                        'rec1_email': application.rec1_email,
                        'rec1_title': application.rec1_title,
                        'rec1_affiliation': application.rec1_affiliation,
                        'rec1_score': application.rec1_score,
                        'rec2_name': application.rec2_name,
                        'rec2_email': application.rec2_email,
                        'rec2_title': application.rec2_title,
                        'rec2_affiliation': application.rec2_affiliation,
                        'rec2_score': application.rec2_score,
                        'rec3_name': application.rec3_name,
                        'rec3_email': application.rec3_email,
                        'rec3_title': application.rec3_title,
                        'rec3_affiliation': application.rec3_affiliation,
                        'rec3_score': application.rec3_score,
                        'transcripts': application.transcripts,
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

    def update_application_attribute(self, attribute_name, user_id, attribute_value):

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("UPDATE application SET {0}=:{0} WHERE user_id=:user_id".format(attribute_name),

                       {'user_id': user_id,
                        '{0}'.format(attribute_name): attribute_value})

        connection.commit()
        connection.close()

        # Update root data
        self.edit_application = self.get_application(user_id)

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

    def get_pending_applications(self):

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM application WHERE "
                       "transcripts IS 1 "
                       "AND (rec1_score IS NOT NULL OR rec2_score IS NOT NULL OR rec3_score IS NOT NULL) "
                       "AND status IS NULL")

        application_tuples = cursor.fetchall()
        connection.close()

        if application_tuples:
            return self.convert_to_application(application_tuples)

    def get_rejected_applications(self, attribute_name, attribute_value):

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM application "
                       "WHERE {0}=:{0} "
                       "AND status LIKE 'Rejected'".format(attribute_name),
                       {'{0}'.format(attribute_name): attribute_value})

        application_tuples = cursor.fetchall()
        connection.close()

        if application_tuples:
            return self.convert_to_application(application_tuples)

    def get_admitted_applications(self, attribute_name, attribute_value):

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM application "
                       "WHERE {0}=:{0} "
                       "AND (status LIKE 'Admitted With Aid' "
                       "OR status LIKE 'Admitted')".format(attribute_name),
                       {'{0}'.format(attribute_name): attribute_value})

        application_tuples = cursor.fetchall()
        connection.close()

        if application_tuples:
            return self.convert_to_application(application_tuples)

    def get_applications_by_attribute(self, attribute_name, attribute_value):

        connection = sqlite3.connect(self.sql_file_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM application WHERE {0}=:{0}".format(attribute_name),
                       {'{0}'.format(attribute_name): attribute_value})

        application_tuples = cursor.fetchall()
        connection.close()

        if application_tuples:
            return self.convert_to_application(application_tuples)

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
    def submit_application(self, application_tuple):

        self.add_application(application_tuple)
        role_tuple = [None, application_tuple[1], 'Applicant', '']
        self.add_role(role_tuple)

    def load_applicant_data(self, user_id):

        self.edit_user = self.get_user(user_id)
        self.edit_application = self.get_application(user_id)

    def get_pending_applicants(self):
        """
        Get and return list of user IDs who applied to university, their data was entered, but decision was not made
        """

        # Clear data
        del self.pending_users[:]
        del self.pending_applications[:]

        pending_applications = self.get_pending_applications()

        if not pending_applications:
            return

        for application in pending_applications:
            self.pending_applications.append(application)
            self.pending_users.append(self.get_user(application.user_id))

    def get_applicants_by_id(self, user_id):

        del self.pending_users[:]
        del self.pending_applications[:]

        self.pending_users.append(self.get_user(user_id))
        self.pending_applications.append(self.get_application(user_id))

    def get_users_for_display(self, user_ids):

        # Clean existing data
        del self.display_users[:]
        del self.display_applications[:]

        # Add new data
        for index, user_id in enumerate(user_ids):

            user = self.get_user(user_id)
            if user:
                self.display_users.append(user)
                self.display_applications.append(self.get_application(user_id))

    # Additional Queries
    def check_roles(self, user_id, role_name):
        """
        Check if user has a certain role
        """

        roles = self.get_user_roles(user_id)

        for role in roles:
            if role.name == role_name:
                return True

    def query_applicants_by_attribute(self, attribute_name, attribute_value):
        """
        Get applicants for given term/degree
        """

        # Clean existing data
        del self.display_users[:]
        del self.display_applications[:]

        applications = self.get_applications_by_attribute(attribute_name, attribute_value)

        if not applications:
            return

        for application in applications:
            user = self.get_user(application.user_id)

            if self.check_roles(user.id, 'Applicant'):
                self.display_users.append(user)
                self.display_applications.append(application)

    def query_admitted_by_attribute(self, attribute_name, attribute_value):

        # Clean existing data
        del self.display_users[:]
        del self.display_applications[:]

        applications = self.get_admitted_applications(attribute_name, attribute_value)

        if not applications:
            return

        for application in applications:
            user = self.get_user(application.user_id)
            self.display_users.append(user)
            self.display_applications.append(application)

    def query_students_by_attribute(self, attribute_name, attribute_value):

        # Clean existing data
        del self.display_users[:]
        del self.display_applications[:]

        applications = self.get_admitted_applications(attribute_name, attribute_value)

        if not applications:
            return

        for application in applications:
            user = self.get_user(application.user_id)

            if self.check_roles(user.id, 'Student'):
                self.display_users.append(user)
                self.display_applications.append(application)

    def get_average_gre(self, attribute_name, attribute_value):
        """
        Get average GRE of admitted students for current degree/term
        """

        verbal = 0
        quantitative = 0
        analytical = 0

        applications = self.get_admitted_applications(attribute_name, attribute_value)

        if not applications:
            return verbal, quantitative, analytical

        number_of_applications = len(applications)

        for application in applications:
            verbal += int(application.gre_verbal)
            quantitative += int(application.gre_quantitative)
            analytical += int(application.gre_analytical)

        verbal = verbal/number_of_applications
        quantitative = quantitative/number_of_applications
        analytical = analytical/number_of_applications

        return verbal, quantitative, analytical


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

        editor = QtGui.QComboBox(parent)
        editor.addItems(self._data)

        return editor

    def setEditorData(self, editor, index):

        model_value = index.model().data(index, QtCore.Qt.EditRole)

        current_index = editor.findText(model_value)
        if current_index > 0:
            editor.setCurrentIndex(current_index)

    def setModelData(self, editor, model, index):
        editor_value = editor.currentText()
        model.setData(index, editor_value, QtCore.Qt.EditRole)


class ReviewApplicantModel(QtCore.QAbstractTableModel):
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


class DisplayApplicantModel(QtCore.QAbstractTableModel):
    def __init__(self, starrs_data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)

        self.starrs_data = starrs_data
        self.header = ['  Id  ',
                       '  Email  ',
                       '  First Name ',
                       '  Last Name  ',
                       '  Admission Term  ',
                       '  Degree  ',
                       '  Status  ']

    def flags(self, index):

        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def headerData(self, col, orientation, role):

        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[col]

    def rowCount(self, parent):

        return len(self.starrs_data.display_users)

    def columnCount(self, parent):

        return len(self.header)

    def data(self, index, role):

        if not index.isValid():
            return

        row = index.row()
        column = index.column()

        if role == QtCore.Qt.DisplayRole:  # Fill table data to DISPLAY
            if column == 0:
                return self.starrs_data.display_users[row].id

            if column == 1:
                return self.starrs_data.display_users[row].email

            if column == 2:
                return self.starrs_data.display_users[row].first_name

            if column == 3:
                return self.starrs_data.display_users[row].last_name

            if column == 4:
                return self.starrs_data.display_applications[row].admission_term

            if column == 5:
                return self.starrs_data.display_applications[row].degree_sought

            if column == 6:
                return self.starrs_data.display_applications[row].status


class EditApplicationModel(QtCore.QAbstractTableModel):
    def __init__(self, starrs_data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)

        self.starrs_data = starrs_data

        self.header = ['  User Id  ',  # 0 User
                       '  First Name ',
                       '  Middle Name ',
                       '  Last Name',
                       '  Email ',
                       '  Address  ',
                       '  Phone  ',
                       '  GRE Verbal  ',  # 7 Application
                       '  GRE Quantitative  ',
                       '  GER Analytical  ',
                       '  Experience  ',
                       '  Interest  ',
                       '  Admission Term  ',
                       '  Degree  ',
                       '  Prior 1 Major  ',
                       '  Prior 1 Year  ',
                       '  Prior 1 GPA  ',
                       '  Prior 1 University  ',
                       '  Prior 2 Major  ',
                       '  Prior 2 Year  ',
                       '  Prior 2 GPA  ',
                       '  Prior 2 University  ',
                       '  R1 Name  ',
                       '  R1 Email  ',
                       '  R1 Title  ',
                       '  R1 Affiliation  ',
                       '  R2 Name  ',
                       '  R2 Email  ',
                       '  R2 Title  ',
                       '  R2 Affiliation  ',
                       '  R3 Name  ',
                       '  R3 Email  ',
                       '  R3 Title  ',
                       '  R3 Affiliation']
        self.schema = {
            'user': {
                0: 'id',
                1: 'first_name',
                2: 'middle_name',
                3: 'last_name',
                4: 'email',
                5: 'address',
                6: 'phone'},

            'application': {
                 7: 'gre_verbal',
                 8: 'gre_quantitative',
                 9: 'gre_analytical',
                 10: 'experience',
                 11: 'interest',
                 12: 'admission_term',
                 13: 'degree_sought',
                 14: 'prior1_major',
                 15: 'prior1_year',
                 16: 'prior1_gpa',
                 17: 'prior1_university',
                 18: 'prior2_major',
                 19: 'prior2_year',
                 20: 'prior2_gpa',
                 21: 'prior2_university',
                 22: 'rec1_name',
                 23: 'rec1_email',
                 24: 'rec1_title',
                 25: 'rec1_affiliation',
                 26: 'rec2_name',
                 27: 'rec2_email',
                 28: 'rec2_title',
                 29: 'rec2_affiliation',
                 30: 'rec3_name',
                 31: 'rec3_email',
                 32: 'rec3_title',
                 33: 'rec3_affiliation'}}

    # Build-in functions
    def flags(self, index):

        column = index.column()
        if column == 0:  # Code State Type
            return QtCore.Qt.ItemIsEnabled
        else:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable

    def headerData(self, col, orientation, role):

        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[col]

    def rowCount(self, parent):

        return 1

    def columnCount(self, parent):

        return len(self.header)

    def data(self, index, role):

        if not index.isValid():
            return

        column = index.column()

        if not self.starrs_data.edit_user:
            return

        if role == QtCore.Qt.DisplayRole:  # Fill table data to DISPLAY

            if column in range(0, 7):
                attribute = self.schema['user'][column]
                return eval('self.starrs_data.edit_user.{0}'.format(attribute))
            else:
                attribute = self.schema['application'][column]
                return eval('self.starrs_data.edit_application.{0}'.format(attribute))

        if role == QtCore.Qt.EditRole:

            if column in range(0, 7):
                attribute = self.schema['user'][column]
                return eval('self.starrs_data.edit_user.{0}'.format(attribute))
            else:
                attribute = self.schema['application'][column]
                return eval('self.starrs_data.edit_application.{0}'.format(attribute))

    def setData(self, index, cell_data, role=QtCore.Qt.EditRole):
        """
        When table cell is edited
        """

        column = index.column()
        user_id = self.starrs_data.edit_user.id

        if role == QtCore.Qt.EditRole:

            if column in range(1, 7):
                attribute = self.schema['user'][column]
                self.starrs_data.update_user_attribute(attribute, user_id, cell_data)
            else:
                attribute = self.schema['application'][column]
                self.starrs_data.update_application_attribute(attribute, user_id, cell_data)

            return True


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
        self.roles = ['GS', 'Reviewer', 'Adviser', 'Instructor', 'Applicant', 'Student', 'Alumni']

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
        self.btnLoadApplicationData.pressed.connect(self.load_application_data)
        self.btnEnroll.pressed.connect(self.enroll)
        # 2)
        self.btnFindApplicant.pressed.connect(self.find_applicants)
        self.btnSetTranscripts.pressed.connect(self.add_transcripts)
        self.btnSetRecomendations.pressed.connect(self.add_recommendations)
        self.btnLoadPendingApplicants.pressed.connect(self.load_pending_applicants)
        self.btnLoadApplicantByID.pressed.connect(self.load_applicant)
        # Queries
        self.btnGetApplicants.pressed.connect(self.query_applicants)
        self.btnGetApplicants.pressed.connect(self.query_statistic)
        self.btnGetAdmittedStudents.pressed.connect(self.query_admitted)
        self.btnGetAdmittedStudents.pressed.connect(self.query_statistic)
        self.btnGetCurrentStudents.pressed.connect(self.query_students)

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
        self.linAddressNumber.setText('310')
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
        self.linRecomendation1Email.setText('atom@alamos.net')
        self.linRecomendation1Title.setText('physicist')
        self.linRecomendation1Affiliation.setText('nuclear')
        self.linRecomendation2Name.setText('Hubert J Farnsworth')
        self.linRecomendation2Email.setText('express@futurama.com')
        self.linRecomendation2Title.setText('professor')
        self.linRecomendation2Affiliation.setText('space')
        self.linRecomendation3Name.setText('Rick Sanchez')
        self.linRecomendation3Email.setText('rick@morty.com')
        self.linRecomendation3Title.setText('psycho')
        self.linRecomendation3Affiliation.setText('universe')

        # UI controls
        self.comDegreeSought.addItems(self.degrees)
        self.comAdmissionTerm.addItems(self.terms)
        self.comRecomendationScore_1.addItems(self.scores)
        self.comRecomendationScore_2.addItems(self.scores)
        self.comRecomendationScore_3.addItems(self.scores)

        self.comDegreeSoughtQ.addItems(self.degrees)
        self.comAdmissionTermQ.addItems(self.terms)

        # Tables
        self.setup_table(self.tabReviewAdmitApplicant)
        self.setup_table(self.tabEditApplication)
        self.setup_table(self.tabFoundApplicants)
        self.setup_table(self.tabAdmissionQuerries)

    def init_data(self):

        self.starrs_data = StarrsData(self.sql_file_path)

    def get_ui_apply(self):

        user_tuple = [
            None,
            self.linStudentFirstName.text(),
            self.linStudentMidName.text(),
            self.linStudentLastName.text(),
            self.linApplicantEmail.text(),
            '{0}, {1}, {2}, {3}, {4}'.format(self.linAddressZip.text(),
                                        self.linAddressState.text(),
                                        self.linAddressCity.text(),
                                        self.linAddressStreet.text(),
                                        self.linAddressNumber.text()),
            self.linApplicantPhone.text(),
            '']

        application_tuple = [
            None,  # id
            None,  # user_id
            date.today().strftime('%Y/%m/%d'),  # date received
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
            self.linRecomendation1Name.text(),
            self.linRecomendation1Email.text(),
            self.linRecomendation1Title.text(),
            self.linRecomendation1Affiliation.text(),
            None,
            self.linRecomendation2Name.text(),
            self.linRecomendation2Email.text(),
            self.linRecomendation2Title.text(),
            self.linRecomendation2Affiliation.text(),
            None,
            self.linRecomendation3Name.text(),
            self.linRecomendation3Email.text(),
            self.linRecomendation3Title.text(),
            self.linRecomendation3Affiliation.text(),
            None,
            0,  # transcripts
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
        populate_database(self.sql_file_path)

    def setup_table(self, table):

        table.verticalHeader().hide()
        table.verticalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        table.horizontalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        table.horizontalHeader().setStretchLastSection(True)
        table.setItemDelegate(AlignDelegate())

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

        # Add application
        application_tuple[1] = user.id
        self.starrs_data.submit_application(application_tuple)

        # Sent password
        self.statusBar().showMessage('>> Password is: {0}'.format(user.id))

    def check_recommendations(self, application):
        """
        Check if GS set recommendation score
        """

        if application.rec1_score or application.rec2_score or application.rec3_score:
            return True

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
            if application.transcripts and self.check_recommendations(application):
                self.linApplicationStatus.setText('Application Received and Decision Pending')
            else:
                missing = ''
                if not application.transcripts:
                    missing = 'transcripts'
                if not self.check_recommendations(application):
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

        if application.status in ['Admitted With Aid', 'Admitted']:

            role_tuple = [None, user_id, 'Student', '']
            self.starrs_data.add_role(role_tuple)
            self.statusBar().showMessage('>> Student {0} enrolled to the Database University!'.format(user_id))

        else:
            self.statusBar().showMessage('>> Only admitted students can enroll to the Database University!')

    def load_application_data(self):

        user_id = self.linStudentID.text()

        if user_id == '':
            self.starrs_data.clear_data()
        else:
            self.starrs_data.load_applicant_data(user_id)

        self.tabEditApplication.setModel(EditApplicationModel(self.starrs_data))

    # 2) Admission process
    def find_applicants(self):

        user_id = self.linSearchApplicantID.text()
        last_name = self.linSearchApplicantLastname.text()

        user_ids = []

        if user_id != '':
            user_ids = [user_id]

        elif last_name != '':
            users = self.starrs_data.get_users_by_name(last_name)
            if users:
                for user in users:
                    user_ids.append(user.id)
        else:
            self.starrs_data.clear_data()
            self.tabFoundApplicants.setModel(DisplayApplicantModel(self.starrs_data))
            self.statusBar().showMessage('>> Enter applicant ID or Last Name!')

        if user_ids:
            self.starrs_data.get_users_for_display(user_ids)
            self.tabFoundApplicants.setModel(DisplayApplicantModel(self.starrs_data))

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

        user_id = self.linStudentIDAdmission.text()
        if user_id == '':
            self.statusBar().showMessage('>> Please, enter the user id!')
            return

        if self.chbDoRecommendation_1.isChecked():
            score = self.comRecomendationScore_1.currentText()
            self.starrs_data.update_application_attribute('rec1_score', user_id, score)

        if self.chbDoRecommendation_2.isChecked():
            score = self.comRecomendationScore_2.currentText()
            self.starrs_data.update_application_attribute('rec2_score', user_id, score)

        if self.chbDoRecommendation_3.isChecked():
            score = self.comRecomendationScore_3.currentText()
            self.starrs_data.update_application_attribute('rec3_score', user_id, score)

        self.statusBar().showMessage('>> Applicant {0} recommendations submitted!'.format(user_id))

    def load_pending_applicants(self):

        self.starrs_data.get_pending_applicants()
        applicant_model = ReviewApplicantModel(self.starrs_data)
        self.tabReviewAdmitApplicant.setModel(applicant_model)

        ranking = DropdownDelegate(self.rankings, self.tabReviewAdmitApplicant)
        decision = DropdownDelegate(self.decisions, self.tabReviewAdmitApplicant)
        self.tabReviewAdmitApplicant.setItemDelegateForColumn(3, ranking)
        self.tabReviewAdmitApplicant.setItemDelegateForColumn(5, decision)

    def load_applicant(self):

        user_id = self.linLoadApplicantByID.text()

        # self.applicant_model.layoutAboutToBeChanged.emit()
        # self.starrs_data.get_applicants_by_id(user_id)
        # self.applicant_model.layoutChanged.emit()

        if user_id != '':
            self.starrs_data.get_applicants_by_id(user_id)
            applicant_model = ReviewApplicantModel(self.starrs_data)
            self.tabReviewAdmitApplicant.setModel(applicant_model)

            ranking = DropdownDelegate(self.rankings, self.tabReviewAdmitApplicant)
            decision = DropdownDelegate(self.decisions, self.tabReviewAdmitApplicant)
            self.tabReviewAdmitApplicant.setItemDelegateForColumn(3, ranking)
            self.tabReviewAdmitApplicant.setItemDelegateForColumn(5, decision)
        else:
            self.starrs_data.clear_data()
            applicant_model = ReviewApplicantModel(self.starrs_data)
            self.tabReviewAdmitApplicant.setModel(applicant_model)

    def query_applicants(self):
        """
        Get list of applicants by term/degree
        """

        if self.radByTerm.isChecked():
            admission_term = self.comAdmissionTermQ.currentText()
            self.starrs_data.query_applicants_by_attribute('admission_term', admission_term)

        else:
            degree_sought = self.comDegreeSoughtQ.currentText()
            self.starrs_data.query_applicants_by_attribute('degree_sought', degree_sought)

        self.tabAdmissionQuerries.setModel(DisplayApplicantModel(self.starrs_data))

    def query_admitted(self):

        if self.radByTerm.isChecked():
            admission_term = self.comAdmissionTermQ.currentText()
            self.starrs_data.query_admitted_by_attribute('admission_term', admission_term)

        else:
            degree_sought = self.comDegreeSoughtQ.currentText()
            self.starrs_data.query_admitted_by_attribute('degree_sought', degree_sought)

        self.tabAdmissionQuerries.setModel(DisplayApplicantModel(self.starrs_data))

    def query_students(self):

        if self.radByTerm.isChecked():
            admission_term = self.comAdmissionTermQ.currentText()
            self.starrs_data.query_students_by_attribute('admission_term', admission_term)

        else:
            degree_sought = self.comDegreeSoughtQ.currentText()
            self.starrs_data.query_students_by_attribute('degree_sought', degree_sought)

        self.tabAdmissionQuerries.setModel(DisplayApplicantModel(self.starrs_data))

    def process_statistic(self, attribute_name, attribute_value):

        # Clear fields
        self.linStatApplicants.setText('')
        self.linStatAdmitted.setText('')
        self.linStatRejected.setText('')
        self.linStatGRE.setText('')

        # Total number of Applicants
        applicants = self.starrs_data.get_applications_by_attribute(attribute_name, attribute_value)

        if applicants:
            applicants = str(len(applicants))
        else:
            applicants = '0'

        self.linStatApplicants.setText(applicants)

        # Total number of Admitted
        admitted = self.starrs_data.get_admitted_applications(attribute_name, attribute_value)

        if admitted:
            admitted = str(len(admitted))
        else:
            admitted = '0'

        self.linStatAdmitted.setText(admitted)

        # Total number of rejected
        rejected = self.starrs_data.get_rejected_applications(attribute_name, attribute_value)

        if rejected:
            rejected = str(len(rejected))
        else:
            rejected = '0'

        self.linStatRejected.setText(rejected)

        # Average GRE
        verbal, quantitative, analytical = self.starrs_data.get_average_gre(attribute_name, attribute_value)
        average_gre = '{0} {1} {2}'.format(verbal, quantitative, analytical)
        self.linStatGRE.setText(average_gre)

    def query_statistic(self):

        if self.radByTerm.isChecked():
            admission_term = self.comAdmissionTermQ.currentText()
            self.process_statistic('admission_term', admission_term)

        else:
            degree_sought = self.comDegreeSoughtQ.currentText()
            self.process_statistic('degree_sought', degree_sought)


if __name__ == "__main__":
    app = QtGui.QApplication([])
    starrs = STARRS()
    starrs.show()
    app.exec_()
