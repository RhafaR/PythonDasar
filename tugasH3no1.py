import turtle

# Inisialisasi tampilan Turtle
t = turtle.Turtle()
t.speed(10)  # Atur kecepatan gambar (1 = lambat, 10 = cepat)

# Fungsi untuk menggambar persegi panjang
def persegi_panjang(panjang, lebar):
    for _ in range(2):
        t.forward(panjang)
        t.left(90)
        t.forward(lebar)
        t.left(90)


def segitiga(sisi):
    for _ in range(3):
        t.forward(sisi)
        t.left(120)

# Fungsi untuk menggambar trapesium
def trapesium(panjang_atas, panjang_bawah, tinggi):
    for _ in range(4):
    t.forward(panjang_atas)
    t.left(90)
    t.forward(tinggi)
    t.left(90)
    t.forward(panjang_bawah)
    t.left(90)
    t.forward(tinggi)
    t.left(90)

# Fungsi untuk menggambar jajar genjang
def jajar_genjang(panjang, tinggi):
    for _ in range(5):
    t.forward(panjang)
    t.left(45)
    t.forward(tinggi)
    t.left(135)
    t.forward(panjang)
    t.left(45)
    t.forward(tinggi)

# Fungsi untuk menggambar belah ketupat
def belah_ketupat(sisi, sudut):
    for _ in range(2):
        t.forward(sisi)
        t.left(sudut)
    t.left(180 - sudut)
    for _ in range(2):
        t.forward(sisi)
        t.left(sudut)

# Menggambar bangun datar
persegi_panjang(100, 50)
t.penup()
t.goto(150, 0)
t.pendown()
segitiga(100)
t.penup()
t.goto(250, 0)
t.pendown()
trapesium(80, 150, 50)
t.penup()
t.goto(350, 0)
t.pendown()
jajar_genjang(100, 70)
t.penup()
t.goto(450, 0)
t.pendown()
belah_ketupat(70, 45)

# Menutup jendela Turtle saat di-klik
turtle.exitonclick()