from flask import Flask


app=Flask("__main__")
@app.get("/")
def home():
    return {'msg':"ola mundo"}

@app.get("/users")
def usuarios():
    users=["Achelton","Paulo","Alberto","Antonio"]
    return {"users":users}


if __name__=="__main__":
    app.run()