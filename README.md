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
