# This is going to be a simple dev server, hence
# No Waitres
# Inbound rules : 127.0.0.1


from flask import Flask, render_template
#render_template is a function that takes the path of the file as input and helps fetch the file and give it as a response
#Flask is a class that helps you to make an instance of the Class that does everything like listening to the port and so on


app=Flask(__name__)

@app.route("/") # @ specifies the endpoint
def welcome():  #specifies the function to run whenever we hit the endpoint
    print(type(render_template("index.html")))
    print(render_template("index.html"))
    # return x
    return render_template("index.html")  #By default, render_template or even Flask organises things in templates/,  and static/ and so on.
                                            # Hence this by default works by looking at the templates folder, hence the name of the function
                                            # WORKS WITH SOMETHING CALLED THE JINJA ENGINE

    return
if (__name__=="__main__"): #So that this only runs directly and not as an imported class in some other code file
    app.run(host="127.0.0.1",port=5000,debug=True) # This is for debug mode and AutoReload





