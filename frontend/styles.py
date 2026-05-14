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

/* ── VIBRATION ── */
.vib-wave{height:60px;background:var(--bg-primary);border:1px solid var(--border);border-radius:var(--radius);display:flex;align-items:flex-end;justify-content:center;gap:2px;padding:8px;overflow:hidden}
.vib-bar{width:3px;border-radius:2px;background:var(--accent);transition:height 0.3s;min-height:3px}
.vib-stats{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-top:10px}
.vib-stat{text-align:center}
.vib-stat .vstat-label{font-size:0.6rem;letter-spacing:1px;text-transform:uppercase;color:var(--text-muted)}
.vib-stat .vstat-val{font-size:0.9rem;font-weight:600;margin-top:2px;font-variant-numeric:tabular-nums}

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
