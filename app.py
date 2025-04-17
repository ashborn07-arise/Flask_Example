from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def home():
   return render_template("Home.html")

@app.route("/abt")
def about():
   return "Its about us"

@app.route("/count")
def contact():
   return "Contact us"

if __name__ =='__main__':
   app.run(debug=True)
