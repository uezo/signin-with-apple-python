# signin-with-apple-python
 
A python sample code for Sign in with Apple.


# Configuration

Clone this repository to your environment then configure your service information in `handle_root()` method in `run.py`.

```python
    config = {
        "client_id": "your.service.id",
        "scope": "email",
        "redirect_uri": "https://your.domain/path/to/redirectpage",
        "state": str(uuid4())
    }
```

Configure the path of redirect uri to the `handle_redirect()` method.

```python
@app.route("/path/to/redirectpage", methods=["POST"])
def handle_redirect():
```

If you don't have any service info to configure, register it at Apple Developer.
This website will help you a lot.
https://developer.okta.com/blog/2019/06/04/what-the-heck-is-sign-in-with-apple


# Run the server

Start webserver. Port 5001 is used by default.

```
$ python run.py
```

If you runs the server on your desktop, use ngrok to tunnel the http access from the internet.
This is the sample command to enable to access to your app by `https://yoursubdomain.ngrok.io/`.

```
$ ngrok http 5001 -subdomain=yoursubdomain
```

# Try Sign in with Apple

Access https://your.domain/ and sign in.





