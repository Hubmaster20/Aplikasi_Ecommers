"""Aplikasi_ecomers2022 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from Aplikasi_ecomers2022 import settings
from django.urls import path
# from django.contrib.auth import views
from django.contrib import admin
from . import views
from .views import index, HomeView, LogoutView, Data_kategori, Tambah_kategori, Edit_kategori, Hapus_kategori, Data_barang, Tambah_barang, Edit_barang, Hapus_barang, Data_pelanggan, Tambah_pelanggan, Edit_pelanggan, Hapus_pelanggan, Data_pemesanan, Tambah_pemesanan, Edit_pemesanan, Hapus_pemesanan, Data_penjualan, Tambah_penjualan, Edit_penjualan, Hapus_penjualan, Check_pemesanan_admin, Data_transaksi_pemesanan, Tambah_transaksi_pemesanan, Hapus_transaksi_pemesanan, Edit_transaksi_pemesanan, Data_kurir, Tambah_kurir, Edit_kurir, Hapus_kurir, Data_pegawai, Tambah_pegawai, Edit_pegawai, Hapus_pegawai, Data_pengiriman, Tambah_pengiriman, Edit_pengiriman, Hapus_pengiriman, Check_pesanan_pengiriman, Cetak_nota_pengiriman, Menu_laporan, lp_transaksi_pemesanan, lp_pemesanan, lp_pengiriman, lp_penjualan, WEBSITE, WEBSITE_REGISTER, WEBSITE_LOGIN, AKSI_LOGIN, Check_pemesanan

urlpatterns = [
    url(r'^$',index, name="index"),
    url(r'^Home/$', HomeView, name="Home"),
    url(r'^logout/$',LogoutView, name="logout"),

    # kategori
    url(r'^kategori/$',Data_kategori, name="kategori"),
    url(r'^Tambah_kategori/$',Tambah_kategori, name="Tambah_kategori"),
    url(r'^hapus_kategori/(?P<hapus_kategori>[0-9]+)$',Hapus_kategori, name="hapus_kategori"),
    url(r'^edit_kategori/(?P<id_kategori>[0-9]+)$',Edit_kategori, name="edit_kategori"),

    # barang
    url(r'^barang/$',Data_barang, name="barang"),
    url(r'^Tambah_barang/$',Tambah_barang, name="Tambah_barang"),
    url(r'^hapus_barang/(?P<hapus_barang>[0-9]+)$',Hapus_barang, name="hapus_barang"),
    url(r'^edit_barang/(?P<id_barang>[0-9]+)$',Edit_barang, name="edit_barang"),

    # pelanggan
    url(r'^pelanggan/$',Data_pelanggan, name="pelanggan"),
    url(r'^Tambah_pelanggan/$',Tambah_pelanggan, name="Tambah_pelanggan"),
    url(r'^hapus_pelanggan/(?P<hapus_pelanggan>[0-9]+)$',Hapus_pelanggan, name="hapus_pelanggan"),
    url(r'^edit_pelanggan/(?P<id_pelanggan>[0-9]+)$',Edit_pelanggan, name="edit_pelanggan"),
    
    # pemesanan
    url(r'^pemesanan/$',Data_pemesanan, name="pemesanan"),
    url(r'^Tambah_pemesanan/$',Tambah_pemesanan, name="Tambah_pemesanan"),
    url(r'^hapus_pemesanan/(?P<hapus_pemesanan>[0-9]+)$',Hapus_pemesanan, name="hapus_pemesanan"),
    url(r'^edit_pemesanan/(?P<id_pemesanan>[0-9]+)$',Edit_pemesanan, name="edit_pemesanan"),

    # penjualan barang
    url(r'^penjualan/$',Data_penjualan, name="penjualan"),    
    url(r'^Tambah_penjualan/$',Tambah_penjualan, name="Tambah_penjualan"),
    url(r'^hapus_penjualan/(?P<hapus_penjualan>[0-9]+)$',Hapus_penjualan, name="hapus_penjualan"),
    url(r'^edit_penjualan/(?P<id_penjualan>[0-9]+)$',Edit_penjualan, name="edit_penjualan"),

    # transaksi pemesanan
    url(r'^Check_pemesanan_admin/$',Check_pemesanan_admin, name="Check_pemesanan_admin"),
    url(r'^transaksi_pemesanan/$',Data_transaksi_pemesanan, name="transaksi_pemesanan"),    
    url(r'^Tambah_transaksi_pemesanan/(?P<check_pemesanan>[0-9]+)$',Tambah_transaksi_pemesanan, name="Tambah_transaksi_pemesanan"),
    url(r'^hapus_transaksi_pemesanan/(?P<hapus_transaksi_pemesanan>[0-9]+)$',Hapus_transaksi_pemesanan, name="hapus_transaksi_pemesanan"),
    url(r'^edit_transaksi_pemesanan/(?P<id_transaksi_pemesanan>[0-9]+)$',Edit_transaksi_pemesanan, name="edit_transaksi_pemesanan"),

    # kurir
    url(r'^kurir/$',Data_kurir, name="kurir"),
    url(r'^Tambah_kurir/$',Tambah_kurir, name="Tambah_kurir"),
    url(r'^hapus_kurir/(?P<hapus_kurir>[0-9]+)$',Hapus_kurir, name="hapus_kurir"),
    url(r'^edit_kurir/(?P<id_kurir>[0-9]+)$',Edit_kurir, name="edit_kurir"),

    # pegawai
    url(r'^pegawai/$',Data_pegawai, name="pegawai"),
    url(r'^Tambah_pegawai/$',Tambah_pegawai, name="Tambah_pegawai"),
    url(r'^hapus_pegawai/(?P<hapus_pegawai>[0-9]+)$',Hapus_pegawai, name="hapus_pegawai"),
    url(r'^edit_pegawai/(?P<id_pegawai>[0-9]+)$',Edit_pegawai, name="edit_pegawai"),

    # pengiriman
    url(r'^pengiriman/$',Data_pengiriman, name="pengiriman"),
    url(r'^check_pesanan_pengirim/$',Check_pesanan_pengiriman, name="check_pesanan_pengirim"),
    url(r'^Tambah_pengiriman/(?P<proses_pengiriman>[0-9]+)$',Tambah_pengiriman, name="Tambah_pengiriman"),
    url(r'^hapus_pengiriman/(?P<hapus_pengiriman>[0-9]+)$',Hapus_pengiriman, name="hapus_pengiriman"),
    url(r'^edit_pengiriman/(?P<id_pengiriman>[0-9]+)$',Edit_pengiriman, name="edit_pengiriman"),
    url(r'^Cetak_nota_pengiriman/(?P<cetak_nota>[0-9]+)$',Cetak_nota_pengiriman, name="Cetak_nota_pengiriman"),

    # menu lapora / proses
    url(r'^Menu_laporan/$',Menu_laporan, name="Menu_laporan"),

    url(r'^lp_pemesanan/$',lp_pemesanan, name="lp_pemesanan"),
    url(r'^lp_penjualan/$',lp_penjualan, name="lp_penjualan"),
    url(r'^lp_pengiriman/$',lp_pengiriman, name="lp_pengiriman"),
    url(r'^lp_transaksi_pemesanan/$',lp_transaksi_pemesanan, name="lp_transaksi_pemesanan"),

    # website
    url(r'^WEBSITE/$',WEBSITE, name="WEBSITE"),
    url(r'^WEBSITE_REGISTER/$',WEBSITE_REGISTER, name="WEBSITE_REGISTER"),
    url(r'^WEBSITE_LOGIN/$',WEBSITE_LOGIN, name="WEBSITE_LOGIN"),
    url(r'^AKSI_LOGIN/$',AKSI_LOGIN, name="AKSI_LOGIN"),
    
    url(r'^Check_pemesanan/$',Check_pemesanan, name="Check_pemesanan"),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:    
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)