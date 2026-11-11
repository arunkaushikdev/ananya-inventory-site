#!/usr/bin/env python3
"""Generates the static pages (index, features, about, contact, 404). Run: python3 tools/build.py"""
import pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
NAME = "Inventory ERP"

def form(fid, compact=False):
    biz = ["Pharmacy / medical store", "Distributor / stockist", "Wholesale", "Retail shop", "Manufacturer", "Other"]
    cur = ["MARG", "Tally", "Busy", "Excel or register", "Another software", "No software yet"]
    opts = lambda xs: "".join(f'<option>{x}</option>' for x in xs)
    return f'''<form data-lead novalidate id="{fid}">
  <div class="form-grid">
    <div class="field" data-name="your name"><label for="{fid}-name">Your name</label><input id="{fid}-name" name="name" autocomplete="name" required><span class="msg"></span></div>
    <div class="field" data-name="your shop or company name"><label for="{fid}-biz">Shop or company</label><input id="{fid}-biz" name="business" autocomplete="organization" required><span class="msg"></span></div>
    <div class="field" data-name="a mobile number"><label for="{fid}-phone">Mobile number</label><input id="{fid}-phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" required><span class="msg"></span></div>
    <div class="field" data-name="your email"><label for="{fid}-email">Email</label><input id="{fid}-email" name="email" type="email" autocomplete="email" required><span class="msg"></span></div>
    <div class="field" data-name="your city"><label for="{fid}-city">City</label><input id="{fid}-city" name="city" autocomplete="address-level2"><span class="msg"></span></div>
    <div class="field" data-name="business type"><label for="{fid}-type">Type of business</label><select id="{fid}-type" name="business_type">{opts(biz)}</select><span class="msg"></span></div>
    <div class="field full" data-name="current software"><label for="{fid}-cur">What do you use for billing today? <span class="opt">(optional)</span></label><select id="{fid}-cur" name="current_software">{opts(cur)}</select><span class="msg"></span></div>
    <div class="field full" data-name="a message"><label for="{fid}-msg">Anything we should know? <span class="opt">(optional)</span></label><textarea id="{fid}-msg" name="message" placeholder="Number of bills a day, godowns, special reports you need..."></textarea><span class="msg"></span></div>
    <div class="hp" aria-hidden="true"><label>Website <input name="website" tabindex="-1" autocomplete="off"></label></div>
  </div>
  <div class="form-status" role="status" aria-live="polite"></div>
  <div class="form-actions" style="margin-top:16px"><button class="btn green" type="submit">Book my demo</button><small>We call you back within one working day.</small></div>
</form>'''

NAV = [("index.html", "Home"), ("features.html", "Features"), ("about.html", "About"), ("contact.html", "Contact")]

def page(fname, title, desc, body, extra_head=""):
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == fname else ""}>{t}</a>' for h, t in NAV)
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<meta name="theme-color" content="#f2f5f3">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
{extra_head}</head>
<body>
<header class="site-head"><div class="wrap">
  <a class="brand" href="index.html"><span class="brand-mark">iE</span>{NAME}</a>
  <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
  <nav class="nav" id="nav" aria-label="Main">{nav}<a class="btn sm" href="contact.html" data-demo style="color:#fff;border-bottom:1.5px solid var(--ink)">Book a demo</a></nav>
</div></header>
<main>
{body}
</main>
<footer class="site-foot"><div class="wrap">
  <div><a class="brand" href="index.html"><span class="brand-mark">iE</span>{NAME}</a><p style="margin-top:12px;max-width:38ch">Stock, billing and GST software for Indian shops and distributors. Runs on your own computer.</p></div>
  <div><h4>Product</h4><ul><li><a href="features.html">Features</a></li><li><a href="features.html#pharma">For pharmacies</a></li><li><a href="contact.html">Book a demo</a></li></ul></div>
  <div><h4>Company</h4><ul><li><a href="about.html">About us</a></li><li><a href="contact.html">Contact</a></li><li><a href="mailto:arun.idevs@gmail.com">arun.idevs@gmail.com</a></li></ul></div>
  <div class="legal">&copy; 2026 {NAME}. All product names and trademarks belong to their owners.</div>
</div></footer>
<dialog id="demo-dialog" aria-labelledby="dlg-title"><div class="dlg-in">
  <div class="dlg-top"><div><h2 id="dlg-title" style="font-size:30px">Book a demo</h2><p class="lead" style="font-size:16px;margin-top:8px">Tell us about your shop. We will show you the software on your kind of business.</p></div><button class="close" aria-label="Close" type="button">&times;</button></div>
  {form("demo")}
</div></dialog>
<script src="assets/site.js" defer></script>
</body>
</html>'''
    (ROOT / fname).write_text(html)

# ---------------------------------------------------------------- home
bill = '''<div class="bill" aria-label="Sample GST tax invoice">
  <div class="bill-top"><div><strong>Sharma Medical Store</strong><span>Tax Invoice SALE-00418 &middot; 11 Nov 2026</span></div><span class="bill-tag">Local sale &middot; GST 12%</span></div>
  <table><thead><tr><th>Item</th><th>Batch / Exp</th><th class="r">Qty</th><th class="r">Amount</th></tr></thead><tbody>
    <tr style="--i:0"><td>Paracetamol 500mg<span class="sub">HSN 3004</span></td><td>B2291 &middot; 08/27</td><td class="r num">10</td><td class="r num">&#8377;312.00</td></tr>
    <tr style="--i:1"><td>Azithromycin 250mg<span class="sub">HSN 3004 &middot; Sch H</span></td><td>AZ118 &middot; <span class="exp-soon">02/27</span></td><td class="r num">6</td><td class="r num">&#8377;468.00</td></tr>
    <tr style="--i:2"><td>ORS Powder<span class="sub">HSN 3004</span></td><td>OR771 &middot; 11/27</td><td class="r num">12</td><td class="r num">&#8377;216.00</td></tr>
    <tr style="--i:3"><td>Cetirizine 10mg<span class="sub">HSN 3004</span></td><td>CT405 &middot; 05/28</td><td class="r num">20</td><td class="r num">&#8377;180.00</td></tr>
  </tbody></table>
  <div class="bill-foot">
    <div style="--j:0"><span>Taxable value</span><span class="num">&#8377;1,176.00</span></div>
    <div style="--j:1"><span>SGST 6% + CGST 6%</span><span class="num">&#8377;141.12</span></div>
    <div class="total" style="--j:2"><span>Invoice total</span><span class="num">&#8377;1,317.00</span></div>
  </div>
  <div class="stamp" aria-hidden="true">SAVED</div>
</div>'''

home = f'''<section class="hero"><div class="wrap">
  <div class="hero-copy">
    <h1>Billing, stock and GST for your counter.</h1>
    <p class="lead">{NAME} is desktop software for pharmacies, distributors and shops. Type fast with the keyboard, bill in seconds, and keep every record on your own computer.</p>
    <div class="hero-cta"><a class="btn green" href="contact.html" data-demo>Book a demo</a><a class="btn ghost" href="features.html">See all features</a></div>
    <p class="hero-note">Works without internet. Your data never leaves your shop.</p>
  </div>
  {bill}
</div></section>

<section class="proof"><div class="wrap">
  <div><b>GST ready</b><span>CGST, SGST and IGST on every bill</span></div>
  <div><b>Batch and expiry</b><span>First-expiry-first-out selling</span></div>
  <div><b>Keyboard first</b><span>Billing without touching the mouse</span></div>
  <div><b>Offline</b><span>No monthly cloud, no lost internet</span></div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-head"><h2>Everything a shop runs on, in one program</h2><p class="lead">From the first sale of the day to the GST return at month end.</p></div>
  <div class="rows">
    <div class="row"><div class="intro"><h3>Sell</h3><p>Fast bills with the right tax and the right batch.</p></div>
      <ul><li>Sale bills, POS, quotations and delivery challans</li><li>Sales types for local and central GST slabs</li><li>Party history on screen while you bill</li><li>Credit and debit notes, sale and purchase returns</li></ul></div>
    <div class="row"><div class="intro"><h3>Buy and stock</h3><p>Know what you hold, where, and until when.</p></div>
      <ul><li>Purchase entry with batch, expiry, MRP and rates</li><li>Godowns and stock transfers</li><li>Stock adjustment, re-order and minimum stock</li><li>Barcode labels and item master with HSN</li></ul></div>
    <div class="row"><div class="intro"><h3>Accounts</h3><p>Ledgers that match how your CA works.</p></div>
      <ul><li>Ledger master with bill-wise opening balances</li><li>Receipts, payments, cash and bank books</li><li>Expenses, contra, journal and cheques</li><li>Bank reconciliation, TDS and TCS</li></ul></div>
    <div class="row"><div class="intro"><h3>Report</h3><p>Numbers you can hand over as they are.</p></div>
      <ul><li>GST reports for filing</li><li>Outstanding, party statements and ageing</li><li>Stock status and expiry reports</li><li>Profit and loss, sales and purchase books</li></ul></div>
  </div>
  <p style="margin-top:28px"><a class="btn ghost" href="features.html">Explore every feature</a></p>
</div></section>

<section class="sec tint" id="pharma"><div class="wrap split">
  <div class="copy">
    <h2>Made for chemists who cannot afford an expired strip</h2>
    <p class="lead">Every batch carries its expiry. The bill picks the earliest-expiring stock first, and warns you before you sell something risky.</p>
    <ul class="checks">
      <li><b>First-expiry-first-out</b> batch selection on every sale</li>
      <li><b>Expired and near-expiry batches</b> are marked in red and amber</li>
      <li><b>Schedule H, H1 and narcotic</b> items flagged, with doctor and patient details on the bill</li>
      <li><b>Party-wise control</b> over which scheduled drugs a customer may be billed</li>
    </ul>
  </div>
  <div class="panel" aria-label="Batch picker example">
    <div class="panel-head"><span>Batches for Azithromycin 250mg</span><span class="num" style="font-weight:400;color:var(--ink-2)">Stock 94</span></div>
    <table><thead><tr><th>Batch</th><th>Expiry</th><th class="r">Qty</th><th class="r">MRP</th></tr></thead><tbody>
      <tr><td>AZ099 <span class="pill bad">Expired</span></td><td class="num">12/26</td><td class="r num">8</td><td class="r num">&#8377;81</td></tr>
      <tr><td>AZ118 <span class="pill warn">Under 90 days</span></td><td class="num">02/27</td><td class="r num">34</td><td class="r num">&#8377;78</td></tr>
      <tr><td>AZ204 <span class="pill ok">Next to sell</span></td><td class="num">09/27</td><td class="r num">52</td><td class="r num">&#8377;78</td></tr>
    </tbody></table>
  </div>
</div></section>

<section class="sec"><div class="wrap split">
  <div class="panel" aria-label="Ledger example">
    <div class="panel-head"><span>Ledger: Gupta Medical Hall</span><span class="pill info">Credit limit &#8377;50,000</span></div>
    <table><thead><tr><th>Bill</th><th>Date</th><th class="r">Days</th><th class="r">Balance</th></tr></thead><tbody>
      <tr><td>SALE-00377</td><td class="num">14 Oct</td><td class="r num">28</td><td class="r num">&#8377;8,420 Dr</td></tr>
      <tr><td>SALE-00402</td><td class="num">02 Nov</td><td class="r num">9</td><td class="r num">&#8377;12,950 Dr</td></tr>
      <tr><td>RCPT-0091</td><td class="num">06 Nov</td><td class="r num">5</td><td class="r num">&#8377;5,000 Cr</td></tr>
    </tbody></table>
  </div>
  <div class="copy">
    <h2>Know who owes you, before you bill</h2>
    <p class="lead">Open a party and see balance, due amount, last sale, last receipt and pending bills. Set credit limits and credit days once, and billing respects them.</p>
    <div class="kbd-line"><span><kbd>Ctrl</kbd> + <kbd>W</kbd> save bill</span><span><kbd>Ins</kbd> add item</span><span><kbd>Ctrl</kbd> + <kbd>D</kbd> hold bill</span></div>
  </div>
</div></section>

<section class="sec tint"><div class="wrap">
  <div class="sec-head"><h2>Fits the way your shop works</h2></div>
  <div class="segs">
    <div class="seg"><h3>Pharmacies</h3><p>Batch, expiry, schedule drugs and prescription details, built in.</p></div>
    <div class="seg"><h3>Distributors and wholesalers</h3><p>Party-wise rates, schemes, credit control and bill-wise outstanding.</p></div>
    <div class="seg"><h3>Retail shops</h3><p>Quick POS billing, barcode labels and simple stock counts.</p></div>
  </div>
</div></section>

<section class="sec"><div class="wrap split">
  <div class="copy">
    <h2>Your data stays with you</h2>
    <p class="lead">{NAME} stores everything on your computer. There is no subscription to the cloud, no outage that stops billing, and nobody else reads your sales.</p>
  </div>
  <ul class="checks">
    <li><b>Works offline</b>, so a power-cut-and-router day still ends with all bills saved</li>
    <li><b>Staff logins with PIN</b> and roles: owner, accountant, salesman, store keeper, viewer</li>
    <li><b>Backups</b> you control, to a drive or folder you choose</li>
    <li><b>Import from Tally</b> to bring your masters across</li>
  </ul>
</div></section>

<section class="sec cta"><div class="wrap">
  <div><h2>See it on your own kind of business</h2><p>Book a 30-minute demo. Bring a few real bills and we will show you how they look here.</p></div>
  <a class="btn" href="contact.html" data-demo>Book a demo</a>
</div></section>'''
page("index.html", f"{NAME}: billing, stock and GST software for Indian shops", "Desktop software for pharmacies, distributors and shops: GST billing, batch and expiry, ledgers and reports. Works offline, data stays on your computer.", home)

# ---------------------------------------------------------------- features
def feat(title, intro, items, anchor=""):
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f'<div class="row"{f" id=\"{anchor}\"" if anchor else ""}><div class="intro"><h3>{title}</h3><p>{intro}</p></div><ul>{lis}</ul></div>'

features = f'''<section class="hero" style="padding-bottom:40px"><div class="wrap" style="grid-template-columns:1fr"><div class="hero-copy">
  <h1 style="font-size:clamp(38px,5.5vw,64px)">Every feature, in plain words</h1>
  <p class="lead">What {NAME} does today, grouped by the job you are doing.</p>
</div></div></section>
<section class="sec" style="padding-top:24px"><div class="wrap"><div class="rows">
{feat("Billing", "The counter screen, built for speed.", ["Sale bills with item search, batch picker and live stock", "Point of sale screen for walk-in customers", "Quotations, sale orders and delivery challans", "Credit notes and debit notes against the original bill", "Save, hold and copy bill lines from the keyboard", "Bill levies and round-off on the final amount"])}
{feat("GST and tax", "Right tax on every line, ready for your CA.", ["CGST and SGST for local sales, IGST for central sales", "Sales types with a tax slab per bill, plus item-wise HSN tax", "A tax error warning when an item's tax differs from the bill", "GSTIN, place of supply and state-wise tax handling", "TDS and TCS on bills", "GST reports for return filing"])}
{feat("Pharmacy tools", "For stores where expiry and schedules matter.", ["Batch-wise stock with expiry and MRP", "First-expiry-first-out batch selection", "Expired and near-expiry batches highlighted", "Schedule H, H1 and narcotic flags on items", "Doctor, patient and prescription number on the bill", "Party-wise rules on which scheduled drugs can be sold"], "pharma")}
{feat("Items and stock", "Know exactly what is on the shelf.", ["Item master with HSN, packing, unit, rack, company and salt", "Rate A, B and C, purchase rate, MRP and minimum margin", "Minimum, maximum and re-order levels", "Godowns, stock transfers and stock adjustment", "Barcode labels", "Item-wise discounts and free-scheme offers"])}
{feat("Parties and ledgers", "Customers and suppliers, with their full story.", ["Create ledger with address, GST, licence and credit details", "Bill-wise opening balances", "Credit limit and credit days", "Party status panel with balance, last sale and last receipt", "Company discount and special rates per party", "Attach documents to a party"])}
{feat("Accounts", "Daily books without a separate accounting package.", ["Receipts and payments against bills", "Cash book and bank book", "Expenses, contra, journal and cheque register", "Bank reconciliation", "Party statements and outstanding", "Profit and loss"])}
{feat("Reports", "Open a report and get your answer.", ["Sales and purchase books", "Stock status and expiry reports", "Outstanding and ageing by party", "Daily analysis and today's gross profit", "Re-order list", "Print or export the numbers you need"])}
{feat("Control and safety", "Your shop, your rules.", ["Staff users with PIN sign-in", "Roles: owner, accountant, salesman, store keeper, viewer", "Hide purchase rates and profit from billing staff", "Backup and restore", "Import from Tally", "Auto capital letters while typing, with a switch to turn it off"])}
</div></div></section>
<section class="sec cta"><div class="wrap">
  <div><h2>Missing something you need?</h2><p>Tell us in the demo form. If your shop needs a report or a flow we do not have, we want to know.</p></div>
  <a class="btn" href="contact.html" data-demo>Book a demo</a>
</div></section>'''
page("features.html", f"Features | {NAME}", "Billing, GST, batch and expiry, godowns, ledgers, reports and staff roles. See everything Inventory ERP does.", features)

# ---------------------------------------------------------------- about
about = f'''<section class="hero" style="padding-bottom:32px"><div class="wrap" style="grid-template-columns:1fr"><div class="hero-copy">
  <h1 style="font-size:clamp(38px,5.5vw,64px)">Software that thinks like a shopkeeper</h1>
  <p class="lead">We build {NAME} for the people who run Indian counters: chemists, stockists, wholesalers and retailers.</p>
</div></div></section>
<section class="sec" style="padding-top:24px"><div class="wrap split" style="align-items:start">
  <div class="prose">
    <p>Most billing software for Indian shops grew up on the desktop, and the best of it taught a generation of shopkeepers to bill with the keyboard. We kept what works: the flows, the terms and the speed your staff already know.</p>
    <p>Then we rebuilt it with a clearer screen, faster search, and a design that does not make a new employee afraid of the software.</p>
    <p><strong>You should own your records.</strong> {NAME} keeps your data on your own computer, so it keeps working when the internet does not, and nobody can switch it off.</p>
    <p>We are an independent team. When you tell us something is missing, we want to hear it.</p>
  </div>
  <div class="facts" style="grid-template-columns:1fr">
    <div><b>Built for Indian GST</b><p>CGST, SGST and IGST, HSN codes, place of supply, TDS and TCS.</p></div>
    <div><b>Keyboard first</b><p>Every common job has a shortcut, so billing never waits for a mouse.</p></div>
    <div><b>Your data, your computer</b><p>Offline by design, with backups you control.</p></div>
    <div><b>Direct support</b><p>Talk to the people who build it.</p></div>
  </div>
</div></section>
<section class="sec cta"><div class="wrap">
  <div><h2>Let's talk about your shop</h2><p>Tell us what you sell and what you use today. We will show you the software on your kind of bills.</p></div>
  <a class="btn" href="contact.html" data-demo>Book a demo</a>
</div></section>'''
page("about.html", f"About us | {NAME}", "Inventory ERP is billing, stock and GST software built for Indian chemists, distributors and shops.", about)

# ---------------------------------------------------------------- contact
contact = f'''<section class="sec" style="padding-top:clamp(40px,6vw,80px)"><div class="wrap contact-grid">
  <div class="contact-side">
    <h1 style="font-size:clamp(38px,5vw,60px)">Book a demo</h1>
    <p class="lead">Share a few details and we will call you within one working day to set up a demo.</p>
    <dl>
      <div><dt>Email</dt><dd><a href="mailto:arun.idevs@gmail.com">arun.idevs@gmail.com</a></dd></div>
      <div><dt>What happens next</dt><dd>We call you, ask about your shop, and show the software with your kind of bills. No payment, no pressure.</dd></div>
      <div><dt>Switching from MARG, Tally or Busy?</dt><dd>Say so in the form. We will tell you what carries over.</dd></div>
    </dl>
  </div>
  <div class="form-card">{form("contact")}</div>
</div></section>'''
page("contact.html", f"Contact | {NAME}", "Book a demo of Inventory ERP. Share your shop details and we will call you within one working day.", contact)

# ---------------------------------------------------------------- 404
nf = '''<section class="sec"><div class="wrap" style="display:grid;gap:20px;justify-items:start"><h1>Page not found</h1><p class="lead">That address does not exist. Go back to the home page or see the features.</p><div class="hero-cta"><a class="btn green" href="index.html">Home</a><a class="btn ghost" href="features.html">Features</a></div></div></section>'''
page("404.html", f"Page not found | {NAME}", "Page not found.", nf)

(ROOT / "assets" / "favicon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="7" fill="#14213d"/><text x="16" y="21.5" font-family="Arial,sans-serif" font-weight="700" font-size="14" text-anchor="middle" fill="#fff">iE</text><circle cx="26" cy="26" r="3" fill="#5fd1a8"/></svg>')
(ROOT / "robots.txt").write_text("User-agent: *\nAllow: /\n")
(ROOT / ".nojekyll").write_text("")
print("built")
