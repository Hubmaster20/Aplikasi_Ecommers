from django.contrib import admin
from .models import Model_kategori, Model_barang1, Model_pelanggan, Model_pemesanan1, Model_penjualan, Model_transaksi_pemesanan1, Model_kurir, Model_pegawai, Model_pengiriman

admin.site.register(Model_kategori)
admin.site.register(Model_barang1)
admin.site.register(Model_pelanggan)
admin.site.register(Model_pemesanan1)
admin.site.register(Model_penjualan)
admin.site.register(Model_transaksi_pemesanan1)
admin.site.register(Model_kurir)
admin.site.register(Model_pegawai)
admin.site.register(Model_pengiriman)