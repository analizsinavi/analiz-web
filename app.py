from flask import Flask, render_template, abort, url_for, Response
from datetime import datetime
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


@app.route('/sitemap.xml')
def seo_sitemap():
    base_url = "https://buildstaticwebsites.com"
    urls = []

    # Static pages
    static_urls = [
        ('/', 'daily'),
        ('/iletisim', 'monthly'),
        ('/hakkimizda', 'monthly'),
        ('/bayiler', 'monthly'),
        ('/urunler', 'daily'),
        ('/e-kitap', 'monthly'),
        ('/gizlilik-sozlesmesi', 'yearly'),
        ('/cerez-politikasi', 'yearly'),
        ('/kullanim-sartlari', 'yearly')
    ]
    for url, changefreq in static_urls:
        urls.append((url, datetime.now().strftime('%Y-%m-%d'), changefreq))

    # Dynamic pages
    urunler = data.fetch_urunler()
    for urun in urunler:
        urls.append((url_for('urunler_detay', urunId=urun['UrunId']), datetime.now().strftime('%Y-%m-%d'), 'weekly'))

    duyurular = data.fetch_duyurular()
    for duyuru in duyurular:
        urls.append(
            (url_for('duyurular_detay', duyuruId=duyuru['DuyuruId']), datetime.now().strftime('%Y-%m-%d'), 'weekly'))

    sitemap_xml = render_template('sitemap.xml', base_url=base_url, urls=urls)
    return Response(sitemap_xml, mimetype='application/xml')


@app.route('/robots.txt')
def seo_robots():
    robots_txt = render_template('robots.txt')
    return Response(robots_txt, mimetype='text/plain')


@app.route('/manifest.json')
def seo_manifest():
    manifest_json = render_template('manifest.json')
    return Response(manifest_json, mimetype='application/json')


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
    return Response(render_template("iletisim.html"), mimetype='text/html')


@app.route("/hakkimizda")
def hakkimizda():
    return Response(render_template("hakkimizda.html"), mimetype='text/html')


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


@app.route("/urun/<urunId>")
def urunler_detay(urunId):
    urun = data.fetch_urun(urunId)

    if not urun:
        abort(404)  # Return a 404 if the product is not found

    return render_template(
        "urunler-detay.html",
        urun=urun
    )


@app.route("/duyurular")
def duyurular():
    duyurular = data.fetch_duyurular()
    return render_template("duyurular.html", duyurular=duyurular)


@app.route("/duyuru/<duyuruId>")
def duyurular_detay(duyuruId):
    duyuru = data.fetch_duyuru(duyuruId)

    if not duyuru:
        abort(404)  # Return a 404 if the product is not found

    return render_template(
        "duyurular-detay.html",
        duyuru=duyuru
    )


@app.route("/e-kitap")
def ekitap():
    return render_template("ekitap.html")


@app.route("/gizlilik-sozlesmesi")
def gizlilik_sozlesmesi():
    return render_template("sozlesme-gizlilik.html")


@app.route("/cerez-politikasi")
def cerez_politikasi():
    return render_template("sozlesme-cerez-politikasi.html")


@app.route("/kullanim-sartlari")
def kullanici_sozlesmesi():
    return render_template("sozlesme-kullanim-sartlari.html")


if __name__ == '__main__':
    app.run(debug=True)
