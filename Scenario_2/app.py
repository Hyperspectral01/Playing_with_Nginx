from flask import Flask, render_template
from waitress import serve


app=Flask(__name__)

@app.route("/")
def welcome_message():
    return render_template("index.html")


if (__name__=="__main__"):
    serve(app,host="0.0.0.0",port=5000)


#Note, the ip address of your laptop can be found using the ipconfig command on cmd, since it doesnt display the current IP

