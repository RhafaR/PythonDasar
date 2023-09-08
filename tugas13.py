class Vehicle:
    def __init__(self, merk, tahun, warna, model):
        self.merk = merk
        self.tahun = tahun
        self.warna = warna

    def tampilan_info(self):
        print(f"Merk: {self.merk}")
        print(f"Tahun: {self.tahun}")
        print(f"Warna: {self.warna}")

class Car(Vehicle):
    def __init__(self, merk, tahun, warna, model):
        super().__init__(merk, tahun, warna)
        self.model = model  
        
    def tampilan_info(self):
        super().tampilkan_info()
        print(f"Model: {self.model}")

if __name__ == "__main__":
    car = Car("Toyota", 2022, "Merah", "Camry")

    print("Info Kendaraan")
    car.tampilan_info()