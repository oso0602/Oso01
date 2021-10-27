from flask import Flask
import pandas as pd
from flask import render_template
app = Flask(__name__,template_folder="templates")

file= "C:\\Users\\oso\\PycharmProjects\\WEB\\static\\email.csv"
@app.route("/")
def show_tables():
     email_df=pd.read_csv(file)
     return render_template("display.html",tables=[email_df.to_html(classes='ylpss_email')], titles=("ylpss_email"))

if __name__ == "__main__":
    app.run(debug=True)