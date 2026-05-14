"""EcoSentinel — Dashboard JavaScript"""

def get_js():
    return """
const THREAT_CLASSES = new Set(['chainsaw','excavator','mining','tractor']);
const API_BASE = window.location.origin;
let systemState = 'safe'; // safe | warn | crit
let alertTimeline = [];
let vibBars = [];
let pollTimer = null;

// ── INIT ──
function initDashboard() {
  initVibBars();
  initUpload();
  startClock();
  pollStatus();
  pollTimer = setInterval(pollStatus, 5000);
}

// ── CLOCK ──
function startClock() {
  const el = document.getElementById('dash-clock');
  if (!el) return;
  const tick = () => { 
    const d = new Date();
    el.textContent = d.toLocaleTimeString('en-GB', {hour12:false});
  };
  tick(); setInterval(tick, 1000);
}

// ── POLL STATUS ──
async function pollStatus() {
  try {
    const r = await fetch(API_BASE + '/api/status');
    if (!r.ok) return;
    const d = await r.json();
    updateStatusUI(d);
  } catch(e) {
    updateOfflineUI();
  }
}

function updateStatusUI(d) {
  const el = (id) => document.getElementById(id);
  if (el('sys-uptime')) {
    const m = Math.floor((d.uptime_seconds||0)/60);
    el('sys-uptime').textContent = m + 'm';
  }
  if (el('sys-predictions')) el('sys-predictions').textContent = d.total_predictions || 0;
  if (el('sys-threats')) el('sys-threats').textContent = d.total_threats || 0;

  if (d.last_prediction) {
    applyPrediction(d.last_prediction);
  }
}

function updateOfflineUI() {
  const el = document.getElementById('sys-status-dot');
  if (el) el.style.background = '#666';
}

// ── APPLY PREDICTION ──
function applyPrediction(p) {
  const dash = document.getElementById('dashboard');
  if (!dash) return;

  // Determine state
  if (p.is_threat && p.confidence > 0.75) {
    systemState = 'crit';
  } else if (p.is_threat) {
    systemState = 'warn';
  } else {
    systemState = 'safe';
  }

  dash.className = 'dash state-' + systemState;

  // Threat panel
  const tc = document.getElementById('threat-class');
  const tcf = document.getElementById('threat-conf');
  const tTag = document.getElementById('threat-tag');
  if (tc) tc.textContent = p.predicted_class;
  if (tcf) tcf.textContent = (p.confidence * 100).toFixed(1) + '% confidence';
  if (tTag) {
    tTag.className = 'tag ' + (systemState === 'crit' ? 'tag-crit' : systemState === 'warn' ? 'tag-warn' : 'tag-safe');
    tTag.textContent = systemState === 'crit' ? 'CRITICAL' : systemState === 'warn' ? 'WARNING' : 'CLEAR';
  }
  if (tc) tc.style.color = systemState === 'crit' ? 'var(--red-critical)' : systemState === 'warn' ? 'var(--amber)' : 'var(--safe)';

  // Score bars
  if (p.all_scores) {
    Object.entries(p.all_scores).forEach(([cls, val]) => {
      const fill = document.getElementById('bar-' + cls);
      const valEl = document.getElementById('val-' + cls);
      if (fill) fill.style.width = (val * 100) + '%';
      if (valEl) valEl.textContent = (val * 100).toFixed(1) + '%';
      if (fill && THREAT_CLASSES.has(cls) && val > 0.5) {
        fill.style.background = val > 0.75 ? 'var(--red-critical)' : 'var(--amber)';
      } else if (fill) {
        fill.style.background = 'var(--accent)';
      }
    });
  }

  // Add to timeline
  addTimelineEntry(p);

  // Pulse vibration bars
  pulseVibration(systemState);
}

// ── VIBRATION BARS ──
function initVibBars() {
  const container = document.getElementById('vib-wave');
  if (!container) return;
  for (let i = 0; i < 40; i++) {
    const bar = document.createElement('div');
    bar.className = 'vib-bar';
    bar.style.height = (3 + Math.random() * 8) + 'px';
    container.appendChild(bar);
    vibBars.push(bar);
  }
  animateVibIdle();
}

function animateVibIdle() {
  vibBars.forEach((bar, i) => {
    const h = 3 + Math.sin(Date.now()/800 + i * 0.3) * 6 + Math.random() * 3;
    bar.style.height = h + 'px';
    bar.style.background = 'var(--accent)';
  });
  requestAnimationFrame(animateVibIdle);
}

function pulseVibration(state) {
  const color = state === 'crit' ? 'var(--red-critical)' : state === 'warn' ? 'var(--amber)' : 'var(--accent)';
  const intensity = state === 'crit' ? 40 : state === 'warn' ? 25 : 10;
  vibBars.forEach((bar) => {
    bar.style.height = (3 + Math.random() * intensity) + 'px';
    bar.style.background = color;
  });
}

// ── SENSOR FUSION RING ──
function updateFusionRing(pct) {
  const circle = document.getElementById('fusion-fill');
  const label = document.getElementById('fusion-pct');
  if (!circle || !label) return;
  const circumference = 2 * Math.PI * 62;
  const offset = circumference - (pct / 100) * circumference;
  circle.style.strokeDasharray = circumference;
  circle.style.strokeDashoffset = offset;
  label.textContent = pct + '%';
}

// ── TIMELINE ──
function addTimelineEntry(p) {
  const tl = document.getElementById('alert-timeline');
  if (!tl) return;

  const now = new Date();
  const timeStr = now.toLocaleTimeString('en-GB', {hour:'2-digit',minute:'2-digit'});
  const isThreat = p.is_threat;
  const cls = p.predicted_class;
  const conf = (p.confidence * 100).toFixed(1);
  const iconClass = isThreat && p.confidence > 0.75 ? 'tl-icon-crit' : isThreat ? 'tl-icon-warn' : 'tl-icon-safe';
  const icon = isThreat ? '!' : '~';
  const title = isThreat ? cls.toUpperCase() + ' Detected' : 'Environment Normal';
  const desc = conf + '% confidence';

  const entry = document.createElement('div');
  entry.className = 'tl-entry fade-in';
  entry.innerHTML = '<div class="tl-time">' + timeStr + '</div>' +
    '<div class="tl-icon ' + iconClass + '">' + icon + '</div>' +
    '<div class="tl-content"><div class="tl-title">' + title + '</div>' +
    '<div class="tl-desc">' + desc + '</div></div>';

  tl.insertBefore(entry, tl.firstChild);
  
  // Keep max 20 entries
  while (tl.children.length > 20) tl.removeChild(tl.lastChild);
}

// ── FILE UPLOAD ──
function initUpload() {
  const zone = document.getElementById('upload-zone');
  const input = document.getElementById('audio-input');
  if (!zone || !input) return;

  zone.addEventListener('click', () => input.click());
  zone.addEventListener('dragover', (e) => { e.preventDefault(); zone.classList.add('dragover'); });
  zone.addEventListener('dragleave', () => zone.classList.remove('dragover'));
  zone.addEventListener('drop', (e) => {
    e.preventDefault();
    zone.classList.remove('dragover');
    if (e.dataTransfer.files.length) uploadFile(e.dataTransfer.files[0]);
  });
  input.addEventListener('change', () => {
    if (input.files.length) uploadFile(input.files[0]);
    input.value = '';
  });
}

async function uploadFile(file) {
  const prog = document.getElementById('upload-progress');
  const progFill = document.getElementById('prog-fill');
  const progText = document.getElementById('prog-text');
  if (!prog) return;

  prog.classList.add('active');
  progFill.style.width = '20%';
  progText.textContent = 'Uploading ' + file.name + '...';

  const form = new FormData();
  form.append('audio', file);

  try {
    progFill.style.width = '50%';
    progText.textContent = 'Running AI inference...';

    const r = await fetch(API_BASE + '/predict', { method: 'POST', body: form });
    progFill.style.width = '90%';

    if (!r.ok) {
      const err = await r.json();
      throw new Error(err.error || 'Prediction failed');
    }

    const result = await r.json();
    progFill.style.width = '100%';
    progText.textContent = 'Detection: ' + result.predicted_class.toUpperCase() + ' (' + (result.confidence * 100).toFixed(1) + '%)';

    applyPrediction(result);
    updateFusionRing(Math.round(result.confidence * 100));

    // Update sensor states
    const dots = document.querySelectorAll('.fusion-s .s-dot');
    dots.forEach(d => d.style.background = 'var(--safe)');

    setTimeout(() => { prog.classList.remove('active'); }, 4000);
  } catch(e) {
    progFill.style.width = '100%';
    progFill.style.background = 'var(--red-critical)';
    progText.textContent = 'Error: ' + e.message;
    setTimeout(() => {
      prog.classList.remove('active');
      progFill.style.background = 'var(--accent-bright)';
    }, 4000);
  }
}

// ── SMOOTH SCROLL ──
function scrollTo(id) {
  const el = document.getElementById(id);
  if (el) el.scrollIntoView({behavior:'smooth',block:'start'});
}

// ── BOOT ──
document.addEventListener('DOMContentLoaded', () => {
  initDashboard();
  updateFusionRing(0);

  // Intersection observer for fade-in
  const obs = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('fade-in'); obs.unobserve(e.target); }});
  }, {threshold:0.1});
  document.querySelectorAll('section,.panel').forEach(el => obs.observe(el));
});
"""
