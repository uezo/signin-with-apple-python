import json
from urllib.parse import parse_qs
import base64
from uuid import uuid4
from flask import (
    Flask,
    request,
    render_template
)


def extract_post_data(post_data):
    params = parse_qs(post_data.decode("utf-8"))
    # decode id_token
    encoded = params["id_token"][0].split(".")[1]
    id_token = base64.urlsafe_b64decode(encoded + "=" * (-len(encoded) % 4))
    # return values as dict
    return {
        "state": params["state"][0],
        "code": params["code"][0],
        "id_token": json.loads(id_token)
    }

app = Flask(__name__)


@app.route("/")
def handle_root():
    config = {
        "client_id": "your.service.id",
        "scope": "email",
        "redirect_uri": "https://your.domain/path/to/redirectpage",
        "state": str(uuid4())
    }
    return render_template("index.html", config=config)


@app.route("/path/to/redirectpage", methods=["POST"])
def handle_redirect():
    raw_data = request.get_data()
    values = extract_post_data(raw_data)
    return render_template("result.html", values=values, raw_data=raw_data, headers=request.headers)

if __name__ == "__main__":
    app.run(port=5001)
