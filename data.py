import pandas as pd

file_path = './data.xlsx'


def fetch_urunler():
    urunler = pd.read_excel(file_path, sheet_name="Urun")

    urunler = urunler.fillna({
        "Baslik": "Ürün Başlığı Yok",
        "Icerik": "Ürün İçeriği Yok",
        "Gorsel": "https://placehold.co/150",
        "Yeni": 0,
        "Populer": 0,
    })

    return urunler.to_dict(orient='records')


def fetch_siniflar():
    sinif = pd.read_excel(file_path, sheet_name="Sinif")
    print(sinif)
    return sinif.to_dict(orient='records')


def fetch_branslar():
    brans = pd.read_excel(file_path, sheet_name="Brans")
    print(brans)
    return brans.to_dict(orient='records')


def fetch_kategoriler():
    kategori = pd.read_excel(file_path, sheet_name="Kategori")
    print(kategori)
    return kategori.to_dict(orient='records')


def fetch_duyurular():
    duyuru = pd.read_excel(file_path, sheet_name="Duyuru")
    print(duyuru)
    return duyuru.to_dict(orient='records')


def fetch_bayiler():
    bayiler = pd.read_excel(file_path, sheet_name="Bayi")

    bayiler = bayiler.fillna({
        "Baslik": "-",
        "Telefon": "-",
        "Email": "-",
        "Adres": "-",
        "Lat": "39",
        "Lng": "39",
    })
    return bayiler.to_dict(orient='records')


def fetch_slidelar():
    slide = pd.read_excel(file_path, sheet_name="Slide")
    print(slide)
    return slide.to_dict(orient='records')
