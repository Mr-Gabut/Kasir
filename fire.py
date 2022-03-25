garis = "\33[37;1m====================================="
total = 0
barang = []
harga = []
#Warna
h="\33[0;32m"
m="\33[31;1m"
p="\33[37;1m"
k="\33[1;33m"

os.system('git pull')
time.sleep(2)
os.system('clear)
print(f"""
{m}╭━━╮╭━━━┳╮╱╱╭━━━┳━╮╱╭┳╮╱╱╭┳━━━╮
┃╭╮┃┃╭━╮┃┃╱╱┃╭━╮┃┃╰╮┃┃╰╮╭╯┃╭━╮┃
┃╰╯╰┫┃╱┃┃┃╱╱┃┃╱┃┃╭╮╰╯┣╮╰╯╭┫┃╱┃┃
{p}┃╭━╮┃╰━╯┃┃╱╭┫╰━╯┃┃╰╮┃┃╰╮╭╯┃╰━╯┃
┃╰━╯┃╭━╮┃╰━╯┃╭━╮┃┃╱┃┃┃╱┃┃╱┃╭━╮┃
╰━━━┻╯╱╰┻━━━┻╯╱╰┻╯╱╰━╯╱╰╯╱╰╯╱╰╯V {m}1.0
{m}[+] {k}Author {p}:{k} Mr-Gabut""")
while True:
  print(f"""{p}=====================\n{h}Daftar Barang\n{p}=====================
{k}1. {h}Bala bala\t1500
{k}2. {h}Oncom Idad\t1000
{k}3. {h}Chiken RFC\t500
{k}4. {h}Janda\t\t10000
{p}=====================""")
  kode = int(input(f"{k}Masukan kode barang : {m}"))
  if kode == 1:
    barang.append('Bala bala')
    harga.append(1500)
    total += 1500
  elif kode == 2:
    barang.append('Oncom Idad')
    harga.append(1000)
    total += 1000
  elif kode == 3:
    barang.append('Chiken RFC')
    harga.append(500)
    total += 500
  elif kode == 4:
    barang.append('Janda')
    harga.append(10000)
    total += 10000
  else:
    print(f"{m}Kode tidak valid!")
  lanjut = input(f"{k}Lanjut belanja? y/n : {m}")
  if lanjut == 'n':
    print(f"{m}TERIMA KASIH ATAS KUNJUNGANNYA{p}\n")
    break

print(garis)
print(f"{h}Barang yang dibeli : ", barang)
print(f"{h}Harga barang : ", harga)
print(f"{m}Total yang harus dibayar : ", total, "\n")
print(garis)
uang = int(input(f"{k}Masukan jumlah uang anda : {m}"))
if uang > total:
  print(f"{h}Sisa uang anda ", uang - total)
elif uang == total:
  print(f"{h}Uangnya pas")
else:
  print(f"{m}Uang anda kurang", uang - total)
os.system('cat README.md')
