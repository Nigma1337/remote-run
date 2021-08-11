## Remote run

This is a small python library, consisting of a server and client part. The server inherits your python env, from when originally called

#### Usage example:

```
from main import remote

a="b"
r = remote(sys.modules.keys(), locals(), globals())
r.run("http://0.0.0.0:8000/run", "a")
```
Server will return "b" here, as it evaluates "a".


#### TODO:
1. Find a way to inherit classes properly
2. Publish as pypi package