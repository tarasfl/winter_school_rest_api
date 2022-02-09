
from crypt import methods
from main import app

@app.route('/')
def index():
    return "Nascho"


@app.route('/fish', methods=["GET"])
def fish_c():
    return "FISH"

@app.route('/fish', methods=["POST"])
def fish_insertion():
    return "You added a fish, good job, go on, you are the best"