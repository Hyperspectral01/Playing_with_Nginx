from flask import Flask, render_template, request

from waitress import serve

app=Flask(__name__)

@app.route("/")
def my_thoughts_welcome_message():
    if (request.host=="my_site_1.com"):
        print("My_site_1_has_contacted")
        return render_template("index.html")
    if (request.host=="my_site_2.com"):
        print("My_site_2_has_contacted")
        return render_template("index.html")
    
    return "Nothing found!!!!!!!"

if (__name__=="__main__"):
    serve(app,host="127.0.0.1",port=5005)