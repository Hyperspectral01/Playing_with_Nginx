from flask import Flask, render_template
from waitress import serve

## REMEMBER THIS IS A NORMAL CASE OF NGINX - DEFAULT LISTENS ON 0.0.0.0 , YOU CAN HIT ON A PORT, AND MENTION PROXY PASSES ACCORDING TO THE ENDPOINTS
## THIS IS GOING TO BE A CASE WHERE DOMAIN NAMES ARE NOT USED YET, SO FOR LOCAL DEV IT CAN BE SET AS LOCALHOST AS SERVER_NAME IN NGINX CONF FILE
## OR IT CAN BE SET AS _, TO MATCH ALL THE DOMAIN NAMES AND ALLOW EVERYTHING



# Strange behaviour, when server_name localhost is applied and the port 80 is hit, it shouldnt be allowing to access the site from my phone, but it does allow, meaning it falls back to default server block for that port

app=Flask(__name__)

@app.route("/")
def welcome_message_from_prod_server():
    print("The endpoint welcome message on the Prod Server has been hit.")

    return render_template("index.html")


serve(app,host="127.0.0.1",port=5001)