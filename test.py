from getDatabase import *
import collections
studenID = "xxx01"
term = "1/2559"

s = Get_Academic(studenID,term)
t = Get_name_credit_subject(studenID,term)
o = Academic_1st_table()
p = Academic_2st_table()
re = return_Method(studenID)
returnda = return_data(studenID)
add = Add_Method(studenID)


c = Check()
# c.T_check("xxx03","xxx03")
# c.S_check(59340500021,"59340500021")
# c.FRAB(2)
# re.t_name()


######################################################
# box = []
# include = []
# for instance in session.query(Profile).order_by(Profile.id_student):
#     x = instance.id_student
#     box.append(str(x))
# for i in box:
#     year = str(i)[:2]
#     frab = int(year) - 56
#     word = "FRAB#"+str(frab)
#     if word not in include:
#         include.append(word)
# print(include)




#########################Activity######################
# add.Act_des("Happy","swimming")

########################Profile########################
# print("Profile: ")
# print(returnda.DicPro(re.name(), re.surname(), re.date(), re.birth(), re.nation(), re.education(), re.disease(), re.relative(),  re.PhoneEmer(), re.Phonestu(), re.address(), re.email()))
# print("Activity: ")
# print(returnda.DicAct(re.Act_name(), re.Act_des(), re.Act_photo(), re.Act_type(), re.Act_advisor(), re.Act_Date(), re.Act_file(), re.Act_confirm()))
# print("output_term: ")
# print(o.output_term(s.get_id_subject(),t.get_nameSubject(),t.get_credit(),s.get_grade()))
# print("output_sum: ")
# print(p.output_sum(s.get_this_semester_credit(),s.get_GPA(),s.get_cumulative_credit(),s.get_GPAX()))
# print(re.name())

# add.id_stu(Profile)
# print(re.disease())
# for item in re.disease():
#     spinach = session.query(Disease).filter_by(id_student = "{}".format(studenID),Disease = "{}".format(item)).one()
#     session.delete(spinach)
# session.commit()
# def edit_disease(edit,data):
#     print(edit)
#     for item in edit:
#         spinach = session.query(Disease).filter_by(id_student = studenID ,Disease = "{}".format(item)).one()
#         session.delete(spinach)
#         print(item)
#     sth = Disease(id_student = studenID,Disease = "{}".format(data))
#     session.add(sth)
#     session.commit()


# add.edit_disease(re.disease(),"xx")
