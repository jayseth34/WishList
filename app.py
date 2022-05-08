from flask import *
from forms import AddForm,DelForm,AddOwnerForm
from flask_wtf.csrf import CSRFProtect, CSRFError
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
basedir=os.path.abspath(os.path.dirname(__file__))
app=Flask(__name__)
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = 'mykey'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'datasqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db=SQLAlchemy(app)
Migrate(app,db)


class Wish(db.Model):

    __tablename__='wishes'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    owner=db.relationship('Owner',backref='wish',uselist=False)

    def __init__(self,name):
        self.name=name

    def __repr__(self):
        if self.owner:
            return f"Your wishlist: {self.name} and the name of the person with whom: {self.owner.name} "
        else:
            return f"Your wishlist: {self.name} and no partner chosen yet"

class Owner(db.Model):
    __tablename__='owners'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    wish_id=db.Column(db.Integer,db.ForeignKey('wishes.id'))

    def __init__(self,name,wish_id):
        self.name=name 
        self.wish_id=wish_id

    def __repr__(self):
        return 'The person with: {self.name}'

#VIEW FUNCT
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add_owner',methods=['GET','POST'])
def add_owner():
    form=AddOwnerForm()
    name=form.name.data
    if form.validate_on_submit():
        name=form.name.data
        wish_id=form.wished_id.data
        new_owner=Owner(name,wish_id)
        db.session.add(new_owner)
        db.session.commit()
        return redirect(url_for('list'))
    return render_template('add_owner.html',form=form)

@app.route('/add',methods=['GET','POST'])
def add():
    form=AddForm()
    if form.validate_on_submit():
        name=form.name.data
        new_own=Wish(name)
        db.session.add(new_own)
        db.session.commit()
        return redirect(url_for('list'))
    return render_template('add.html',form=form)

@app.route('/list')
def list():
    wishes=Wish.query.all()
    return render_template('list.html',wishes=wishes)

@app.route('/delete',methods=['GET','POST'])
def delete():
    form=DelForm()
    if form.validate_on_submit():
        id=form.id.data
        del_wish=Wish.query.get(id)
        db.session.delete(del_wish)
        db.session.commit()
        return redirect(url_for('list'))
    return render_template('delete.html',form=form)


if __name__=='__main__':
    app.run(debug=True)