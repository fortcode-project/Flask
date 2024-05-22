from flask import Flask


app=Flask("__main__")
@app.get("/")
def home():
    return {'msg':"ola mundo"}


if __name__=="__main__":
    app.run()