# coding: utf-8
from mongoengine import connect, Document, EmbeddedDocument, StringField, IntField, FloatField, ListField,EmbeddedDocumentField

connect('students')
SEX_CHOICE = (
    ('male', '男'),
    ('female', '女'),
)

class Grade(EmbeddedDocument):
    """成绩"""
    name = StringField(required=True)
    score = FloatField(required=True)

class Student(Document):
    name = StringField(max_length=32, required=True)
    age = IntField(required = True)
    grade = FloatField()
    address = StringField()
    sex = StringField(choices=SEX_CHOICE, required=True )
    grades = ListField(EmbeddedDocumentField(Grade))
    
    meta = {
        'collection': 'students',
        'ordering':['-age']
    }

class TestMongoEngine(object):
    def add_one(self):
        yuwen = Grade(
            name="语文",
            score=90
        )
        shuxue = Grade(
            name="数学",
            score="95"
        )
        stu_obj = Student(
            name="张三",
            age=15,
            sex='male',
            # grades=[yuwen, shuxue]
        )
        stu_obj.remark = 'remark'
        stu_obj.save()
        return stu_obj

    def get_one(self):
        return Student.objects.first()

    def get_more(self):
        return Student.objects.all()

    def get_from_oid(self, oid):
        return Student.objects.filter(pk=oid).first()

    def get_one_get(self):
        """查询一条数据"""
        return Student.objects.get(age=18)

    def update(self):
        """"修改数据"""
        #修改所有女生的年龄
        # return Student.objects.filter(sex='female').update(inc__age=10)
        #修改一条数据
        return Student.objects.filter(sex='male').update_one(inc__age=100)

    def delete(self):
        """删除数据"""
        #删除一条数据
        # return Student.objects.filter(sex='male').first().delete()
        #删除多条数据
        return Student.objects.filter(sex='male').delete()



def main():
    obj = TestMongoEngine()
    # rest = obj.get_more()
    # for item in rest:
    #     print(item.name)
    # rest = obj.get_from_oid('5c318342ed4e3e14f4e30fff')
    # print(rest.name, rest.id,'rest')
    # rest = obj.update()
    # print(rest,'rest')
    rest = obj.delete()

if __name__ =='__main__':
    main()


        