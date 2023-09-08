print ("Menghitung Keliling dan Luas Persegi Panjang")
p = int(input("Masukan panjang persegi panjang :"))
l = int(input("Masukan lebar persegi panjang :"))

luas = p * l
keliling = 2 * (p+l)

print(f'luas persegi panjang adalah \t : {luas}')
print(f'Keliling persegi panjang adalah \t : {keliling}')

print("\nMenghitung keliling dan luas persegi")
s = int(input('masukan panjang persegi :'))
luas = s * s
keliling = 4 * s

print(f'luas persegi panjang \t : {luas}')
print(f'Keliling persegi panjang adalah \t : {keliling}')


print("\nMenghitung keliling dan luas trapesium")
a = float(input('Masukan sisi a :'))
b = float(input('Masukan sisi b :'))
c = float(input('Masukan sisi c :'))
d = float(input('Masukan sisi d :'))
t = float(input("masukan tinggi :"))

luas = 0.5 * (a+b) * t
keliling = a+b+c+d
print('luas Trapesium adalah \t\t : {luas}')
print('Keliling Trapesium adalah \t : {keliling}')