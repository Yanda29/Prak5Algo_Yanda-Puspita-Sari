print("@   @  @@@@@  @    @  @@@@    @@@@@")
print(" @ @   @   @  @ @  @  @   @   @   @")
print("  @    @@@@@  @  @ @  @    @  @@@@@")
print("  @    @   @  @   @@  @   @   @   @")
print("  @    @   @  @    @  @@@@    @   @")

from math import floor

print("Menghitung Gaji")
satuan = float(input("masukkan Jam kerja : "))
if satuan <= 10.00:
    print("Selamat Pagi")
elif satuan < 14.59:
    print("Selamat Siang")
elif satuan <= 18.59:
    print("Selamat Sore")
elif satuan <= 24.00:
    print("Selamat Malam")

keluar = float(input("Jam Keluar Kerja : "))
if keluar <= 10.00:
    print("Selamat Pagi")
elif keluar <= 18.59:
    print("Selamat Sore")
elif keluar < 14.59:
    print("Selamat Siang")
elif keluar <= 24.00:
    print("Selamat Malam")

gaji = 175.000
durasiKerja = floor(keluar) - floor(satuan)
durasiLembur = durasiKerja - 8

print("------Rincian Gaji------")
print(f"Waktu Kerja   : {floor(durasiKerja)} Jam ( %.2f s/d %.2f )" % (satuan, keluar))
print("Gaji Per Hari : Rp %.3f" % (gaji))
if durasiKerja > 8:
    lembur = floor(durasiLembur) * 15.000
    total = gaji + lembur
    print(f"Lembur        : Rp %.3f ( {floor(durasiLembur)} jam x @ Rp 15.000 )" % (lembur))
elif durasiKerja <8:
    total= ((gaji - ((8-(int(keluar-satuan)))*15.000)))  
else:
    lembur = 0
    total = gaji + lembur
    print(f"Lembur        : Rp %.3f" % (lembur))
print("Total Gaji    : Rp %.3f" % (total))