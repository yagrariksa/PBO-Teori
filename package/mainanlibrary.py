import math, array, os, datetime

from datetime import date

# library math
x = 9.3
y = 9.6
print("++++ library math ++++")
print(">> method ceil :: menurunkan segala koma pada float")
print(math.ceil(x))
print(math.ceil(y))
print(">> method comb(n,k) :: memilih k item dari n item tanpa perulangan")
print(math.comb(3,2))
print(">> method floor :: sama seperti ceil")
print(math.floor(x))
print(math.floor(y))
print(">> method factorial :: mengembalika factorial dari x")
print(math.factorial(3))

# library array
print("++++ library array ++++")
print(">> method append :: menambahkan item ke paling akhir dri array")
arr = [1,2,3]
arr.append(1)
print(arr)
print(">> method count(x) :: menghitung banyak anggota x yang ada di array")
print(arr.count(1))
print(">> method pop(x) :: menghapus anggota ke x di array")
print(arr, "-> sebelum pop")
arr.pop(0)
print(arr, "-> setelah pop")
print(">> method reverse :: membalik urutan item di array")
arr.append(5)
print(arr, "-> sebelum reverse")
arr.reverse()
print(arr, "-> setelah reverse")

# library os.path
print("++++ library os.path ++++")
print(">> method dirname :: mengembalikan direktori dari suatu path")
print(os.path.dirname(__file__))
print(">> method basename :: mengembalikan nama dari suatu path")
print(os.path.basename(__file__))
print(">> method abspath :: mengembalikan direktori hingga namafile dari suatu path ((dirname+basename))")
print(os.path.abspath(__file__))
print(">> method getsize :: mengembalikan besar file dalam bytes suatu path")
print(os.path.getsize(__file__))

# library datetime
print("++++ library datetime menggunakan class date ++++")
print(">> method fromisoformat :: mengatur waktu berdasarkan tanggal yang dimasukkan dari argumen")
time = date.fromisoformat('2020-12-31')
print(time)
print(">> method today :: untuk mendapatkan tanggal saat ini")
today = date.today()
print(today)
print(">> method strftime :: mengatur output sesuai format")
pakeslash = today.strftime("%d/%m/%y")
rincian = today.strftime("%A %d. %B %Y")
print(pakeslash)
print(rincian)
icCal = today.isocalendar()
print(">> method isocalendar :: mengubah tanggal menjadi array dengan index 0 adalah tahun, 1 pekan ke, 2 hari ke (1->monday/senin)")
print(icCal)

# library str
print("++++ library str -> Text Sequence Type")
mystring = "Universitas Airlangga"
print(">> method capitalize :: mengkapitalkan hanya char pertama pada string")
print(mystring.capitalize())
print(">> method format :: untuk memasukkan sesuatu dengan format argumen")
print("argumen satu : {0}, argumen dua : {1}".format(3,4))
print(">> method replace :: mengganti suatu string dengan string")
print(mystring.replace("Airlangga","Brawijaya"))
print(">> method split :: memisahkan karakter berdasarkan index menjadi array")
stringsplit = mystring.split(' ')
print(stringsplit)