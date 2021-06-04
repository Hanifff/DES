from flask import Flask, request
import time
import json
from part2_3des import *
from part2_des import *
from part2_helpers import *

app = Flask(__name__)

keys = {
    "k1":"1000101110",
    "k2": "0110101110"
}

@app.route("/decrypting")
def decrypting():
    ct  = request.args.get('cipher', None)
    if ct:
        k1 = keys["k1"]
        k2 = keys["k2"]
        in_bites = des3_decryption(k1,k2, ct)
        return in_bites
    return ""


@app.route("/")
def index():
    return app.send_static_file("loading.html")


if __name__ == "__main__":
    app.run()
