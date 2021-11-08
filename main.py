from website import create_app
from flask_mail import Mail, Message

app = create_app()
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ortctf@gmail.com'
app.config['MAIL_PASSWORD'] = 'alushalgrablee'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

if __name__ == '__main__':
    app.run(debug=True)
