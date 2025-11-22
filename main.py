from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def index():
    return {'message':'asosiy bolim'}

@app.get("/about")
def abuot():
    return {'message':'abuot page'}

@app.get("/contact")
def contact():
    return {'message':'contact page'}

@app.get("/me")
def me():
    return {'message':'bu mening shaxsiy sahifam'}

@app.get("/student/{ism}")
def salom(ism :str):
    return {'message':f"salom {ism}" }

@app.get("/qidir")
def qidir(s):
    return {'message': f"siz {s}ni qidirib topdingiz"}