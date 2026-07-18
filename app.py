from flask import Flask, render_template_string, request, jsonify
import requests
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

# ====== TUMHARA BUSINESS CONTACT ======
YOUR_BUSINESS_WHATSAPP = "917251863769"  # 91 + 7251863769
YOUR_EMAIL = os.environ.get('YOUR_EMAIL', 'mohdraja2693@gmail.com')

# IMPORTANT: Never hardcode passwords in code. Set these as environment variables on your host.
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
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<!-- GSAP & Three.js Libraries for Luxury 3D Animations -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>

<style>
  :root{
    --black:#050505;
    --charcoal:#0d0d0d;
    --gold: #D4AF37;
    --gold-light: #F4E4BC;
    --gold-dim: #AA7C11;
    --cream:#F5F1E8;
    --grey:#888888;
    --shadow: 0 20px 50px rgba(212, 175, 55, 0.15);
  }
  
  *{margin:0;padding:0;box-sizing:border-box;}
  html{scroll-behavior:smooth;}
  body{background:var(--black);color:var(--cream);font-family:'Montserrat',sans-serif;overflow-x:hidden;}
  
  /* 3D Canvas Styling */
  #webgl-canvas {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 1;
    pointer-events: none;
    opacity: 0.6;
  }

  .content-wrapper {
    position: relative;
    z-index: 2;
  }

  .wrap{max-width:1300px;margin:0 auto;padding:0 50px;}

  header{position:fixed;top:0;width:100%;background:rgba(5,5,5,0.75);backdrop-filter:blur(30px);border-bottom:1px solid rgba(212,175,55,0.15);z-index:1000;}
  .navrow{display:flex;align-items:center;justify-content:space-between;padding:20px 50px;}
  .logo{display:flex;align-items:center;gap:15px;font-family:'Cinzel',serif;font-size:1.6rem;color:var(--gold);letter-spacing:4px;font-weight:700;}
  .logo-icon{font-size:2.2rem;filter:drop-shadow(0 0 10px var(--gold));}
  .nav-cta{background:transparent;color:var(--gold);border: 1px solid var(--gold);padding:12px 30px;font-weight:600;letter-spacing:2px;text-decoration:none;border-radius:0px;transition:.4s cubic-bezier(0.16, 1, 0.3, 1);}
  .nav-cta:hover{background:var(--gold);color:var(--black);box-shadow:var(--shadow);transform:translateY(-2px);}

  .hero{min-height:100vh;display:flex;align-items:center;justify-content:center;position:relative;padding-top:100px;background: radial-gradient(circle at 50% 50%, rgba(20,20,20,0.2), var(--black));}
  .hero-content{text-align:center;width:100%;opacity: 0;transform: translateY(30px);}
  .eyebrow{font-size:.85rem;letter-spacing:.6em;text-transform:uppercase;color:var(--gold);font-weight:600;margin-bottom:25px;}
  .hero h1{font-family:'Cinzel',serif;font-size:clamp(2.8rem, 8vw, 6.5rem);letter-spacing:6px;line-height:1.2;font-weight:700;text-transform:uppercase;}
  .hero h1 span{color:transparent;-webkit-text-stroke: 1px var(--gold);filter:drop-shadow(0 0 15px rgba(212,175,55,0.3));}
  .hero p{color:var(--grey);font-size:1.2rem;margin:30px 0 50px;font-weight:300;letter-spacing:2px;}
  .btn-primary{background:linear-gradient(135deg,var(--gold),var(--gold-dim));color:var(--black);padding:20px 50px;font-weight:700;letter-spacing:3px;text-decoration:none;font-size:1rem;border-radius:0px;transition:.4s;display:inline-block;box-shadow:var(--shadow);border:none;}
  .btn-primary:hover{transform:translateY(-5px) scale(1.02);box-shadow:0 30px 60px rgba(212,175,55,0.35);}

  .timing-bar{background:rgba(212,175,55,0.1);backdrop-filter:blur(10px);border-top:1px solid rgba(212,175,55,0.2);border-bottom:1px solid rgba(212,175,55,0.2);color:var(--gold-light);text-align:center;padding:20px;font-weight:600;font-size:1rem;letter-spacing:3px;}

  #services{padding:140px 0;background:transparent;}
  .sec-head{text-align:center;margin-bottom:90px;}
  .sec-head h2{font-family:'Cinzel',serif;font-size:3.2rem;color:var(--gold);letter-spacing:4px;}
  .svc-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:40px;}
  .svc-category{background:rgba(15,15,15,0.7);backdrop-filter:blur(10px);border:1px solid rgba(212,175,55,0.1);padding:50px 35px;transition:.5s;border-radius:0px;}
  .svc-category:hover{border-color:var(--gold);box-shadow:var(--shadow);transform:translateY(-10px);}
  .svc-category h3{font-family:'Cinzel',serif;font-size:1.6rem;color:var(--gold);margin-bottom:30px;letter-spacing:3px;text-align:center;border-bottom: 1px solid rgba(212,175,55,0.2);padding-bottom:15px;}
  .svc-item{display:flex;justify-content:space-between;padding:18px 0;border-bottom:1px solid rgba(212,175,55,0.08);font-size:0.95rem;letter-spacing:1px;}
  .svc-item:last-child{border:none;}
  .svc-price{color:var(--gold-light);font-weight:700;font-size:1.05rem;}

  #book{padding:140px 0;background:transparent;}
  .book-shell{max-width:850px;margin:0 auto;background:rgba(10,10,10,0.85);backdrop-filter:blur(15px);border:1px solid var(--gold);padding:70px 60px;box-shadow:var(--shadow);}
  .book-shell h2{text-align:center;font-family:'Cinzel',serif;font-size:2.8rem;color:var(--gold);letter-spacing:4px;margin-bottom:10px;}
  .off-note{text-align:center;color:#ff4f4f;font-weight:600;margin-bottom:45px;letter-spacing:2px;font-size:0.85rem;}
  .f-row{display:grid;grid-template-columns:1fr 1fr;gap:30px;margin-bottom:30px;}
  .field label{display:block;font-size:.75rem;letter-spacing:3px;color:var(--gold);margin-bottom:12px;font-weight:600;text-transform:uppercase;}
  .field input,.field select{width:100%;padding:18px;background:rgba(5,5,5,0.8);border:1px solid rgba(212,175,55,0.25);color:var(--cream);font-family:'Montserrat';font-size:0.95rem;transition: 0.3s;}
  .field input:focus,.field select:focus{outline:none;border-color:var(--gold);box-shadow:0 0 15px rgba(212,175,55,0.2);}
  .btn-book{background:linear-gradient(135deg,var(--gold),var(--gold-dim));color:var(--black);width:100%;padding:20px;font-weight:700;letter-spacing:4px;font-size:1rem;border:none;margin-top:25px;cursor:pointer;transition: 0.3s;}
  .btn-book:hover{filter:brightness(1.1);letter-spacing:5px;}
  .confirm-box{display:none;text-align:center;padding:40px;border:1px solid var(--gold);margin-top:40px;background:rgba(212,175,55,0.05);}
  .confirm-box h3{color:var(--gold);font-family:'Cinzel',serif;font-size:2rem;margin-bottom:15px;}

  #contact{padding:90px 0;background:var(--charcoal);border-top:1px solid rgba(212,175,55,0.15);}
  .contact-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:50px;text-align:center;}
  .contact-grid h4{color:var(--gold);margin-bottom:25px;letter-spacing:3px;font-family:'Cinzel',serif;font-size:1.1rem;}
  .contact-info{font-size:1rem;color:var(--grey);line-height:1.8;letter-spacing:1px;}
  .contact-info span{color:var(--gold-light);font-weight:600;}
  .foot-bottom{padding-top:40px;color:var(--grey);border-top:1px solid rgba(212,175,55,0.08);margin-top:60px;text-align:center;letter-spacing:2px;font-size:0.85rem;}

  @media(max-width:1000px){.svc-grid{grid-template-columns:1fr;}.contact-grid{grid-template-columns:1fr;}}
  @media(max-width:900px){.f-row{grid-template-columns:1fr;}.wrap{padding:0 25px;}.book-shell{padding:40px 25px;}}
</style>
</head>
<body>

<!-- Three.js Container for 3D Background -->
<canvas id="webgl-canvas"></canvas>

<div class="content-wrapper">
  <header>
    <div class="navrow">
      <div class="logo"><span class="logo-icon">🧔</span> THE CUTTING EDGE</div>
      <a href="#book" class="nav-cta">BOOK NOW</a>
    </div>
  </header>

  <section class="hero">
    <div class="hero-content">
      <p class="eyebrow">Premium Gents Grooming</p>
      <h1>THE <span>CUTTING EDGE</span><br>GENTS SALON</h1>
      <p>Where Style Meets Attitude. KGF Style Grooming Experience.</p>
      <a href="#book" class="btn-primary">RESERVE YOUR EXPERIENCE</a>
    </div>
  </section>

  <div class="timing-bar">⏰ TIMING: 9:00 AM TO 9:30 PM DAILY | MONDAY CLOSED</div>

  <section id="services">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">Signature Services</p>
        <h2>SERVICES & PRICING</h2>
      </div>
      <div class="svc-grid">
        <div class="svc-category">
          <h3>HAIR & BEARD</h3>
          <div class="svc-item"><span>Hair Cut</span><span class="svc-price">₹130</span></div>
          <div class="svc-item"><span>Beard Trim + Shave</span><span class="svc-price">₹90</span></div>
          <div class="svc-item"><span>Beard Clear</span><span class="svc-price">₹80</span></div>
          <div class="svc-item"><span>Zero Trim</span><span class="svc-price">₹70</span></div>
          <div class="svc-item"><span>Curl Hair cutting</span><span class="svc-price">₹150</span></div>
        </div>
        <div class="svc-category">
          <h3>HAIR COLOR</h3>
          <div class="svc-item"><span>Loreal Majrel</span><span class="svc-price">₹380</span></div>
          <div class="svc-item"><span>Loreal Inoa</span><span class="svc-price">₹550</span></div>
          <div class="svc-item"><span>Garnier</span><span class="svc-price">₹250</span></div>
          <div class="svc-item"><span>Raaga</span><span class="svc-price">₹250</span></div>
          <div class="svc-item"><span>Strex</span><span class="svc-price">₹250</span></div>
        </div>
        <div class="svc-category">
          <h3>FACIAL & D-TAN</h3>
          <div class="svc-item"><span>Hydra Facial</span><span class="svc-price">₹2999</span></div>
          <div class="svc-item"><span>Loreal Facial</span><span class="svc-price">₹1299</span></div>
          <div class="svc-item"><span>Lotus Facial</span><span class="svc-price">₹999</span></div>
          <div class="svc-item"><span>O3+ Facial</span><span class="svc-price">₹2299</span></div>
          <div class="svc-item"><span>O3+ Cleanup</span><span class="svc-price">₹1399</span></div>
          <div class="svc-item"><span>D-Tan Raaga</span><span class="svc-price">₹299</span></div>
          <div class="svc-item"><span>D-Tan O3+</span><span class="svc-price">₹399</span></div>
        </div>
      </div>
    </div>
  </section>

  <section id="book">
    <div class="wrap">
      <div class="book-shell">
        <h2>BOOK APPOINTMENT</h2>
        <p class="off-note">* NOTE: WE ARE CLOSED ON MONDAY *</p>
        <form id="booking-form">
          <div class="f-row">
            <div class="field"><label>Full Name</label><input type="text" id="name" required></div>
            <div class="field"><label>Phone Number</label><input type="tel" id="phone" required pattern="[0-9]{10}" title="Enter a 10-digit phone number"></div>
          </div>
          <div class="f-row">
            <div class="field">
              <label>Select Service</label>
              <select id="service" required>
                <option value="">-- Choose Service --</option>
                <option>Hair Cut - ₹130</option><option>Beard Trim + Shave - ₹90</option>
                <option>Beard Clear - ₹80</option><option>Zero Trim - ₹70</option><option>Curl Hair Setting - ₹150</option>
                <option>Loreal Majrel - ₹380</option><option>Loreal Inoa - ₹550</option><option>Garnier - ₹250</option><option>Raaga - ₹250</option><option>Strex - ₹250</option>
                <option>Hydra Facial - ₹2999</option><option>Loreal Facial - ₹1299</option><option>Lotus Facial - ₹999</option><option>O3+ Facial - ₹2299</option><option>O3+ Cleanup - ₹1399</option><option>D-Tan Raaga - ₹299</option><option>D-Tan O3+ - ₹399</option>
              </select>
            </div>
            <div class="field"><label>Preferred Date</label><input type="date" id="date" required></div>
          </div>
          <div class="field"><label>Preferred Time - 9:00 AM to 9:30 PM</label><input type="time" id="time" min="09:00" max="21:30" required></div>
          <button type="submit" class="btn-book">CONFIRM BOOKING</button>
        </form>
        <div class="confirm-box" id="confirmBox">
          <h3>BOOKING CONFIRMED</h3>
          <p id="confirmText"></p>
        </div>
      </div>
    </div>
  </section>

  <footer id="contact">
    <div class="wrap">
      <div class="contact-grid">
        <div><h4>VISIT US</h4><p class="contact-info">Sasane Nagar, Lane 5<br>Hadapsar, Pune 411028</p></div>
        <div><h4>CONTACT</h4><p class="contact-info">📞 <span>7251863769</span><br>📧 <span>mohdraja2693@gmail.com</span></p></div>
        <div><h4>HOURS</h4><p class="contact-info">Tue-Sun: 9AM - 9:30PM<br><span style="color:#ff6b6b;">Monday: CLOSED</span></p></div>
      </div>
      <div class="foot-bottom">© 2026 THE CUTTING EDGE GENTS SALON. LUXURY REDEFINED.</div>
    </div>
  </footer>
</div>

<script>
  // ==========================================
  # THREE.JS LUXURY 3D ENGINE
  // ==========================================
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
  const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('webgl-canvas'), alpha: true, antialias: true });
  
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  // Create 3D Floating Geometry (Luxury Grid Node Effect)
  const geometry = new THREE.BufferGeometry();
  const verticesCount = 600;
  const posArray = new Float32Array(verticesCount * 3);

  for(let i=0; i < verticesCount * 3; i++) {
    posArray[i] = (Math.random() - 0.5) * 8;
  }
  geometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));

  // Premium Gold Particles Material
  const material = new THREE.PointsMaterial({
    size: 0.025,
    color: 0xD4AF37,
    transparent: true,
    opacity: 0.8,
    blending: THREE.AdditiveBlending
  });

  const particlesMesh = new THREE.Points(geometry, material);
  scene.add(particlesMesh);
  camera.position.z = 3;

  // Mouse Interaction Variables
  let mouseX = 0, mouseY = 0;
  document.addEventListener('mousemove', (e) => {
    mouseX = (e.clientX / window.innerWidth) - 0.5;
    mouseY = (e.clientY / window.innerHeight) - 0.5;
  });

  // 3D Animation Loop
  const clock = new THREE.Clock();
  const animate = () => {
    const elapsedTime = clock.getElapsedTime();
    particlesMesh.rotation.y = elapsedTime * 0.05;
    particlesMesh.rotation.x = elapsedTime * 0.03;

    // Smooth physics inertia tracking mouse movements
    particlesMesh.position.x += (mouseX * 0.5 - particlesMesh.position.x) * 0.05;
    particlesMesh.position.y += (-mouseY * 0.5 - particlesMesh.position.y) * 0.05;

    renderer.render(scene, camera);
    requestAnimationFrame(animate);
  };
  animate();

  // Window Resize Event
  window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
  });

  // ==========================================
  # GSAP LUXURY CINEMATIC ANIMATIONS
  // ==========================================
  gsap.registerPlugin(ScrollTrigger);

  // Hero Entry Animation
  gsap.to(".hero-content", {
    opacity: 1,
    y: 0,
    duration: 1.5,
    ease: "power4.out",
    delay: 0.2
  });

  // Scroll Animations for Service Cards
  gsap.from(".svc-category", {
    scrollTrigger: {
      trigger: "#services",
      start: "top 70%",
    },
    opacity: 0,
    y: 50,
    duration: 1,
    stagger: 0.2,
    ease: "power3.out"
  });

  // Scroll Animations for Booking Shell
  gsap.from(".book-shell", {
    scrollTrigger: {
      trigger: "#book",
      start: "top 75%",
    },
    opacity: 0,
    scale: 0.95,
    duration: 1.2,
    ease: "power2.out"
  });

  // ==========================================
  # FUNCTIONAL BOOKING VALIDATION & SUBMIT
  // ==========================================
  const dateInput = document.getElementById('date');
  dateInput.min = new Date().toISOString().split('T')[0];
  dateInput.addEventListener('input', function(){
    const selectedDate = new Date(this.value);
    if(selectedDate.getDay() === 1){
      alert('Sorry, We are Closed on Monday. Please select another day.');
      this.value = '';
    }
  });

  document.getElementById('booking-form').addEventListener('submit', async (e)=>{
    e.preventDefault();
    const submitBtn = e.target.querySelector('button[type="submit"]');
    submitBtn.disabled = true;
    submitBtn.innerText = 'PROCESSING RESERVATION...';
    
    const data = {
      name: document.getElementById('name').value,
      phone: document.getElementById('phone').value,
      service: document.getElementById('service').value,
      date: document.getElementById('date').value,
      time: document.getElementById('time').value
    };
    
    try {
      const res = await fetch('/book', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(data)});
      if(!res.ok) throw new Error('Booking failed');
      document.getElementById('booking-form').style.display = 'none';
      document.getElementById('confirmBox').style.display = 'block';
      document.getElementById('confirmText').innerText = `Thank you ${data.name}! Your premium reservation for '${data.service}' on ${data.date} at ${data.time} has been processed successfully.`;
    } catch (err) {
      alert('Something went wrong. Please try again or contact the front desk directly.');
      submitBtn.disabled = false;
      submitBtn.innerText = 'CONFIRM BOOKING';
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
    message = f"🔔 *NEW LUXURY GENTS BOOKING*\n\n👤 {name}\n📞 {phone}\n💈 {service}\n📅 {date} | ⏰ {time}"
    data = {"messaging_product": "whatsapp", "to": YOUR_BUSINESS_WHATSAPP, "type": "text", "text": {"body": message}}
    try:
        resp = requests.post(url, headers=headers, json=data, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"[WhatsApp] Failed to send notification: {e}")

def send_email(name, phone, service, date, time):
    if not EMAIL_PASSWORD:
        print("[Email] EMAIL_PASSWORD environment variable not set, skipping notification.")
        return
    msg = EmailMessage()
    msg.set_content(f"New Booking\nName: {name}\nPhone: {phone}\nService: {service}\nDate: {date}\nTime: {time}")
    msg['Subject'] = '🔔 New Luxury Booking - The Cutting Edge'
    msg['From'] = YOUR_EMAIL
    msg['To'] = YOUR_EMAIL
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(YOUR_EMAIL, EMAIL_PASSWORD)
            smtp.send_message(msg)
    except smtplib.SMTPException as e:
        print(f"[Email] Failed to send notification: {e}")

@app.route('/')
def home():
    return render_template_string(HTML_CODE)

@app.route('/book', methods=['POST'])
def book():
    d = request.get_json(silent=True)
    if not d:
        return jsonify({"error": "Invalid or missing JSON body"}), 400

    required_fields = ['name', 'phone', 'service', 'date', 'time']
    missing = [f for f in required_fields if not d.get(f)]
    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    try:
        send_whatsapp(d['name'], d['phone'], d['service'], d['date'], d['time'])
        send_email(d['name'], d['phone'], d['service'], d['date'], d['time'])
    except Exception as e:
        print(f"[Booking] Notification error: {e}")

    return jsonify({"message": "ok"})

if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
