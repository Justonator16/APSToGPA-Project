from flask import Flask, flash, redirect, render_template, request, session
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash
from aps_and_gpa_calculators import APSLevel , GradeToLetter, GradeToGpaScale

app = Flask(__name__)
app.secret_key = 'APSToGPA'


db = SQL("sqlite:///apstogpa.db")

@app.route("/")
def index():
        return render_template("index.html")

@app.route("/signup", methods=["GET","POST"])
def signup():
    """ Create a new account for a user """
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        """ Check if new user is not registering using an existing account """
        users = db.execute("SELECT * FROM users")
        for user in users:
             if username == user['username']:
                  flash("Username exists")
                  return render_template("signup.html")

        """ Flash error messages. User input form """
        if not request.form.get("username"):
             flash("Enter username")
             return render_template("signup.html")
        elif not request.form.get("password"):
             flash("Enter password")
             return render_template("signup.html")
        elif not request.form.get("confirmation"):
            flash("Enter password again for confirmation")
            return render_template("signup.html")
        elif password != confirmation:
             flash("Passwords do not match")
             return render_template("signup.html")
        else:
             db.execute("INSERT INTO users (username, hash_password) VALUES (?,?)", username, generate_password_hash(password))

             flash("Account created successfully")
             return render_template("login.html")
    else:
        return render_template("signup.html")

@app.route("/login", methods=["GET","POST"])
def login():
     """ Forgets an user logged in """
     session.clear()

     if request.method == 'POST':
          username = request.form.get("username")
          password = request.form.get("password")


          """ Check if user exists in database """
          users = db.execute("SELECT username, hash_password FROM users")
          for user in users:
               if username != user['username']:
                    flash("User does not exist")
                    return render_template("login.html")
               elif not check_password_hash(user['hash_password'] ,password):
                    flash("Invalid password")
                    return render_template("login.html")

          if not username or not password:
               flash("Enter username/password")
               return render_template("login.html")

          """ Update current_user table , with username value in user_logged_in so that it remembers """
          db.execute("UPDATE current_user set user_logged_in = ?", username)

          flash(f"Welcome {username}")
          return render_template("home.html")
     else:
          return render_template("login.html")

@app.route("/logout")
def logout():
     """ Forgets an user logged in """
     session.clear()

     return redirect("/")

@app.route("/home")
def home():
     return render_template("home.html")

@app.route("/aps", methods=['GET','POST'])
def aps_level_calculator():
     """ Calculates the APS level for a specific subject. """
     return render_template("aps.html")

@app.route("/aps_score", methods=['GET','POST'])
def aps_score_calculator():
     """Calculates the APS Score for a set of subjects."""
     if request.method == "POST":
          """ Get name of report """
          report_name = request.form.get("transcript")

          """ get the user logged in information from current_user table """
          current_user = db.execute("SELECT user_logged_in FROM current_user")
          user_id = db.execute("SELECT id FROM users WHERE username = ?", current_user[0]["user_logged_in"])

          """ Get all reports and their names based on the user logged in """
          report_names = db.execute("SELECT DISTINCT(report_name) FROM user_reports WHERE user_id = ?", user_id[0]["id"])

          """ Insert all subjects and grades in user_reports table in apstogpa database """
          if not report_name:
               """ By default if there is no name provided to the latest subjects and grades there should be N/A """
               report_name = "N/A"

               subject1 = request.form.get("subject1")
               grade1 = request.form.get("grade1")
               db.execute("INSERT INTO user_reports (user_id ,report_name ,subject ,grade) VALUES (?,?,?,?)", user_id[0]["id"] , report_name, subject1, grade1)

               subject2 = request.form.get("subject2")
               grade2 = request.form.get("grade2")
               db.execute("INSERT INTO user_reports (user_id ,report_name ,subject ,grade) VALUES (?,?,?,?)", user_id[0]["id"] , report_name, subject2, grade2)

               subject3 = request.form.get("subject3")
               grade3 = request.form.get("grade3")
               db.execute("INSERT INTO user_reports (user_id ,report_name ,subject ,grade) VALUES (?,?,?,?)", user_id[0]["id"] , report_name, subject3, grade3)

               subject4 = request.form.get("subject4")
               grade4 = request.form.get("grade4")
               db.execute("INSERT INTO user_reports (user_id ,report_name ,subject ,grade) VALUES (?,?,?,?)", user_id[0]["id"] , report_name, subject4, grade4)

               subject5 = request.form.get("subject5")
               grade5 = request.form.get("grade5")
               db.execute("INSERT INTO user_reports (user_id ,report_name ,subject ,grade) VALUES (?,?,?,?)", user_id[0]["id"] , report_name, subject5, grade5)

               subject6 = request.form.get("subject6")
               grade6 = request.form.get("grade6")
               db.execute("INSERT INTO user_reports (user_id ,report_name ,subject ,grade) VALUES (?,?,?,?)", user_id[0]["id"] , report_name, subject6, grade6)

               subject7 = request.form.get("subject7")
               grade7 = request.form.get("grade7")
               db.execute("INSERT INTO user_reports (user_id ,report_name ,subject ,grade) VALUES (?,?,?,?)", user_id[0]["id"] , report_name, subject7, grade7)
          else:
               report_name = request.form.get("transcript")

               """ Check that the user does not use the same name for many reports, since this would result in an error. """
               if report_name in [ name['report_name'] for name in report_names ]:
                    flash("A report with the same name already exists for another record.")
                    return render_template("aps_score.html")

               """ Update default report name with the report name provided by the user  """
               if report_name :
                    db.execute("UPDATE user_reports set report_name = ? WHERE user_id = (SELECT id FROM users WHERE username = (SELECT * FROM current_user)) ORDER BY report_id DESC LIMIT 7" , report_name)
                    flash(f"Report name {report_name} saved")
                    return render_template("transcript.html")

          return render_template("aps_score.html")
     else:
          return render_template("aps_score.html")


@app.route("/transcript", methods=['GET','POST'])
def transcripts():
          """ User logged in id """
          username_logged_in = db.execute("SELECT * FROM current_user")

          user_id = db.execute("SELECT id FROM users WHERE username = ?", username_logged_in[0]["user_logged_in"])

          """ Get all reports and their names based on the user logged in """
          report_names = db.execute("SELECT DISTINCT(report_name) FROM user_reports WHERE user_id = ?", user_id[0]["id"])

          """ Remove all reports with name N/A from list """
          names_list = [ name['report_name'] for name in report_names ]
          names_list.remove('N/A')

          if request.method == "POST":
               """ Diplays full academic record of all 7 subjects and grades with thier GPA's and APS score"""
               selected_report_name = request.form.get("selected_report_name")

               if not selected_report_name:
                    flash("Select a report name")
                    return render_template("transcript_default.html", names_list=names_list)

               """ Find the full transcript name in database  """
               transcript_name = "".join([selected_report_name, "%"])

               user_report = db.execute("SELECT report_name, subject, grade FROM user_reports WHERE user_id = ? AND report_name LIKE ?", user_id[0]["id"], transcript_name)

               """ Retrieve the complete `report_name` from the database, which will serve as the heading for the report. """
               full_report_name = db.execute("SELECT report_name FROM user_reports WHERE user_id = ? AND report_name LIKE ? LIMIT 1", user_id[0]["id"], transcript_name)

               grades = [row["grade"] for row in user_report]

               """ Grade converted to Aps level and gpa wieghting """
               apslevels = [ APSLevel(grade) for grade in grades ]
               letter_grades = [ GradeToLetter(grade) for grade in grades]
               gpa_scale_grades = [ GradeToGpaScale(grade) for grade in grades ]

               """ Aps score and gpa  """
               aps_score = sum(apslevels)
               gpa_score = round(sum(gpa_scale_grades) / len(gpa_scale_grades), 1)

               return render_template("transcript.html", names_list=names_list ,user_report=user_report ,apslevels=apslevels ,letter_grades=letter_grades ,gpa_scale_grades=gpa_scale_grades ,aps_score=aps_score ,gpa_score=gpa_score, full_report_name=full_report_name)
          else:
               return render_template("transcript_default.html", names_list=names_list)



