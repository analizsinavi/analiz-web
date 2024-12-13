import pandas as pd

file_path = './data.xlsx'


def fetch_urunler():
    urun = pd.read_excel(file_path, sheet_name="Urun")
    print(urun)
    return urun.to_numpy()


def fetch_siniflar():
    sinif = pd.read_excel(file_path, sheet_name="Sinif")
    print(sinif)
    return sinif.to_numpy()


def fetch_branslar():
    brans = pd.read_excel(file_path, sheet_name="Brans")
    print(brans)
    return brans.to_numpy()


def fetch_kategoriler():
    kategori = pd.read_excel(file_path, sheet_name="Kategori")
    print(kategori)
    return kategori.to_numpy()


def fetch_duyurular():
    duyuru = pd.read_excel(file_path, sheet_name="Duyuru")
    print(duyuru)
    return duyuru.to_numpy()


def fetch_bayiler():
    bayi = pd.read_excel(file_path, sheet_name="Bayi")
    print(bayi)
    return bayi.to_numpy()
