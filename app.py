from flask import Flask, render_template, request
from flask_mail import Mail, Message
app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'gopalnarayanantn@gmail.com'
app.config['MAIL_PASSWORD'] = '*******password******'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send', methods=['POST'])
def send():
    gname = request.form.get('guest_name')
    gmail = request.form.get('guest_mail_id')
    gmsg = request.form.get('feedback_msg')
    msg = Message(
        gname,
        sender=gmail,
        recipients=['gopalnarayanantn@gmail.com']
    )
    msg.body = gmsg + '\n\n' + gname+'\n' + gmail
    mail.send(msg)
    return render_template('success.html')


@app.route('/send', methods=['GET'])
def errormsg():
    return "<center><h1> 404 </h1></center>"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
