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

cursor = connection.cursor()

alldict = {}

truncate_sqls = [
    "TRUNCATE table jph_users;",
    "TRUNCATE table jph_sections;",
    "TRUNCATE table jph_roles;",
    "TRUNCATE table jph_enrollments;",
    "TRUNCATE table jph_finalgrades;"
]

for sql in truncate_sqls:
    cursor.execute(sql)

user_sql = "INSERT INTO jph_users (FirstName, LastName, Phone) VALUES "
for x in range(500):
    user_sql += f"('{fake.first_name()}', '{fake.last_name()}', '{fake.phone_number()}'), "
user_sql = user_sql.rstrip(', ') + ';'
print(user_sql)
cursor.execute(user_sql)

section_sql = "INSERT INTO jph_sections (ClassID, SectionNumber, YearTermID) VALUES "
for ytID in range(1, 4):
    for sN in range(1, 51):
        cID = random.randrange(1, 20)
        section_sql += f"({cID}, {sN}, {ytID}), "
section_sql = section_sql.rstrip(', ') + ';'
print(section_sql)
cursor.execute(section_sql)

role_sql = "INSERT INTO jph_roles (RoleName) VALUES ('Teacher'), ('Student');"
print(role_sql)
cursor.execute(role_sql)

enrollment_sql = "INSERT INTO jph_enrollments (UserID, SectionID, RoleID) VALUES "

for loop in range(5):  # 600 total teacher enrollments
    for teacherUID in range(1, 101):
        sID = random.randrange(1, 200)
        enrollment_sql += f"({teacherUID}, {sID}, 1), "
        
for loop in range(10):  # 4400 total student enrollments
    for studentUID in range(101, 500):
        sID = random.randrange(1, 200)
        enrollment_sql += f"({studentUID}, {sID}, 2), "
enrollment_sql = enrollment_sql.rstrip(', ') + ';'
print(enrollment_sql)
cursor.execute(enrollment_sql)

finalgrade_sql = "INSERT INTO jph_finalgrades (EnrollmentID, GradeLetterID) VALUES "
for eID in range(101, 500):
    glID = random.randrange(1, 5)
    finalgrade_sql += f"({eID}, {glID}), "
finalgrade_sql = finalgrade_sql.rstrip(', ') + ';'
print(finalgrade_sql)
cursor.execute(finalgrade_sql)

connection.commit()
cursor.close()
connection.close()
