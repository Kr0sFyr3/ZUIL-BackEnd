from Data.api import API

api = API()

api.login("tnc.banh1@ad-academie.nl", "20qKy_u}5R")

print(api.get_student_by_tag_id(332613414))
