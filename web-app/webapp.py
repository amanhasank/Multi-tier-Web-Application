import logging
from fluent import handler
from flask import Flask, render_template, request

app = Flask(__name__)

# Configure Fluentd logging
fluentd_handler = handler.FluentHandler('app', host='localhost', port=24224)
fluentd_handler.setFormatter(logging.Formatter('%(name)s: %(levelname)s %(message)s'))
app.logger.addHandler(fluentd_handler)

# Set the logging level for the Flask app
app.logger.setLevel(logging.INFO)

@app.before_request
def before_request():
    if request.headers.get('X-Forwarded-Proto') == 'http':
        request.url = request.url.replace('http://', 'https://', 1)

    # Log the request information
    app.logger.info('Request received', extra={'path': request.path, 'method': request.method})

@app.route('/')
def home():
    # Log information about the home route access
    app.logger.info('Home page accessed')
    return render_template('home.html')

@app.route('/about')
def contact():
    # Log information about the about route access
    app.logger.info('About page accessed')
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

