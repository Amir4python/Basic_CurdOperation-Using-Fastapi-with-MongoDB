#scheemas helps to serialize and also convert mongodb  format json into our UI needed

def studentEntity(dbitem):
  return {
    'sid':str(dbitem['_id']),
    'sname':dbitem['name'],
    'semail':dbitem['email'],
    'sphone':dbitem['phone']
  }


def studentEntityList(dbitem_list):
  listOfStudents=[]
  for item in dbitem_list:
    listOfStudents.append(studentEntity(item))
  return listOfStudents