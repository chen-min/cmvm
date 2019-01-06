# coding: utf-8
from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId

class TestMongo(object):
  def __init__(self):
    self.client = MongoClient('localhost', 27017)
    self.db = self.client['blog']

  def add_one(self):
    ''''add data'''
    post = {
      'title': 'test4',  
      'content': 'testcontent4....',
      'created_at': datetime.now(),
      'x':4
    }
    return self.db.blog.posts.insert_one(post)

  def get_one(self):
    return self.db.blog.posts.find_one()

  def get_more(self):
    return self.db.blog.posts.find({'x': 2 })

  def get_one_from_oid(self, oid):
    obj = ObjectId(oid)
    return self.db.blog.posts.find_one({'_id': obj})
  
  def update(self):
    # return self.db.blog.posts.update_one({'x':23}, {'$inc':{'x':111}})
    return self.db.blog.posts.update_many({},{'$inc':{'x':10}})

  def delete(self):
    # return self.db.blog.posts.delete_one({'x':1})
    return self.db.blog.posts.delete_many({'x':1})

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
