class Kullanici:
    def __init__(self, isim, soyisim, yaş):
        self.isim = isim
        self.soyisim = soyisim
        self.yaş = yaş

    def show_info(self):
        print(f"İsim: {self.isim}\nSoyisim: {self.soyisim}\nYaş: {self.yaş}\n")

    @staticmethod
    def selamla(isim,soyisim):
        print(f"Merhaba {isim} {soyisim}!\n")

    def yaş_kontrol(self):
        if self.yaş < 18:
            print("\n18 yaşından küçükler bu testi yapamaz!")
            return True
        else:
            return False

class KişilikTesti(Kullanici):
    sorular = [
                "Yalnız kalmak yerine başkalarıyla vakit geçirmeyi tercih ederim ", ## sosyallik
                "Yeni insanlarla tanışmaktan hoşlanırım ", ## sosyallik
                "Başka birinin üzüldüğünü gördüğünüzde, onunla duygusal olarak bağ kurma isteği duyuyorum ", ## duygusallık
                "Küçük olaylar veya sözler beni çok kırar ", ## duygusallık
                "Yeni şeyler öğrenmeye ve farklı bakış açıları geliştirmeye istekliyim ", ## yenilikçilik
                "Yapmakta olduğunuz işin rutine bağlanmasını istemem ", ## yenilikçilik
                "Bir proje veya etkinlikte sorumluluk almakta zorlanmam ", ## liderlik
                "Zorlu bir projeyi yönetmek için inisiyatif almak konusunda kendime güveniyorum " # liderlik
            ]

    def __init__(self, isim, soyisim, yaş):
        super().__init__(isim, soyisim, yaş)
        self.sosyallik = []
        self.duygusallık = []
        self.yenilikçilik = []
        self.liderlik = []
    
    def soruları_yazdır(self):
        print("\n----------SORULAR----------")
        for soru in self.sorular:
            print(soru)
        print()

    def testi_baslat(self):
        sayac = 0
        while len(self.sosyallik) < 2:
            try:
                print(self.sorular[sayac])
                cevap = int(input("CEVABINIZI BURAYA GİRİNİZ(1-10): "))
                if 1 <= cevap <= 10:
                    self.sosyallik.append(cevap)
                    sayac += 1
                else:
                    print("Lütfen 1-10 arasında bir değer giriniz.")
            except ValueError:
                print("Lütfen geçerli bir sayı giriniz!")
                continue
        self.sosyallik = sum(self.sosyallik)

        sayac2 = 2
        while len(self.duygusallık) < 2:
            try:
                print(self.sorular[sayac2])
                cevap = int(input("CEVABINIZI BURAYA GİRİNİZ(1-10): "))
                if 1 <= cevap <= 10:
                    self.duygusallık.append(cevap)
                    sayac2 += 1
                else:
                    print("Lütfen 1-10 arasında bir değer giriniz.")
            except ValueError:
                print("Lütfen geçerli bir sayı giriniz!")
                continue
        self.duygusallık = sum(self.duygusallık)

        sayac3 = 4
        while len(self.yenilikçilik) < 2:
            try:
                print(self.sorular[sayac3])
                cevap = int(input("CEVABINIZI BURAYA GİRİNİZ(1-10): "))
                if 1 <= cevap <= 10:
                    self.yenilikçilik.append(cevap)
                    sayac3 += 1
                else:
                    print("Lütfen 1-10 arasında bir değer giriniz.")
            except ValueError:
                print("Lütfen geçerli bir sayı giriniz!")
                continue
        self.yenilikçilik = sum(self.yenilikçilik)

        sayac4 = 6
        while len(self.liderlik) < 2:
            try:
                print(self.sorular[sayac4])
                cevap = int(input("CEVABINIZI BURAYA GİRİNİZ(1-10): "))
                if 1 <= cevap <= 10:
                    self.liderlik.append(cevap)
                    sayac4 += 1
                else:
                    print("Lütfen 1-10 arasında bir değer giriniz.")
            except ValueError:
                print("Lütfen geçerli bir sayı giriniz!")
                continue
        self.liderlik = sum(self.liderlik)

class Analiz(KişilikTesti):
    def __init__(self, isim, soyisim, yaş):
        super().__init__(isim, soyisim, yaş)
        self.değerlendirme = {
            "sosyallik" : "",
            "duygusallik": "",
            "yenilikcilik": "",
            "liderlik": ""      
        }

    def analiz_yap(self):
        if self.sosyallik < 7:
            self.değerlendirme["sosyallik"] = "Asosyal bir insansınız, başka insanlarla bir araya gelmek size katlanılmaz geliyor."
        elif 7 < self.sosyallik < 12:
            self.değerlendirme["sosyallik"] = "Sosyal bir insansınız. Farklı insanlarla tanışmaktan fazla çekinmezsiniz."
        else:
            self.değerlendirme["sosyallik"] = "Yeni insanlarla tanışmak size heyecan veriyor! Aşırı sosyal bir insansınız ve bunu her alanda gösteriyorsunuz."


        if self.duygusallık < 7:
            self.değerlendirme["duygusallık"] = "Bununla birlikte duygularınız yerine mantığınızı kullanmayı tercih ediyorsunuz. Duygusal olmaktan fazlasıyla uzaksınız."
        elif 7 < self.duygusallık < 12:
            self.değerlendirme["duygusallık"] = "Bununla birlikte ne az ne de çok duygusal bir insansınız. Duygularınızın sizi yönetmesine izin vermiyorsunuz ama tamamen hissiz de değilsiniz."
        else:
            self.değerlendirme["duygusallık"] = "Bununla birlikte çok duygusal bir insansınız. İnsanlarla bağ kurmak ve onları anlamak istiyorsunuz."


        if self.yenilikçilik < 7:
            self.değerlendirme["yenilikçilik"] = "Geleneksel bir düşünce yapısına sahipsiniz ve yeniliklere pek açık sayılmazsınız."
        elif 7 < self.yenilikçilik < 12:
            self.değerlendirme["yenilikçilik"] = "Yeniliklere açık bir insansınız ve farklı düşüncelere açıksınız."
        else:
            self.değerlendirme["yenilikçilik"] = "Çok yenilikçi ve yaratıcı bir insansınız. Yenilik kelimesi adeta sizi heyecenlandırmaya yetiyor."


        if self.liderlik < 7:
            self.değerlendirme["liderlik"] = "Son olarak kişiliğiniz destekleyici bir yapıya sahip. Bir adım öne atılmak yerine geride kalmayı tercih ediyorsunuz."
        elif 7 < self.liderlik < 12:
            self.değerlendirme["liderlik"] = "Son olarak kişiliğiniz pek liderlik yapmaya uygun değil gibi gözüküyor. Biraz daha geri planda kalmak sizin tercihiniz."
        else:
            self.değerlendirme["liderlik"] = "Son olarak diyebiliriz ki tam bir lidersiniz! Kişiliğiniz insan topluluklarını yönetmek için çok uygun."

        
    def sonucu_göster(self):
        print("\nKullanici bilgileri:")
        self.show_info()
        print("\nTest sonucu:", self.değerlendirme["sosyallik"],self.değerlendirme["duygusallık"],self.değerlendirme["yenilikçilik"],self.değerlendirme["liderlik"],)

class VeriTabanı:
    def __init__(self):
        self.profiller = []

    def sonuc_ekle(self, Kullanici):
        self.profiller.append({
            "isim": Kullanici.isim,
            "soyisim": Kullanici.soyisim,
            "yaş": Kullanici.yaş,
            "değerlendirme": Kullanici.değerlendirme
        })

    def profilleri_goster(self):
        if  len(self.profiller) == 0:
            print("\nHenüz bir profil kaydedilmedi!\n")
            return

        print("\n\n----------VERİTABANINDAKİ PROFİLLER----------")
        for profil in self.profiller:
            print()
            print("İsim: ", profil["isim"], "\nSoyisim: ", profil["soyisim"], "\nYaş: ", profil["yaş"])
            
            değerlendirme = profil["değerlendirme"]
            print("Sonucu: ", 
                değerlendirme.get("sosyallik", ""), 
                değerlendirme.get("duygusallık", ""), 
                değerlendirme.get("yenilikçilik", ""), 
                değerlendirme.get("liderlik", ""))
        
        print()

veritabanı1 = VeriTabanı()

print("---------------------------------KİŞİLİK TESTİ---------------------------------")

while True:
    try:
        print("1-Testi başlat\n2-Test sorularını yazdır\n3-Profilleri göster\n4-Programı sonlandır")
        işlem = int(input("Lütfen yapmak istediğiniz işlemi seçiniz(1-4): "))
        if işlem == 1:
            i = str(input("\nİsminiz: "))
            s = str(input("Soyisminiz: "))
            y = int(input("Yaşınız: "))

            Kullanici.selamla(i,s)
            Kullanici1 = Analiz(i,s,y)
            if Kullanici1.yaş_kontrol():
                break            
            print("\nLütfen sorulara kendinizi 1-10 arasında puanlayarak cevaplayınız!")
            Kullanici1.testi_baslat()
            print()

            Kullanici1.analiz_yap()
            Kullanici1.sonucu_göster()
            print()
            veritabanı1.sonuc_ekle(Kullanici1)
        elif işlem == 2:
            Kullanici2 = KişilikTesti("Abdurrahman", "Demirci", 20)
            Kullanici2.soruları_yazdır()
            continue
        elif işlem == 3:
            veritabanı1.profilleri_goster()
        elif işlem == 4:
            print("\nProgram sonlandırılmıştır!")
            print()
            break
        else:
            print("Lütfen 1-4 arası sayı giriniz!")
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz!")