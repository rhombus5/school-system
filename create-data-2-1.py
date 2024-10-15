import random
import pymysql
from faker import Faker
fake = Faker()

host = 'svu-database.cxraefksllhd.us-east-1.rds.amazonaws.com'
port = 3306
user = 'student'
password = 'Aloha123!'
database = 'SVU1'

connection = pymysql.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)

conn = connection.cursor()

alldict = {}

sql1 = ("TRUNCATE table jph_users;")
conn.execute(sql1)
sql2 = ("TRUNCATE table jph_sections;")
conn.execute(sql2)
sql3 = ("TRUNCATE table jph_roles;")
conn.execute(sql3)
sql4 = ("TRUNCATE table jph_enrollments;")
conn.execute(sql4)
sql5 = ("TRUNCATE table jph_finalgrades;")
conn.execute(sql5)

user_sql = "INSERT INTO jph_users (FirstName, LastName, Phone) VALUES "
for x in range (0, 500):
    user_sql += f"({fake.first_name()}, {fake.last_name()}, {fake.phone_number()}) "
print(user_sql)
conn.execute(user_sql)

section_sql = "INSERT INTO jph_sections (ClassID, SectionNumber, YearTermID) VALUES "
for ytID in range(1, 4):
    for sN in range(1, 51):
        cID = random.randrange(1, 20)
        section_sql += f"({cID}, {sN}, {ytID}) "
print(section_sql)
conn.execute(section_sql)

role_sql = "INSERT INTO jph_roles (RoleName) VALUES ('Teacher'), ('Student')"
print(role_sql)
conn.execute(role_sql)

enrollment_sql = "INSERT INTO jph_enrollments (UserID, SectionID, RoleID) VALUES "
for loop in range(1, 6): #600 total teacher enrollments
    for teacherUID in range(1, 100):
        sID = random.randrange(1, 200)
        enrollment_sql += f"({teacherUID}, {sID}, {1}) "
for loop in range(1, 11): #4400 total student enrollments
    for studentUID in range(101, 500):
        sID = random.randrange(1, 200)
        enrollment_sql += f"({studentUID}, {sID}, {2}) "
print(enrollment_sql)
conn.execute(enrollment_sql)

finalgrade_sql = "INSERT INTO jph_finalgrade (EnrollmentID, GradeLetterID) VALUES "
for eID in range(101, 500):
    glID = random.randrange(1, 5)
    finalgrade_sql += f"({eID}, {glID}) "
print(finalgrade_sql)
conn.execute(finalgrade_sql)


conn.commit()
conn.close()

data = conn.fetchall()
