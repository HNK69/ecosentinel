"""EcoSentinel — Dashboard HTML Template"""

def get_template():
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>EcoSentinel — Edge-AI Environmental Intelligence</title>
<meta name="description" content="EcoSentinel: Edge-AI environmental monitoring and illegal activity detection system using TinyML, multi-sensor fusion, and real-time wireless alerts.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{{CSS}}</style>
</head>
<body>

<!-- ════════════════════════════════════════════ HERO ════════════════════════════════════════════ -->
<div class="hero">
  <div class="hero-badge"><span class="dot"></span> EDGE-AI ENVIRONMENTAL INTELLIGENCE</div>
  <h1>Protecting Environmental Zones Through <span>Edge AI Intelligence</span></h1>
  <p class="hero-sub">EcoSentinel is an Edge-AI environmental monitoring and illegal activity detection system using TinyML, multi-sensor fusion, vibration sensing, GPS intelligence, and real-time wireless alerts.</p>
  <div class="hero-btns">
    <button class="btn btn-primary" onclick="scrollTo('dashboard')">Launch Monitoring System</button>
    <button class="btn btn-outline" onclick="scrollTo('architecture')">View Architecture</button>
  </div>
</div>

<!-- ════════════════════════════════════════════ ABOUT ════════════════════════════════════════════ -->
<section id="about">
  <div class="section-label">About</div>
  <h2 class="section-title">Environmental Intelligence at the Edge</h2>
  <p class="section-desc">EcoSentinel deploys TinyML-powered sensor nodes in remote environmental zones, detecting illegal activities through acoustic analysis, vibration profiling, and GPS tracking — all processed at the edge with sub-second latency.</p>
  <div class="about-grid">
    <div class="about-card"><div class="ic">&#x1F399;</div><h3>Acoustic Detection</h3><p>Real-time audio classification identifies chainsaws, excavators, mining equipment, and tractors using MFCC-based TinyML inference.</p></div>
    <div class="about-card"><div class="ic">&#x1F4F3;</div><h3>Vibration Sensing</h3><p>Accelerometer-based vibration profiling detects ground disturbances from heavy machinery and illegal excavation operations.</p></div>
    <div class="about-card"><div class="ic">&#x1F4E1;</div><h3>GPS Intelligence</h3><p>Geofenced monitoring with real-time position tracking enables precise localization of detected threats within protected zones.</p></div>
    <div class="about-card"><div class="ic">&#x26A0;</div><h3>Wireless Alerts</h3><p>Instant alert propagation via WiFi to command centers enables rapid response to detected environmental violations.</p></div>
  </div>
</section>

<!-- ════════════════════════════════════════════ STACK ════════════════════════════════════════════ -->
<section id="stack">
  <div class="section-label">Operational Stack</div>
  <h2 class="section-title">Technology Infrastructure</h2>
  <p class="section-desc">Purpose-built hardware and software stack optimized for edge deployment in remote, power-constrained environments.</p>
  <div class="stack-list">
    <div class="stack-item"><div class="num">01</div><span>ESP32 Microcontroller</span></div>
    <div class="stack-item"><div class="num">02</div><span>INMP441 MEMS Microphone</span></div>
    <div class="stack-item"><div class="num">03</div><span>ADXL345 Accelerometer</span></div>
    <div class="stack-item"><div class="num">04</div><span>NEO-6M GPS Module</span></div>
    <div class="stack-item"><div class="num">05</div><span>TensorFlow Lite Micro</span></div>
    <div class="stack-item"><div class="num">06</div><span>INT8 Quantized CNN Model</span></div>
    <div class="stack-item"><div class="num">07</div><span>Flask Inference Server</span></div>
    <div class="stack-item"><div class="num">08</div><span>WiFi Alert Mechanism</span></div>
  </div>
</section>

<!-- ════════════════════════════════════════════ WORKFLOW ════════════════════════════════════════════ -->
<section id="workflow">
  <div class="section-label">System Workflow</div>
  <h2 class="section-title">Detection Pipeline</h2>
  <p class="section-desc">End-to-end data flow from environmental sensing through AI classification to alert dispatch.</p>
  <div class="workflow-steps">
    <div class="wf-step"><h4>Capture</h4><p>ESP32 samples environmental audio at 16kHz via I2S MEMS microphone and reads vibration data from accelerometer.</p></div>
    <div class="wf-step"><h4>Process</h4><p>3-second audio clips are extracted and converted to 40-coefficient MFCC spectrograms with Z-score normalization.</p></div>
    <div class="wf-step"><h4>Classify</h4><p>INT8-quantized CNN model runs inference on MFCC features, producing probability scores across 6 environmental classes.</p></div>
    <div class="wf-step"><h4>Fuse</h4><p>Acoustic predictions are correlated with vibration signatures and GPS data for multi-sensor threat validation.</p></div>
    <div class="wf-step"><h4>Alert</h4><p>Confirmed threats trigger wireless alerts with GPS coordinates, threat classification, and confidence scores to command center.</p></div>
  </div>
</section>

<!-- ════════════════════════════════════════════ ARCHITECTURE ════════════════════════════════════════════ -->
<section id="architecture">
  <div class="section-label">Architecture</div>
  <h2 class="section-title">System Architecture</h2>
  <p class="section-desc">Distributed edge-cloud architecture with on-device preprocessing and server-side deep inference.</p>
  <div class="arch-diagram">
    <div class="arch-flow">
      <div class="arch-node"><div class="node-label">Sensor</div><div class="node-name">MEMS Mic + ADXL345</div></div>
      <div class="arch-arrow">&#x2192;</div>
      <div class="arch-node"><div class="node-label">Edge</div><div class="node-name">ESP32 Node</div></div>
      <div class="arch-arrow">&#x2192;</div>
      <div class="arch-node"><div class="node-label">Transport</div><div class="node-name">WiFi / HTTP</div></div>
      <div class="arch-arrow">&#x2192;</div>
      <div class="arch-node"><div class="node-label">Inference</div><div class="node-name">Flask + TFLite</div></div>
      <div class="arch-arrow">&#x2192;</div>
      <div class="arch-node"><div class="node-label">Output</div><div class="node-name">Dashboard + Alert</div></div>
    </div>
  </div>
</section>

<!-- ════════════════════════════════════════════ LAUNCH ════════════════════════════════════════════ -->
<div class="launch-section">
  <div class="section-label">Command Center</div>
  <h2 class="section-title">Launch Monitoring System</h2>
  <p class="section-desc" style="margin:0 auto 2rem">Access the integrated real-time surveillance dashboard with AI threat detection, sensor fusion, and alert management.</p>
  <button class="btn btn-primary" onclick="scrollTo('dashboard')">Enter Command Center</button>
</div>

<!-- ════════════════════════════════════════════ DASHBOARD ════════════════════════════════════════════ -->
<div class="dash state-safe" id="dashboard">
  <div class="dash-header">
    <div class="dash-brand">
      <span class="status-dot" id="sys-status-dot"></span>
      <h2>EcoSentinel Command Center</h2>
    </div>
    <div class="dash-meta">
      <span>UPTIME <strong id="sys-uptime">0m</strong></span>
      <span>SCANS <strong id="sys-predictions">0</strong></span>
      <span>THREATS <strong id="sys-threats">0</strong></span>
      <span id="dash-clock">--:--:--</span>
    </div>
  </div>

  <div class="dash-grid">
    <!-- ── AI THREAT DETECTION ── -->
    <div class="panel" id="panel-threat">
      <div class="panel-head">
        <h3>&#x1F916; AI Threat Detection</h3>
        <span class="tag tag-safe" id="threat-tag">STANDBY</span>
      </div>
      <div class="panel-body">
        <div class="threat-display">
          <div class="threat-class" id="threat-class" style="color:var(--text-muted)">Awaiting Input</div>
          <div class="threat-conf" id="threat-conf">No audio analyzed</div>
        </div>
        <div class="score-bars">
          <div class="score-row"><span class="score-label">chainsaw</span><div class="score-track"><div class="score-fill" id="bar-chainsaw" style="width:0%"></div></div><span class="score-val" id="val-chainsaw">—</span></div>
          <div class="score-row"><span class="score-label">excavator</span><div class="score-track"><div class="score-fill" id="bar-excavator" style="width:0%"></div></div><span class="score-val" id="val-excavator">—</span></div>
          <div class="score-row"><span class="score-label">forest</span><div class="score-track"><div class="score-fill" id="bar-forest" style="width:0%"></div></div><span class="score-val" id="val-forest">—</span></div>
          <div class="score-row"><span class="score-label">mining</span><div class="score-track"><div class="score-fill" id="bar-mining" style="width:0%"></div></div><span class="score-val" id="val-mining">—</span></div>
          <div class="score-row"><span class="score-label">noise</span><div class="score-track"><div class="score-fill" id="bar-noise" style="width:0%"></div></div><span class="score-val" id="val-noise">—</span></div>
          <div class="score-row"><span class="score-label">tractor</span><div class="score-track"><div class="score-fill" id="bar-tractor" style="width:0%"></div></div><span class="score-val" id="val-tractor">—</span></div>
        </div>
      </div>
    </div>

    <!-- ── ENVIRONMENTAL RADAR ── -->
    <div class="panel" id="panel-radar">
      <div class="panel-head">
        <h3>&#x1F4E1; Environmental Radar</h3>
        <span class="tag tag-safe">SCANNING</span>
      </div>
      <div class="panel-body">
        <div class="radar-container">
          <div class="radar-bg">
            <div class="radar-ring"></div>
            <div class="radar-ring"></div>
            <div class="radar-ring"></div>
            <div class="radar-cross"></div>
            <div class="radar-cross-v"></div>
            <div class="radar-sweep"></div>
            <div class="radar-center"></div>
          </div>
        </div>
        <div class="radar-label">Sweep Active — Monitoring Perimeter</div>
      </div>
    </div>

    <!-- ── AUDIO UPLOAD ── -->
    <div class="panel" id="panel-upload">
      <div class="panel-head">
        <h3>&#x1F3A4; Audio Analysis</h3>
        <span class="tag tag-safe">READY</span>
      </div>
      <div class="panel-body">
        <div class="upload-zone" id="upload-zone">
          <div class="uz-icon">&#x1F4C1;</div>
          <div class="uz-text">Drop audio file or click to upload</div>
          <div class="uz-hint">.wav .mp3 .flac .ogg — max 16MB</div>
          <input type="file" id="audio-input" accept=".wav,.mp3,.flac,.ogg,.webm,.m4a" hidden>
        </div>
        <div class="upload-progress" id="upload-progress">
          <div class="prog-bar"><div class="prog-fill" id="prog-fill"></div></div>
          <div class="prog-text" id="prog-text">Processing...</div>
        </div>
      </div>
    </div>

    <!-- ── GPS MONITORING ── -->
    <div class="panel" id="panel-gps">
      <div class="panel-head">
        <h3>&#x1F4CD; GPS Monitoring</h3>
        <span class="tag tag-offline">AWAITING</span>
      </div>
      <div class="panel-body">
        <div class="gps-grid">
          <div class="gps-field"><div class="gps-lbl">Latitude</div><div class="gps-val" style="color:var(--text-muted)">— —</div></div>
          <div class="gps-field"><div class="gps-lbl">Longitude</div><div class="gps-val" style="color:var(--text-muted)">— —</div></div>
          <div class="gps-field"><div class="gps-lbl">Altitude</div><div class="gps-val" style="color:var(--text-muted)">— —</div></div>
          <div class="gps-field"><div class="gps-lbl">Satellites</div><div class="gps-val" style="color:var(--text-muted)">— —</div></div>
        </div>
        <div style="text-align:center;margin-top:10px;font-size:0.7rem;color:var(--text-muted);letter-spacing:0.5px">GPS unavailable — awaiting ESP32 sensor feed</div>
      </div>
    </div>

    <!-- ── VIBRATION MONITORING ── -->
    <div class="panel" id="panel-vib">
      <div class="panel-head">
        <h3>&#x1F4F3; Vibration Monitoring</h3>
        <span class="tag tag-safe">IDLE</span>
      </div>
      <div class="panel-body">
        <div class="vib-wave" id="vib-wave"></div>
        <div class="vib-stats">
          <div class="vib-stat"><div class="vstat-label">X-Axis</div><div class="vstat-val" style="color:var(--text-muted)">—</div></div>
          <div class="vib-stat"><div class="vstat-label">Y-Axis</div><div class="vstat-val" style="color:var(--text-muted)">—</div></div>
          <div class="vib-stat"><div class="vstat-label">Z-Axis</div><div class="vstat-val" style="color:var(--text-muted)">—</div></div>
        </div>
        <div style="text-align:center;margin-top:8px;font-size:0.68rem;color:var(--text-muted)">Sensor offline — awaiting accelerometer data</div>
      </div>
    </div>

    <!-- ── SENSOR FUSION ── -->
    <div class="panel" id="panel-fusion">
      <div class="panel-head">
        <h3>&#x1F517; Sensor Fusion</h3>
        <span class="tag tag-safe">NOMINAL</span>
      </div>
      <div class="panel-body">
        <div class="fusion-ring">
          <svg viewBox="0 0 140 140">
            <circle class="ring-bg" cx="70" cy="70" r="62"/>
            <circle class="ring-fill" id="fusion-fill" cx="70" cy="70" r="62" stroke-dasharray="389.56" stroke-dashoffset="389.56"/>
          </svg>
          <div class="fusion-center">
            <div class="fusion-pct" id="fusion-pct">0%</div>
            <div class="fusion-label">Confidence</div>
          </div>
        </div>
        <div class="fusion-sensors">
          <div class="fusion-s"><div class="s-dot" style="background:var(--safe)"></div><span class="s-name">Audio</span></div>
          <div class="fusion-s"><div class="s-dot" style="background:var(--text-muted)"></div><span class="s-name">Vibration</span></div>
          <div class="fusion-s"><div class="s-dot" style="background:var(--text-muted)"></div><span class="s-name">GPS</span></div>
          <div class="fusion-s"><div class="s-dot" style="background:var(--safe)"></div><span class="s-name">Server</span></div>
        </div>
      </div>
    </div>

    <!-- ── ALERT TIMELINE ── -->
    <div class="panel" id="panel-timeline" style="grid-column:1/-1">
      <div class="panel-head">
        <h3>&#x1F4CB; Alert Timeline</h3>
        <span class="tag tag-safe">MONITORING</span>
      </div>
      <div class="panel-body">
        <div class="timeline" id="alert-timeline">
          <div class="tl-entry">
            <div class="tl-time">--:--</div>
            <div class="tl-icon tl-icon-safe">~</div>
            <div class="tl-content"><div class="tl-title">System Initialized</div><div class="tl-desc">Awaiting sensor input — upload audio or connect ESP32 node</div></div>
          </div>
        </div>
      </div>
    </div>

  </div>
</div>

<!-- ── FOOTER ── -->
<div class="site-footer">
  <p>EcoSentinel Environmental Intelligence System &mdash; Edge-AI Powered</p>
</div>

<script>{{JS}}</script>
</body>
</html>"""
