from flask import Flask, render_template, send_from_directory
from flask_compress import Compress

app = Flask(__name__, template_folder='templates', static_folder='static')
Compress(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('details/about.html')

@app.route('/contact')
def contact():
    return render_template('details/contact.html')

@app.route('/terms')
def terms():
    return render_template('details/terms.html')

@app.route('/privacy')
def privacy():
    return render_template('details/privacy.html')

@app.route('/faq')
def faq():
    return render_template('details/faq.html')

@app.route('/guides')
def guides():
    return render_template('details/guides.html')




#ai-code-editors
@app.route('/ai-online-compilers')
def ai_code_editors():
    return render_template('code-editors/index.html')

@app.route('/free-online-ai-python-compiler')
def python():
    return render_template('code-editors/python.html')

@app.route('/free-online-ai-java-compiler')
def java():
    return render_template('code-editors/java.html')

@app.route('/free-online-ai-c-compiler')
def c():
    return render_template('code-editors/c.html')

@app.route('/free-online-ai-cpp-compiler')
def cpp():
    return render_template('code-editors/cpp.html')

@app.route('/free-online-ai-javascript-compiler')
def js():
    return render_template('code-editors/js.html')

@app.route('/free-online-ai-html-editor')
def html():
    return render_template('code-editors/html.html')

@app.route('/free-online-ai-sql-editor')
def sql():
    return render_template('code-editors/sql.html')

@app.route('/free-php-online-ai-compiler')
def php():
    return render_template('code-editors/php.html')

@app.route('/free-online-text-editor')
def text_editor():
    return render_template('code-editors/text-editor.html')

@app.route('/free-online-markdown-editor')
def markdown_editor():
    return render_template('code-editors/markdown-editor.html')



#code-editors
@app.route('/online-compilers')
def online_compilers():
    return render_template('normal-compilers/index.html')

@app.route('/python-compiler')
def opython():
    return render_template('normal-compilers/opython.html')

@app.route('/java-compiler')
def ojava():
    return render_template('normal-compilers/ojava.html')

@app.route('/c-compiler')
def oc():
    return render_template('normal-compilers/oc.html')

@app.route('/cpp-compiler')
def ocpp():
    return render_template('normal-compilers/ocpp.html')

@app.route('/javascript-editor')
def ojs():
    return render_template('normal-compilers/ojs.html')

@app.route('/html-editor')
def ohtml():
    return render_template('normal-compilers/ohtml.html')

@app.route('/sql-editor')
def osql():
    return render_template('normal-compilers/osql.html')

@app.route('/online-text-editor')
def otext_editor():
    return render_template('normal-compilers/otext-editor.html')



#coding-tools
@app.route('/coding-tools')
def coding_tools():
    return render_template('coding-tools/index.html')

@app.route('/free-online-json-formatter')
def json_formatter():
    return render_template('coding-tools/json-formatter.html')

@app.route('/free-online-base64-encoder')
def base64_encoder():
    return render_template('coding-tools/base64-encoder.html')

@app.route('/free-online-css-obfuscator')
def css_obfuscator():
    return render_template('coding-tools/css-obfuscator.html')

@app.route('/css-obfuscator')
def css_obfuscator_short():
    return render_template('coding-tools/css-obfuscator.html')

@app.route('/free-online-text-editor')
def js_obfuscator():
    return render_template('coding-tools/js-obfuscator.html')

@app.route('/free-online-code-diff-tool')
def code_diff_tool():
    return render_template('coding-tools/code-diff-tool.html')

@app.route('/free-online-regex-tester')
def regex_tester():
    return render_template('coding-tools/regex-tester.html')

@app.route('/free-online-xml-beautifier')
def xml_beautifier():
    return render_template('coding-tools/xml-beautifier.html')


#Utility Tools
@app.route('/utility-tools')
def utility_tools():
    return render_template('utility-tools/index.html')

@app.route('/free-online-color-picker')
def cp():
    return render_template('utility-tools/c-p.html')

@app.route('/free-online-favicon-generator')
def favicon_generator():
    return render_template('utility-tools/favicon-maker.html')

@app.route('/free-online-qr-code-scanner')
def qr_code_scanner():
    return render_template('utility-tools/qr-scanner.html')

@app.route('/convert-qr-to-url-online')
def qr_to_url():
    return render_template('utility-tools/qr-to-url-code-generator.html')

@app.route('/free-online-url-encoder-decoder')
def url_encoder_decoder():
    return render_template('utility-tools/url-encoder-decoder.html')

@app.route('/convert-url-to-qr-code-online')
def url_to_qr():
    return render_template('utility-tools/url-to-qr-code-generator.html')

@app.route('/temp-mail')
def temp_mail():
    return render_template('utility-tools/temp-mail-generator.html')



#error handlers
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
