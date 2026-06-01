<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{% block title %}Armstrong Buys Houses | We Buy Houses Fast in Louisiana{% endblock %}</title>
  <meta name="description" content="{% block meta_desc %}Armstrong Buys Houses — We buy houses fast in ALL 64 Louisiana parishes. Get a fair cash offer in 24 hours. No repairs, no fees, no commissions. Call now!{% endblock %}" />
  <meta name="keywords" content="{% block meta_keys %}we buy houses Louisiana, sell my house fast Louisiana, cash home buyers Louisiana, sell house as-is Louisiana, cash offer Louisiana{% endblock %}" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="https://www.armstrongbuyshouses.com{% block canonical %}{% endblock %}" />

  <!-- Open Graph -->
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://www.armstrongbuyshouses.com{% block og_url %}{% endblock %}" />
  <meta property="og:title" content="{% block og_title %}Armstrong Buys Houses | Cash Home Buyers in Louisiana{% endblock %}" />
  <meta property="og:description" content="{% block og_desc %}We buy houses fast in all 64 Louisiana parishes. Fair cash offer in 24 hours. No repairs, no fees.{% endblock %}" />
  <meta property="og:image" content="https://www.armstrongbuyshouses.com/static/images/og-image.jpg" />

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{% block tw_title %}Armstrong Buys Houses | Louisiana Cash Home Buyers{% endblock %}" />
  <meta name="twitter:description" content="Sell your Louisiana home fast for cash. All 64 parishes. No fees, no repairs, close in 7 days." />

  <!-- Schema.org Local Business -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "RealEstateAgent",
    "name": "Armstrong Buys Houses",
    "url": "https://www.armstrongbuyshouses.com",
    "telephone": "+1-337-270-0518",
    "address": {
      "@type": "PostalAddress",
      "addressRegion": "LA",
      "addressCountry": "US"
    },
    "areaServed": "Louisiana",
    "description": "We buy houses fast in all 64 Louisiana parishes. Cash offers in 24 hours.",
    "sameAs": [
      "https://www.facebook.com/armstrongbuyshouses",
      "https://www.instagram.com/armstrongbuyshouses"
    ]
  }
  </script>

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet" />

  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --brand-green: #1a5c3a;
      --brand-green-dark: #0f3d26;
      --brand-green-light: #2a7a50;
      --accent-gold: #c8922a;
      --accent-gold-light: #e8b04a;
      --text-dark: #1a1a1a;
      --text-mid: #444;
      --text-light: #777;
      --bg-cream: #faf8f4;
      --bg-white: #ffffff;
      --border: #e8e4dc;
      --shadow: 0 4px 24px rgba(0,0,0,0.08);
      --shadow-lg: 0 16px 48px rgba(0,0,0,0.12);
    }

    html { scroll-behavior: smooth; }

    body {
      font-family: 'DM Sans', sans-serif;
      color: var(--text-dark);
      background: var(--bg-white);
      font-size: 16px;
      line-height: 1.7;
    }

    h1, h2, h3, h4 { font-family: 'Playfair Display', serif; line-height: 1.2; }

    a { color: var(--brand-green); text-decoration: none; }
    a:hover { color: var(--brand-green-light); }

    .container { max-width: 1200px; margin: 0 auto; padding: 0 24px; }
    .container-sm { max-width: 820px; margin: 0 auto; padding: 0 24px; }

    /* ===== TOP BAR ===== */
    .topbar {
      background: var(--brand-green-dark);
      color: rgba(255,255,255,0.9);
      font-size: 13px;
      padding: 8px 0;
      text-align: center;
    }
    .topbar a { color: var(--accent-gold-light); font-weight: 500; }
    .topbar strong { color: #fff; }

    /* ===== NAVBAR ===== */
    nav {
      background: var(--bg-white);
      border-bottom: 2px solid var(--brand-green);
      position: sticky;
      top: 0;
      z-index: 1000;
      box-shadow: 0 2px 12px rgba(0,0,0,0.08);
    }
    .nav-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 24px;
      max-width: 1200px;
      margin: 0 auto;
      height: 72px;
    }
    .logo {
      font-family: 'Playfair Display', serif;
      font-size: 22px;
      font-weight: 900;
      color: var(--brand-green-dark);
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .logo-icon {
      width: 42px; height: 42px;
      background: var(--brand-green);
      border-radius: 8px;
      display: flex; align-items: center; justify-content: center;
      color: #fff;
      font-size: 20px;
    }
    .logo span { color: var(--accent-gold); }

    .nav-links {
      display: flex;
      align-items: center;
      gap: 4px;
      list-style: none;
    }
    .nav-links a {
      color: var(--text-dark);
      font-size: 14px;
      font-weight: 500;
      padding: 8px 14px;
      border-radius: 6px;
      transition: all 0.2s;
    }
    .nav-links a:hover { background: #f0f7f3; color: var(--brand-green); }

    /* Dropdown */
    .dropdown { position: relative; }
    .dropdown-menu {
      display: none;
      position: absolute;
      top: calc(100% + 4px);
      left: 0;
      background: #fff;
      border: 1px solid var(--border);
      border-radius: 10px;
      box-shadow: var(--shadow-lg);
      min-width: 220px;
      padding: 8px 0;
      z-index: 100;
      max-height: 320px;
      overflow-y: auto;
    }
    .dropdown:hover .dropdown-menu { display: block; }
    .dropdown-menu a {
      display: block;
      padding: 8px 20px;
      font-size: 13px;
      color: var(--text-mid);
      border-radius: 0;
    }
    .dropdown-menu a:hover { background: #f0f7f3; color: var(--brand-green); }

    .nav-cta {
      background: var(--brand-green) !important;
      color: #fff !important;
      padding: 10px 20px !important;
      border-radius: 8px !important;
      font-weight: 600 !important;
    }
    .nav-cta:hover { background: var(--brand-green-dark) !important; }

    .mobile-toggle {
      display: none;
      background: none;
      border: none;
      cursor: pointer;
      font-size: 24px;
      color: var(--brand-green);
    }

    /* ===== HERO ===== */
    .hero {
      background: linear-gradient(135deg, var(--brand-green-dark) 0%, var(--brand-green) 60%, #2d8a5e 100%);
      padding: 80px 0 100px;
      position: relative;
      overflow: hidden;
    }
    .hero::before {
      content: '';
      position: absolute;
      inset: 0;
      background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.03'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
    }
    .hero-grid {
      display: grid;
      grid-template-columns: 1fr 420px;
      gap: 64px;
      align-items: center;
    }
    .hero-text h1 {
      font-size: clamp(36px, 5vw, 58px);
      color: #fff;
      margin-bottom: 20px;
      line-height: 1.1;
    }
    .hero-text h1 em { color: var(--accent-gold-light); font-style: normal; }
    .hero-text p { color: rgba(255,255,255,0.85); font-size: 18px; margin-bottom: 32px; }
    .hero-badges {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-bottom: 32px;
    }
    .badge {
      background: rgba(255,255,255,0.15);
      border: 1px solid rgba(255,255,255,0.25);
      color: #fff;
      padding: 6px 16px;
      border-radius: 100px;
      font-size: 13px;
      font-weight: 500;
    }
    .badge-gold {
      background: var(--accent-gold);
      border-color: var(--accent-gold);
      color: #fff;
    }
    .hero-stats {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
    }
    .stat-card {
      background: rgba(255,255,255,0.12);
      border: 1px solid rgba(255,255,255,0.2);
      border-radius: 12px;
      padding: 16px;
      text-align: center;
    }
    .stat-card .num {
      font-family: 'Playfair Display', serif;
      font-size: 32px;
      font-weight: 900;
      color: var(--accent-gold-light);
      display: block;
    }
    .stat-card .label {
      font-size: 12px;
      color: rgba(255,255,255,0.8);
    }

    /* ===== OFFER FORM ===== */
    .offer-card {
      background: #fff;
      border-radius: 16px;
      padding: 36px;
      box-shadow: var(--shadow-lg);
    }
    .offer-card h3 {
      font-family: 'Playfair Display', serif;
      font-size: 22px;
      color: var(--brand-green-dark);
      margin-bottom: 8px;
    }
    .offer-card p.sub { color: var(--text-light); font-size: 14px; margin-bottom: 24px; }

    .form-group { margin-bottom: 16px; }
    .form-group label {
      display: block;
      font-size: 13px;
      font-weight: 600;
      color: var(--text-mid);
      margin-bottom: 6px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .form-group input,
    .form-group select,
    .form-group textarea {
      width: 100%;
      padding: 12px 16px;
      border: 1.5px solid var(--border);
      border-radius: 8px;
      font-family: 'DM Sans', sans-serif;
      font-size: 15px;
      color: var(--text-dark);
      background: #fff;
      transition: border-color 0.2s;
      outline: none;
    }
    .form-group input:focus,
    .form-group select:focus,
    .form-group textarea:focus { border-color: var(--brand-green); }

    .btn-primary {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--brand-green);
      color: #fff;
      border: none;
      padding: 16px 32px;
      border-radius: 10px;
      font-family: 'DM Sans', sans-serif;
      font-size: 17px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
      width: 100%;
      justify-content: center;
    }
    .btn-primary:hover {
      background: var(--brand-green-dark);
      transform: translateY(-1px);
      box-shadow: 0 8px 24px rgba(26,92,58,0.3);
    }
    .btn-secondary {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: transparent;
      color: var(--brand-green);
      border: 2px solid var(--brand-green);
      padding: 14px 32px;
      border-radius: 10px;
      font-family: 'DM Sans', sans-serif;
      font-size: 16px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }
    .btn-secondary:hover { background: var(--brand-green); color: #fff; }

    .form-disclaimer {
      font-size: 11px;
      color: var(--text-light);
      margin-top: 12px;
      line-height: 1.5;
    }

    /* ===== SECTIONS ===== */
    .section { padding: 80px 0; }
    .section-alt { background: var(--bg-cream); }
    .section-dark { background: var(--brand-green-dark); color: #fff; }

    .section-header { text-align: center; margin-bottom: 56px; }
    .section-header .eyebrow {
      display: inline-block;
      color: var(--brand-green);
      font-size: 13px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 2px;
      margin-bottom: 12px;
    }
    .section-header h2 { font-size: clamp(28px, 4vw, 42px); margin-bottom: 16px; }
    .section-header p { color: var(--text-mid); font-size: 17px; max-width: 580px; margin: 0 auto; }

    /* ===== HOW IT WORKS ===== */
    .steps-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 32px;
    }
    .step-card {
      text-align: center;
      padding: 40px 32px;
      background: #fff;
      border-radius: 16px;
      border: 1px solid var(--border);
      position: relative;
    }
    .step-num {
      width: 56px; height: 56px;
      background: var(--brand-green);
      color: #fff;
      border-radius: 50%;
      display: flex; align-items: center; justify-content: center;
      font-family: 'Playfair Display', serif;
      font-size: 24px;
      font-weight: 700;
      margin: 0 auto 24px;
    }
    .step-card h3 { font-size: 20px; margin-bottom: 12px; }
    .step-card p { color: var(--text-mid); font-size: 15px; }

    /* ===== REASONS GRID ===== */
    .reasons-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
    }
    .reason-card {
      padding: 28px;
      background: #fff;
      border-radius: 12px;
      border: 1px solid var(--border);
      border-left: 4px solid var(--brand-green);
    }
    .reason-icon {
      font-size: 32px;
      margin-bottom: 12px;
    }
    .reason-card h3 { font-size: 18px; margin-bottom: 8px; }
    .reason-card p { color: var(--text-mid); font-size: 14px; }

    /* ===== COMPARISON TABLE ===== */
    .comparison-table {
      width: 100%;
      border-collapse: collapse;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: var(--shadow);
    }
    .comparison-table th {
      padding: 20px;
      text-align: center;
      font-family: 'DM Sans', sans-serif;
      font-size: 15px;
      font-weight: 600;
    }
    .comparison-table th:first-child { text-align: left; }
    .comparison-table thead tr { background: var(--brand-green-dark); color: #fff; }
    .comparison-table thead th.highlight { background: var(--brand-green); }
    .comparison-table td {
      padding: 16px 20px;
      border-bottom: 1px solid var(--border);
      font-size: 14px;
    }
    .comparison-table tbody tr:nth-child(even) { background: var(--bg-cream); }
    .comparison-table td.check { text-align: center; color: #22a05e; font-size: 20px; }
    .comparison-table td.cross { text-align: center; color: #d44; font-size: 18px; }
    .comparison-table td.maybe { text-align: center; color: var(--accent-gold); font-size: 18px; }

    /* ===== TESTIMONIALS ===== */
    .testimonials-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
    }
    .testimonial-card {
      background: #fff;
      border-radius: 12px;
      padding: 28px;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }
    .stars { color: var(--accent-gold); font-size: 18px; margin-bottom: 12px; }
    .testimonial-text { color: var(--text-mid); font-size: 15px; margin-bottom: 16px; font-style: italic; }
    .reviewer { font-weight: 600; font-size: 14px; color: var(--text-dark); }
    .reviewer-location { font-size: 12px; color: var(--text-light); }

    /* ===== PARISHES SECTION ===== */
    .parishes-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
      gap: 12px;
    }
    .parish-link {
      display: block;
      padding: 12px 16px;
      background: #fff;
      border: 1px solid var(--border);
      border-radius: 8px;
      font-size: 14px;
      color: var(--text-mid);
      font-weight: 500;
      transition: all 0.2s;
      text-align: center;
    }
    .parish-link:hover {
      border-color: var(--brand-green);
      color: var(--brand-green);
      background: #f0f7f3;
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(26,92,58,0.1);
    }

    /* ===== FAQ ===== */
    .faq-item {
      border-bottom: 1px solid var(--border);
      padding: 20px 0;
    }
    .faq-question {
      font-family: 'Playfair Display', serif;
      font-size: 18px;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      color: var(--text-dark);
    }
    .faq-answer {
      color: var(--text-mid);
      font-size: 15px;
      margin-top: 12px;
      display: none;
      line-height: 1.8;
    }
    .faq-item.open .faq-answer { display: block; }
    .faq-toggle { font-size: 22px; color: var(--brand-green); font-weight: 300; }

    /* ===== CTA BANNER ===== */
    .cta-banner {
      background: var(--brand-green);
      padding: 64px 0;
      text-align: center;
    }
    .cta-banner h2 { color: #fff; font-size: 36px; margin-bottom: 16px; }
    .cta-banner p { color: rgba(255,255,255,0.85); font-size: 18px; margin-bottom: 32px; }
    .cta-buttons { display: flex; gap: 16px; justify-content: center; flex-wrap: wrap; }
    .btn-white {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #fff;
      color: var(--brand-green);
      border: none;
      padding: 14px 32px;
      border-radius: 10px;
      font-size: 16px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
      text-decoration: none;
    }
    .btn-white:hover { background: #f0f0f0; transform: translateY(-1px); }
    .btn-outline-white {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: transparent;
      color: #fff;
      border: 2px solid rgba(255,255,255,0.6);
      padding: 14px 32px;
      border-radius: 10px;
      font-size: 16px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
      text-decoration: none;
    }
    .btn-outline-white:hover { background: rgba(255,255,255,0.1); border-color: #fff; color: #fff; }

    /* ===== FOOTER ===== */
    footer {
      background: var(--brand-green-dark);
      color: rgba(255,255,255,0.8);
      padding: 64px 0 32px;
    }
    .footer-grid {
      display: grid;
      grid-template-columns: 2fr 1fr 1fr 1fr;
      gap: 48px;
      margin-bottom: 48px;
    }
    .footer-brand .logo { color: #fff; margin-bottom: 16px; }
    .footer-brand p { font-size: 14px; color: rgba(255,255,255,0.65); margin-bottom: 20px; }
    .footer-col h4 {
      color: #fff;
      font-family: 'DM Sans', sans-serif;
      font-weight: 600;
      font-size: 14px;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 16px;
    }
    .footer-col ul { list-style: none; }
    .footer-col ul li { margin-bottom: 10px; }
    .footer-col ul a { color: rgba(255,255,255,0.7); font-size: 14px; transition: color 0.2s; }
    .footer-col ul a:hover { color: var(--accent-gold-light); }
    .footer-bottom {
      border-top: 1px solid rgba(255,255,255,0.1);
      padding-top: 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 13px;
      color: rgba(255,255,255,0.5);
      flex-wrap: wrap;
      gap: 12px;
    }
    .footer-bottom a { color: rgba(255,255,255,0.6); }
    .social-links { display: flex; gap: 12px; }
    .social-link {
      width: 36px; height: 36px;
      background: rgba(255,255,255,0.1);
      border-radius: 50%;
      display: flex; align-items: center; justify-content: center;
      color: rgba(255,255,255,0.8);
      font-size: 16px;
      transition: all 0.2s;
    }
    .social-link:hover { background: var(--accent-gold); color: #fff; }

    /* ===== PHONE CTA ===== */
    .phone-cta {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 22px;
      font-weight: 700;
      color: var(--accent-gold-light);
      text-decoration: none;
    }
    .phone-cta:hover { color: #fff; }

    /* ===== PAGE HEADER ===== */
    .page-header {
      background: linear-gradient(135deg, var(--brand-green-dark), var(--brand-green));
      padding: 64px 0;
      text-align: center;
    }
    .page-header h1 { color: #fff; font-size: clamp(28px, 4vw, 48px); margin-bottom: 12px; }
    .page-header p { color: rgba(255,255,255,0.85); font-size: 18px; max-width: 600px; margin: 0 auto; }

    /* ===== STICKY MOBILE CTA ===== */
    .mobile-cta-bar {
      display: none;
      position: fixed;
      bottom: 0;
      left: 0; right: 0;
      background: var(--brand-green-dark);
      padding: 12px 20px;
      z-index: 999;
      gap: 12px;
    }
    .mobile-cta-bar a {
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 14px;
      border-radius: 8px;
      font-weight: 600;
      font-size: 15px;
      text-decoration: none;
    }
    .mobile-cta-bar .call { background: var(--accent-gold); color: #fff; }
    .mobile-cta-bar .offer { background: #fff; color: var(--brand-green); }

    /* ===== RESPONSIVE ===== */
    @media (max-width: 900px) {
      .nav-links { display: none; }
      .mobile-toggle { display: block; }
      .nav-links.open {
        display: flex;
        flex-direction: column;
        position: absolute;
        top: 72px;
        left: 0; right: 0;
        background: #fff;
        border-top: 1px solid var(--border);
        padding: 16px;
        box-shadow: var(--shadow-lg);
      }
      .hero-grid { grid-template-columns: 1fr; }
      .steps-grid { grid-template-columns: 1fr; }
      .reasons-grid { grid-template-columns: 1fr 1fr; }
      .testimonials-grid { grid-template-columns: 1fr; }
      .footer-grid { grid-template-columns: 1fr 1fr; }
      .mobile-cta-bar { display: flex; }
      body { padding-bottom: 72px; }
    }
    @media (max-width: 600px) {
      .reasons-grid { grid-template-columns: 1fr; }
      .footer-grid { grid-template-columns: 1fr; }
      .hero-stats { grid-template-columns: 1fr 1fr 1fr; }
    }

    /* ===== TRUST BAR ===== */
    .trust-bar {
      background: #fff;
      border-bottom: 1px solid var(--border);
      padding: 16px 0;
    }
    .trust-items {
      display: flex;
      justify-content: center;
      gap: 40px;
      flex-wrap: wrap;
    }
    .trust-item {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 14px;
      font-weight: 500;
      color: var(--text-mid);
    }
    .trust-item .icon { color: var(--brand-green); font-size: 18px; }

    /* Success message */
    .success-msg {
      display: none;
      background: #d4edda;
      border: 1px solid #c3e6cb;
      color: #155724;
      padding: 16px;
      border-radius: 8px;
      margin-top: 16px;
      text-align: center;
      font-weight: 500;
    }
  </style>
  {% block head %}{% endblock %}
</head>
<body>
  <!-- Top Bar -->
  <div class="topbar">
    <strong>📞 Call or Text:</strong>
    <a href="tel:+13372700518">(337) 270-0518</a>
    &nbsp;|&nbsp;
    We Buy Houses in ALL 64 Louisiana Parishes — <strong>Cash Offer in 24 Hours!</strong>
  </div>

  <!-- Navigation -->
  <nav>
    <div class="nav-inner">
      <a href="/" class="logo">
        <div class="logo-icon">🏠</div>
        Armstrong<span>Buys</span>Houses
      </a>
      <button class="mobile-toggle" onclick="toggleNav()" aria-label="Menu">☰</button>
      <ul class="nav-links" id="navLinks">
        <li><a href="/">Home</a></li>
        <li><a href="/how-it-works">How It Works</a></li>
        <li><a href="/sell-your-house">Sell Your House</a></li>
        <li><a href="/we-buy-houses">We Buy Houses</a></li>
        <li class="dropdown">
          <a href="#" onclick="return false;">Parishes ▾</a>
          <div class="dropdown-menu">
            {% for parish in parishes %}
            <a href="/parish/{{ parish.lower().replace(' ', '-').replace('.', '') }}">{{ parish }} Parish</a>
            {% endfor %}
          </div>
        </li>
        <li><a href="/faq">FAQ</a></li>
        <li><a href="/reviews">Reviews</a></li>
        <li><a href="/blog">Blog</a></li>
        <li><a href="/about">About Us</a></li>
        <li><a href="/cash-offer" class="nav-cta">Get Cash Offer</a></li>
      </ul>
    </div>
  </nav>

  {% block content %}{% endblock %}

  <!-- CTA Banner -->
  {% block cta_banner %}
  <section class="cta-banner">
    <div class="container">
      <h2>Ready to Sell Your Louisiana Home Fast?</h2>
      <p>Get a fair, no-obligation cash offer within 24 hours. We buy in all 64 parishes.</p>
      <div class="cta-buttons">
        <a href="/cash-offer" class="btn-white">🏡 Get My Cash Offer</a>
        <a href="tel:+13372700518" class="btn-outline-white">📞 Call (337) 270-0518</a>
      </div>
    </div>
  </section>
  {% endblock %}

  <!-- Footer -->
  <footer>
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="logo" style="color:#fff; margin-bottom:16px;">
            <div class="logo-icon">🏠</div>
            Armstrong<span style="color:var(--accent-gold-light);">Buys</span>Houses
          </div>
          <p>Louisiana's trusted cash home buyer since 2020. We buy houses in all 64 parishes — fast, fair, and hassle-free.</p>
          <a href="tel:+13372700518" class="phone-cta">📞 (337) 270-0518</a>
          <div class="social-links" style="margin-top:20px;">
            <a href="#" class="social-link" aria-label="Facebook">f</a>
            <a href="#" class="social-link" aria-label="Instagram">in</a>
            <a href="#" class="social-link" aria-label="Google">G</a>
          </div>
        </div>
        <div class="footer-col">
          <h4>Quick Links</h4>
          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/how-it-works">How It Works</a></li>
            <li><a href="/sell-your-house">Sell Your House</a></li>
            <li><a href="/we-buy-houses">We Buy Houses</a></li>
            <li><a href="/cash-offer">Get Cash Offer</a></li>
            <li><a href="/reviews">Reviews</a></li>
            <li><a href="/faq">FAQ</a></li>
            <li><a href="/blog">Blog</a></li>
            <li><a href="/about">About Us</a></li>
            <li><a href="/contact">Contact</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Major Parishes</h4>
          <ul>
            <li><a href="/parish/orleans">Orleans Parish</a></li>
            <li><a href="/parish/east-baton-rouge">East Baton Rouge</a></li>
            <li><a href="/parish/jefferson">Jefferson Parish</a></li>
            <li><a href="/parish/caddo">Caddo Parish</a></li>
            <li><a href="/parish/lafayette">Lafayette Parish</a></li>
            <li><a href="/parish/calcasieu">Calcasieu Parish</a></li>
            <li><a href="/parish/st-tammany">St. Tammany Parish</a></li>
            <li><a href="/parish/livingston">Livingston Parish</a></li>
            <li><a href="/parish/tangipahoa">Tangipahoa Parish</a></li>
            <li><a href="/parish/ouachita">Ouachita Parish</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>We Buy Houses</h4>
          <ul>
            <li><a href="/sell-your-house#foreclosure">Facing Foreclosure</a></li>
            <li><a href="/sell-your-house#divorce">Going Through Divorce</a></li>
            <li><a href="/sell-your-house#inherited">Inherited Property</a></li>
            <li><a href="/sell-your-house#repairs">Needs Major Repairs</a></li>
            <li><a href="/sell-your-house#behind">Behind on Payments</a></li>
            <li><a href="/sell-your-house#relocation">Relocating Fast</a></li>
            <li><a href="/sell-your-house#rental">Problem Rental</a></li>
            <li><a href="/sell-your-house#downsizing">Downsizing</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© 2025 Armstrong Buys Houses. All rights reserved. | Louisiana Cash Home Buyers</span>
        <span>
          <a href="/privacy-policy">Privacy Policy</a> &nbsp;·&nbsp;
          <a href="/terms">Terms of Service</a> &nbsp;·&nbsp;
          <a href="/sitemap.xml">Sitemap</a>
        </span>
      </div>
    </div>
  </footer>

  <!-- Mobile Sticky CTA -->
  <div class="mobile-cta-bar">
    <a href="tel:+13372700518" class="call">📞 Call Us</a>
    <a href="/cash-offer" class="offer">💰 Get Offer</a>
  </div>

  <script>
    function toggleNav() {
      document.getElementById('navLinks').classList.toggle('open');
    }
    document.querySelectorAll('.faq-question').forEach(q => {
      q.addEventListener('click', () => {
        q.closest('.faq-item').classList.toggle('open');
        q.querySelector('.faq-toggle').textContent =
          q.closest('.faq-item').classList.contains('open') ? '−' : '+';
      });
    });
    // Offer form submission
    document.querySelectorAll('.offer-form').forEach(form => {
      form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const btn = form.querySelector('button[type=submit]');
        btn.textContent = 'Sending...';
        btn.disabled = true;
        try {
          const res = await fetch('/submit-offer', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(Object.fromEntries(new FormData(form)))
          });
          const data = await res.json();
          if (data.success) {
            form.reset();
            const msg = form.querySelector('.success-msg');
            if (msg) { msg.style.display = 'block'; }
            btn.textContent = '✓ Offer Request Sent!';
          }
        } catch(err) {
          btn.textContent = 'Get My Cash Offer →';
          btn.disabled = false;
        }
      });
    });
  </script>
  {% block scripts %}{% endblock %}
</body>
</html>
