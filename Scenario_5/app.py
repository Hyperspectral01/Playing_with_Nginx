from flask import Flask, render_template, request
from waitress import serve

app=Flask(__name__)


@app.route("/")
def welcome():
    if (request.host=="my_site_1.com"):
        print("Server-1")
        return render_template("index.html")
    if (request.host=="my_site_2.com"):
        print("Server-2")
        return render_template("index.html")

    return "Nothing to show here!!!"


if (__name__=="__main__"):
    serve(app,host="127.0.0.1",port=5006)


