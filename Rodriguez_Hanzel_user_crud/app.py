from flask import Flask, render_template, request, redirect
from user import User

app = Flask(__name__)


@app.route("/")
@app.route("/user")
def read_all():
    users = User.find_all()
    return render_template("read_all.html", users=users)


@app.get("/user/new")
def new_user():
    return render_template("read_all.html")


@app.post("/user/create")
def create_user():
    print(request.form)
    user_id = User.create(request.form)
    print("This is the new Users id:" + str(user_id))
    return redirect("/user")


@app.get("/user/<int:user_id>")
def user_details(user_id):
    user = User.find_by_id(user_id)
    if user == None:
        return " Cannot find User"
    return render_template("user_details.html", user=user)


if __name__ == "__main__":
    app.run(debug=True)
