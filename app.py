from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///shop.db'
app.config['SQLAKCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Item (db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    price=db.Column(db.Integer,nullable=False)
    isAktiv=db.Column(db.Boolean,default=True)

    def __repr__(self):
        return self.title

@app.route('/')
def index():
    items=Item.query.order_by(Item.price).all()
    return render_template('index.html',data=items)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/create', methods=['POST','GET'])
def create():

    if request.method == 'POST':

        title = request.form['title']
        price = request.form['price']

        item = Item(title=title,price=price)

        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except:
            return "Произошла ошибка"

    else:
        return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True)





