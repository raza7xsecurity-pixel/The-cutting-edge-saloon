from flask import Flask, render_template_string, request, jsonify
import requests
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

# ====== TUMHARA BUSINESS CONTACT ======
YOUR_BUSINESS_WHATSAPP = "917251863769"  # 91 + 7251863769
YOUR_EMAIL = os.environ.get('YOUR_EMAIL', 'mohdraja2693@gmail.com')

# IMPORTANT: Environment variable fallback for high security hosting
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD', 'jwmnvehlzpgxqtxt')  

# ====== META WHATSAPP KEYS ======
WHATSAPP_TOKEN = os.environ.get('WHATSAPP_TOKEN')
PHONE_NUMBER_ID = os.environ.get('PHONE_NUMBER_ID')

HTML_CODE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Cutting Edge | Luxury Gents Salon - Pune</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@200;300;400;500;600;700&display=swap" rel="stylesheet">
<!-- Premium 3D Engine & Animation Controllers -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>

<style>
  :root{
    --pure-black: #000000;
    --luxury-charcoal: #0a0a0a;
    --looks-gold: #cfa63a;
    --looks-gold-hover: #e5be53;
    --clean-white: #ffffff;
    --muted-grey: #999999;
    --input-bg: #111111;
    --border-color: rgba(207, 166, 58, 0.25);
  }
  
  *{margin:0;padding:0;box-sizing:border-box;}
  html{scroll-behavior:smooth;}
  body{background:var(--pure-black);color:var(--clean-white);font-family:'Montserrat',sans-serif;overflow-x:hidden;}
  
  /* 3D Immersive Canvas */
  #webgl-canvas {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 1;
    pointer-events: none;
    opacity: 0.45;
  }

  .main-container {
    position: relative;
    z-index: 2;
  }

  .wrap{max-width:1400px;margin:0 auto;padding:0 40px;}

  /* Corporate Header System */
  header{position:fixed;top:0;width:100%;background:rgba(0,0,0,0.9);backdrop-filter:blur(20px);border-bottom:1px solid rgba(255,255,255,0.06);z-index:1000;}
  .navrow{display:flex;align-items:center;justify-content:space-between;padding:15px 40px;}
  
  /* Upgraded Brand Typography Logo */
  .brand-logo-container {
    display: flex;
    flex-direction: column;
    line-height: 1;
    text-decoration: none;
  }
  .brand-main-title {
    font-size: 1.6rem;
    font-weight: 700;
    letter-spacing: 5px;
    color: var(--clean-white);
    text-transform: uppercase;
  }
  .brand-sub-title {
    font-size: 0.75rem;
    font-weight: 400;
    letter-spacing: 9px;
    color: var(--looks-gold);
    margin-top: 5px;
    text-transform: uppercase;
  }
  
  .nav-menu {
    display: flex;
    gap: 30px;
    align-items: center;
  }
  .nav-link {
    color: var(--clean-white);
    text-decoration: none;
    font-size: 0.85rem;
    font-weight: 500;
    letter-spacing: 2px;
    text-transform: uppercase;
    transition: 0.3s;
  }
  .nav-link:hover {
    color: var(--looks-gold);
  }
  .nav-action-btn {
    background: var(--looks-gold);
    color: var(--pure-black);
    padding: 10px 22px;
    font-weight: 600;
    font-size: 0.8rem;
    letter-spacing: 1.5px;
    text-decoration: none;
    text-transform: uppercase;
    transition: 0.3s;
  }
  .nav-action-btn:hover {
    background: var(--looks-gold-hover);
    transform: translateY(-1px);
  }

  /* Looks Themed Hero Showcase */
  .hero-showcase{min-height:90vh;display:flex;align-items:center;justify-content:center;position:relative;padding-top:80px;background: radial-gradient(circle at center, rgba(20,20,20,0.8) 0%, var(--pure-black) 100%);}
  .hero-inner{text-align:center;width:100%;max-width:900px;opacity:0;transform:translateY(40px);}
  .hero-badge{font-size:0.8rem;letter-spacing:7px;text-transform:uppercase;color:var(--looks-gold);font-weight:600;margin-bottom:20px;}
  .hero-showcase h1{font-size:clamp(2.5rem, 6vw, 4.8rem);letter-spacing:4px;line-height:1.2;font-weight:300;text-transform:uppercase;color:var(--clean-white);}
  .hero-showcase h1 span{font-weight:700; color: var(--looks-gold);}
  .hero-showcase p{color:var(--muted-grey);font-size:1.1rem;margin:25px 0 45px;font-weight:400;letter-spacing:2px;text-transform: uppercase;}
  
  .btn-luxury-cta {
    background: transparent;
    color: var(--looks-gold);
    border: 1px solid var(--looks-gold);
    padding: 16px 40px;
    font-weight: 600;
    letter-spacing: 3px;
    text-decoration: none;
    font-size: 0.9rem;
    text-transform: uppercase;
    transition: 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  }
  .btn-luxury-cta:hover {
    background: var(--looks-gold);
    color: var(--pure-black);
    box-shadow: 0 15px 30px rgba(207,166,58,0.2);
  }

  .alert-timing-strip{background:var(--luxury-charcoal);border-top:1px solid rgba(255,255,255,0.08);border-bottom:1px solid rgba(255,255,255,0.08);color:var(--looks-gold);text-align:center;padding:16px;font-weight:500;font-size:0.9rem;letter-spacing:3px;}

  /* Portfolio In-Vogue Grid Layout */
  #services{padding:120px 0;}
  .section-header-panel{text-align:center;margin-bottom:80px;}
  .section-header-panel h2{font-size:2.5rem;font-weight:300;letter-spacing:5px;text-transform:uppercase;}
  .section-header-panel h2 span{color:var(--looks-gold);font-weight:700;}
  
  .editorial-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:30px;}
  .editorial-card{background:var(--luxury-charcoal);border:1px solid rgba(255,255,255,0.05);padding:45px 35px;transition:0.4s;}
  .editorial-card:hover{border-color:var(--looks-gold);transform:translateY(-5px);}
  .editorial-card h3{font-size:1.3rem;font-weight:600;color:var(--looks-gold);margin-bottom:25px;letter-spacing:2px;text-transform:uppercase;border-bottom:1px solid rgba(255,255,255,0.1);padding-bottom:15px;}
  .menu-line-item{display:flex;justify-content:space-between;padding:14px 0;border-bottom:1px solid rgba(255,255,255,0.03);font-size:0.9rem;letter-spacing:1px;color:#dddddd;}
  .menu-line-item:last-child{border:none;}
  .menu-item-price{color:var(--looks-gold);font-weight:600;}

  /* Clean Corporate Booking Platform Style */
  #book{padding:120px 0;background:var(--luxury-charcoal);}
  .booking-mainframe{max-width:950px;margin:0 auto;background:var(--pure-black);border:1px solid var(--border-color);padding:60px 50px;}
  .booking-mainframe h2{text-align:center;font-size:2.2rem;font-weight:300;letter-spacing:4px;margin-bottom:10px;text-transform:uppercase;}
  .booking-mainframe h2 span{font-weight:700;color:var(--looks-gold);}
  .booking-policy-notice{text-align:center;color:#ff4444;font-weight:500;margin-bottom:50px;letter-spacing:2px;font-size:0.8rem;text-transform:uppercase;}
  
  .form-matrix{display:grid;grid-template-columns:1fr 1fr;gap:35px;margin-bottom:30px;}
  .input-wrapper{position:relative;}
  .input-wrapper label{display:block;font-size:0.75rem;letter-spacing:2px;color:var(--looks-gold);margin-bottom:10px;font-weight:600;text-transform:uppercase;}
  .input-wrapper input, .input-wrapper select{width:100%;padding:15px;background:var(--input-bg);border:1px solid rgba(255,255,255,0.15);color:var(--clean-white);font-family:'Montserrat';font-size:0.9rem;transition:0.3s;}
  .input-wrapper input:focus, .input-wrapper select:focus{outline:none;border-color:var(--looks-gold);}
  
  .full-width-matrix{margin-bottom:35px;}
  
  .submit-luxury-btn{background:var(--looks-gold);color:var(--pure-black);width:100%;padding:18px;font-weight:700;letter-spacing:3px;font-size:0.95rem;border:none;cursor:pointer;text-transform:uppercase;transition:0.3s;}
  .submit-luxury-btn:hover{background:var(--looks-gold-hover);letter-spacing:4px;}
  
  .success-feedback{display:none;text-align:center;padding:40px;border:1px solid var(--looks-gold);margin-top:30px;background:rgba(207,166,58,0.05);}
  .success-feedback h3{color:var(--looks-gold);font-size:1.8rem;margin-bottom:15px;letter-spacing:2px;}

  /* Corporate Footer Styling */
  footer{padding:80px 0;background:var(--pure-black);border-top:1px solid rgba(255,255,255,0.08);}
  .footer-columns{display:grid;grid-template-columns:repeat(3,1fr);gap:40px;text-align:center;}
  .footer-columns h4{color:var(--looks-gold);margin-bottom:20px;letter-spacing:3px;font-size:1rem;font-weight:600;text-transform:uppercase;}
  .footer-meta-text{font-size:0.95rem;color:var(--muted-grey);line-height:1.8;letter-spacing:1px;}
  .footer-bottom-bar{padding-top:40px;color:var(--muted-grey);border-top:1px solid rgba(255,255,255,0.05);margin-top:60px;text-align:center;letter-spacing:2px;font-size:0.8rem;}

  @media(max-width:1024px){.editorial-grid{grid-template-columns:1fr;}.footer-columns{grid-template-columns:1fr;}.nav-menu{display:none;}}
  @media(max-width:768px){.form-matrix{grid-template-columns:1fr;}.booking-mainframe{padding:40px 20px;}}
</style>
</head>
<body>

<!-- High-End 3D Particle Canvas System -->
<canvas id="webgl-canvas"></canvas>

<div class="main-container">
  <header>
    <div class="navrow">
      <a href="#" class="brand-logo-container">
        <span class="brand-main-title">The Cutting Edge</span>
        <span class="brand-sub-title">S A L O N</span>
      </a>
      <div class="nav-menu">
        <a href="#services" class="nav-link">Services</a>
        <a href="#book" class="nav-link">Bookings</a>
        <a href="#contact" class="nav-link">Contact</a>
        <a href="#book" class="nav-action-btn">Book Appointment</a>
      </div>
    </div>
  </header>

  <section class="hero-showcase">
    <div class="hero-inner">
      <p class="hero-badge">Luxury Gents Grooming Identity</p>
      <h1>LET'S NOT WAIT FOR THE<br><span>"PERFECT LOOK"</span></h1>
      <p>Where Precision Meets Masterclass Artistry</p>
      <a href="#book" class="btn-luxury-cta">Book An Appointment Now</a>
    </div>
  </section>

  <div class="alert-timing-strip">TIMING: 9:00 AM TO 9:30 PM DAILY | MONDAY CLOSED</div>

  <section id="services">
    <div class="wrap">
      <div class="section-header-panel">
        <h2>Our <span>Signature Services</span></h2>
      </div>
      <div class="editorial-grid">
        <div class="editorial-card">
          <h3>HAIR & BEARD</h3>
          <div class="menu-line-item"><span>Hair Cut</span><span class="menu-item-price">₹130</span></div>
          <div class="menu-line-item"><span>Beard Trim + Shave</span><span class="menu-item-price">₹90</span></div>
          <div class="menu-line-item"><span>Beard Clear</span><span class="menu-item-price">₹80</span></div>
          <div class="menu-line-item"><span>Zero Trim</span><span class="menu-item-price">₹70</span></div>
          <div class="menu-line-item"><span>Curl Hair cutting</span><span class="menu-item-price">₹150</span></div>
        </div>
        <div class="editorial-card">
          <h3>HAIR COLOR</h3>
          <div class="menu-line-item"><span>Loreal Majrel</span><span class="menu-item-price">₹380</span></div>
          <div class="menu-line-item"><span>Loreal Inoa</span><span class="menu-item-price">₹550</span></div>
          <div class="menu-line-item"><span>Garnier</span><span class="menu-item-price">₹250</span></div>
          <div class="menu-line-item"><span>Raaga</span><span class="menu-item-price">₹250</span></div>
          <div class="menu-line-item"><span>Strex</span><span class="menu-item-price">₹250</span></div>
        </div>
        <div class="editorial-card">
          <h3>FACIAL & D-TAN</h3>
          <div class="menu-line-item"><span>Hydra Facial</span><span class="menu-item-price">₹2999</span></div>
          <div class="menu-line-item"><span>Loreal Facial</span><span class="menu-item-price">₹1299</span></div>
          <div class="menu-line-item"><span>Lotus Facial</span><span class="menu-item-price">₹999</span></div>
          <div class="menu-line-item"><span>O3+ Facial</span><span class="menu-item-price">₹2299</span></div>
          <div class="menu-line-item"><span>O3+ Cleanup</span><span class="menu-item-price">₹1399</span></div>
          <div class="menu-line-item"><span>D-Tan Raaga</span><span class="menu-item-price">₹299</span></div>
        </div>
      </div>
    </div>
  </section>

  <section id="book">
    <div class="wrap">
      <div class="booking-mainframe">
        <h2>Book <span>An Appointment</span></h2>
        <p class="booking-policy-notice">* Please Note: Management remains closed on Mondays *</p>
        <form id="booking-form">
          <div class="form-matrix">
            <div class="input-wrapper"><label>Full Name*</label><input type="text" id="name" required></div>
            <div class="input-wrapper">
              <label>Gender*</label>
              <select id="gender" required>
                <option value="">-- Select Gender --</option>
                <option>Male</option>
                <option>Female</option>
                <option>Other</option>
              </select>
            </div>
          </div>
          <div class="form-matrix">
            <div class="input-wrapper"><label>Contact Number*</label><input type="tel" id="phone" required pattern="[0-9]{10}" title="Enter valid 10-digit number"></div>
            <div class="input-wrapper">
              <label>Service Type*</label>
              <select id="service" required>
                <option value="">-- Choose Service --</option>
                <option>Hair Cut - ₹130</option><option>Beard Trim + Shave - ₹90</option>
                <option>Beard Clear - ₹80</option><option>Zero Trim - ₹70</option><option>Curl Hair Setting - ₹150</option>
                <option>Loreal Majrel - ₹380</option><option>Loreal Inoa - ₹550</option><option>Hydra Facial - ₹2999</option><option>O3+ Facial - ₹2299</option>
              </select>
            </div>
          </div>
          <div class="form-matrix">
            <div class="input-wrapper"><label>Email Id*</label><input type="email" id="email" required></div>
            <div class="input-wrapper"><label>Preferred Date*</label><input type="date" id="date" required></div>
          </div>
          <div class="form-matrix">
            <div class="input-wrapper">
              <label>City*</label>
              <select id="city" required>
                <option>Pune</option>
              </select>
            </div>
            <div class="input-wrapper"><label>Preferred Time*</label><input type="time" id="time" min="09:00" max="21:30" required></div>
          </div>
          <button type="submit" class="submit-luxury-btn">Book Appointment</button>
        </form>
        <div class="success-feedback" id="confirmBox">
          <h3>RESERVATION REQUESTED</h3>
          <p id="confirmText"></p>
        </div>
      </div>
    </div>
  </section>

  <footer id="contact">
    <div class="wrap">
      <div class="footer-columns">
        <div><h4>LOCATION</h4><p class="footer-meta-text">Sasane Nagar, Lane 5<br>Hadapsar, Pune 411028</p></div>
        <div><h4>CONCIERGE</h4><p class="footer-meta-text">📞 <span>7251863769</span><br>📧 <span>mohdraja2693@gmail.com</span></p></div>
        <div><h4>TIMELINE</h4><p class="footer-meta-text">Tue-Sun: 9:00 AM - 9:30 PM<br><span style="color:#ff4444;">Monday: CLOSED</span></p></div>
      </div>
      <div class="footer-bottom-bar">© 2026 THE CUTTING EDGE SALON. ARCHITECTURAL GRAPHICS & DESIGN INSPIRATION.</div>
    </div>
  </footer>
</div>

<script>
  // ==========================================
  // THREE.JS HIGH-END CORE 3D SPATIAL ENGINE
  // ==========================================
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);
  const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('webgl-canvas'), alpha: true, antialias: true });
  
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  const geometry = new THREE.BufferGeometry();
  const pointsCount = 450;
  const positions = new Float32Array(pointsCount * 3);

  for(let i=0; i < pointsCount * 3; i++) {
    positions[i] = (Math.random() - 0.5) * 7;
  }
  geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));

  const material = new THREE.PointsMaterial({
    size: 0.03,
    color: 0xcfa63a,
    transparent: true,
    opacity: 0.7,
    blending: THREE.AdditiveBlending
  });

  const particleNetwork = new THREE.Points(geometry, material);
  scene.add(particleNetwork);
  camera.position.z = 2.5;

  let coordinateX = 0, coordinateY = 0;
  document.addEventListener('mousemove', (event) => {
    coordinateX = (event.clientX / window.innerWidth) - 0.5;
    coordinateY = (event.clientY / window.innerHeight) - 0.5;
  });

  const clock = new THREE.Clock();
  const renderLoop = () => {
    const elapsed = clock.getElapsedTime();
    particleNetwork.rotation.y = elapsed * 0.03;
    particleNetwork.rotation.x = elapsed * 0.02;

    particleNetwork.position.x += (coordinateX * 0.4 - particleNetwork.position.x) * 0.05;
    particleNetwork.position.y += (-coordinateY * 0.4 - particleNetwork.position.y) * 0.05;

    renderer.render(scene, camera);
    requestAnimationFrame(renderLoop);
  };
  renderLoop();

  window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
  });

  // ==========================================
  // GSAP MOVEMENT CONTROL
  // ==========================================
  gsap.to(".hero-inner", { opacity: 1, y: 0, duration: 1.4, ease: "power4.out" });

  // ==========================================
  // OPERATIONAL CONTROLS
  // ==========================================
  const dateInput = document.getElementById('date');
  dateInput.min = new Date().toISOString().split('T')[0];
  dateInput.addEventListener('input', function(){
    if(new Date(this.value).getDay() === 1){
      alert('Management is closed on Mondays. Kindly choose an alternative slot.');
      this.value = '';
    }
  });

  document.getElementById('booking-form').addEventListener('submit', async (e)=>{
    e.preventDefault();
    const targetBtn = e.target.querySelector('button[type="submit"]');
    targetBtn.disabled = true;
    targetBtn.innerText = 'TRANSMITTING RESERVATION...';
    
    const operationalData = {
      name: document.getElementById('name').value,
      phone: document.getElementById('phone').value,
      service: document.getElementById('service').value,
      date: document.getElementById('date').value,
      time: document.getElementById('time').value
    };
    
    try {
      const res = await fetch('/book', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(operationalData)});
      if(!res.ok) throw new Error();
      document.getElementById('booking-form').style.display = 'none';
      document.getElementById('confirmBox').style.display = 'block';
      document.getElementById('confirmText').innerText = `Thank you ${operationalData.name}. Your appointment sequence for '${operationalData.service}' has been registered for ${operationalData.date} at ${operationalData.time}.`;
    } catch (err) {
      alert('Transmission error. Contact salon desk.');
      targetBtn.disabled = false;
      targetBtn.innerText = 'Book Appointment';
    }
  });
</script>
</body>
</html>"""

def send_whatsapp(name, phone, service, date, time):
    if not WHATSAPP_TOKEN or not PHONE_NUMBER_ID:
        return
    url = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"
    headers = {"Authorization": f"Bearer {WHATSAPP_TOKEN}", "Content-Type": "application/json"}
    message = f"🔔 *NEW SALON BOOKING*\n\n👤 {name}\n📞 {phone}\n💈 {service}\n📅 {date} | ⏰ {time}"
    data = {"messaging_product": "whatsapp", "to": YOUR_BUSINESS_WHATSAPP, "type": "text", "text": {"body": message}}
    try:
        requests.post(url, headers=headers, json=data, timeout=10).raise_for_status()
    except Exception as e:
        print(f"WhatsApp Error: {e}")

def send_email(name, phone, service, date, time):
    if not EMAIL_PASSWORD:
        return
    msg = EmailMessage()
    msg.set_content(f"New Booking Secured:\\n\\nName: {name}\\nPhone: {phone}\\nService: {service}\\nDate: {date}\\nTime: {time}")
    msg['Subject'] = '🔔 New Premium Booking Acknowledged'
    msg['From'] = YOUR_EMAIL
    msg['To'] = YOUR_EMAIL
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(YOUR_EMAIL, EMAIL_PASSWORD)
            smtp.send_message(msg)
    except Exception as e:
        print(f"Email Error: {e}")

@app.route('/')
def home():
    return render_template_string(HTML_CODE)

@app.route('/book', methods=['POST'])
def book():
    d = request.get_json(silent=True)
    if not d or not all(k in d for k in ['name', 'phone', 'service', 'date', 'time']):
        return jsonify({"error": "Invalid Data"}), 400
    try:
        send_whatsapp(d['name'], d['phone'], d['service'], d['date'], d['time'])
        send_email(d['name'], d['phone'], d['service'], d['date'], d['time'])
    except Exception as e:
        print(f"Notification error: {e}")
    return jsonify({"message": "ok"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
