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
      'title': '新的标题',  
      'content': '博客内容....',
      'created_at': datetime.now()
    }
    return self.db.blog.posts.insert_one(post)

  def get_one(self):
    return self.db.blog.posts.find_one()

  def get_more(self):
    return self.db.blog.posts.find({'x': 2 })

  def get_one_from_oid(self, oid):
    obj = ObjectId(oid)
    return self.db.blog.posts.find_one({'_id': obj})

def main():
  obj = TestMongo()
  # rest = obj.get_one()
  # print(rest["_id"],'rest')
  # rest = obj.get_more()
  # for item in rest:
  #   print(item["_id"])
  # rest = obj.get_one_from_oid('5c308ce57f1d0910248d7235')
  # print(rest)

if __name__ == "__main__":
  main()

