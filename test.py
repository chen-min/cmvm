# coding: utf-8
from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId

class TestMongo(object):
  def __init__(self):
    self.client = MongoClient('localhost', 27017)
    self.db = self.client['students']

  def add_one(self):
    ''''add data'''
    post = {
      'name': 'bob',  
      'age': 19.0,
      'sex': 'male',
      'address':'--'
    }
    post1 = {
      'name': 'john',  
      'age': 18.0,
      'sex': 'male',
      'address':'--'
    }
    post2 = {
      'name': 'jef',  
      'age': 29.0,
      'sex': 'male',
      'address':'--'
    }
    post3 = {
      'name': 'haleo',  
      'age': 16.0,
      'sex': 'female',
      'address':'--'
    }
    post4 = {
      'name': 'anne',  
      'age': 17.0,
      'sex': 'female',
      'address':'--'
    }
    post5 = {
      'name': 'tom',  
      'age': 12.0,
      'sex': 'male',
      'address':'--'
    }

    self.db.students.insert_one(post)
    self.db.students.insert_one(post1)
    self.db.students.insert_one(post2)
    self.db.students.insert_one(post3)
    self.db.students.insert_one(post4)
    self.db.students.insert_one(post5)



def main():
  obj = TestMongo()
  rest = obj.add_one()
  # print(rest["_id"],'rest')
  # rest = obj.get_more()
  # for item in rest:
  #   print(item["_id"])
  # rest = obj.get_one_from_oid('5c308ce57f1d0910248d7235')
  # print(rest)
  # rest = obj.update()
  # print(rest,'rest')
  # print(rest.matched_count)
  # print(rest.modified_count)
  # rest = obj.delete()
  # print(rest.deleted_count)

if __name__ == "__main__":
  main()
