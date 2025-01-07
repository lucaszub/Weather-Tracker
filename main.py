from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Lucas!"}

@app.get("/message/anothermessage")
def read_message2():
    return {"message": "Holla estoy lucas!"}


@app.get("/lucas/hola")
def read_message2():
    return {"message": "Changement pour test!"}