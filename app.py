from flask import Flask, render_template_string, request, jsonify
import requests
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

# ====== TUMHARA BUSINESS CONTACT ======
YOUR_BUSINESS_WHATSAPP = "917251863769" # 91 + 7251863769
YOUR_EMAIL = "mohdraja2693@gmail.com"
EMAIL_PASSWORD = os.environ.get('xqgt gspi fscv xosd') # Abhi khali rehne do

# ====== META WHATSAPP KEYS ======
WHATSAPP_TOKEN = os.environ.get('WHATSAPP_TOKEN') # Baad me dalenge
PHONE_NUMBER_ID = os.environ.get('PHONE_NUMBER_ID') # Baad me dalenge


HTML_CODE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Cutting Edge | Luxury Gents Salon - Pune</title>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root{
    --black:#000;
    --charcoal:#0F0F0F;
    --gold:#D4AF37;
    --gold-light:#F4E4BC;
    --gold-dim:#B8941F;
    --cream:#F5F1E8;
    --grey:#A0A0A0;
    --shadow: 0 20px 60px -20px rgba(212,175,55,.4);
  }
  *{margin:0;padding:0;box-sizing:border-box;}
  html{scroll-behavior:smooth;}
  body{background:var(--black);color:var(--cream);font-family:'Montserrat',sans-serif;overflow-x:hidden;}
 .wrap{max-width:1300px;margin:0 auto;padding:0 50px;}

  header{position:fixed;top:0;width:100%;background:rgba(0,0,0,.85);backdrop-filter:blur(20px);border-bottom:1px solid rgba(212,175,55,.3);z-index:1000;}
 .navrow{display:flex;align-items:center;justify-content:space-between;padding:25px 50px;}
 .logo{display:flex;align-items:center;gap:15px;font-family:'Cinzel',serif;font-size:1.8rem;color:var(--gold);letter-spacing:3px;font-weight:700;}
 .logo-icon{font-size:2.8rem;filter:drop-shadow(0 0 10px var(--gold));}
 .nav-cta{background:linear-gradient(135deg,var(--gold),var(--gold-dim));color:var(--black);padding:14px 35px;font-weight:700;letter-spacing:1.5px;text-decoration:none;border-radius:2px;transition:.3s;box-shadow:var(--shadow);}
 .nav-cta:hover{transform:translateY(-3px);box-shadow:0 25px 70px -20px rgba(212,175,55,.6);}

 .hero{min-height:100vh;background:radial-gradient(circle at 50% 50%, rgba(212,175,55,.1), transparent 70%), linear-gradient(rgba(0,0,0,.85),rgba(0,0,0,.95)), url('https://images.unsplash.com/photo-1503951914875-452162b0f3f1?q=80&w=1920') center/cover;display:flex;align-items:center;padding-top:100px;position:relative;}
 .hero-content{position:relative;z-index:2;text-align:center;width:100%;}
 .eyebrow{font-size:.8rem;letter-spacing:.5em;text-transform:uppercase;color:var(--gold);font-weight:500;margin-bottom:20px;}
 .hero h1{font-family:'Cinzel',serif;font-size:clamp(3rem,9vw,7rem);letter-spacing:4px;line-height:1.1;font-weight:700;}
 .hero h1 span{color:var(--gold);text-shadow:0 0 30px rgba(212,175,55,.5);}
 .hero p{color:var(--grey);font-size:1.3rem;margin:30px 0 50px;font-weight:300;letter-spacing:1px;}
 .btn-primary{background:linear-gradient(135deg,var(--gold),var(--gold-dim));color:var(--black);padding:20px 50px;font-weight:700;letter-spacing:2px;text-decoration:none;font-size:1.1rem;border-radius:2px;transition:.4s;display:inline-block;box-shadow:var(--shadow);}
 .btn-primary:hover{transform:translateY(-5px);box-shadow:0 30px 80px -20px rgba(212,175,55,.7);}

 .timing-bar{background:linear-gradient(90deg,var(--gold-dim),var(--gold),var(--gold-dim));color:var(--black);text-align:center;padding:18px;font-weight:700;font-size:1.1rem;letter-spacing:2px;box-shadow:0 10px 30px rgba(212,175,55,.3);}

  #services{padding:120px 0;background:var(--charcoal);}
 .sec-head{text-align:center;margin-bottom:70px;}
 .sec-head h2{font-family:'Cinzel',serif;font-size:3.5rem;color:var(--gold);letter-spacing:3px;}
 .svc-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:40px;}
 .svc-category{background:linear-gradient(145deg,var(--black),var(--charcoal));border:1px solid rgba(212,175,55,.2);padding:50px 35px;transition:.5s;}
 .svc-category:hover{border-color:var(--gold);transform:translateY(-15px);box-shadow:var(--shadow);}
 .svc-category h3{font-family:'Cinzel',serif;font-size:1.8rem;color:var(--gold);margin-bottom:30px;letter-spacing:2px;text-align:center;}
 .svc-item{display:flex;justify-content:space-between;padding:15px 0;border-bottom:1px solid rgba(212,175,55,.15);font-size:1rem;}
 .svc-item:last-child{border:none;}
 .svc-price{color:var(--gold-light);font-weight:700;font-size:1.1rem;}

  #book{padding:120px 0;background:var(--black);}
 .book-shell{max-width:800px;margin:0 auto;background:linear-gradient(145deg,var(--charcoal),var(--black));border:2px solid var(--gold);padding:70px 60px;box-shadow:var(--shadow);}
 .book-shell h2{text-align:center;font-family:'Cinzel',serif;font-size:3rem;color:var(--gold);letter-spacing:3px;margin-bottom:10px;}
 .off-note{text-align:center;color:#ff6b6b;font-weight:600;margin-bottom:40px;letter-spacing:1px;}
 .f-row{display:grid;grid-template-columns:1fr 1fr;gap:25px;margin-bottom:25px;}
 .field label{display:block;font-size:.8rem;letter-spacing:2px;color:var(--gold);margin-bottom:10px;font-weight:600;text-transform:uppercase;}
 .field input,.field select{width:100%;padding:16px 18px;background:var(--black);border:2px solid rgba(212,175,55,.3);color:var(--cream);font-family:'Montserrat';font-size:1rem;}
 .btn-book{background:linear-gradient(135deg,var(--gold),var(--gold-dim));color:var(--black);width:100%;padding:20px;font-weight:700;letter-spacing:3px;font-size:1.1rem;border:none;margin-top:20px;}
 .confirm-box{display:none;text-align:center;padding:40px;border:2px solid var(--gold);margin-top:40px;background:rgba(212,175,55,.05);}
 .confirm-box h3{color:var(--gold);font-family:'Cinzel',serif;font-size:2rem;margin-bottom:15px;}

  #contact{padding:80px 0;background:var(--charcoal);border-top:1px solid rgba(212,175,55,.3);}
 .contact-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:50px;text-align:center;}
 .contact-grid h4{color:var(--gold);margin-bottom:20px;letter-spacing:2px;font-family:'Cinzel',serif;font-size:1.2rem;}
 .contact-info{font-size:1.1rem;color:var(--grey);}
 .contact-info span{color:var(--gold-light);font-weight:700;}
 .foot-bottom{padding-top:40px;color:var(--grey);border-top:1px solid rgba(212,175,55,.2);margin-top:50px;text-align:center;letter-spacing:1px;}

  @media(max-width:1000px){.svc-grid{grid-template-columns:1fr;}.contact-grid{grid-template-columns:1fr;}}
  @media(max-width:900px){.f-row{grid-template-columns:1fr;}.wrap{padding:0 25px;}.book-shell{padding:40px 30px;}}
</style>
</head>
<body>

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
          <div class="field"><label>Phone Number</label><input type="tel" id="phone" required></div>
        </div>
        <div class="f-row">
          <div class="field">
            <label>Select Service</label>
            <select id="service" required>
              <option value="">-- Choose Service --</option>
              <option>Hair Cut - ₹130</option><option>Beard Trim + Shave - ₹90</option>
              <option>Beard Clear - ₹80</option><option>Zero Trim - ₹70</option><option>Curl Hair Setting - ₹150</option>
              <option>Loreal Majrel - ₹380</option><option>Loreal Inoa - ₹550</option><option>Garnier - ₹250</option><option>Raaga - ₹250</option><option>Strex - ₹250</option>
              <option>Hydra Facial - ₹2999</option><option>Loreal Facial - ₹1199</option><option>Lotus Facial - ₹799</option><option>O3+ Facial - ₹2299</option><option>O3+ Cleanup - ₹11s99</option><option>D-Tan Raaga - ₹299</option><option>D-Tan O3+ - ₹399</option>
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

<script>
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
    const data = {
      name: document.getElementById('name').value,
      phone: document.getElementById('phone').value,
      service: document.getElementById('service').value,
      date: document.getElementById('date').value,
      time: document.getElementById('time').value
    };
    await fetch('/book', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(data)});
    document.getElementById('booking-form').style.display = 'none';
    document.getElementById('confirmBox').style.display = 'block';
    document.getElementById('confirmText').innerText = `Thank you ${data.name}! Your booking for '${data.service}' on ${data.date} at ${data.time} is received.`;
  });
</script>
</body>
</html>"""


def send_whatsapp(name, phone, service, date, time):
    if not WHATSAPP_TOKEN: return
    url = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"
    headers = {"Authorization": f"Bearer {WHATSAPP_TOKEN}", "Content-Type": "application/json"}
    message = f"🔔 *NEW LUXURY GENTS BOOKING*\n\n👤 {name}\n📞 {phone}\n💈 {service}\n📅 {date} | ⏰ {time}"
    data = {"messaging_product": "whatsapp", "to": YOUR_BUSINESS_WHATSAPP, "type": "text", "text": {"body": message}}
    requests.post(url, headers=headers, json=data)

def send_email(name, phone, service, date, time):
    if not EMAIL_PASSWORD: return
    msg = EmailMessage()
    msg.set_content(f"New Booking\nName: {name}\nPhone: {phone}\nService: {service}\nDate: {date}\nTime: {time}")
    msg['Subject'] = '🔔 New Booking - The Cutting Edge'
    msg['From'] = YOUR_EMAIL; msg['To'] = YOUR_EMAIL
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(mohdraja2693@gmail.com, "xqgt gspi fscv xosd); smtp.send_message(msg)

@app.route('/')
def home(): return render_template_string(HTML_CODE)

@app.route('/book', methods=['POST'])
def book():
    d = request.json
    send_whatsapp(d['name'], d['phone'], d['service'], d['date'], d['time'])
    send_email(d['name'], d['phone'], d['service'], d['date'], d['time'])
    return jsonify({"message": "ok"})

if __name__ == '__main__': 
    app.run(debug=True)
