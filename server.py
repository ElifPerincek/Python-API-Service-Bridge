from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Simülasyon verisi: Otonom sisteminin tespit sonuçlarını temsil eder
detection_data = {
    "target_detected": True,
    "target_type": "Drone",
    "coordinates": {"x": 120, "y": 450},
    "last_update": time.strftime("%H:%M:%S")
}

@app.route('/get_detection', methods=['GET'])
def get_detection():
    """Program arayüzü bu adrese sorduğunda güncel veriyi döner."""
    detection_data["last_update"] = time.strftime("%H:%M:%S")
    return jsonify(detection_data)

@app.route('/set_command', methods=['POST'])
def set_command():
    """Arayüzden gelen komutları (örn: 'Sistemi Durdur') işler."""
    incoming_command = request.json
    print(f"[SUNUCU] Arayüzden gelen emir: {incoming_command['action']}")
    return jsonify({"status": "success", "message": "Komut alındı!"})

if __name__ == '__main__':
    print("API Server aktif edildi. Port: 5000 üzerinden dinleniyor...")
    # host='0.0.0.0' sayesinde ağdaki diğer cihazlar da bağlanabilir
    app.run(host='0.0.0.0', port=5000, debug=True)
