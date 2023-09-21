#!/home/simon/.pyenv/versions/learning-celeri/bin/python
from redis import Redis
r = Redis(host='localhost', port=6379, db=0)
r.set('foo', 'bar')
value = r.get('foo')
print(f"foo = {value}")
