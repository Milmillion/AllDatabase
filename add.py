from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databaseSetup import *

engine = create_engine('sqlite:///Database.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

#---------------------------add subject and grade------------------------------#
# studenID = "59340500017"
# term = "1/2559"
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA141",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA161",Grade = "3.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "GEN101",Grade = "3" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "LNG101",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "MTH101",Grade = "2.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "PHY103",Grade = "3" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "PHY191",Grade = "3.5" )
# session.add(student)
# # session.commit()
#
# studenID = "59340500021"
# term = "1/2559"
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA141",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA161",Grade = "3.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "GEN101",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "LNG101",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "MTH101",Grade = "3.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "PHY103",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "PHY191",Grade = "4" )
# session.add(student)
# # session.commit()
#
# studenID = "59340500035"
# term = "1/2559"
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA141",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA161",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "GEN101",Grade = "3.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "LNG102",Grade = "3.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "MTH101",Grade = "3.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "PHY103",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "PHY191",Grade = "3.5" )
# session.add(student)
# # session.commit()
# #-------------------------------------------------------------------#
# studenID = "59340500017"
# term = "2/2559"
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA121",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA142",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA162",Grade = "3.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA163",Grade = "3" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "GEN111",Grade = "3.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "GEN121",Grade = "3.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "MTH102",Grade = "2.5" )
# session.add(student)
# # session.commit()
#
# studenID = "59340500021"
# term = "2/2559"
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA121",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA142",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA162",Grade = "3.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA163",Grade = "3.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "GEN111",Grade = "3.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "GEN121",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "MTH102",Grade = "3.5" )
# session.add(student)
# # session.commit()
#
# studenID = "59340500035"
# term = "2/2559"
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA121",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA142",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA162",Grade = "3.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA163",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "GEN111",Grade = "3.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "GEN121",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "MTH102",Grade = "3.5" )
# session.add(student)
# # session.commit()
#
# #--------------------------------add GPA---------------------------------------#
# term = "1/2559"
# gpa = Gpa(Student_ID = "59340500017",Term =term,sum_credit =17,GPA ="3.38")
# session.add(gpa)
# gpa = Gpa(Student_ID = "59340500021",Term =term,sum_credit =17,GPA ="3.82")
# session.add(gpa)
# gpa = Gpa(Student_ID = "59340500035",Term =term,sum_credit =17,GPA ="3.76")
# session.add(gpa)
# # session.commit()
#
# term = "2/2559"
# gpa = Gpa(Student_ID = "59340500017",Term =term,sum_credit =17,GPA ="3.47")
# session.add(gpa)
# gpa = Gpa(Student_ID = "59340500021",Term =term,sum_credit =17,GPA ="3.76")
# session.add(gpa)
# gpa = Gpa(Student_ID = "59340500035",Term =term,sum_credit =17,GPA ="3.79")
# session.add(gpa)
# # session.commit()
#
# #------------------------------add GPAX----------------------------------------#
# gpaxx = Gpax(Student_ID ="59340500017",sum_all_credit =34,GPAX ="3.42")
# session.add(gpaxx)
# gpaxx = Gpax(Student_ID ="59340500021",sum_all_credit =34,GPAX ="3.79")
# session.add(gpaxx)
# gpaxx = Gpax(Student_ID ="59340500035",sum_all_credit =34,GPAX ="3.77")
# session.add(gpaxx)
# # session.commit()
#
# #----------------------------add subject---------------------------------------#
#
# sub = Subject(ID_Subject ="FRA141",name_subject ="COMPUTER PROGRAMMING",
#  Credit =3)
# session.add(sub)
# sub = Subject(ID_Subject ="FRA161",name_subject ="ROBOTICS EXPLORATION",
#  Credit =3)
# session.add(sub)
# sub = Subject(ID_Subject ="GEN101",name_subject ="PHYSICAL EDUCATION",
#  Credit =1)
# session.add(sub)
# sub = Subject(ID_Subject ="LNG101",name_subject ="GENERAL ENGLISH",
#  Credit =3)
# session.add(sub)
# sub = Subject(ID_Subject ="LNG102",name_subject ="TECHNICAL ENGLISH",
#  Credit =3)
# session.add(sub)
# sub = Subject(ID_Subject ="MTH101",name_subject ="MATHEMATICS I",
#  Credit =3)
# session.add(sub)
# sub = Subject(ID_Subject ="PHY103",name_subject ="GENERAL PHYSICS",
#  Credit =3)
# session.add(sub)
# sub = Subject(ID_Subject ="PHY191",name_subject ="GENERAL PHYSICS LABORATORY I",
#  Credit =1)
# session.add(sub)
# sub = Subject(ID_Subject ="FRA121",name_subject ="ELECTRONIC CIRCUITS",
#  Credit =3)
# session.add(sub)
# sub = Subject(ID_Subject ="FRA142",name_subject ="COMPUTER PROGRAMMING",
#  Credit =3)
# session.add(sub)
# sub = Subject(ID_Subject ="FRA162",name_subject ="ROBOTICS AND AUTOMATION",
#  Credit =1)
# session.add(sub)
# sub = Subject(ID_Subject ="FRA163",name_subject ="ROBOTICS MACHINE SHOP",
#  Credit =1)
# session.add(sub)
# sub = Subject(ID_Subject ="GEN111",name_subject ="MAN AND ETHICS OF LIVING",
#  Credit =3)
# session.add(sub)
# sub = Subject(ID_Subject ="GEN121",name_subject ="LEARNING AND PROBLEM SOLVING SKILLS",
#  Credit =3)
# session.add(sub)
# sub = Subject(ID_Subject ="MTH102",name_subject ="MATHEMATICS II",
#  Credit =3)
# session.add(sub)
# # session.commit()
# # -------------------------------------------------------------------#
#
# sth = Profile(id_student = 59340500035,Name = "Panchalee",Surname  = "Sookprao", Sex = "Miss", Year = 1, Dateofbirth = "12/21/41",Birthplace = "Hospital",Nationality = "Thai",Education = "Surin",Relative = "mom",PhoneforEmergency = "3434343434",Phonestudent = "66666666" ,Address = "Surin",Email = "pop@gmail.com")
# sth1 = Profile(id_student = 59340500021,Name = "Thipawan",Surname  = "Pairam", Sex = "Miss", Year =1 ,Dateofbirth = "14/09/40",Birthplace = "Hospital1",Nationality = "Thai",Education = "Bungkan",Relative = "Dad",PhoneforEmergency = "0941234567",Phonestudent = "0867654321" ,Address = "Bungkan",Email = "pair@gmail.com")
# sth2 = Profile(id_student = 59340500017,Name = "Natthaphon",Surname  = "Sudadech", Sex = "Mr", Year =1, Dateofbirth = "05/03/39",Birthplace = "Hospital2",Nationality = "Thai",Education = "Bungkan",Relative = "Mom",PhoneforEmergency = "087654321",Phonestudent = "0865432111" ,Address = "Bungkan",Email = "mill@gmail.com")
# session.add(sth) #add sth into database.
# session.add(sth1) #add sth into database.
# session.add(sth2) #add sth into database.
# sth = Activity(id_student = 59340500017,NameActivity = "Natthaphon",Description = "this is so fun.",Photo = "Mill.jpg",Type = "Dynamics",Advisor = "Prof.Ton",Date_Activity = "14/12/60",File = "file of the Dynamic",Confirm = "Not Confirm yet")
# sth1 = Activity(id_student = 59340500021,NameActivity = "Thipawan",Description = "Receive a lot of knowledges.",Photo = "Pair.jpg",Type = "Calculas",Advisor = "Prof.Somran",Date_Activity = "15/12/61",File = "file of the Calculas",Confirm = "confirm")
# sth2 = Activity(id_student = 59340500035,NameActivity = "Panchalee",Description = "It is will be useful.",Photo = "Popperzz.jpg",Type = "Digital",Advisor = "Prof.Pi",Date_Activity = "15/12/60",File = "file of the Digital",Confirm = "Not Confirm yet")
# sth3 = Activity(id_student = 59340500035,NameActivity = "Table tennnis.",Description = "Table tennis is good.",Photo = "Popperzztennis.jpg",Type = "Sport",Advisor = "Prof.__",Date_Activity = "29/05/60",File = "file of the table tennis",Confirm = "Confirm")
# session.add(sth) #add sth into database.
# session.add(sth1) #add sth into database.
# session.add(sth2) #add sth into database.
# session.add(sth3) #add sth into database.
#
#
# sth = Disease(id_student = 59340500017,Disease = "gout")
# sth1 = Disease(id_student = 59340500017,Disease = "hemorrhoids")
# sth2 = Disease(id_student = 59340500017,Disease = "pneumonia")
# session.add(sth) #add sth into database.
# session.add(sth1) #add sth into database.
# session.add(sth2) #add sth into database.
#
# sth = Disease(id_student = 59340500035,Disease = "diarrhea")
# sth1 = Disease(id_student = 59340500035,Disease = "enteritis")
# session.add(sth) #add sth into database.
# session.add(sth1) #add sth into database.
#
# sth = Disease(id_student = 59340500021,Disease = "heart disease")
# sth1 = Disease(id_student = 59340500021,Disease = "measles")
# session.add(sth) #add sth into database.
# session.add(sth1) #add sth into database.
# # session.commit() #commit data that increase.
#
# sth = TeacherPW(id_teacher = "xxx01",Name = "warasinee", Surname = "chaisangmongkon",T_Password = "xxx01")
# sth1 = TeacherPW(id_teacher = "xxx02",Name = "bawornsak", Surname = "sakulkueakulsuk",T_Password = "xxx02")
# sth2 = TeacherPW(id_teacher = "xxx03",Name = "Suriya", Surname = "Natsupakpong",T_Password = "xxx03")
# session.add(sth) #add sth into database.
# session.add(sth1) #add sth into database.
# session.add(sth2) #add sth into database.
#
# sth = StudentPW(id_student = 59340500021,S_Password = "59340500021")
# sth1 = StudentPW(id_student = 59340500035,S_Password = "59340500035")
# sth2 = StudentPW(id_student = 59340500017,S_Password = "59340500017")
# session.add(sth) #add sth into database.
# session.add(sth1) #add sth into database.
# session.add(sth2) #add sth into database.
# session.commit() #commit data that increase.







