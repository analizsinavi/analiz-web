from flask import Flask, render_template
from datetime import datetime
import data

app = Flask(__name__)


@app.errorhandler(403)
def forbidden(e):
    return render_template("error/error-403.html")


@app.errorhandler(404)
def notfound(e):
    return render_template("error/error-404.html")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/iletisim")
def iletisim():
    return render_template("iletisim.html")


@app.route("/hakkimizda")
def hakkimizda():
    return render_template("hakkimizda.html")


@app.route("/bayiler")
def bayiler():
    bayiler = data.fetch_bayiler()
    return render_template("bayiler.html", bayiler=bayiler)


@app.route("/urunler")
def urunler():
    urunler = data.fetch_urunler()
    return render_template("urunler.html", urunler=urunler)


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
