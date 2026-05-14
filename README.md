# EcoSentinel — Edge-AI Environmental Monitoring System

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Server

```bash
cd backend
python app.py
```

The server starts at `http://0.0.0.0:5000`

### 3. Open Dashboard

Navigate to `http://localhost:5000` in your browser.

---

## API Endpoints

### `POST /predict`

Upload audio for AI threat detection.

**Request:**
```bash
curl -X POST http://localhost:5000/predict \
  -F "audio=@sample.wav"
```

**Response:**
```json
{
  "predicted_class": "chainsaw",
  "confidence": 0.91,
  "is_threat": true,
  "timestamp": "2026-05-14T13:00:00+00:00",
  "all_scores": {
    "chainsaw": 0.91,
    "excavator": 0.03,
    "forest": 0.02,
    "mining": 0.01,
    "noise": 0.02,
    "tractor": 0.01
  },
  "audio_duration_seconds": 3.0,
  "clips_analyzed": 1,
  "request_id": "a1b2c3d4",
  "inference_latency_ms": 125.3
}
```

### `GET /health`

System health check.

### `GET /api/status`

Live system status for dashboard polling.

### `GET /`

Integrated ESP32-compatible dashboard.

---

## ESP32 Upload Example (Arduino)

```cpp
#include <WiFi.h>
#include <HTTPClient.h>

void uploadAudio(uint8_t* buffer, size_t len) {
  HTTPClient http;
  http.begin("http://<SERVER_IP>:5000/predict");
  http.addHeader("Content-Type", "multipart/form-data; boundary=----boundary");
  
  String head = "------boundary\r\nContent-Disposition: form-data; name=\"audio\"; filename=\"clip.wav\"\r\nContent-Type: audio/wav\r\n\r\n";
  String tail = "\r\n------boundary--\r\n";
  
  size_t totalLen = head.length() + len + tail.length();
  uint8_t* payload = (uint8_t*)malloc(totalLen);
  
  memcpy(payload, head.c_str(), head.length());
  memcpy(payload + head.length(), buffer, len);
  memcpy(payload + head.length() + len, tail.c_str(), tail.length());
  
  int code = http.POST(payload, totalLen);
  String response = http.getString();
  
  Serial.println(response);
  free(payload);
  http.end();
}
```

---

## Project Structure

```
idp/
├── ecosentinel_int8.tflite    # TFLite INT8 model
├── label_map.json             # Class label mapping
├── infer.py                   # Original inference pipeline
├── requirements.txt           # Python dependencies
├── backend/
│   ├── app.py                 # Flask application
│   ├── config.py              # Configuration
│   ├── models/
│   │   └── engine.py          # Inference engine wrapper
│   └── utils/
│       ├── logger.py          # Logging system
│       └── cleanup.py         # Upload cleanup
└── frontend/
    ├── dashboard.py           # HTML assembler
    ├── styles.py              # CSS styles
    ├── scripts.py             # JavaScript
    └── template.py            # HTML template
```

## Detection Classes

| Class | Type | Description |
|-------|------|-------------|
| chainsaw | THREAT | Chainsaw activity detection |
| excavator | THREAT | Excavator/heavy equipment |
| mining | THREAT | Illegal mining activity |
| tractor | THREAT | Tractor/machinery movement |
| forest | SAFE | Natural forest sounds |
| noise | SAFE | Background/ambient noise |
