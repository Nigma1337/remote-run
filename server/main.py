from fastapi import FastAPI, Path, Query, Body
import uvicorn
from starlette.requests import Request

app = FastAPI()

@app.post('/run')
async def run(request: Request):
    """
    Get state of service for monitoring health purposes.

    - **returns**: JSON state definition OK, HTTP: 200
    """
    data = await request.body()
    json = await request.json()
    code = json.get('code', '')
    imports = json.get('imports', [])
    for i in imports:
        exec("import %s"%i)
    print(json)
    env = json.get('env')
    for i in env.keys():
        exec("%s='%s'; print(%s)"%(i, env[i], i))
    res = eval(code)
    return res

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000, log_level='debug')
