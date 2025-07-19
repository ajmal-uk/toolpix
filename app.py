from flask import Flask, render_template, request, send_from_directory
from flask_compress import Compress

app = Flask(__name__, template_folder='templates', static_folder='static')
Compress(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')



@app.route('/python-compiler')
def python():
    return render_template('python.html')

@app.route('/java-compiler', methods=['GET', 'POST'])
def java():
    initial_code = None
    if request.method == 'POST':
        # Retrieve initial code from POST form data
        initial_code = request.form.get('initialCode')
    elif request.method == 'GET':
        # Optionally, still support GET for backward compatibility or direct access
        initial_code = request.args.get('initialCode')
    # Render the template, passing the initial code (None if not provided)
    return render_template('java.html', initial_code=initial_code)

@app.route('/c-compiler')
def c():
    return render_template('c.html')

@app.route('/cpp-compiler')
def cpp():
    return render_template('cpp.html')

@app.route('/javascript-editor')
def js():
    return render_template('js.html')

@app.route('/html-editor')
def html():
    return render_template('html.html')

@app.route('/sql-editor')
def sql():
    return render_template('sql.html')



@app.route('/json-formatter')
def json_formatter():
    return render_template('json-formatter.html')

@app.route('/base64-encoder')
def base64_encoder():
    return render_template('base64-encoder.html')

@app.route('/css-obfuscator')
def css_obfuscator():
    return render_template('css-obfuscator.html')

@app.route('/javascript-obfuscator')
def js_obfuscator():
    return render_template('js-obfuscator.html')

@app.route('/online-text-editor')
def text_editor():
    return render_template('text-editor.html')




@app.errorhandler(400)
def bad_request(error):
    return render_template('errors/400.html', title='400 Bad Request'), 400

@app.errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html', title='403 Forbidden'), 403

@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html', title='404 Not Found'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html', title='500 Internal Server Error'), 500





@app.route('/google83f8616f6a5b1974.html')
def google_verification():
    return send_from_directory('assets', 'google83f8616f6a5b1974.html')

@app.route('/robots.txt')
def robots():
    return send_from_directory('assets', 'robots.txt')

@app.route('/ads.txt')
def ads():
    return send_from_directory('assets', 'ads.txt')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('assets', 'sitemap.xml')

@app.route('/logo.png')
def logo():
    return send_from_directory('assets', 'logo.png')

@app.route('/og-image.jpg')
def og_image():
    return send_from_directory('assets', 'og-image.jpg')

@app.route('/twitter-image.jpg')
def twitter_image():
    return send_from_directory('assets', 'twitter-image.jpg')




@app.route('/favicon.ico')
def favicon_ico():
    return send_from_directory('assets/favicon', 'favicon.ico')

@app.route('/favicon.svg')
def favicon_svg():
    return send_from_directory('assets/favicon', 'favicon.svg')

@app.route('/favicon-32x32.png')
def favicon_32():
    return send_from_directory('assets/favicon', 'favicon-32x32.png')

@app.route('/favicon-16x16.png')
def favicon_16():
    return send_from_directory('assets/favicon', 'favicon-16x16.png')

@app.route('/favicon-96x96.png')
def favicon_96():
    return send_from_directory('assets/favicon', 'favicon-96x96.png')

@app.route('/web-app-manifest-192x192.png')
def web_app_manifest_192():
    return send_from_directory('assets/favicon', 'web-app-manifest-192x192.png')

@app.route('/web-app-manifest-512x512.png')
def web_app_manifest_512():
    return send_from_directory('assets/favicon', 'web-app-manifest-512x512.png')

@app.route('/apple-touch-icon.png')
def apple_icon():
    return send_from_directory('assets/favicon', 'apple-touch-icon.png')

@app.route('/site.webmanifest')
def webmanifest():
    return send_from_directory('assets/favicon', 'site.webmanifest')


if __name__ == '__main__':
    app.run(debug=False, threaded=True, host='0.0.0.0', port=5000)
