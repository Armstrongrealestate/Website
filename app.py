from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

app = Flask(__name__)

# All 64 Louisiana parishes
LOUISIANA_PARISHES = [
    "Acadia", "Allen", "Ascension", "Assumption", "Avoyelles",
    "Beauregard", "Bienville", "Bossier", "Caddo", "Calcasieu",
    "Caldwell", "Cameron", "Catahoula", "Claiborne", "Concordia",
    "De Soto", "East Baton Rouge", "East Carroll", "East Feliciana",
    "Evangeline", "Franklin", "Grant", "Iberia", "Iberville",
    "Jackson", "Jefferson", "Jefferson Davis", "Lafayette", "Lafourche",
    "La Salle", "Lincoln", "Livingston", "Madison", "Morehouse",
    "Natchitoches", "Orleans", "Ouachita", "Plaquemines", "Pointe Coupee",
    "Rapides", "Red River", "Richland", "Sabine", "St. Bernard",
    "St. Charles", "St. Helena", "St. James", "St. John the Baptist",
    "St. Landry", "St. Martin", "St. Mary", "St. Tammany",
    "Tangipahoa", "Tensas", "Terrebonne", "Union", "Vermilion",
    "Vernon", "Washington", "Webster", "West Baton Rouge",
    "West Carroll", "West Feliciana", "Winn"
]

MAJOR_CITIES = {
    "Orleans": ["New Orleans", "Metairie", "Kenner"],
    "East Baton Rouge": ["Baton Rouge", "Baker", "Central", "Zachary"],
    "Jefferson": ["Metairie", "Kenner", "Gretna", "Harvey"],
    "Caddo": ["Shreveport", "Bossier City"],
    "Bossier": ["Bossier City", "Haughton"],
    "Lafayette": ["Lafayette", "Youngsville", "Broussard", "Carencro"],
    "Calcasieu": ["Lake Charles", "Sulphur", "Westlake"],
    "St. Tammany": ["Covington", "Mandeville", "Slidell"],
    "Livingston": ["Denham Springs", "Walker", "Livingston"],
    "Tangipahoa": ["Hammond", "Ponchatoula", "Amite"],
    "Ascension": ["Gonzales", "Prairieville", "Sorrento"],
    "Ouachita": ["Monroe", "West Monroe"],
    "Rapides": ["Alexandria", "Pineville"],
    "Terrebonne": ["Houma", "Gray", "Thibodaux"],
    "Lafourche": ["Thibodaux", "Raceland", "Golden Meadow"],
    "St. Landry": ["Opelousas", "Eunice", "Sunset"],
    "Iberia": ["New Iberia", "Jeanerette"],
}

def get_parish_cities(parish):
    return MAJOR_CITIES.get(parish, [f"{parish} Parish"])

# ─────────────────────────────────────────
# CORE PAGES
# ─────────────────────────────────────────

@app.route('/')
def home():
    return render_template('index.html', parishes=LOUISIANA_PARISHES)

@app.route('/how-it-works')
def how_it_works():
    return render_template('how_it_works.html', parishes=LOUISIANA_PARISHES)

@app.route('/about')
def about():
    return render_template('about.html', parishes=LOUISIANA_PARISHES)

@app.route('/sell-your-house')
def sell_your_house():
    return render_template('sell_your_house.html', parishes=LOUISIANA_PARISHES)

@app.route('/we-buy-houses')
def we_buy_houses():
    return render_template('we_buy_houses.html', parishes=LOUISIANA_PARISHES)

@app.route('/cash-offer')
def cash_offer():
    return render_template('cash_offer.html', parishes=LOUISIANA_PARISHES)

@app.route('/faq')
def faq():
    return render_template('faq.html', parishes=LOUISIANA_PARISHES)

@app.route('/reviews')
def reviews():
    return render_template('reviews.html', parishes=LOUISIANA_PARISHES)

@app.route('/contact')
def contact():
    return render_template('contact.html', parishes=LOUISIANA_PARISHES)

@app.route('/privacy-policy')
def privacy():
    return render_template('privacy.html', parishes=LOUISIANA_PARISHES)

@app.route('/terms')
def terms():
    return render_template('terms.html', parishes=LOUISIANA_PARISHES)

# ─────────────────────────────────────────
# BLOG — INDEX
# ─────────────────────────────────────────

@app.route('/blog')
def blog():
    return render_template('blog.html', parishes=LOUISIANA_PARISHES)

@app.route('/blog/<slug>')
def blog_post(slug):
    posts = {
        'how-to-sell-house-fast-louisiana': {
            'title': 'How to Sell Your House Fast in Louisiana',
            'date': 'May 15, 2025',
            'content': 'Selling a house in Louisiana can be complex...'
        },
        'cash-vs-traditional-sale': {
            'title': 'Cash Sale vs. Traditional Sale: What Louisiana Homeowners Need to Know',
            'date': 'April 22, 2025',
            'content': 'When it comes time to sell your home...'
        },
        'avoiding-foreclosure-louisiana': {
            'title': 'How to Avoid Foreclosure in Louisiana',
            'date': 'March 10, 2025',
            'content': 'Facing foreclosure is one of the most stressful situations...'
        }
    }
    post = posts.get(slug, None)
    return render_template('blog_post.html', post=post, slug=slug, parishes=LOUISIANA_PARISHES)

# ─────────────────────────────────────────
# BLOG — CITY PAGES (existing)
# ─────────────────────────────────────────

@app.route('/blog/sell-my-house-fast-lake-charles')
def blog_lake_charles():
    return render_template('blog_lake_charles.html', parishes=LOUISIANA_PARISHES)

@app.route('/blog/sell-my-house-fast-deridder')
def blog_deridder():
    return render_template('blog_deridder.html', parishes=LOUISIANA_PARISHES)

@app.route('/blog/sell-my-house-fast-leesville')
def blog_leesville():
    return render_template('blog_leesville.html', parishes=LOUISIANA_PARISHES)

@app.route('/blog/sell-my-house-fast-sulphur')
def blog_sulphur():
    return render_template('blog_sulphur.html', parishes=LOUISIANA_PARISHES)

@app.route('/blog/sell-my-house-fast-westlake')
def blog_westlake():
    return render_template('blog_westlake.html', parishes=LOUISIANA_PARISHES)

@app.route('/blog/sell-my-house-fast-lafayette')
def blog_lafayette():
    return render_template('blog_lafayette.html', parishes=LOUISIANA_PARISHES)

@app.route('/blog/sell-my-house-fast-baton-rouge')
def blog_baton_rouge():
    return render_template('blog_baton_rouge.html', parishes=LOUISIANA_PARISHES)

# ─────────────────────────────────────────
# BLOG — CITY PAGES (new — your priority markets)
# ─────────────────────────────────────────

@app.route('/blog/sell-my-house-fast-alexandria-la')
def blog_alexandria():
    return render_template('blog_alexandria.html', parishes=LOUISIANA_PARISHES)

@app.route('/blog/sell-my-house-fast-many-la')
def blog_many():
    return render_template('blog_many.html', parishes=LOUISIANA_PARISHES)

@app.route('/blog/sell-my-house-fast-oberlin-la')
def blog_oberlin():
    return render_template('blog_oberlin.html', parishes=LOUISIANA_PARISHES)

@app.route('/blog/sell-my-house-fast-iowa-la')
def blog_iowa():
    return render_template('blog_iowa.html', parishes=LOUISIANA_PARISHES)

# ─────────────────────────────────────────
# BLOG — TOPIC / SITUATION PAGES
# ─────────────────────────────────────────

@app.route('/blog/inherited-property-louisiana')
def blog_inherited_property():
    return render_template('blog_inherited_property.html', parishes=LOUISIANA_PARISHES)

@app.route('/blog/buying-partial-interest-property-louisiana')
def blog_partial_interest():
    return render_template('blog_partial_interest.html', parishes=LOUISIANA_PARISHES)

@app.route('/blog/sell-house-during-foreclosure-louisiana')
def blog_foreclosure():
    return render_template('blog_foreclosure.html', parishes=LOUISIANA_PARISHES)

@app.route('/blog/selling-house-during-divorce-louisiana')
def blog_divorce():
    return render_template('blog_divorce.html', parishes=LOUISIANA_PARISHES)

@app.route('/blog/probate-property-louisiana')
def blog_probate():
    return render_template('blog_probate.html', parishes=LOUISIANA_PARISHES)

@app.route('/blog/storm-damage-house-louisiana')
def blog_storm_damage():
    return render_template('blog_storm_damage.html', parishes=LOUISIANA_PARISHES)

@app.route('/blog/tax-delinquent-property-louisiana')
def blog_tax_delinquent():
    return render_template('blog_tax_delinquent.html', parishes=LOUISIANA_PARISHES)

@app.route('/blog/behind-on-mortgage-payments-louisiana')
def blog_behind_payments():
    return render_template('blog_behind_payments.html', parishes=LOUISIANA_PARISHES)

@app.route('/blog/relocating-need-to-sell-house-louisiana')
def blog_relocating():
    return render_template('blog_relocating.html', parishes=LOUISIANA_PARISHES)

@app.route('/blog/sell-house-that-needs-repairs-louisiana')
def blog_needs_repairs():
    return render_template('blog_needs_repairs.html', parishes=LOUISIANA_PARISHES)

# ─────────────────────────────────────────
# PARISH PAGES
# ─────────────────────────────────────────

@app.route('/parish/<parish_slug>')
def parish_page(parish_slug):
    parish_name = parish_slug.replace('-', ' ').title()
    parish_name = parish_name.replace('St ', 'St. ')
    parish_name = parish_name.replace('La ', 'La ')
    cities = get_parish_cities(parish_name)
    if parish_name not in LOUISIANA_PARISHES:
        parish_name = None
    return render_template('parish.html',
                           parish=parish_name,
                           cities=cities,
                           parishes=LOUISIANA_PARISHES,
                           parish_slug=parish_slug)

# ─────────────────────────────────────────
# FORM SUBMISSION
# ─────────────────────────────────────────

@app.route('/submit-offer', methods=['POST'])
def submit_offer():
    return jsonify({'success': True, 'message': 'Thank you! We will contact you within 24 hours.'})

# ─────────────────────────────────────────
# SEO — SITEMAP & ROBOTS
# ─────────────────────────────────────────

@app.route('/sitemap.xml')
def sitemap():
    pages = [
        '/', '/how-it-works', '/about', '/sell-your-house',
        '/we-buy-houses', '/cash-offer', '/faq', '/reviews',
        '/blog', '/contact',
        # Topic blogs
        '/blog/inherited-property-louisiana',
        '/blog/buying-partial-interest-property-louisiana',
        '/blog/sell-house-during-foreclosure-louisiana',
        '/blog/selling-house-during-divorce-louisiana',
        '/blog/probate-property-louisiana',
        '/blog/storm-damage-house-louisiana',
        '/blog/tax-delinquent-property-louisiana',
        '/blog/behind-on-mortgage-payments-louisiana',
        '/blog/relocating-need-to-sell-house-louisiana',
        '/blog/sell-house-that-needs-repairs-louisiana',
        # City blogs
        '/blog/sell-my-house-fast-lake-charles',
        '/blog/sell-my-house-fast-deridder',
        '/blog/sell-my-house-fast-leesville',
        '/blog/sell-my-house-fast-sulphur',
        '/blog/sell-my-house-fast-westlake',
        '/blog/sell-my-house-fast-lafayette',
        '/blog/sell-my-house-fast-baton-rouge',
        '/blog/sell-my-house-fast-alexandria-la',
        '/blog/sell-my-house-fast-many-la',
        '/blog/sell-my-house-fast-oberlin-la',
        '/blog/sell-my-house-fast-iowa-la',
    ]
    parish_pages = [f'/parish/{p.lower().replace(" ", "-").replace(".", "")}' for p in LOUISIANA_PARISHES]
    all_pages = pages + parish_pages
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for page in all_pages:
        priority = '1.0' if page == '/' else '0.8'
        xml += f'  <url><loc>https://www.armstrongbuyshouses.com{page}</loc><changefreq>monthly</changefreq><priority>{priority}</priority></url>\n'
    xml += '</urlset>'
    return app.response_class(xml, mimetype='application/xml')

@app.route('/robots.txt')
def robots():
    txt = "User-agent: *\nAllow: /\nSitemap: https://www.armstrongbuyshouses.com/sitemap.xml"
    return app.response_class(txt, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
