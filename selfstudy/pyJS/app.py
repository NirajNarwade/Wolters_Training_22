from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///rockpaperscissor.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class RockPaperScissor(db.Model):
    name = db.Column(db.String(200), primary_key=True)
    score = db.Column(db.Integer , nullable = False)

    def __repr__(self) -> str:
        return f"{self.name} --> {self.score}"  

@app.route('/')
def hello_world():
    # return 'Hello, World!'
    return render_template('game.html')

if __name__== "__main__":
    app.run(debug=True)