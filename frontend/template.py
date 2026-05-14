"""EcoSentinel — HTML Templates (Landing + Dashboard)"""


def get_landing_template():
    """Cinematic landing page served at /"""
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>EcoSentinel — Edge-AI Environmental Intelligence</title>
<meta name="description" content="EcoSentinel: Edge-AI environmental monitoring and illegal activity detection system.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>{{LANDING_CSS}}</style>
</head>
<body>

<!-- Cinematic Background Layers -->
<canvas id="particle-canvas"></canvas>
<div class="fog"></div>
<div class="topo-overlay"></div>
<div class="scan-line"></div>

<div class="page-content">

<!-- NAVBAR -->
<nav class="nav">
  <div class="nav-container">
    <div class="logo">
      <span class="logo-icon"></span>
      <span class="logo-text">ECO<span>SENTINEL</span></span>
    </div>
    <div class="nav-links">
      <a href="/dashboard" class="nav-btn">COMMAND CENTER</a>
    </div>
  </div>
</nav>

<!-- HERO -->
<div class="hero">
  <div class="hero-badge"><span class="dot"></span> EDGE-AI ENVIRONMENTAL INTELLIGENCE</div>
  <h1 class="hero-title">
    <span class="line">Protecting Environmental Zones</span>
    <span class="line">Through <span class="accent">Edge AI Intelligence</span></span>
  </h1>
  <p class="hero-sub">EcoSentinel deploys TinyML-powered sensor nodes in protected zones — detecting chainsaws, excavators, and illegal operations through acoustic AI, vibration profiling, and GPS intelligence at the edge.</p>
  <div class="hero-btns">
    <a class="btn btn-primary" href="/dashboard">&#x25B6; Launch Monitoring System</a>
    <button class="btn btn-outline" onclick="smoothScroll('about')">Explore System</button>
  </div>
</div>

<!-- ABOUT -->
<section id="about">
  <div class="sr">
    <div class="section-label">About</div>
    <h2 class="section-title">Environmental Intelligence at the Edge</h2>
    <p class="section-desc">EcoSentinel deploys TinyML-powered sensor nodes in remote zones, detecting illegal activities through acoustic analysis, vibration profiling, and GPS tracking — all processed at the edge with sub-second latency.</p>
  </div>
  <div class="about-grid">
    <div class="about-card sr sr-delay-1"><div class="ic">&#x1F399;</div><h3>Acoustic Detection</h3><p>Real-time audio classification identifies chainsaws, excavators, mining equipment, and tractors using MFCC-based TinyML inference.</p></div>
    <div class="about-card sr sr-delay-2"><div class="ic">&#x1F4F3;</div><h3>Vibration Sensing</h3><p>Accelerometer-based vibration profiling detects ground disturbances from heavy machinery and illegal excavation operations.</p></div>
    <div class="about-card sr sr-delay-3"><div class="ic">&#x1F4E1;</div><h3>GPS Intelligence</h3><p>Geofenced monitoring with real-time position tracking enables precise localization of detected threats within protected zones.</p></div>
    <div class="about-card sr sr-delay-4"><div class="ic">&#x26A0;</div><h3>Wireless Alerts</h3><p>Instant alert propagation via WiFi to command centers enables rapid response to detected environmental violations.</p></div>
  </div>
</section>

<!-- STACK -->
<section id="stack">
  <div class="sr">
    <div class="section-label">Operational Stack</div>
    <h2 class="section-title">Technology Infrastructure</h2>
    <p class="section-desc">Purpose-built hardware and software stack optimized for edge deployment in remote, power-constrained environments.</p>
  </div>
  <div class="stack-list">
    <div class="stack-item sr sr-delay-1"><div class="num">01</div><span>ESP32 Microcontroller</span></div>
    <div class="stack-item sr sr-delay-1"><div class="num">02</div><span>INMP441 MEMS Microphone</span></div>
    <div class="stack-item sr sr-delay-2"><div class="num">03</div><span>ADXL345 Accelerometer</span></div>
    <div class="stack-item sr sr-delay-2"><div class="num">04</div><span>NEO-6M GPS Module</span></div>
    <div class="stack-item sr sr-delay-3"><div class="num">05</div><span>TensorFlow Lite Micro</span></div>
    <div class="stack-item sr sr-delay-3"><div class="num">06</div><span>INT8 Quantized CNN Model</span></div>
    <div class="stack-item sr sr-delay-4"><div class="num">07</div><span>Flask Inference Server</span></div>
    <div class="stack-item sr sr-delay-4"><div class="num">08</div><span>WiFi Alert Mechanism</span></div>
  </div>
</section>

<!-- WORKFLOW -->
<section id="workflow">
  <div class="sr">
    <div class="section-label">System Workflow</div>
    <h2 class="section-title">Detection Pipeline</h2>
    <p class="section-desc">End-to-end data flow from environmental sensing through AI classification to alert dispatch.</p>
  </div>
  <div class="workflow-steps">
    <div class="wf-step sr sr-delay-1"><h4>Capture</h4><p>ESP32 samples environmental audio at 16kHz via I2S MEMS microphone and reads vibration data from accelerometer.</p></div>
    <div class="wf-step sr sr-delay-2"><h4>Process</h4><p>3-second audio clips are extracted and converted to 40-coefficient MFCC spectrograms with Z-score normalization.</p></div>
    <div class="wf-step sr sr-delay-3"><h4>Classify</h4><p>INT8-quantized CNN model runs inference on MFCC features, producing probability scores across 6 environmental classes.</p></div>
    <div class="wf-step sr sr-delay-3"><h4>Fuse</h4><p>Acoustic predictions are correlated with vibration signatures and GPS data for multi-sensor threat validation.</p></div>
    <div class="wf-step sr sr-delay-4"><h4>Alert</h4><p>Confirmed threats trigger wireless alerts with GPS coordinates, threat classification, and confidence scores.</p></div>
  </div>
</section>

<!-- ARCHITECTURE -->
<section id="architecture">
  <div class="sr">
    <div class="section-label">Architecture</div>
    <h2 class="section-title">System Architecture</h2>
    <p class="section-desc">Distributed edge-cloud architecture with on-device preprocessing and server-side deep inference.</p>
  </div>
  <div class="arch-diagram sr sr-delay-1">
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

<!-- LAUNCH CTA -->
<div class="launch-section sr">
  <div class="section-label">Command Center</div>
  <h2 class="section-title">Launch Monitoring System</h2>
  <p class="section-desc" style="margin:0 auto 2rem">Access the integrated real-time surveillance dashboard with AI threat detection, sensor fusion, and alert management.</p>
  <a class="btn btn-primary" href="/dashboard">&#x25B6; Enter Command Center</a>
</div>

<!-- FOOTER -->
<div class="site-footer">
  <p>EcoSentinel Environmental Intelligence System &mdash; Edge-AI Powered</p>
</div>

</div><!-- /page-content -->

<script>
// ── Particle System ──
(function(){
  var c=document.getElementById('particle-canvas'),ctx=c.getContext('2d');
  var particles=[],count=55,mouse={x:-999,y:-999};
  function resize(){c.width=window.innerWidth;c.height=window.innerHeight;}
  resize();window.addEventListener('resize',resize);
  document.addEventListener('mousemove',function(e){mouse.x=e.clientX;mouse.y=e.clientY;});
  for(var i=0;i<count;i++){
    particles.push({x:Math.random()*c.width,y:Math.random()*c.height,
      vx:(Math.random()-0.5)*0.3,vy:-Math.random()*0.4-0.1,
      r:Math.random()*2+0.5,a:Math.random()*0.5+0.15});
  }
  function draw(){
    ctx.clearRect(0,0,c.width,c.height);
    for(var i=0;i<particles.length;i++){
      var p=particles[i];
      p.x+=p.vx;p.y+=p.vy;
      if(p.y<-10){p.y=c.height+10;p.x=Math.random()*c.width;}
      if(p.x<-10)p.x=c.width+10;
      if(p.x>c.width+10)p.x=-10;
      ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
      ctx.fillStyle='rgba(0,232,123,'+p.a+')';ctx.fill();
      // connections
      for(var j=i+1;j<particles.length;j++){
        var q=particles[j],dx=p.x-q.x,dy=p.y-q.y,d=dx*dx+dy*dy;
        if(d<14000){
          ctx.beginPath();ctx.moveTo(p.x,p.y);ctx.lineTo(q.x,q.y);
          ctx.strokeStyle='rgba(0,232,123,'+(0.06*(1-d/14000))+')';
          ctx.lineWidth=0.5;ctx.stroke();
        }
      }
      // mouse interaction
      var mx=p.x-mouse.x,my=p.y-mouse.y,md=mx*mx+my*my;
      if(md<22000){
        ctx.beginPath();ctx.moveTo(p.x,p.y);ctx.lineTo(mouse.x,mouse.y);
        ctx.strokeStyle='rgba(0,232,123,'+(0.1*(1-md/22000))+')';
        ctx.lineWidth=0.6;ctx.stroke();
      }
    }
    requestAnimationFrame(draw);
  }
  draw();
})();

// ── Scroll Reveal ──
(function(){
  var obs=new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if(e.isIntersecting){e.target.classList.add('visible');obs.unobserve(e.target);}
    });
  },{threshold:0.12,rootMargin:'0px 0px -40px 0px'});
  document.querySelectorAll('.sr').forEach(function(el){obs.observe(el);});
})();

// ── Smooth Scroll ──
function smoothScroll(id){
  var el=document.getElementById(id);
  if(el)el.scrollIntoView({behavior:'smooth',block:'start'});
}
</script>
</body>
</html>"""


def get_dashboard_template():
    """Dashboard page served at /dashboard"""
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>EcoSentinel — Command Center</title>
<meta name="description" content="EcoSentinel real-time monitoring dashboard with AI threat detection, sensor fusion, and alert management.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{{CSS}}</style>
</head>
<body>

<div class="dash state-safe" id="dashboard">
  <div class="dash-header">
    <div class="dash-brand">
      <a href="/" class="back-btn" title="Back to Landing Page">&#x2190;</a>
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
    <!-- AI THREAT DETECTION -->
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

    <!-- ENVIRONMENTAL RADAR -->
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

    <!-- AUDIO UPLOAD -->
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

    <!-- GPS MONITORING -->
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

    <!-- VIBRATION MONITORING -->
    <div class="panel" id="panel-vib">
      <div class="panel-head">
        <h3>&#x1F4F3; Vibration Monitoring</h3>
        <span class="tag tag-safe" id="vib-tag">IDLE</span>
      </div>
      <div class="panel-body">
        <div class="vib-wave" id="vib-wave"></div>
        <div class="vib-status-container" id="vib-status-container">
          <div class="vib-status-label" id="vib-status-text">Monitoring Stable</div>
          <div class="vib-activity-indicator"></div>
        </div>
        <div style="text-align:center;margin-top:10px;font-size:0.68rem;color:var(--text-muted)" id="vib-footer">Secure Perimeter &mdash; Vibration Scanning Active</div>
      </div>
    </div>

    <!-- SENSOR FUSION -->
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

    <!-- ALERT TIMELINE -->
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

<!-- FOOTER -->
<div class="site-footer">
  <p>EcoSentinel Environmental Intelligence System &mdash; Edge-AI Powered</p>
</div>

<script>{{JS}}</script>
</body>
</html>"""
