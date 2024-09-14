from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask('Town')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Town(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    town = db.Column(db.String(300))
    visit_date = db.Column(db.String(20))

    def __repr__(self):
        return f'<Town {self.id} / {self.visit_date}> {self.town}'


@app.route('/')
def main():
    towns = Town.query.all()
    print(towns)
    return render_template('index.html', towns_list=towns)


@app.route('/town', methods=['POST'])
def add_town():
    data = request.json
    town = Town(**data)
    db.session.add(town)
    db.session.commit()

    # id_last = products[-1]['id']
    # id_new = id_last + 1
    # data['id'] = id_new
    # products.append(data)
    return 'OK'



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)