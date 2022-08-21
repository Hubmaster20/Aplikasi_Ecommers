from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
from django.contrib.auth.models import User

class Model_kategori(models.Model):
	nama_kategori	= models.CharField(max_length = 1200)
	keterangan	=models.CharField(max_length = 25200)	

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_kategori)

class Model_barang1(models.Model):
	nama_barang	= models.CharField(max_length = 1200)
	nama_kategori	=models.CharField(max_length = 22500)	
	satuan	=models.CharField(max_length = 25000)	
	stock	=models.CharField(max_length = 25)	
	harga	=models.CharField(max_length = 25)	
	gambar	=models.ImageField(upload_to ='Berkas/', null=True)	
	deskripsi	=models.CharField(max_length = 22500)	


	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_kategori)

class Model_pelanggan(models.Model):
	noktp	= models.CharField(max_length = 1200)
	nama_lengkap	=models.CharField(max_length = 252000)
	alamat	=models.CharField(max_length = 252000)
	jk	=models.CharField(max_length = 252000)
	nohp	=models.CharField(max_length = 252000)
	email	=models.CharField(max_length = 252000)
	password	=models.CharField(max_length = 252000)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_lengkap)

class Model_pemesanan1(models.Model):
	nama_barang	= models.CharField(max_length = 1200)
	nama_kategori	=models.CharField(max_length = 25200)	
	ukuran	=models.CharField(max_length = 25200)	
	noktp	=models.CharField(max_length = 25200)	
	nama_lengkap	=models.CharField(max_length = 25200)	
	jumlah_pesanan	=models.CharField(max_length = 25200)	
	harga_barang	=models.CharField(max_length = 25200)	
	tanggal_pemesanan	=models.CharField(max_length = 25200)	

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_barang)

# penjualan
class Model_penjualan(models.Model):
	nota	= models.CharField(max_length = 1200)
	nama_kategori	= models.CharField(max_length = 1200)
	nama_barang	=models.CharField(max_length = 25200)
	harga	=models.CharField(max_length = 25200)
	jumlah	=models.CharField(max_length = 25200)
	total	=models.CharField(max_length = 25200)
	bayar	=models.CharField(max_length = 25200)
	kembalian	=models.CharField(max_length = 25200)
	tanggal_penjulan	=models.CharField(max_length = 25200)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_kategori)

# transaksi pemesanan
class Model_transaksi_pemesanan1(models.Model):
	nota	=models.CharField(max_length = 25200)
	noktp	= models.CharField(max_length = 1200)
	nama_lengkap	=models.CharField(max_length = 25200)
	nama_kategori	=models.CharField(max_length = 25200)
	nama_barang	=models.CharField(max_length = 25200)
	jumlah_pesanan	=models.CharField(max_length = 25200)
	harga_barang	=models.CharField(max_length = 25200)
	total	=models.CharField(max_length = 25200)
	bayar	=models.CharField(max_length = 25200)
	kembalian	=models.CharField(max_length = 25200)
	status_pembayaran	=models.CharField(max_length = 25200)
	tanggal_pemesanan	=models.CharField(max_length = 25200)


	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_kategori)

class Model_kurir(models.Model):
	kode_kurir	= models.CharField(max_length = 1200)
	nama_kurir	=models.CharField(max_length = 25200)	
	nohp	=models.CharField(max_length = 25200)	

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_kategori)

class Model_pegawai(models.Model):
	nik	= models.CharField(max_length = 1200)
	nama_pegawai	=models.CharField(max_length = 25200)	
	alamat	=models.CharField(max_length = 25200)	
	jk	=models.CharField(max_length = 25200)	
	nohp	=models.CharField(max_length = 25200)	

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_pegawai)

class Model_pengiriman(models.Model):
	kode_pengiriman	=models.CharField(max_length = 25200)
	noktp	=models.CharField(max_length = 25200)
	nama_lengkap	=models.CharField(max_length = 25200)	
	alamat_pengiriman	=models.CharField(max_length = 25200)	
	nama_barang	= models.CharField(max_length = 1200)
	jumlah_pesanan	=models.CharField(max_length = 25200)	
	harga	=models.CharField(max_length = 25200)	
	total	=models.CharField(max_length = 25200)	
	nama_kurir	=models.CharField(max_length = 25200)	


	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_barang)