from flask import Flask,request, jsonify
import pandas as pd
from flask import render_template
from firebase_admin import credentials,firestore,initialize_app
app = Flask(__name__,template_folder="templates")
cred = credentials.Certificate('my-project1-e02f1-firebase-adminsdk-oe3n6-60f3d631b5.json')
default_app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('todos')
file= "C:\\Users\\oso\\PycharmProjects\\WEB\\static\\email.csv"
@app.route("/")
def show_tables():
     email_df=pd.read_csv(file)
     return render_template(
         "display.html",
         tables=[email_df.to_html(classes='ylpss_email')],
         title="email_history"
     )

if __name__ == "__main__":
    app.run(app.run(threaded=True, host='0.0.0.0', port=80)
)