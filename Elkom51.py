print("@   @  @@@@@  @    @  @@@@    @@@@@")
print(" @ @   @   @  @ @  @  @   @   @   @")
print("  @    @@@@@  @  @ @  @    @  @@@@@")
print("  @    @   @  @   @@  @   @   @   @")
print("  @    @   @  @    @  @@@@    @   @")


masukan = int(input("Mau berapa bilangan kak: "))
masukan2=int(input("masukan angka yang ke-1: "))
masukan3 = int(input("masukan angka yang ke-2: "))
for i in range(masukan):
  v=masukan2
  
  x = masukan2+masukan3
  masukan2=masukan3
  masukan3=x
  print(v)