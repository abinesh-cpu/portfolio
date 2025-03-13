from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message

app = Flask(__name__)

# Secret key for flash messages
app.secret_key = 'supersecretkey'

# Flask-Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Use Gmail's SMTP server
app.config['MAIL_PORT'] = 587  # TLS Port
app.config['MAIL_USE_TLS'] = True  # Enable TLS
app.config['MAIL_USE_SSL'] = False  # No SSL needed
app.config['MAIL_USERNAME'] = 'abineshabi0487@gmail.com'  # Replace with your Gmail account
app.config['MAIL_PASSWORD'] = 'zyil aman degx pgxe'  # Replace with your Gmail password
app.config['MAIL_DEFAULT_SENDER'] = 'abineshabi0487@gmail.com'  # Replace with your email

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        
        # Create the email message
        msg = Message(
            subject=subject,
            recipients=['abineshrl476@gmail.com'],  # Replace with the recipient's email address
            body=f"Subject: {subject}\nName: {name}\nEmail: {email}\nMessage: {message}"
        )
        
        try:
            # Send the email
            mail.send(msg)
            flash('Message sent successfully! I will contact you as soon as possible.', 'success')
        except Exception as e:
            flash(f'Error sending message: {e}', 'danger')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
