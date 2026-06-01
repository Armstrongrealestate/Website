# Armstrong Buys Houses — Website

**Full website for armstrongbuyshouses.com — Louisiana cash home buyers.**

## 📁 Project Structure

```
armstrongbuyshouses/
├── app.py                    ← Flask application (all routes, SEO)
├── requirements.txt          ← Python dependencies
├── templates/
│   ├── base.html             ← Master template (nav, footer, SEO meta)
│   ├── index.html            ← Homepage with hero, offer form, testimonials
│   ├── how_it_works.html     ← How It Works page
│   ├── sell_your_house.html  ← Sell Your House (situations)
│   ├── we_buy_houses.html    ← We Buy Houses (property types)
│   ├── cash_offer.html       ← Full cash offer form page
│   ├── faq.html              ← 14+ FAQ questions
│   ├── reviews.html          ← Testimonials/reviews page
│   ├── about.html            ← About Us page
│   ├── blog.html             ← Blog listing page
│   ├── blog_post.html        ← Individual blog post template
│   ├── contact.html          ← Contact page
│   ├── parish.html           ← ★ SEO parish pages (all 64 parishes)
│   ├── privacy.html          ← Privacy Policy
│   └── terms.html            ← Terms of Service
└── static/
    ├── css/                  ← Optional external CSS
    ├── js/                   ← Optional external JS
    └── images/               ← Add your images here
```

## 🚀 Pages Included

| Page | URL | Purpose |
|------|-----|---------|
| Home | `/` | Main landing page with offer form |
| How It Works | `/how-it-works` | 3-step process explanation |
| Sell Your House | `/sell-your-house` | All selling situations |
| We Buy Houses | `/we-buy-houses` | Property types we buy |
| Cash Offer | `/cash-offer` | Dedicated offer form page |
| FAQ | `/faq` | 14+ common questions |
| Reviews | `/reviews` | Customer testimonials |
| About | `/about` | Company story |
| Blog | `/blog` | SEO blog listing |
| Blog Posts | `/blog/<slug>` | Individual articles |
| Contact | `/contact` | Contact form + info |
| Parish Pages | `/parish/<name>` | ★ All 64 Louisiana parishes |
| Privacy Policy | `/privacy-policy` | Legal |
| Terms | `/terms` | Legal |
| Sitemap | `/sitemap.xml` | SEO sitemap |
| Robots | `/robots.txt` | SEO robots file |

## 🗺️ All 64 Louisiana Parish URLs

Every parish gets its own fully SEO-optimized page at `/parish/<parish-name>`:

- `/parish/orleans` → Orleans Parish (New Orleans)
- `/parish/east-baton-rouge` → East Baton Rouge Parish
- `/parish/jefferson` → Jefferson Parish
- `/parish/caddo` → Caddo Parish (Shreveport)
- `/parish/lafayette` → Lafayette Parish
- `/parish/calcasieu` → Calcasieu Parish (Lake Charles)
- `/parish/st-tammany` → St. Tammany Parish
- `/parish/livingston` → Livingston Parish
- `/parish/tangipahoa` → Tangipahoa Parish
- `/parish/ouachita` → Ouachita Parish (Monroe)
- ... all 64 parishes

## 🔧 Local Setup

```bash
# 1. Clone repo
git clone https://github.com/YOURUSERNAME/armstrongbuyshouses.git
cd armstrongbuyshouses

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run development server
python app.py
# Visit: http://localhost:5000
```

## 🌐 GitHub Pages / Static Deployment

For GitHub Pages (static HTML), generate all pages:

```bash
pip install flask frozen-flask
python freeze.py  # Generates /build folder with static HTML
```

## ☁️ Deploy to Render.com (Free)

1. Push code to GitHub
2. Go to [render.com](https://render.com) → New Web Service
3. Connect your GitHub repo
4. Build command: `pip install -r requirements.txt`
5. Start command: `gunicorn app:app`
6. Set environment: Python 3
7. Done! Your site will be live at `yourapp.onrender.com`

## ☁️ Deploy to Railway.app

```bash
# Install Railway CLI
npm install -g @railway/cli
railway login
railway init
railway up
```

## 🔧 Before Going Live — Customize These

1. **Phone Number** — Search and replace `(504) 123-4567` with your real number
2. **Email** — Replace `info@armstrongbuyshouses.com` 
3. **Google Tag Manager** — Add your GTM ID to `base.html`
4. **Google Analytics** — Add GA4 tracking code
5. **Google Search Console** — Add verification meta tag to `base.html`
6. **Reviews** — Update testimonials with real customer names/stories
7. **Social Links** — Add real Facebook, Instagram, Google Business links
8. **Blog Posts** — Expand blog content with real articles (1,500+ words each for SEO)
9. **Schema.org** — Add real address and phone to JSON-LD in `base.html`
10. **CRM Integration** — In `app.py` → `submit_offer()`, connect to your CRM or email

## 📈 SEO Features Built-In

- ✅ Unique `<title>` and `<meta description>` for every page
- ✅ Schema.org JSON-LD structured data (RealEstateAgent)
- ✅ Open Graph tags for social sharing
- ✅ Twitter Card tags
- ✅ Canonical URLs
- ✅ XML Sitemap at `/sitemap.xml` (auto-includes all 64 parish pages)
- ✅ Robots.txt at `/robots.txt`
- ✅ 64 individual parish landing pages with unique content
- ✅ Louisiana-specific keyword targeting
- ✅ Mobile-responsive design
- ✅ Fast load speed (no heavy frameworks)
- ✅ Internal linking across all pages

## 📞 Support

Site built for Armstrong Buys Houses — armstrongbuyshouses.com
