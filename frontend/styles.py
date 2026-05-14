"""EcoSentinel — Dashboard CSS Styles"""

def get_css():
    return """
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg-primary:#0a0e0d;--bg-secondary:#111916;--bg-tertiary:#182420;--bg-panel:#141c19;
  --text-primary:#d4e4dc;--text-secondary:#8a9e94;--text-muted:#56665e;
  --accent:#2d6b4f;--accent-bright:#3a8f6a;--accent-glow:rgba(45,107,79,0.15);
  --amber:#c79a2e;--amber-dim:rgba(199,154,46,0.12);
  --red-critical:#b84040;--red-dim:rgba(184,64,64,0.12);
  --safe:#2d8b5e;--safe-dim:rgba(45,139,94,0.1);
  --border:#1e2e28;--border-active:#2d6b4f;
  --radius:6px;--radius-lg:10px;
  --font:'Inter',system-ui,-apple-system,sans-serif;
}
html{scroll-behavior:smooth}
body{font-family:var(--font);background:var(--bg-primary);color:var(--text-primary);line-height:1.6;overflow-x:hidden;-webkit-font-smoothing:antialiased}
a{color:var(--accent-bright);text-decoration:none}

/* ── SCROLLBAR ── */
::-webkit-scrollbar{width:6px}
::-webkit-scrollbar-track{background:var(--bg-primary)}
::-webkit-scrollbar-thumb{background:var(--border);border-radius:3px}

/* ── HERO ── */
.hero{min-height:100vh;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:3rem 1.5rem;position:relative;overflow:hidden}
.hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 50% 40%,rgba(45,107,79,0.08) 0%,transparent 70%);pointer-events:none}
.hero-badge{display:inline-flex;align-items:center;gap:8px;padding:6px 16px;border:1px solid var(--border);border-radius:20px;font-size:0.72rem;letter-spacing:1.8px;text-transform:uppercase;color:var(--text-secondary);margin-bottom:2rem;background:var(--bg-secondary)}
.hero-badge .dot{width:6px;height:6px;border-radius:50%;background:var(--safe);animation:pulse-dot 2s ease infinite}
.hero h1{font-size:clamp(1.8rem,4.5vw,3.2rem);font-weight:700;line-height:1.15;max-width:800px;margin-bottom:1.2rem;letter-spacing:-0.5px;color:var(--text-primary)}
.hero h1 span{color:var(--accent-bright)}
.hero-sub{font-size:clamp(0.85rem,1.6vw,1rem);color:var(--text-secondary);max-width:620px;line-height:1.7;margin-bottom:2.5rem}
.hero-btns{display:flex;gap:12px;flex-wrap:wrap;justify-content:center}
.btn{padding:10px 24px;border-radius:var(--radius);font-size:0.82rem;font-weight:600;letter-spacing:0.5px;cursor:pointer;transition:all 0.25s;border:none;font-family:var(--font)}
.btn-primary{background:var(--accent);color:#fff}.btn-primary:hover{background:var(--accent-bright)}
.btn-outline{background:transparent;color:var(--text-secondary);border:1px solid var(--border)}.btn-outline:hover{border-color:var(--accent);color:var(--text-primary)}

/* ── SECTIONS ── */
section{padding:5rem 1.5rem;max-width:1100px;margin:0 auto}
.section-label{font-size:0.68rem;letter-spacing:2.5px;text-transform:uppercase;color:var(--accent-bright);margin-bottom:0.6rem}
.section-title{font-size:clamp(1.3rem,3vw,1.9rem);font-weight:700;margin-bottom:1rem;letter-spacing:-0.3px}
.section-desc{color:var(--text-secondary);max-width:600px;font-size:0.9rem;margin-bottom:2.5rem;line-height:1.7}

/* ── ABOUT GRID ── */
.about-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px}
.about-card{background:var(--bg-secondary);border:1px solid var(--border);border-radius:var(--radius-lg);padding:1.5rem;transition:border-color 0.3s}
.about-card:hover{border-color:var(--accent)}
.about-card .ic{width:36px;height:36px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:1.1rem;margin-bottom:0.8rem;background:var(--accent-glow)}
.about-card h3{font-size:0.95rem;font-weight:600;margin-bottom:0.4rem}
.about-card p{font-size:0.82rem;color:var(--text-secondary);line-height:1.6}

/* ── STACK / WORKFLOW ── */
.stack-list{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px}
.stack-item{background:var(--bg-secondary);border:1px solid var(--border);border-radius:var(--radius);padding:1.1rem 1.2rem;display:flex;align-items:center;gap:12px;transition:border-color 0.3s}
.stack-item:hover{border-color:var(--accent)}
.stack-item .num{width:28px;height:28px;border-radius:6px;background:var(--accent-glow);color:var(--accent-bright);display:flex;align-items:center;justify-content:center;font-size:0.72rem;font-weight:700;flex-shrink:0}
.stack-item span{font-size:0.82rem;font-weight:500}
.workflow-steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;counter-reset:step}
.wf-step{background:var(--bg-secondary);border:1px solid var(--border);border-radius:var(--radius-lg);padding:1.4rem;position:relative;counter-increment:step}
.wf-step::before{content:counter(step,decimal-leading-zero);font-size:2rem;font-weight:800;color:var(--bg-tertiary);position:absolute;top:10px;right:14px}
.wf-step h4{font-size:0.88rem;font-weight:600;margin-bottom:0.3rem}
.wf-step p{font-size:0.78rem;color:var(--text-secondary);line-height:1.6}

/* ── ARCHITECTURE ── */
.arch-diagram{background:var(--bg-secondary);border:1px solid var(--border);border-radius:var(--radius-lg);padding:2rem;overflow-x:auto}
.arch-flow{display:flex;align-items:center;gap:0;justify-content:center;flex-wrap:wrap}
.arch-node{background:var(--bg-tertiary);border:1px solid var(--border);border-radius:var(--radius);padding:1rem 1.3rem;text-align:center;min-width:140px;transition:border-color 0.3s}
.arch-node:hover{border-color:var(--accent-bright)}
.arch-node .node-label{font-size:0.65rem;letter-spacing:1.5px;text-transform:uppercase;color:var(--text-muted);margin-bottom:4px}
.arch-node .node-name{font-size:0.88rem;font-weight:600}
.arch-arrow{color:var(--text-muted);font-size:1.2rem;padding:0 6px;flex-shrink:0}

/* ── LAUNCH SECTION ── */
.launch-section{text-align:center;padding:4rem 1.5rem}
.launch-section .btn-primary{font-size:0.95rem;padding:14px 36px}

/* ── DASHBOARD ── */
.dash{background:var(--bg-primary);min-height:100vh;padding:1.5rem}
.dash-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:1.5rem;padding-bottom:1rem;border-bottom:1px solid var(--border);flex-wrap:wrap;gap:10px}
.dash-brand{display:flex;align-items:center;gap:10px}
.dash-brand h2{font-size:1rem;font-weight:700;letter-spacing:-0.3px}
.back-btn{display:inline-flex;align-items:center;justify-content:center;width:32px;height:32px;border-radius:var(--radius);border:1px solid var(--border);background:var(--bg-secondary);color:var(--text-secondary);font-size:1.1rem;text-decoration:none;transition:all 0.25s;cursor:pointer;flex-shrink:0}
.back-btn:hover{border-color:var(--accent);color:var(--text-primary);background:var(--accent-glow)}
.dash-brand .status-dot{width:8px;height:8px;border-radius:50%;background:var(--safe);animation:pulse-dot 2s ease infinite}
.dash-meta{display:flex;gap:16px;align-items:center}
.dash-meta span{font-size:0.72rem;color:var(--text-muted);letter-spacing:0.5px}

.dash-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:14px}

/* ── PANELS ── */
.panel{background:var(--bg-panel);border:1px solid var(--border);border-radius:var(--radius-lg);overflow:hidden;transition:border-color 0.3s}
.panel:hover{border-color:var(--border-active)}
.panel-head{display:flex;align-items:center;justify-content:space-between;padding:0.9rem 1.1rem;border-bottom:1px solid var(--border)}
.panel-head h3{font-size:0.78rem;font-weight:600;letter-spacing:0.5px;text-transform:uppercase;display:flex;align-items:center;gap:8px}
.panel-head .tag{font-size:0.6rem;padding:2px 8px;border-radius:10px;letter-spacing:0.8px;text-transform:uppercase;font-weight:600}
.tag-safe{background:var(--safe-dim);color:var(--safe)}
.tag-warn{background:var(--amber-dim);color:var(--amber)}
.tag-crit{background:var(--red-dim);color:var(--red-critical)}
.tag-offline{background:rgba(100,100,100,0.15);color:#666}
.panel-body{padding:1.1rem}

/* ── THREAT PANEL ── */
.threat-display{text-align:center;padding:1rem 0}
.threat-class{font-size:1.6rem;font-weight:800;letter-spacing:1px;text-transform:uppercase;margin-bottom:4px}
.threat-conf{font-size:0.82rem;color:var(--text-secondary)}
.score-bars{margin-top:1rem}
.score-row{display:flex;align-items:center;gap:8px;margin-bottom:6px;font-size:0.75rem}
.score-label{width:72px;text-align:right;color:var(--text-secondary);font-weight:500}
.score-track{flex:1;height:6px;background:var(--bg-primary);border-radius:3px;overflow:hidden}
.score-fill{height:100%;border-radius:3px;transition:width 0.6s ease;background:var(--accent)}
.score-val{width:40px;color:var(--text-muted);font-size:0.7rem}

/* ── RADAR ── */
.radar-container{position:relative;width:180px;height:180px;margin:0.5rem auto}
.radar-bg{width:100%;height:100%;border-radius:50%;border:1px solid var(--border);position:relative;overflow:hidden;background:radial-gradient(circle,var(--bg-tertiary) 0%,var(--bg-primary) 100%)}
.radar-ring{position:absolute;border-radius:50%;border:1px solid var(--border);top:50%;left:50%;transform:translate(-50%,-50%)}
.radar-ring:nth-child(1){width:33%;height:33%}
.radar-ring:nth-child(2){width:66%;height:66%}
.radar-ring:nth-child(3){width:100%;height:100%}
.radar-cross{position:absolute;top:50%;left:50%;width:100%;height:1px;background:var(--border);transform:translate(-50%,-50%)}
.radar-cross-v{position:absolute;top:50%;left:50%;width:1px;height:100%;background:var(--border);transform:translate(-50%,-50%)}
.radar-sweep{position:absolute;top:50%;left:50%;width:50%;height:2px;transform-origin:left center;background:linear-gradient(90deg,var(--accent-bright),transparent);animation:sweep 4s linear infinite;opacity:0.7}
.radar-center{position:absolute;top:50%;left:50%;width:6px;height:6px;border-radius:50%;background:var(--accent-bright);transform:translate(-50%,-50%);z-index:2}
.radar-label{text-align:center;font-size:0.7rem;color:var(--text-muted);margin-top:8px;letter-spacing:1px;text-transform:uppercase}

/* ── GPS ── */
.gps-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.gps-field{background:var(--bg-primary);border:1px solid var(--border);border-radius:var(--radius);padding:0.7rem 0.9rem}
.gps-field .gps-lbl{font-size:0.62rem;letter-spacing:1.2px;text-transform:uppercase;color:var(--text-muted);margin-bottom:2px}
.gps-field .gps-val{font-size:0.95rem;font-weight:600;font-variant-numeric:tabular-nums}

/* ── VIBRATION REFACTORED ── */
.vib-wave{height:60px;background:var(--bg-primary);border:1px solid var(--border);border-radius:var(--radius);display:flex;align-items:flex-end;justify-content:center;gap:2px;padding:8px;overflow:hidden;position:relative}
.vib-bar{width:3px;border-radius:2px;background:var(--accent);transition:height 0.3s;min-height:3px}
.vib-status-container{display:flex;flex-direction:column;align-items:center;justify-content:center;margin-top:12px;gap:6px;position:relative;z-index:2}
.vib-status-label{font-size:1.1rem;font-weight:800;text-transform:uppercase;letter-spacing:2px;transition:all 0.3s;color:var(--text-muted)}
.vib-activity-indicator{width:100%;height:3px;background:var(--border);border-radius:2px;position:relative;overflow:hidden;margin-top:4px}
.vib-activity-indicator::after{content:'';position:absolute;top:0;left:-100%;width:100%;height:100%;background:linear-gradient(90deg,transparent,var(--accent-bright),transparent);transition:opacity 0.3s;opacity:0}
.state-vibrating .vib-activity-indicator::after{animation:slide-glow 1.5s infinite;opacity:1}
.state-vibrating .vib-status-label{color:var(--accent-bright);text-shadow:0 0 12px var(--accent-glow)}
.state-vibrating .vib-bar{background:var(--accent-bright);box-shadow:0 0 8px var(--accent-glow)}

@keyframes slide-glow{from{left:-100%}to{left:100%}}

/* ── FUSION ── */
.fusion-ring{width:140px;height:140px;margin:0.5rem auto;position:relative}
.fusion-ring svg{width:100%;height:100%;transform:rotate(-90deg)}
.fusion-ring circle{fill:none;stroke-width:6;stroke-linecap:round}
.fusion-ring .ring-bg{stroke:var(--border)}
.fusion-ring .ring-fill{stroke:var(--accent-bright);transition:stroke-dashoffset 0.8s ease}
.fusion-center{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center}
.fusion-pct{font-size:1.4rem;font-weight:700}
.fusion-label{font-size:0.6rem;color:var(--text-muted);letter-spacing:1px;text-transform:uppercase}
.fusion-sensors{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:10px}
.fusion-s{background:var(--bg-primary);border:1px solid var(--border);border-radius:var(--radius);padding:6px 10px;display:flex;align-items:center;gap:8px;font-size:0.75rem}
.fusion-s .s-dot{width:6px;height:6px;border-radius:50%;flex-shrink:0}
.fusion-s .s-name{color:var(--text-secondary)}

/* ── TIMELINE ── */
.timeline{max-height:260px;overflow-y:auto;padding-right:4px}
.tl-entry{display:flex;gap:10px;padding:8px 0;border-bottom:1px solid var(--border)}
.tl-entry:last-child{border-bottom:none}
.tl-time{font-size:0.68rem;color:var(--text-muted);width:50px;flex-shrink:0;font-variant-numeric:tabular-nums;padding-top:2px}
.tl-icon{width:22px;height:22px;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:0.7rem;flex-shrink:0}
.tl-icon-safe{background:var(--safe-dim);color:var(--safe)}
.tl-icon-warn{background:var(--amber-dim);color:var(--amber)}
.tl-icon-crit{background:var(--red-dim);color:var(--red-critical)}
.tl-content{flex:1;min-width:0}
.tl-title{font-size:0.78rem;font-weight:600}
.tl-desc{font-size:0.7rem;color:var(--text-secondary);margin-top:1px}

/* ── UPLOAD PANEL ── */
.upload-zone{border:2px dashed var(--border);border-radius:var(--radius-lg);padding:2rem;text-align:center;cursor:pointer;transition:all 0.3s;background:var(--bg-primary)}
.upload-zone:hover,.upload-zone.dragover{border-color:var(--accent);background:var(--accent-glow)}
.upload-zone .uz-icon{font-size:1.8rem;margin-bottom:0.5rem}
.upload-zone .uz-text{font-size:0.82rem;color:var(--text-secondary)}
.upload-zone .uz-hint{font-size:0.7rem;color:var(--text-muted);margin-top:4px}
.upload-progress{margin-top:1rem;display:none}
.upload-progress.active{display:block}
.prog-bar{height:4px;background:var(--bg-primary);border-radius:2px;overflow:hidden;margin-bottom:6px}
.prog-fill{height:100%;background:var(--accent-bright);border-radius:2px;transition:width 0.3s;width:0}
.prog-text{font-size:0.72rem;color:var(--text-secondary);text-align:center}

/* ── STATES ── */
.state-safe .threat-class{color:var(--safe)}
.state-warn .threat-class{color:var(--amber)}
.state-crit .threat-class{color:var(--red-critical)}
.state-warn .radar-sweep{animation-duration:2s;background:linear-gradient(90deg,var(--amber),transparent)}
.state-crit .radar-sweep{animation-duration:1s;background:linear-gradient(90deg,var(--red-critical),transparent)}
.state-crit .radar-center{background:var(--red-critical);animation:pulse-dot 0.8s ease infinite}
.state-warn .panel{border-color:rgba(199,154,46,0.2)}
.state-crit .panel{border-color:rgba(184,64,64,0.2)}

/* ── FOOTER ── */
.site-footer{text-align:center;padding:2rem;border-top:1px solid var(--border);margin-top:2rem}
.site-footer p{font-size:0.72rem;color:var(--text-muted)}

/* ── KEYFRAMES ── */
@keyframes pulse-dot{0%,100%{opacity:1}50%{opacity:0.4}}
@keyframes sweep{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}
@keyframes fade-in{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}
.fade-in{animation:fade-in 0.5s ease both}

/* ── RESPONSIVE ── */
@media(max-width:768px){
  .dash-grid{grid-template-columns:1fr}
  .hero h1{font-size:1.6rem}
  .arch-flow{flex-direction:column}
  .arch-arrow{transform:rotate(90deg)}
  .gps-grid{grid-template-columns:1fr}
}
"""


def get_landing_css():
    return """
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#050a08;--bg2:#0a1610;--bg3:#0f1f18;
  --text:#d4e4dc;--text2:#8a9e94;--text3:#56665e;
  --green:#00e87b;--green2:#00ff88;--green-dim:rgba(0,232,123,0.08);--green-glow:rgba(0,232,123,0.15);
  --teal:#00d4aa;--amber:#c79a2e;--red:#b84040;
  --border:#1a2e25;--radius:8px;--radius-lg:12px;
  --font:'Inter',system-ui,-apple-system,sans-serif;
}
html{scroll-behavior:smooth}
body{font-family:var(--font);background:var(--bg);color:var(--text);line-height:1.6;overflow-x:hidden;-webkit-font-smoothing:antialiased}
a{color:var(--green);text-decoration:none}
::-webkit-scrollbar{width:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--border);border-radius:3px}

/* ── CANVAS ── */
#particle-canvas{position:fixed;inset:0;z-index:0;pointer-events:none}

/* ── FOG ── */
.fog{position:fixed;inset:0;z-index:1;pointer-events:none;overflow:hidden}
.fog::before,.fog::after{content:'';position:absolute;width:200%;height:100%;top:0;left:-50%;opacity:0.04}
.fog::before{background:radial-gradient(ellipse at 30% 50%,var(--green) 0%,transparent 50%);animation:fogDrift 25s ease-in-out infinite}
.fog::after{background:radial-gradient(ellipse at 70% 60%,var(--teal) 0%,transparent 45%);animation:fogDrift 30s ease-in-out infinite reverse}

/* ── SCAN LINE ── */
.scan-line{position:fixed;top:0;left:0;width:100%;height:2px;background:linear-gradient(90deg,transparent,var(--green2),transparent);opacity:0.12;z-index:2;pointer-events:none;animation:scanDown 8s linear infinite}

/* ── TOPO GRID ── */
.topo-overlay{position:fixed;inset:0;z-index:1;pointer-events:none;opacity:0.025;
  background-image:repeating-linear-gradient(0deg,var(--green) 0px,transparent 1px,transparent 60px),
    repeating-linear-gradient(90deg,var(--green) 0px,transparent 1px,transparent 60px);
  animation:gridShift 20s linear infinite}

/* ── NAVBAR ── */
.nav{position:fixed;top:0;left:0;width:100%;z-index:100;padding:1.5rem 0;backdrop-filter:blur(10px);border-bottom:1px solid rgba(0,232,123,0.05);background:rgba(5,10,8,0.3)}
.nav-container{max-width:1200px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;padding:0 2rem}

.logo{display:flex;align-items:center;gap:12px;cursor:pointer}
.logo-icon{width:24px;height:24px;background:var(--green);clip-path:polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);position:relative;animation:logoPulse 3s ease-in-out infinite}
.logo-icon::after{content:'';position:absolute;inset:4px;background:var(--bg);clip-path:polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)}
.logo-text{font-size:1.1rem;font-weight:900;letter-spacing:4px;color:var(--text);position:relative}
.logo-text span{color:var(--green);opacity:0.8}
.logo-text::after{content:'';position:absolute;bottom:-4px;left:0;width:0;height:1px;background:var(--green);transition:width 0.4s;box-shadow:0 0 10px var(--green)}
.logo:hover .logo-text::after{width:100%}

.nav-btn{font-size:0.65rem;letter-spacing:2px;font-weight:700;color:var(--green);border:1px solid rgba(0,232,123,0.3);padding:8px 18px;border-radius:4px;transition:all 0.3s;background:rgba(0,232,123,0.02)}
.nav-btn:hover{background:var(--green);color:var(--bg);box-shadow:0 0 20px rgba(0,232,123,0.3);transform:translateY(-1px)}

@keyframes logoPulse{0%,100%{transform:scale(1);opacity:1;filter:drop-shadow(0 0 5px var(--green))}50%{transform:scale(1.1);opacity:0.8;filter:drop-shadow(0 0 15px var(--green))}}

/* ── CONTENT WRAPPER ── */
.page-content{position:relative;z-index:10;padding-top:80px}

/* ── HERO ── */
.hero{min-height:100vh;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:3rem 1.5rem;position:relative;overflow:hidden}
.hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 50% 40%,rgba(0,232,123,0.06) 0%,transparent 65%);pointer-events:none;animation:heroPulse 6s ease-in-out infinite}
.hero::after{content:'';position:absolute;bottom:0;left:0;right:0;height:200px;background:linear-gradient(to top,var(--bg),transparent);pointer-events:none;z-index:1}

.hero-badge{display:inline-flex;align-items:center;gap:8px;padding:7px 18px;border:1px solid rgba(0,232,123,0.2);border-radius:24px;font-size:0.68rem;letter-spacing:2.2px;text-transform:uppercase;color:var(--green);margin-bottom:2rem;background:rgba(0,232,123,0.04);backdrop-filter:blur(8px);opacity:0;animation:fadeUp 1s ease 0.3s forwards}
.hero-badge .dot{width:7px;height:7px;border-radius:50%;background:var(--green);box-shadow:0 0 12px var(--green);animation:pulseDot 2s ease infinite}

.hero-title{font-size:clamp(2.2rem,5.5vw,4rem);font-weight:800;line-height:1.1;max-width:900px;margin-bottom:1.5rem;letter-spacing:-1px;position:relative}
.hero-title .line{display:block;opacity:0;animation:textReveal 1s cubic-bezier(0.16,1,0.3,1) forwards}
.hero-title .line:nth-child(1){animation-delay:0.5s}
.hero-title .line:nth-child(2){animation-delay:0.7s}
.hero-title .accent{color:var(--green);position:relative}
.hero-title .accent::after{content:'';position:absolute;inset:-2px -6px;background:linear-gradient(90deg,transparent,rgba(0,232,123,0.15),transparent);border-radius:4px;animation:glowSweep 3s ease 1.5s infinite}

.hero-sub{font-size:clamp(0.9rem,1.6vw,1.05rem);color:var(--text2);max-width:640px;line-height:1.8;margin-bottom:2.5rem;opacity:0;animation:fadeUp 1s ease 1s forwards}
.hero-btns{display:flex;gap:14px;flex-wrap:wrap;justify-content:center;opacity:0;animation:fadeUp 1s ease 1.2s forwards}

/* ── BUTTONS ── */
.btn{padding:12px 28px;border-radius:var(--radius);font-size:0.85rem;font-weight:600;letter-spacing:0.5px;cursor:pointer;transition:all 0.3s;border:none;font-family:var(--font);text-decoration:none;display:inline-flex;align-items:center;gap:8px}
.btn-primary{background:var(--green);color:#050a08;position:relative;overflow:hidden}
.btn-primary::before{content:'';position:absolute;top:0;left:-100%;width:100%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.2),transparent);transition:0.5s}
.btn-primary:hover::before{left:100%}
.btn-primary:hover{box-shadow:0 0 30px rgba(0,232,123,0.3);transform:translateY(-2px)}
.btn-outline{background:transparent;color:var(--text2);border:1px solid var(--border)}
.btn-outline:hover{border-color:var(--green);color:var(--text);transform:translateY(-2px)}

/* ── SECTIONS ── */
section{padding:6rem 1.5rem;max-width:1100px;margin:0 auto}
.section-label{font-size:0.65rem;letter-spacing:3px;text-transform:uppercase;color:var(--green);margin-bottom:0.7rem;position:relative;display:inline-block}
.section-label::after{content:'';display:inline-block;width:30px;height:1px;background:var(--green);margin-left:10px;vertical-align:middle;opacity:0.4}
.section-title{font-size:clamp(1.5rem,3.5vw,2.2rem);font-weight:700;margin-bottom:1.2rem;letter-spacing:-0.5px}
.section-desc{color:var(--text2);max-width:600px;font-size:0.92rem;margin-bottom:3rem;line-height:1.8}

/* ── ABOUT GRID ── */
.about-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:16px}
.about-card{background:rgba(15,31,24,0.6);border:1px solid var(--border);border-radius:var(--radius-lg);padding:1.6rem;transition:all 0.4s;backdrop-filter:blur(4px)}
.about-card:hover{border-color:rgba(0,232,123,0.3);transform:translateY(-4px);box-shadow:0 8px 30px rgba(0,232,123,0.06)}
.about-card .ic{width:40px;height:40px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1.2rem;margin-bottom:1rem;background:var(--green-dim);border:1px solid rgba(0,232,123,0.1)}
.about-card h3{font-size:0.95rem;font-weight:600;margin-bottom:0.5rem}
.about-card p{font-size:0.82rem;color:var(--text2);line-height:1.7}

/* ── STACK ── */
.stack-list{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px}
.stack-item{background:rgba(15,31,24,0.5);border:1px solid var(--border);border-radius:var(--radius);padding:1.1rem 1.3rem;display:flex;align-items:center;gap:14px;transition:all 0.35s}
.stack-item:hover{border-color:rgba(0,232,123,0.3);transform:translateX(6px)}
.stack-item .num{width:30px;height:30px;border-radius:8px;background:var(--green-dim);color:var(--green);display:flex;align-items:center;justify-content:center;font-size:0.72rem;font-weight:700;flex-shrink:0;border:1px solid rgba(0,232,123,0.1)}
.stack-item span{font-size:0.84rem;font-weight:500}

/* ── WORKFLOW ── */
.workflow-steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;counter-reset:step}
.wf-step{background:rgba(15,31,24,0.5);border:1px solid var(--border);border-radius:var(--radius-lg);padding:1.5rem;position:relative;counter-increment:step;transition:all 0.35s;overflow:hidden}
.wf-step::before{content:counter(step,decimal-leading-zero);font-size:2.5rem;font-weight:800;color:rgba(0,232,123,0.06);position:absolute;top:8px;right:14px;line-height:1}
.wf-step::after{content:'';position:absolute;bottom:0;left:0;width:0;height:2px;background:var(--green);transition:width 0.4s}
.wf-step:hover::after{width:100%}
.wf-step:hover{border-color:rgba(0,232,123,0.2)}
.wf-step h4{font-size:0.9rem;font-weight:600;margin-bottom:0.4rem;color:var(--green)}
.wf-step p{font-size:0.8rem;color:var(--text2);line-height:1.7}

/* ── ARCHITECTURE ── */
.arch-diagram{background:rgba(15,31,24,0.5);border:1px solid var(--border);border-radius:var(--radius-lg);padding:2.5rem;overflow-x:auto}
.arch-flow{display:flex;align-items:center;gap:0;justify-content:center;flex-wrap:wrap}
.arch-node{background:rgba(5,10,8,0.8);border:1px solid var(--border);border-radius:var(--radius);padding:1.1rem 1.4rem;text-align:center;min-width:140px;transition:all 0.35s}
.arch-node:hover{border-color:var(--green);box-shadow:0 0 20px rgba(0,232,123,0.08)}
.arch-node .node-label{font-size:0.6rem;letter-spacing:2px;text-transform:uppercase;color:var(--green);margin-bottom:4px;opacity:0.7}
.arch-node .node-name{font-size:0.9rem;font-weight:600}
.arch-arrow{color:var(--green);font-size:1.3rem;padding:0 8px;flex-shrink:0;opacity:0.4}

/* ── LAUNCH CTA ── */
.launch-section{text-align:center;padding:6rem 1.5rem;position:relative}
.launch-section::before{content:'';position:absolute;top:0;left:50%;transform:translateX(-50%);width:1px;height:60px;background:linear-gradient(to bottom,transparent,var(--green),transparent);opacity:0.3}
.launch-section .btn-primary{font-size:1rem;padding:16px 40px}

/* ── FOOTER ── */
.site-footer{text-align:center;padding:2.5rem;border-top:1px solid var(--border);margin-top:2rem}
.site-footer p{font-size:0.72rem;color:var(--text3);letter-spacing:0.5px}

/* ── SCROLL REVEAL ── */
.sr{opacity:0;transform:translateY(40px);transition:opacity 0.8s cubic-bezier(0.16,1,0.3,1),transform 0.8s cubic-bezier(0.16,1,0.3,1)}
.sr.visible{opacity:1;transform:translateY(0)}
.sr-delay-1{transition-delay:0.1s}
.sr-delay-2{transition-delay:0.2s}
.sr-delay-3{transition-delay:0.3s}
.sr-delay-4{transition-delay:0.4s}

/* ── KEYFRAMES ── */
@keyframes fadeUp{from{opacity:0;transform:translateY(30px)}to{opacity:1;transform:translateY(0)}}
@keyframes textReveal{from{opacity:0;transform:translateY(40px) scale(0.97);filter:blur(4px)}to{opacity:1;transform:translateY(0) scale(1);filter:blur(0)}}
@keyframes pulseDot{0%,100%{opacity:1;box-shadow:0 0 12px var(--green)}50%{opacity:0.5;box-shadow:0 0 4px var(--green)}}
@keyframes glowSweep{0%,100%{opacity:0;transform:translateX(-100%)}50%{opacity:1;transform:translateX(100%)}}
@keyframes heroPulse{0%,100%{opacity:1}50%{opacity:0.6}}
@keyframes fogDrift{0%{transform:translateX(0)}50%{transform:translateX(10%)}100%{transform:translateX(0)}}
@keyframes scanDown{0%{top:-2px}100%{top:100%}}
@keyframes gridShift{0%{transform:translate(0,0)}100%{transform:translate(60px,60px)}}

/* ── RESPONSIVE ── */
@media(max-width:768px){
  .hero-title{font-size:1.8rem}
  .arch-flow{flex-direction:column}
  .arch-arrow{transform:rotate(90deg)}
}
"""
