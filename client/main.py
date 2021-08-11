import sys, requests, inspect
class remote():
    def __init__(self, imports, loc, glo):
        loc = {item: loc[item] for item in loc if not inspect.isclass(loc[item]) and not inspect.ismodule(loc[item])}
        del loc["__loader__"]
        for i in loc.keys():
            locals()[i] = loc[i]
        for i in glo.keys():
            globals()[i] = glo[i]
        self.env = [loc, glo]
        self.imports = list(imports)
        self.local = loc
        #print(self.env)
        print(dir())
        for i in imports:
            exec("import %s"%i)
    def run(self, host, code):
        print(self.imports)
        print(self.local)
        requests.post(host, json={"imports": self.imports, "code": code, "env": self.local})
#remote()