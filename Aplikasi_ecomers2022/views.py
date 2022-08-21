# from .forms import Form_user
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
# from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .models import Model_kategori, Model_barang1, Model_pelanggan, Model_pemesanan1, Model_penjualan, Model_transaksi_pemesanan1, Model_kurir, Model_pegawai, Model_pengiriman
import hashlib


def index(request):
	context = {
	'page_title':'Login',
	}
	#print(request.user)
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('Home')
		else:
			return redirect('index')

	return render(request, 'index.html',  context)

def HomeView(request):	
	context = {
	'page_title':'Home'
	}
	return render(request, 'home.html',  context)

def LogoutView(request):
	context = {
	'page_title':'logout',
	}
	if request.method == "POST":
		if request.POST["logout"] == "Submit":	
			logout(request)

		return redirect('index')

	return render(request, 'logout.html',  context)	

# kategori
def Data_kategori(request):
	tampil = Model_kategori.objects.all()
	context = {	
	'tampil': tampil,
	}
	return render(request, 'Master_data/data_kategori/tabel.html',  context)	

def Tambah_kategori(request):
	if request.method == 'POST':
		Model_kategori.objects.create(
			nama_kategori = request.POST['nama_kategori'],
			keterangan = request.POST['keterangan'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/kategori/")	
	context = {	
	'Tambah': 'Tambah'
	}
	return render(request, 'Master_data/data_kategori/tambah.html', context)

def Hapus_kategori(request, hapus_kategori):
	Model_kategori.objects.filter(id=hapus_kategori).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('kategori')			

def Edit_kategori(request, id_kategori):		
	edit_data = Model_kategori.objects.get(id=id_kategori)
	if request.method == 'POST':		
			edit_data.nama_kategori = request.POST.get('nama_kategori')
			edit_data.keterangan = request.POST.get('keterangan')	
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('kategori')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_kategori/edit.html',  context)

# barang
def Data_barang(request):
	tampil = Model_barang1.objects.all()
	context = {	
	'tampil': tampil,
	}
	return render(request, 'Master_data/data_barang/tabel.html',  context)	

def Tambah_barang(request):
	select_kategori = Model_kategori.objects.all()
	if request.method == 'POST':
		Model_barang1.objects.create(
			nama_barang = request.POST['nama_barang'],
			nama_kategori = request.POST['nama_kategori'],
			satuan = request.POST['satuan'],
			stock = request.POST['stock'],
			harga = request.POST['harga'],
			gambar = request.FILES['gambar'],
			deskripsi = request.POST['deskripsi'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/barang/")	
	context = {	
	'Tambah': 'Tambah',
	'select_kategori': select_kategori
	}
	return render(request, 'Master_data/data_barang/tambah.html', context)

def Hapus_barang(request, hapus_barang):
	Model_barang1.objects.filter(id=hapus_barang).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('barang')			

def Edit_barang(request, id_barang):		
	select_kategori = Model_kategori.objects.all()
	edit_data = Model_barang1.objects.get(id=id_barang)
	if request.method == 'POST':		
			edit_data.nama_barang = request.POST.get('nama_barang')
			edit_data.nama_kategori = request.POST.get('nama_kategori')
			edit_data.satuan = request.POST.get('satuan')	
			edit_data.stock = request.POST.get('stock')	
			edit_data.harga = request.POST.get('harga')	
			edit_data.gambar = request.FILES.get('gambar')	
			edit_data.deskripsi = request.POST.get('deskripsi')	
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('barang')

	context = {
	'edit_data': edit_data,
	'select_kategori': select_kategori
	}
	return render(request, 'Master_data/data_barang/edit.html',  context)

# pelanggan
def Data_pelanggan(request):
	tampil = Model_pelanggan.objects.all()
	context = {	
	'tampil': tampil,
	}
	return render(request, 'Master_data/data_pelanggan/tabel.html',  context)	

def Tambah_pelanggan(request):
	if request.method == 'POST':
		Model_pelanggan.objects.create(
			noktp = request.POST['noktp'],
			nama_lengkap = request.POST['nama_lengkap'],
			alamat = request.POST['alamat'],
			jk = request.POST['jk'],
			nohp = request.POST['nohp'],
			email = request.POST['email'],
			password = request.POST['password'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/pelanggan/")	
	context = {	
	'Tambah': 'Tambah'
	}
	return render(request, 'Master_data/data_pelanggan/tambah.html', context)

def Hapus_pelanggan(request, hapus_pelanggan):
	Model_pelanggan.objects.filter(id=hapus_pelanggan).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('pelanggan')			

def Edit_pelanggan(request, id_pelanggan):		
	edit_data = Model_pelanggan.objects.get(id=id_pelanggan)
	if request.method == 'POST':		
			edit_data.noktp = request.POST.get('noktp')
			edit_data.nama_lengkap = request.POST.get('nama_lengkap')	
			edit_data.alamat = request.POST.get('alamat')	
			edit_data.jk = request.POST.get('jk')	
			edit_data.nohp = request.POST.get('nohp')	
			edit_data.email = request.POST.get('email')	
			edit_data.password = request.POST.get('password')	
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('pelanggan')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_pelanggan/edit.html',  context)

# pemesanan barang
def Data_pemesanan(request):
	tampil = Model_pemesanan1.objects.all()
	context = {	
	'tampil': tampil,
	}
	return render(request, 'Master_data/data_pemesanan/tabel.html',  context)	

def Tambah_pemesanan(request):
	select_kategori = Model_barang1.objects.all()
	# cari barang kategori
	if 'cari_kategori' in request.GET:
		cari_kategori=request.GET['cari_kategori']
		tampil_kategori = Model_barang1.objects.filter(nama_kategori=cari_kategori)
	else:
		tampil_kategori = Model_barang1.objects.filter(nama_kategori=None)

	if request.method == 'POST':
		Model_pemesanan1.objects.create(
			nama_barang = request.POST['nama_barang'],
			nama_kategori = request.POST['nama_kategori'],
			ukuran = request.POST['ukuran'],
			noktp = request.POST['noktp'],
			nama_lengkap = request.POST['nama_lengkap'],
			jumlah_pesanan = request.POST['jumlah_pesanan'],
			harga_barang = request.POST['harga_barang'],
			tanggal_pemesanan = request.POST['tanggal_pemesanan'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/pemesanan/")	
	context = {	
	'Tambah': 'Tambah',
	'select_kategori': select_kategori,
	'tampil_kategori': tampil_kategori
	}
	return render(request, 'Master_data/data_pemesanan/tambah.html', context)

def Hapus_pemesanan(request, hapus_pemesanan):
	Model_pemesanan1.objects.filter(id=hapus_pemesanan).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('pemesanan')			

def Edit_pemesanan(request, id_pemesanan):		
	select_kategori = Model_kategori.objects.all()

	edit_data = Model_pemesanan1.objects.get(id=id_pemesanan)
	if request.method == 'POST':		
			edit_data.nama_barang = request.POST.get('nama_barang')
			edit_data.nama_kategori = request.POST.get('nama_kategori')	
			edit_data.ukuran = request.POST.get('ukuran')	
			edit_data.noktp = request.POST.get('noktp')	
			edit_data.nama_lengkap = request.POST.get('nama_lengkap')	
			edit_data.jumlah_pesanan = request.POST.get('jumlah_pesanan')	
			edit_data.harga_barang = request.POST.get('harga_barang')	
			edit_data.tanggal_pemesanan = request.POST.get('tanggal_pemesanan')	
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('pemesanan')

	context = {
	'edit_data': edit_data,
	'select_kategori': select_kategori
	}
	return render(request, 'Master_data/data_pemesanan/edit.html',  context)


# penjualan barang
def Data_penjualan(request):
	tampil = Model_penjualan.objects.all()
	context = {	
	'tampil': tampil,
	}
	return render(request, 'Master_data/data_penjualan/tabel.html',  context)	

def Tambah_penjualan(request):
	nota = Model_penjualan.objects.count()
	nota_kode = nota + 1;

	select_kategori = Model_kategori.objects.all()
	if 'cari_barang' in request.GET:
		cari_barang=request.GET['cari_barang']
		tampil_barang = Model_barang1.objects.filter(nama_kategori=cari_barang)
	else:
		tampil_barang = Model_barang1.objects.filter(nama_kategori=None)

	if request.method == 'POST':
		Model_penjualan.objects.create(
			nota = request.POST['nota'],
			nama_kategori = request.POST['nama_kategori'],
			nama_barang = request.POST['nama_barang'],
			harga = request.POST['harga'],
			jumlah = request.POST['jumlah'],
			total = request.POST['total'],
			bayar = request.POST['bayar'],
			kembalian = request.POST['kembalian'],
			tanggal_penjulan = request.POST['tanggal_penjulan'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/penjualan/")	
	context = {	
	'Tambah': 'Tambah',
	'nota_kode': nota_kode,
	'select_kategori': select_kategori,
	'tampil_barang': tampil_barang
	}
	return render(request, 'Master_data/data_penjualan/tambah.html', context)

def Hapus_penjualan(request, hapus_penjualan):
	Model_penjualan.objects.filter(id=hapus_penjualan).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('penjualan')			

def Edit_penjualan(request, id_penjualan):		
	edit_data = Model_penjualan.objects.get(id=id_penjualan)

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_penjualan/cetak_nota.html',  context)


# transaksi pemesanan
def Data_transaksi_pemesanan(request):
	tampil = Model_transaksi_pemesanan1.objects.all()
	context = {	
	'tampil': tampil,
	}
	return render(request, 'Master_data/data_transaksi_pemesanan/tabel.html',  context)	

def Check_pemesanan_admin(request):
	tampil = Model_pemesanan1.objects.all()
	context = {	
	'tampil': tampil,
	}
	return render(request, 'Master_data/data_transaksi_pemesanan/Check_pemesanan.html',  context)	

def Tambah_transaksi_pemesanan(request, check_pemesanan):
	check_data = Model_pemesanan1.objects.get(id=check_pemesanan)
	kode_nota = Model_transaksi_pemesanan1.objects.count()
	nota = kode_nota + 1; 

	if request.method == 'POST':
		Model_transaksi_pemesanan1.objects.create(
			nota = request.POST['nota'],
			noktp = request.POST['noktp'],
			nama_lengkap = request.POST['nama_lengkap'],
			nama_kategori = request.POST['nama_kategori'],
			nama_barang = request.POST['nama_barang'],
			jumlah_pesanan = request.POST['jumlah_pesanan'],
			harga_barang = request.POST['harga_barang'],
			total = request.POST['total'],
			bayar = request.POST['bayar'],
			kembalian = request.POST['kembalian'],
			status_pembayaran = request.POST['status_pembayaran'],
			tanggal_pemesanan = request.POST['tanggal_pemesanan'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/transaksi_pemesanan/")	
	context = {	
	'Tambah': 'Tambah',
	'check_data': check_data,
	'nota': nota
	}
	return render(request, 'Master_data/data_transaksi_pemesanan/tambah.html', context)

def Hapus_transaksi_pemesanan(request, hapus_transaksi_pemesanan):
	Model_transaksi_pemesanan1.objects.filter(id=hapus_transaksi_pemesanan).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('transaksi_pemesanan')			

def Edit_transaksi_pemesanan(request, id_transaksi_pemesanan):		
	edit_data = Model_transaksi_pemesanan1.objects.get(id=id_transaksi_pemesanan)

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_transaksi_pemesanan/nota.html',  context)

# kurir
def Data_kurir(request):
	tampil = Model_kurir.objects.all()
	context = {	
	'tampil': tampil,
	}
	return render(request, 'Master_data/data_kurir/tabel.html',  context)	

def Tambah_kurir(request):
	kode_otomatis = Model_kurir.objects.count()
	kode_kurir_o = kode_otomatis + 1;
	if request.method == 'POST':
		Model_kurir.objects.create(
			kode_kurir = request.POST['kode_kurir'],
			nama_kurir = request.POST['nama_kurir'],
			nohp = request.POST['nohp'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/kurir/")	
	context = {	
	'Tambah': 'Tambah',
	'kode_kurir_o': kode_kurir_o
	}
	return render(request, 'Master_data/data_kurir/tambah.html', context)

def Hapus_kurir(request, hapus_kurir):
	Model_kurir.objects.filter(id=hapus_kurir).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('kurir')			

def Edit_kurir(request, id_kurir):		
	edit_data = Model_kurir.objects.get(id=id_kurir)
	if request.method == 'POST':		
			edit_data.kode_kurir = request.POST.get('kode_kurir')
			edit_data.nama_kurir = request.POST.get('nama_kurir')	
			edit_data.nohp = request.POST.get('nohp')	
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('kurir')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_kurir/edit.html',  context)

# pegawai
def Data_pegawai(request):
	tampil = Model_pegawai.objects.all()
	context = {	
	'tampil': tampil,
	}
	return render(request, 'Master_data/data_pegawai/tabel.html',  context)	

def Tambah_pegawai(request):
	kode = Model_pegawai.objects.count()
	kode_otomatis = kode + 1;
	if request.method == 'POST':
		Model_pegawai.objects.create(
			nik = request.POST['nik'],
			nama_pegawai = request.POST['nama_pegawai'],
			alamat = request.POST['alamat'],
			jk = request.POST['jk'],
			nohp = request.POST['nohp'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/pegawai/")	
	context = {	
	'Tambah': 'Tambah',
	'kode_otomatis': kode_otomatis
	}
	return render(request, 'Master_data/data_pegawai/tambah.html', context)

def Hapus_pegawai(request, hapus_pegawai):
	Model_pegawai.objects.filter(id=hapus_pegawai).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('pegawai')			

def Edit_pegawai(request, id_pegawai):		
	edit_data = Model_pegawai.objects.get(id=id_pegawai)
	if request.method == 'POST':		
			edit_data.nik = request.POST.get('nik')
			edit_data.nama_pegawai = request.POST.get('nama_pegawai')	
			edit_data.alamat = request.POST.get('alamat')	
			edit_data.jk = request.POST.get('jk')	
			edit_data.nohp = request.POST.get('nohp')	
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('pegawai')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_pegawai/edit.html',  context)


# pengiriman
def Data_pengiriman(request):
	tampil = Model_pengiriman.objects.all()
	context = {	
	'tampil': tampil,
	}
	return render(request, 'Master_data/data_pengiriman/tabel.html',  context)	

def Check_pesanan_pengiriman(request):
	tampil = Model_transaksi_pemesanan1.objects.all()
	context = {	
	'tampil': tampil,
	}
	return render(request, 'Master_data/data_pengiriman/check_pesanan.html',  context)	

def Tambah_pengiriman(request, proses_pengiriman):
	tampil_transaksi = Model_transaksi_pemesanan1.objects.get(id=proses_pengiriman)
	kode_nota = Model_pengiriman.objects.count()
	kode_otomatis = kode_nota + 1;
	select_kurir = Model_kurir.objects.all()

	if request.method == 'POST':
		Model_pengiriman.objects.create(
			kode_pengiriman = request.POST['kode_pengiriman'],
			noktp = request.POST['noktp'],
			nama_lengkap = request.POST['nama_lengkap'],
			alamat_pengiriman = request.POST['alamat_pengiriman'],
			nama_barang = request.POST['nama_barang'],
			jumlah_pesanan = request.POST['jumlah_pesanan'],
			harga = request.POST['harga'],
			total = request.POST['total'],
			nama_kurir = request.POST['nama_kurir'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/pengiriman/")	
	context = {	
	'Tambah': 'Tambah',
	'tampil_transaksi': tampil_transaksi,
	'kode_otomatis': kode_otomatis,
	'select_kurir': select_kurir
	}
	return render(request, 'Master_data/data_pengiriman/tambah.html', context)

def Hapus_pengiriman(request, hapus_pengiriman):
	Model_pengiriman.objects.filter(id=hapus_pengiriman).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('pengiriman')			

def Edit_pengiriman(request, id_pengiriman):		
	select_kurir = Model_kurir.objects.all()

	edit_data = Model_pengiriman.objects.get(id=id_pengiriman)
	if request.method == 'POST':		
			edit_data.kode_pengiriman = request.POST.get('kode_pengiriman')
			edit_data.noktp = request.POST.get('noktp')	
			edit_data.nama_lengkap = request.POST.get('nama_lengkap')	
			edit_data.alamat_pengiriman = request.POST.get('alamat_pengiriman')	
			edit_data.nama_barang = request.POST.get('nama_barang')	
			edit_data.jumlah_pesanan = request.POST.get('jumlah_pesanan')	
			edit_data.harga = request.POST.get('harga')	
			edit_data.total = request.POST.get('total')	
			edit_data.nama_kurir = request.POST.get('nama_kurir')	
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('pengiriman')

	context = {
	'edit_data': edit_data,
	'select_kurir': select_kurir
	}
	return render(request, 'Master_data/data_pengiriman/edit.html',  context)

def Cetak_nota_pengiriman(request, cetak_nota):
	tampil = Model_pengiriman.objects.get(id=cetak_nota)
	context = {	
	'tampil': tampil,
	}
	return render(request, 'Master_data/data_pengiriman/Cetak_nota_pengiriman.html',  context)	


# menu laporan / proses laporan
def Menu_laporan(request):	
	context = {	
	'':''
	}
	return render(request, 'Master_data/laporan/menu_laporan.html',  context)

def lp_pemesanan(request):	
	tampil = Model_pemesanan1.objects.all()
	context = {	
	'tampil': tampil,
	}
	return render(request, 'Master_data/laporan/lp_pemesanan.html',  context)

def lp_pengiriman(request):	
	tampil = Model_pengiriman.objects.all()
	context = {	
	'tampil': tampil,
	}
	return render(request, 'Master_data/laporan/lp_pengiriman.html',  context)

def lp_penjualan(request):	
	tampil = Model_penjualan.objects.all()
	context = {	
	'tampil': tampil,
	}
	return render(request, 'Master_data/laporan/lp_penjualan.html',  context)

def lp_transaksi_pemesanan(request):	
	tampil = Model_transaksi_pemesanan1.objects.all()
	context = {	
	'tampil': tampil,
	}
	return render(request, 'Master_data/laporan/lp_transaksi_pemesanan.html',  context)

# halaman website

def WEBSITE(request):	
	select_kategori = Model_kategori.objects.all()
	# cari barang kategori
	if 'cari_kategori' in request.GET:
		cari_kategori=request.GET['cari_kategori']
		tampil = Model_barang1.objects.filter(nama_kategori=cari_kategori)
	else:
		tampil = Model_barang1.objects.all()
	context = {	
	'tampil': tampil,
	'select_kategori': select_kategori
	}
	return render(request, 'WEBSITE/website.html',  context)

def WEBSITE_REGISTER(request):	
	select_kategori = Model_kategori.objects.all()
	# cari barang kategori
	if 'cari_kategori' in request.GET:
		cari_kategori=request.GET['cari_kategori']
		tampil = Model_barang1.objects.filter(nama_kategori=cari_kategori)
	else:
		tampil = Model_barang1.objects.all()

	if request.method == 'POST':
		Model_pelanggan.objects.create(
			noktp = request.POST['noktp'],
			nama_lengkap = request.POST['nama_lengkap'],
			alamat = request.POST['alamat'],
			jk = request.POST['jk'],
			nohp = request.POST['nohp'],
			email = request.POST['email'],
			password = request.POST['password'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/WEBSITE_LOGIN/")	
	context = {	
	'tampil': tampil,
	'select_kategori': select_kategori
	}
	return render(request, 'WEBSITE/website_register.html',  context)

# website
def WEBSITE_LOGIN(request):	
	select_kategori = Model_kategori.objects.all()
	# cari barang kategori
	if 'cari_kategori' in request.GET:
		cari_kategori=request.GET['cari_kategori']
		tampil = Model_barang1.objects.filter(nama_kategori=cari_kategori)
	else:
		tampil = Model_barang1.objects.all()

	
	context = {	
	'tampil': tampil,
	'select_kategori': select_kategori
	}
	return render(request, 'WEBSITE/website_login.html',  context)

def AKSI_LOGIN(request):	
	select_kategori = Model_kategori.objects.all()
	if 'cari_kategori' in request.GET:
		cari_kategori=request.GET['cari_kategori']
		tampil = Model_barang1.objects.filter(nama_kategori=cari_kategori)
	else:
		tampil = Model_barang1.objects.all()
	# cari barang kategori
	if 'email' in request.GET:
		email=request.GET['email']
		tampil_email = Model_pelanggan.objects.filter(email=email)
	else:
		tampil_email = Model_pelanggan.objects.all()

	if 'password' in request.GET:
		password=request.GET['password']
		tampil_password = Model_pelanggan.objects.filter(password=password)
	else:
		tampil_password = Model_pelanggan.objects.all()

	# proses pemesanan
	if request.method == 'POST':
		Model_pemesanan1.objects.create(
			nama_barang = request.POST['nama_barang'],
			nama_kategori = request.POST['nama_kategori'],
			ukuran = request.POST['ukuran'],
			noktp = request.POST['noktp'],
			nama_lengkap = request.POST['nama_lengkap'],
			jumlah_pesanan = request.POST['jumlah_pesanan'],
			harga_barang = request.POST['harga_barang'],
			tanggal_pemesanan = request.POST['tanggal_pemesanan'],
			)
		messages.info(request, 'Data Berhasil Di Booking..')
		return HttpResponseRedirect("/WEBSITE/")	
	
	context = {	
	'tampil': tampil,
	'select_kategori': select_kategori,
	'tampil_email': tampil_email,
	'tampil_password': tampil_password
	}
	return render(request, 'WEBSITE/Master_pemesanan/website.html',  context)

# data pemesanan
def Check_pemesanan(request):
	tampil_data = Model_pemesanan1.objects.all()
	select_kategori = Model_kategori.objects.all()
	if 'cari_kategori' in request.GET:
		cari_kategori=request.GET['cari_kategori']
		tampil = Model_barang1.objects.filter(nama_kategori=cari_kategori)
	else:
		tampil = Model_barang1.objects.all()

	context = {		
	'tampil_data': tampil_data,
	'tampil': tampil,
	'select_kategori': select_kategori,
	}
	return render(request, 'WEBSITE/Master_pemesanan/website_pemesanan.html',  context)