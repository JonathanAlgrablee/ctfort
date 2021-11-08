from flask import Flask
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
from flask_mail import Mail, Message
app = Flask(__name__)
mail = Mail(app)


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    
    if request.method == 'POST':
        msg = Message('Hello', sender = 'admincftort@gmail.com', recipients = [request.form.get('email')])
        msg.body = "This is the email body"
        mail.send(msg)

    return render_template("admin.html", user=current_user)