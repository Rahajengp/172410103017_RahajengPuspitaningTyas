nama = str()
jumlah_makan=0
harga=7000
total=int()

nama=input("Masukkan nama:")
jumlah_makan=input("Masukkan jumlah makan")
if str (nama =="agus"):
  harga=6000
  print ( harga)
else:
  if jumlah_makan>10:
  
    total =((jumlah_makan*harga)-2000)
    print (total)
  else:
    if jumlah_makan>5:
      total=((jumlah_makan*harga)-1000)
      print (total)
    else:
      total=(jumlah_makan*harga)


