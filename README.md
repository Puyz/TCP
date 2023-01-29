# TCP

Yazılım Proje Dokümantasyonu

 


Proje adı			: TCP ile PC Kontrol Sistemi
Versiyon Numarası		: 1.0
Yayım Tarihi			: 27.12.2022
Hazırlayan 			: Ömer TEMEL - 200542013
 
İçerikler
1.	GİRİŞ	2
1.1	AMAÇ	2
1.2	KAPSAM	3
1.3	TANIMLAR VE KISALTMALAR	3
1.4	REFERANSLAR	3
1.5	HEDEF KİTLE	3
1.6	DOKÜMANA GENEL BAKIŞ	3
2.	GENEL TANIM	4
2.1	ÜRÜNE BAKIŞ	4
2.1.1	Sistem Arayüzleri	4
2.1.2	Yazılım Arayüzleri	5
2.1.3	Saha Uyumlama Gereksinimleri	5
2.2	ÜRÜNÜN İŞLEVLERİ	5
2.3	KISITLAR	6
2.4	BAĞIMLILIKLAR	6
3.	ÖZEL GEREKSİNİMLER	6
3.1	İŞLEVSEL GEREKSİNİMLER	6
3.2	TASARIM KISITLARI	8
3.3	KALİTE ÖZELLİKLERİ	8
4.	GEREKSİNİMLERİN İZLENEBİLİRLİĞİ	9
5.	EKLER	9



1.	Giriş
1.1	Amaç
Bu projenin amacı, bir bilgisayarın diğer bir bilgisayardan TCP (Transmission Control Protocol) üzerinden uzaktan kontrol edilebilmesini sağlamaktır. Bu sayede, bir bilgisayarın uzaktaki bir bilgisayar tarafından kontrol edilebilmesi için gereken yazılım öğelerinin (İstemci, Sunucu) oluşturulması hedeflenmektedir.
1.2	Kapsam
Bu proje, iki bilgisayar arasında bir bağlantı kurulmasını ve bu bağlantı üzerinden bir bilgisayarın diğer bilgisayarı kontrol etmesini sağlayacak bir yazılım sisteminin oluşturulmasını içerecektir. Örneğin, bir bilgisayar üzerinden diğer bilgisayarın ekran görüntüsünü gösterebilir, komut satırına erişebilir, dosya transferi yapabilir ve pano işlemi yapabilir.
1.3	Tanımlar ve Kısaltmalar
PKS	PC Kontrol Sistemi
İstemci	Kurban kişinin arka planda çalışacağı malware
Sunucu	İstemci bilgisayara erişim sağlayacak yazılım

1.4	Referanslar
Bu belge şablonu için, “IEEE Std 830-1998: IEEE Recommended Practice for Software Requirements Specifications” referans alınmıştır.
1.5	Hedef Kitle
•	Bilgisayarına erişilmek istenilen kişiler
1.6	Dokümana Genel Bakış
Bu belge “PKS” projesinin gereksinim belirtimleri belgesidir.
1.Bölüm – Giriş: Projenin amacını, kapsamını ve hedef kitlesini tanımlamıştır.
2.Bölüm – Genel Tanım: Ürüne bakış, ürün işlevleri, kullanıcı özellikleri, varsayımlar ve bağımlılıkları tanımlar.
3.Bölüm – Özel Gereksinimler: Bu bölümde, geliştirilecek sistemde olması istenen özellikler bölümlere ayrılarak açıklanmıştır.
4.Bölüm – Gereksinim İzlenebilirliği: “Özel Gereksinimler” başlığı altında tanımlanan yazılım gereksinimlerinin izlenebilirliği tanımlanmıştır, belge içinde gereksinimler için özel kimlik numaraları kullanılmaktadır.





2.	Genel Tanım
2.1	Ürüne Bakış

 

2.1.1	Sistem Arayüzleri
•	Komut satırı arayüzü
2.1.2	Yazılım Arayüzleri
•	TCP/IP Protokolü
2.1.3	Saha Uyumlama Gereksinimleri
PKS için windows işletim sistemi olması yeterlidir.

2.2	Ürünün İşlevleri
•	Komut satırına erişme
•	Dosya transferi gerçekleştirme
•	Ekran görüntüsü alma
•	Panoya kopyalanan yazıyı öğrenme
2.3	Kısıtlar
•	Projenin gerçekleştirilmesi sırasında mevcut yazılım ve donanım bileşenlerinin yetersiz olması veya olmaması durumunda proje gerçekleştirilemeyebilir.
2.4	Bağımlılıklar
•	Projenin çalışması için TCP/IP protokolünün kurulu olması gerekmektedir.
•	Projenin çalışması için bir bilgisayarın Windows işletim sistemi kurulu olması gerekmektedir.
•	Projenin çalışması için Sunucu ve İstemci bağlı olması gerekmektedir.
•	Projenin çalışması için internet olması gerekmektedir.


3.	Özel Gereksinimler
•	Bu projenin gerçekleştirilmesi için iki adet bilgisayar gerekmektedir. Bu bilgisayarlar birbirlerine TCP üzerinden bağlantı kurabilecek şekilde yapılandırılmalıdır.
•	Bağlantının kesilmesi durumunda sistemin otomatik olarak bağlantıyı tekrar kurması gerekmektedir.
•	Sistemin çalışması sırasında herhangi bir nedenle çökmesi durumunda sistemin otomatik olarak yeniden başlatılması gerekmektedir.
3.1	İşlevsel Gereksinimler
•	Bir bilgisayarın diğer bir bilgisayardan uzaktan masaüstünü gösterme işlevi.
•	Bir bilgisayarın diğer bir bilgisayardan uzaktan komut girişi yapma.
•	Bir bilgisayarın diğer bir bilgisayardan dosya transferi gerçekleştirme.
•	Bir bilgisayarın diğer bir bilgisayardan panoyu okuma işlevi.
 
3.2	Tasarım Kısıtları 
•	Proje TCP/IP protokolü kullanılarak gerçekleştirilecektir.
•	Proje Python programlama dili kullanılarak gerçekleştirilecektir.
•	Proje Windows işletim sistemi üzerinde gerçekleştirilecektir.
3.3	Kalite Özellikleri
3.3.1	Kullanılabilirlik (“Availability”)
PKS, internete bağımlı bir sistem olduğu için internet olduğu sürece kullanılabilir.
3.3.2	Bakım-yapılabilirlik (“Maintainability”)
PKS, istemci bilgisayara bir kere atıldığından ve sisteme gömülü olduğundan bakımı zordur.

4.	Gereksinimlerin İzlenebilirliği
Gereksinimler belirli bir kimliğe (numaraya) göre sıralanmaktadır ve kısaltma ile desteklenmektedir.

 
5.	Ekler
EK-1
 
- Listele
 
- Bağlan ve İstek listesi
 
- CMD (Komut satırı)
 
