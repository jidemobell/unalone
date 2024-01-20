from src.package_unalone import app


@app.route('/')
def index():
    return "<h1> Hello World </h1>"
