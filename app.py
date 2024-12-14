from flask import Flask, render_template
import data
import locale
import json

# Set locale to Turkish
locale.setlocale(locale.LC_TIME, 'tr_TR.UTF-8')  # 'tr_TR.UTF-8' for Linux/MacOS, 'Turkish_Turkey.1254' for Windows

app = Flask(__name__)


@app.template_filter('format_turkish_date')
def format_turkish_date(value):
    return value.strftime('%d %B %Y')  # Turkish format


@app.errorhandler(403)
def forbidden(e):
    return render_template("error/error-403.html")


@app.errorhandler(404)
def notfound(e):
    return render_template("error/error-404.html")


@app.route("/")
def home():
    slidelar = data.fetch_slidelar()
    urunler_yeni = data.fetch_urunler_yeni()
    urunler_populer = data.fetch_urunler_populer()
    duyurular_yeni = data.fetch_duyurular_yeni()
    return render_template(
        "index.html",
        slidelar=slidelar,
        urunler_yeni=urunler_yeni,
        urunler_populer=urunler_populer,
        duyurular_yeni=duyurular_yeni
    )


@app.route("/iletisim")
def iletisim():
    return render_template("iletisim.html")


@app.route("/hakkimizda")
def hakkimizda():
    return render_template("hakkimizda.html")


@app.route("/bayiler")
def bayiler():
    bayiler = data.fetch_bayiler()
    return render_template(
        "bayiler.html",
        data=json.dumps({"bayiler": bayiler})
    )


@app.route("/urunler")
def urunler():
    urunler = data.fetch_urunler()
    siniflar = data.fetch_siniflar()
    branslar = data.fetch_branslar()
    kategoriler = data.fetch_kategoriler()
    return render_template(
        "urunler.html",
        data=json.dumps({
            "urunler": urunler,
            "siniflar": siniflar,
            "branslar": branslar,
            "kategoriler": kategoriler
        })
    )


@app.route("/duyurular")
def duyurular():
    duyurular = data.fetch_duyurular()
    return render_template("duyurular.html", duyurular=duyurular)


@app.route("/e-kitap")
def ekitap():
    return render_template("ekitap.html")


@app.route('/sitemap.xml')
def seo_sitemap():
    # articles = sorted(flatpages, key=lambda item:item.meta['published'], reverse=False)
    # return render_template('sitemap.xml', articles=articles, base_url="https://buildstaticwebsites.com")
    return render_template('sitemap.xml', base_url="https://buildstaticwebsites.com")


@app.route('/robots.txt')
def seo_robots():
    return render_template('robots.txt')


@app.route('/manifest.json')
def seo_manifest():
    return render_template('manifest.json')
