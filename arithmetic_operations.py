def islem(a, b, range_end=10):
    x = list(range(1, range_end + 1))
    if b == "*":
        return [a * eleman for eleman in x]
    elif b == "+":
        return [a + eleman for eleman in x]
    elif b == "-":
        return [a - eleman for eleman in x]
    elif b == "/":
        return [a / eleman for eleman in x]
    else:
        return None  # Geçersiz işlem girildiğinde None döndürülür

def main():
    while True:  # Ana döngü, kullanıcı doğru sayı girene kadar devam eder
        try:
            a = int(input("Lütfen bir sayı giriniz: "))  # Kullanıcıdan bir sayı alınır
            while True:  # İşlem seçimi için iç içe bir döngü
                b = input("Bir işlem giriniz (*, +, -, /): ")  # Kullanıcıdan bir işlem alınır
                sonuc = islem(a, b)  # İşlem fonksiyonu çağrılır
                if sonuc is not None:  # Geçerli bir işlem girilmişse
                    print(sonuc)  # Sonuç ekrana yazdırılır
                    return  # İşlem başarılı ise fonksiyondan çıkılır
                else:
                    print("Geçersiz işlem, lütfen geçerli bir işlem giriniz: [*, +, -, /]")  # Geçersiz işlem uyarısı verilir
        except ValueError:
            print("Geçersiz sayısal ifade. Lütfen bir tam sayı giriniz.")  # Sayı girişi hatası için uyarı
        except Exception as e:
            print(f"Hata oluştu: {e}")  # Beklenmeyen hatalar için genel bir hata mesajı

if __name__ == "__main__":
    main()
