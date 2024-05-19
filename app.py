# from flask import Flask, render_template, session, redirect, url_for

# app = Flask(__name__)
# app.secret_key = '!nimish'  # Required for session management

# @app.route('/')
# def index():
#     # Reset or initialize the session number
#     session['number'] = 0
#     return render_template('index.html')

# @app.route('/next-number')
# def next_number():
#     # Increment the number stored in the session
#     if 'number' in session:
#         session['number'] += 1
#     else:
#         session['number'] = 1
#     return str(session['number'])

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, session, request, Response
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/numbers')
def numbers():
    def generate_numbers():
        for number in range(1, 101):  # Generate numbers from 1 to 100
            time.sleep(1)  # Delay to simulate real-time update
            yield f"data:{number}\n\n"
    return Response(generate_numbers(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
