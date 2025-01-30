from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the CSV data into a Pandas DataFrame
df = pd.read_csv("student_data.csv")

# changing/set the path
@app.route("/yosh/ind", methods=["GET", "POST"])
def index():
    student_details = None
    if request.method == "POST":
        student_id = request.form.get("student_id")
        if student_id and student_id.isdigit():
            # Find the student details by StudentID
            student_details = df[df["StudentID"] == int(student_id)].to_dict(orient="records")
            if not student_details:
                student_details = "Student ID not found."
    
    return render_template("index.html", student_details=student_details)

# changing/set the path and redirecting it (blog) that website and also changing/replacing the variables
@app.route("/blog")
def home():
    return render_template("blog.html", name = 'yosh', popular_posts = ['gucci', 'LV', 'Pepe'])

if __name__ == "__main__":
    app.run(debug=True)
