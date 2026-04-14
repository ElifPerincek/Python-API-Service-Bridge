# 🌐 Python API Server & Client Interface Bridge

Bu proje, bir sistemin (Sunucu/Server) arka planda sürekli çalışarak veri üretmesi ve başka bir arayüzün (İstemci/Client) bu verileri bir API üzerinden sorgulaması mantığını (Decoupled Architecture) göstermek amacıyla hazırlanmıştır.

Özellikle otonom sistem simülasyonları ve görüntü işleme projelerinde, ağır işlem yükünü (Backend) kullanıcı arayüzünden (Frontend) ayırmak için bu mimari standart kabul edilir.

---

## 🚀 1. Bölüm: Neden Bu Mimariyi Kullandık?

Bu yapının klasik tek dosyalık scriptlere göre sağladığı kritik avantajlar şunlardır:

* **Performans (Decoupling):** Görüntü işleme veya karmaşık hesaplamalar arayüzü dondurmaz.
* **Modülerlik:** Sunucu Python'da kalırken, ileride istemci farklı bir dilde (C#, Java, Javascript) yazılabilir.
* **Dağıtık Sistemler:** Sunucu ve istemci farklı bilgisayarlarda veya ağlarda çalışabilir.



---

## 🛠️ 2. Bölüm: Kurulum ve Çalıştırma

### Gereksinimler
Sistemi çalıştırmak için `Flask` ve `requests` kütüphanelerinin yüklü olması gerekir:
```bash
pip install flask requests
Adım Adım Kullanım
API Server'ı Başlat (Enable Server):
İlk olarak server.py dosyasını çalıştırın. Sunucu varsayılan olarak 5000 portu üzerinden dinlemeye başlar.

Bash
python server.py
Arayüz Üzerinden Sorgula (Client Interface):
Sunucu aktifken client_interface.py dosyasını çalıştırın. Bu program, API üzerinden sunucuya "Sistem durumu nedir?" sorusunu soracak ve yanıtı ekrana yazdıracaktır.

Bash
python client_interface.py
📊 3. Bölüm: Sistem İşleyişi (Logic)
Notlarımda belirttiğim "Program arayüzü ile sorduk" mantığı şu şekilde işlemektedir:

API Endpoint (/get_detection): Sunucu, otonom sistemden gelen koordinat ve tespit verilerini JSON formatında hazır tutar.

HTTP GET Request: İstemci, bu adrese bir istek gönderir.

JSON Response: Sunucu, o anki güncel veriyi paketleyip istemciye döner.

🎓 Hazırlayan
Elif Perincek 
