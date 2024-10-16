import redis
import random

redis_conn = redis.Redis(host='10.131.38.133', port=6379, db=0)

alphabet = '0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()-+=.'
values = random.sample(alphabet,30)
value = ''.join(values)*100000

for i in range(1,1500):
    num = random.randint(1,30)
    keys = random.sample(alphabet,num)
    key = ''.join(keys)
    #values = random.sample(alphabet,num)
    #value = ''.join(values)
    #print(key,value)

    redis_conn.setex(key,60000,value)
