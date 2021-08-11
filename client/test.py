from main import remote
import sys

a="b"
#print(locals())
r = remote(sys.modules.keys(), locals(), globals())
r.run("http://0.0.0.0:8000/run", "a")
