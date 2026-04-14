import requests
import json

BASE_URL = "http://localhost:5000"

def sistemi_sorgula():
    """Sunucudaki güncel durumu sorar."""
    try:
        response = requests.get(f"{BASE_URL}/get_detection")
        if response.status_code == 200:
            veriler = response.json()
            print(f"--- SİSTEM DURUMU ({veriler['last_update']}) ---")
            print(f"Hedef Tespit Edildi mi: {'Evet' if veriler['target_detected'] else 'Hayır'}")
            print(f"Hedef Türü: {veriler['target_type']}")
            print(f"Koordinatlar: X:{veriler['coordinates']['x']} Y:{veriler['coordinates']['y']}")
    except Exception as e:
        print("Hata: Sunucu aktif değil!")

def komut_gonder(eylem):
    """Sunucuya bir komut gönderir."""
    payload = {"action": eylem}
    response = requests.post(f"{BASE_URL}/set_command", json=payload)
    print("Sunucu Yanıtı:", response.json()['message'])

if __name__ == '__main__':
    # 1. Önce durumu sorgulayalım
    sistemi_sorgula()
    
    # 2. Sunucuya bir komut gönderelim
    komut_gonder("ANGALMANI_BASLAT")
