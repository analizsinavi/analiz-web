import pandas as pd

file_path = './data.xlsx'


def fetch_urunler():
    urunler = pd.read_excel(file_path, sheet_name="Urun")
    urunler = urunler.fillna({
        "Baslik": "Ürün Başlığı Yok",
        "Icerik": "Ürün İçeriği Yok",
        "Gorsel": "https://placehold.co/150",
        "LinkSatinAlma": "",
        "LinkOrnekSayfa": "",
        "Yeni": 0,
        "Populer": 0,
    })

    return urunler.to_dict(orient='records')


def fetch_urunler_yeni():
    urunler = pd.read_excel(file_path, sheet_name="Urun")
    urunler = urunler[urunler["Yeni"] == 1]
    urunler = urunler.fillna({
        "Baslik": "Ürün Başlığı Yok",
        "Icerik": "Ürün İçeriği Yok",
        "Gorsel": "https://placehold.co/150",
        "LinkSatinAlma": "",
        "LinkOrnekSayfa": "",
        "Yeni": 0,
        "Populer": 0,
    })

    return urunler.to_dict(orient='records')


def fetch_urunler_populer():
    urunler = pd.read_excel(file_path, sheet_name="Urun")
    urunler = urunler[urunler["Populer"] == 1]
    urunler = urunler.fillna({
        "Baslik": "Ürün Başlığı Yok",
        "Icerik": "Ürün İçeriği Yok",
        "Gorsel": "https://placehold.co/150",
        "LinkSatinAlma": "",
        "LinkOrnekSayfa": "",
        "Yeni": 0,
        "Populer": 0,
    })

    return urunler.to_dict(orient='records')


def fetch_urun(urunId):
    urunler = fetch_urunler()
    for urun in urunler:
        if int(urun["UrunId"]) == urunId:
            return urun
    return None


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
    duyurular = pd.read_excel(file_path, sheet_name="Duyuru")
    print(duyurular)
    return duyurular.to_dict(orient='records')


def fetch_duyurular_yeni():
    duyurular = pd.read_excel(file_path, sheet_name="Duyuru")

    # Ensure the 'Tarih' column is properly parsed as a datetime type
    duyurular['Tarih'] = pd.to_datetime(duyurular['Tarih'], errors='coerce')

    # Drop rows where 'Tarih' is NaT (not a valid datetime)
    duyurular = duyurular.dropna(subset=['Tarih'])

    # Sort by 'Tarih' in descending order (latest first)
    duyurular = duyurular.sort_values(by='Tarih', ascending=False)

    # Select the first 4 rows
    duyurular = duyurular.head(3)

    return duyurular.to_dict(orient='records')


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
