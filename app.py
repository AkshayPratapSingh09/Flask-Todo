from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    srno = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200),nullable=False)
    desc = db.Column(db.String(500),nullable=False)
    data_created = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.srno} - {self.title}"
# db.init_app(app)

# with app.app_context():
#     db.create_all()

@app.route('/update/<int:srno>', methods=["GET", "POST"])
def update(srno):
    if request.method=="POST":
        # print("Post")
        title = request.form['title']
        desc = request.form["desc"]
        todo = Todo.query.filter_by(srno=srno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    
    todo = Todo.query.filter_by(srno=srno).first()
    return render_template("update.html", todo=todo)


@app.route('/', methods=["GET", "POST"])
def Products():
    if request.method=="POST":
        # print("Post")
        title = request.form['title']
        desc = request.form["desc"]
        todo = Todo(title=title,desc =desc)
        db.session.add(todo)
        db.session.commit()
    alltodo = Todo.query.all()
    print(alltodo)
    return render_template("index.html", alltodo=alltodo)

@app.route('/delete/<int:srno>')
def delete(srno):
    todo = Todo.query.filter_by(srno=srno).first()
    # todo = db.select(Todo).filter_by(srno=srno).one()
    # print(todo)
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")
    # user = db.session.execute(db.select(User).filter_by(username=username)).one()

if __name__ =="__main__":
    app.run(debug=True)