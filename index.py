from flask import Flask, render_template, url_for, request, json, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # request.form['academic_period']
        # request.form['aos_code']
        # request.form['aos_period']
        # request.form['assesment_id']
        # request.form['hand_in_date']
        # request.form['feedback_date']
        # request.form['email']
        # request.form['email_cc']
        # request.form['description']
        # request.form['Batch ID']
        return render_template('index.html', data=request.form['academic_period'])
    else:
        return render_template('index.html')