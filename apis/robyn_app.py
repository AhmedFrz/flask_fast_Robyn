from robyn import Robyn

app = Robyn(__name__)

app.get("/")
def hello():
    return "hi this is a Robyn test"

app.start(port=8080)
