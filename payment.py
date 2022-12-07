from flask import Flask
app = Flask (_name_)

def calculate (a, b):
    c = a+b
    return c

@app.route ("/")
def index ():

    return "This is a payment page! Please pay %s USD"%(calculate(10, 20))

if _name_ == "_main_":
    app.run(host="127.0.0.1", port=8080, debug=True)