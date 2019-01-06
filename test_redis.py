import redis
# r = redis.Redis(host='localhost',port=6379, db=0)能兼容老版本
r = redis.StrictRedis(host='localhost', port=6379, db=0)

user1=r.get('user1')
print(user1)