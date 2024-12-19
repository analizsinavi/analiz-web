from flask_frozen import Freezer
from app import app
import data

freezer = Freezer(app)


@freezer.register_generator
def urunler_detay():
    # Ürünleri veritabanından veya data modülünden al
    urunler = data.fetch_urunler()

    # Her ürün için bir URL oluştur
    for urun in urunler:
        if 'UrunId' in urun:
            yield {'urunId': urun['UrunId']}
        else:
            print(f"Ürün id'si bulunamadı: {urun}")

@freezer.register_generator
def duyurular_detay():
    # Ürünleri veritabanından veya data modülünden al
    duyurular = data.fetch_duyurular()

    # Her ürün için bir URL oluştur
    for duyuru in duyurular:
        if 'DuyuruId' in duyuru:
            yield {'duyuruId': duyuru['DuyuruId']}
        else:
            print(f"Duyuru id'si bulunamadı: {duyuru}")


if __name__ == '__main__':
    freezer.freeze()
