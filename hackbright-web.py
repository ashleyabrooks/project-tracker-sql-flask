from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    projects = hackbright.get_grades_by_github(github)
    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           projects=projects)

    return html


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/add-student")
def add_student():
    """Add a student."""

    return render_template("create_new_student.html")


@app.route("/new-student-success", methods=["POST"])
def new_student_success():
    """Return success message after user adds new student."""


    fname = request.form.get("fname")
    lname = request.form.get("lname")
    github = request.form.get("github")

    hackbright.make_new_student(fname, lname, github)

    return render_template("new_student_confirmation.html",
                           fname=fname,
                           lname=lname,
                           github=github)


@app.route("/project")
def see_project():
    """Display information about a student project."""

    title = request.args.get("title")
    project_info = hackbright.get_project_by_title(title)

    return render_template("display_project.html", project_info=project_info)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
