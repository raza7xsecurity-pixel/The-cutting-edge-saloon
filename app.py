from flask import Flask, render_template_string, request, jsonify
import requests
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

# ====== TUMHARA BUSINESS CONTACT ======
YOUR_BUSINESS_WHATSAPP = "917251863769" # 91 + 7251863769
YOUR_EMAIL = "mohdraja2693@gmail.com"
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

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
<style>
  :root{
    --black:#000000;
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
  
  /* LUXURY HEADER */
  header{position:fixed;top:0;width:100%;background:rgba(0,0,0,.85);backdrop-filter:blur(20px);border-bottom:1px solid rgba(212,175,55,.3);z-index:1000;}
.navrow{display:flex;align-items:center;justify-content:space-between;padding:25px 50px;}
.logo{display:flex;align-items:center;gap:15px;font-family:'Cinzel',serif;font-size:1.8rem;color:var(--gold);letter-spacing:3px;font-weight:700;}
.logo-icon{font-size:2.8rem;filter:drop-shadow(0 0 10px var(--gold));}
.nav-cta{background:linear-gradient(135deg,var(--gold),var(--gold-dim));color:var(--black);padding:14px 35px;font-weight:700;letter-spacing:1.5px;text-decoration:none;border-radius:2px;transition:.3s;box-shadow:var(--shadow);}
.nav-cta:hover{transform:translateY(-3px);box-shadow:0 25px 70px -20px rgba(212,175,55,.6);}

  /* LUXURY HERO */
 .hero{min-height:100vh;background:radial-gradient(circle at 50% 50%, rgba(212,175,55,.1), transparent 70%), linear-gradient(rgba(0,0,0,.85),rgba(0,0,0,.95)), url('https://images.unsplash.com/photo-1503951914875-452162b0f3f1?q=80&w=1920') center/cover;display:flex;align-items:center;padding-top:100px;position:relative;}
 .hero::before{content:'';position:absolute;top:0;left:0;right:0;bottom:0;background:linear-gradient(45deg,transparent 30%,rgba(212,175,55,.05) 50%,transparent 70%);}
 .hero-content{position:relative;z-index:2;text-align:center;width:100%;}
.hero .eyebrow{font-size:.8rem;letter-spacing:.5em;text-transform:uppercase;color:var(--gold);font-weight:500;margin-bottom:20px;}
.hero h1{font-family:'Cinzel',serif;font-size:clamp(3rem,9vw,7rem);letter-spacing:4px;line-height:1.1;font-weight:700;}
.hero h1 span{color:var(--gold);text-shadow:0 0 30px rgba(212,175,55,.5);}
.hero p{color:var(--grey);font-size:1.3rem;margin:30px 0 50px;font-weight:300;letter-spacing:1px;}
.btn-primary{background:linear-gradient(135deg,var(--gold),var(--gold-dim));color:var(--black);padding:20px 50px;font-weight:700;letter-spacing:2px;text-decoration:none;font-size:1.1rem;border-radius:2px;transition:.4s;display:inline-block;box-shadow:var(--shadow);}
.btn-primary:hover{transform:translateY(-5px);box-shadow:0 30px 80px -20px rgba(212,175,55,.7);}

  /* TIMING BAR LUXURY */
.timing-bar{background:linear-gradient(90deg,var(--gold-dim),var(--gold),var(--gold-dim));color:var(--black);text-align:center;padding:18px;font-weight:700;font-size:1.1rem;letter-spacing:2px;box-shadow:0 10px 30px rgba(212,175,55,.3);}

  /* SERVICES LUXURY CARDS */
  #services{padding:120px 0;background:var(--charcoal);}
.sec-head{text-align:center;margin-bottom:70px;}
.sec-head .eyebrow{margin-bottom:15px;}
.sec-head h2{font-family:'Cinzel',serif;font-size:3.5rem;color:var(--gold);letter-spacing:3px;}
.svc-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:40px;}
.svc-category{background:linear-gradient(145deg,var(--black),var(--charcoal));border:1px solid rgba(212,175,55,.2);padding:50px 35px;transition:.5s;position:relative;overflow:hidden;}
.svc-category::before{content:'';position:absolute;top:0;left:-100%;width:100%;height:2px;background:linear-gradient(90deg,transparent,var(--gold),transparent);transition:.5s;}
.svc-category:hover::before{left:100%;}
.svc-category:hover{border-color:var(--gold);transform:translateY(-15px);box-shadow:var(--shadow);}
.svc-category h3{font-family:'Cinzel',serif;font-size:1.8rem;color:var(--gold);margin-bottom:30px;letter-spacing:2px;text-align:center;}
.svc-item{display:flex;justify-content:space-between;padding:15px 0;border-bottom:1px solid rgba(212,175,55,.15);font-size:1rem;}
.svc-item:last-child{border:none;}
.svc-price{color:var(--gold-light);font-weight:700;font-size:1.1rem;}

  /* BOOKING LUXURY FORM */
  #book{padding:120px 0;background:var(--black);}
.book-shell{max-width:800px;margin:0 auto;background:linear-gradient(145deg,var(--charcoal),var(--black));border:2px solid var(--gold);padding:70px 60px;box-shadow:var(--shadow);}
.book-shell h2{text-align:center;font-family:'Cinzel',serif;font-size:3rem;color:var(--gold);letter-spacing:3px;margin-bottom:10px;}
.off-note{text-align:center;color:#ff6b6b;font-weight:600;margin-bottom:40px;letter-spacing:1px;}
.f-row{display:grid;grid-template-columns:1fr 1fr;gap:25px;margin-bottom:25px;}
.field label{display:block;font-size:.8rem;letter-spacing:2px;color:var(--gold);margin-bottom:10px;font-weight:600;text-transform:uppercase;}
.field input,.field select{width:100%;padding:16px 18px;background:var(--black);border:2px solid rgba(212,175,55,.3);color:var(--cream);font-family:'Montserrat';font-size:1rem;transition:.3s;}
.field input:focus,.field select:focus{outline:none;border-color:var(--gold);box-shadow:0 0 20px rgba(212,175,55,.2);}
.btn-book{background:linear-gradient(135deg,var(--gold),var(--gold-dim));color:var(--black);width:100%;padding:20px;font-weight:700;letter-spacing:3px;font-size:1.1rem;border:none;margin-top:20px;transition:.4s;}
.btn-book:hover{transform:translateY(-3px);box-shadow:var(--shadow);}
.confirm-box{display:none;text-align:center;padding:40px;border:2px solid var(--gold);margin-top:40px;background:rgba(212,175,55,.05);}
.confirm-box h3{color:var(--gold);font-family:'Cinzel',serif;font-size:2rem;margin-bottom:15px;}

  /* CONTACT LUXURY */
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
        <div class="svc-item"><span>Curl Hair Setting</span><span class="svc-price">₹150</span></div>
      </div>
      <div class="svc-category">
        <h3>HAIR COLOR</h3>
        <div class="svc-item"><span>Loreal Majrel</span><span class="svc-price">₹380</span></div>