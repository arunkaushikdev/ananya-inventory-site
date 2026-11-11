#!/usr/bin/env python3
"""Generates the static pages (index, features, about, contact, 404). Run: python3 tools/build.py"""
import pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
NAME = "Ananya Inventory"

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
  <a class="brand" href="index.html"><span class="brand-mark">A</span>{NAME}</a>
  <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
  <nav class="nav" id="nav" aria-label="Main">{nav}<a class="btn sm" href="contact.html" data-demo style="color:#fff;border-bottom:1.5px solid var(--ink)">Book a demo</a></nav>
</div></header>
<main>
{body}
</main>
<footer class="site-foot"><div class="wrap">
  <div><a class="brand" href="index.html"><span class="brand-mark">A</span>{NAME}</a><p style="margin-top:12px;max-width:38ch">Stock aur GST, dono aasaan. Billing and stock software for Indian shops and distributors, on your own computer.</p></div>
  <div><h4>Product</h4><ul><li><a href="features.html">Features</a></li><li><a href="features.html#pharma">For pharmacies</a></li><li><a href="contact.html">Book a demo</a></li></ul></div>
  <div><h4>Company</h4><ul><li><a href="about.html">About us</a></li><li><a href="contact.html">Contact</a></li><li><a href="mailto:arun.idevs@gmail.com">arun.idevs@gmail.com</a></li></ul></div>
  <div><h4>Legal</h4><ul><li><a href="privacy.html">Privacy Policy</a></li><li><a href="terms.html">Terms of Use</a></li><li><a href="terms.html#refunds">Refunds and cancellation</a></li></ul></div>
  <div class="legal">&copy; 2026 {NAME}, a product of Arun Datt Kaushik. All product names and trademarks belong to their owners. <a href="privacy.html">Privacy</a> &middot; <a href="terms.html">Terms</a></div>
</div></footer>
<div class="m-cta"><a class="btn green" href="contact.html" data-demo>Book a demo</a></div>
<dialog id="demo-dialog" aria-labelledby="dlg-title">
  <div class="dlg-top"><div><h2 id="dlg-title">Book a demo</h2><p>Tell us about your shop. We will show you the software on your kind of business.</p></div><button class="close" aria-label="Close" type="button">&times;</button></div>
  <div class="dlg-body">{form("demo")}</div>
</dialog>
<script src="assets/site.js" defer></script>
<script src="assets/motion.js" defer></script>
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
  <div class="bill-wrap">{bill}
    <div class="bill-tabs" role="group" aria-label="Sample bills">
      <button type="button" class="on" aria-selected="true">Pharmacy</button><button type="button" aria-selected="false">Retail</button><button type="button" aria-selected="false">Distributor</button>
    </div>
  </div>
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
    <div class="credit"><div class="credit-row"><span>Credit used</span><b class="num"><span class="credit-used">&#8377;16,370</span> of &#8377;50,000</b></div><div class="credit-bar"><i></i></div></div>
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
page("features.html", f"Features | {NAME}", "Billing, GST, batch and expiry, godowns, ledgers, reports and staff roles. See everything Ananya Inventory does.", features)

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
page("about.html", f"About us | {NAME}", "Ananya Inventory is billing, stock and GST software built for Indian chemists, distributors and shops.", about)

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
page("contact.html", f"Contact | {NAME}", "Book a demo of Ananya Inventory. Share your shop details and we will call you within one working day.", contact)


# ---------------------------------------------------------------- legal pages
def legal(fname, title, desc, heading, updated, sections):
    toc = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t, _ in sections)
    body = "".join(f'<section id="{i}"><h2>{t}</h2>{b}</section>' for i, t, b in sections)
    html = f"""<section class="sec plain" style="padding-top:clamp(40px,6vw,80px)"><div class="wrap">
  <div class="legal-head"><h1 style="font-size:clamp(36px,5vw,56px)">{heading}</h1><p class="lead" style="font-size:16px">Last updated {updated}</p></div>
  <div class="legal-grid">
    <nav class="legal-toc" aria-label="On this page"><b>On this page</b><ol>{toc}</ol></nav>
    <article class="legal-body">{body}</article>
  </div>
</div></section>"""
    page(fname, title, desc, html)

UPDATED = "11 November 2026"
PRIVACY = [
 ("who", "Who we are", """<p>{NAME} is billing, stock and GST software for Windows, made by Arun Datt Kaushik ("we", "us"). This policy covers the {NAME} desktop app, this website, and the licence service that activates the app.</p>
 <p>Questions or requests about your data: <a href="mailto:arun.idevs@gmail.com">arun.idevs@gmail.com</a>.</p>"""),
 ("short", "The short version", """<ul>
 <li>Your business data (items, parties, bills, ledgers, reports) is stored <strong>on your own computer</strong>. We do not receive it, and we cannot read it.</li>
 <li>The app talks to our licence service only to check your trial or licence. It sends a device identifier, not your business data.</li>
 <li>If you fill a form on this website, we receive what you type, and we use it to contact you about {NAME}.</li>
 <li>We do not sell personal data and we do not run advertising or tracking cookies.</li></ul>"""),
 ("app", "Data in the desktop app", """<p>Everything you enter in {NAME} is saved in a database on your computer: company details, items and stock, parties and ledgers, sale and purchase bills, GSTIN, PAN, licence numbers, staff users, and reports. This stays on that computer.</p>
 <ul><li><strong>Backups.</strong> Backups go to the folder you choose. We do not upload them anywhere.</li>
 <li><strong>Several computers in one shop.</strong> If you use the Main PC and other PCs option, data moves only between computers on your own network.</li>
 <li><strong>Staff PINs.</strong> PINs are kept on your computer. We cannot recover a forgotten PIN for you.</li>
 <li><strong>Printing, import and export.</strong> Files you create or import stay where you save them.</li></ul>
 <p>Because we do not hold your business data, you are responsible for keeping your computer and backups safe. See the <a href="terms.html#your-data">Terms of Use</a>.</p>"""),
 ("licence", "Licence and trial checks", """<p>To run a free trial or a paid licence, the app contacts our licence service. This is the only information the app sends to us:</p>
 <ul><li>your activation code or licence key, when you activate or renew;</li>
 <li>a device identifier. It is a one-way hash made from your computer, so it cannot be turned back into your hardware details;</li>
 <li>your computer name, as shown in the app, so you can recognise a device when you manage your licence;</li>
 <li>the app version, and the date your trial started.</li></ul>
 <p>We use this to limit a licence to the number of computers you bought, to apply trial days, and to tell you when a licence expires. We do not receive bills, parties, items, or any figures from your business.</p>
 <p>The app can also be activated offline with a code, without contacting our service.</p>"""),
 ("buying", "Buying a licence", """<p>When you buy or renew online, you pay on the payment page of our payment partner, Razorpay. Razorpay collects and processes your card, UPI or net banking details under its own privacy policy. We never see or store your full card number, UPI PIN or bank password.</p>
 <p>We receive your name, email address, phone number, the plan and amount, and the payment reference. We keep these to issue your licence key, send you a receipt, handle renewals and support, and meet tax and accounting rules. We may email you the licence key.</p>"""),
 ("website", "This website", """<ul><li><strong>Forms.</strong> When you book a demo or contact us, we receive the details you enter: name, shop or company, mobile number, email, city, business type, the software you use today, and your message. The form is delivered to us as email through FormSubmit, a form-handling service. We use the details only to reply to you, arrange a demo, and follow up about {NAME}.</li>
 <li><strong>Fonts.</strong> Pages load a font from Google Fonts. Google receives your IP address and browser details when it serves the font.</li>
 <li><strong>Hosting.</strong> The site is hosted on GitHub Pages. GitHub may keep standard server logs such as IP addresses.</li>
 <li><strong>Cookies and analytics.</strong> The site does not set cookies and does not use analytics or advertising trackers.</li></ul>"""),
 ("use", "Why we use data, and our legal basis", """<p>We use personal data to provide and secure the software and licence, reply to your enquiries, process payments and issue invoices, keep records the law requires, and improve the product based on what you tell us. We process it because you gave it to us for these purposes, to carry out a purchase you asked for, or because the law requires it, in line with the Digital Personal Data Protection Act, 2023 and other Indian law that applies.</p>"""),
 ("share", "Who we share data with", """<p>We share personal data only with the services that help us run {NAME}: Razorpay for payments, our email service for sending receipts and licence emails, the form service named above, and our hosting providers. They may process data only to provide their service. We may also disclose data if a court or authority lawfully requires it. We do not sell personal data.</p>"""),
 ("keep", "How long we keep it", """<p>Enquiry details: until your request is handled, and up to 24 months after if you may still become a customer. Licence and payment records: as long as the licence exists and for the period tax and accounting law requires. After that we delete or anonymise them. Data on your own computer stays until you delete it.</p>"""),
 ("security", "Security", """<p>The licence service uses encrypted connections. Licences are signed so they cannot be edited, and our signing keys are not part of the app. No system is perfectly secure, so we cannot promise absolute security, but we work to protect the data we hold.</p>"""),
 ("rights", "Your rights and choices", """<p>You can ask us to tell you what personal data we hold about you, correct it, or delete it, and you can withdraw consent for things like follow-up emails at any time. Write to <a href="mailto:arun.idevs@gmail.com">arun.idevs@gmail.com</a> from the email address you used. We aim to reply within 30 days. If you are not satisfied with our answer, you may complain to the Data Protection Board of India once it is operational.</p>
 <p>To remove a computer from your licence, use Settings &rarr; Licence in the app, or write to us.</p>"""),
 ("children", "Children", """<p>{NAME} is business software and is not meant for children. We do not knowingly collect personal data from anyone under 18.</p>"""),
 ("changes", "Changes to this policy", """<p>If we change this policy, we will update the date at the top. If a change is significant, we will also tell customers by email or inside the app.</p>"""),
 ("grievance", "Grievance contact", """<p>Arun Datt Kaushik, {NAME}<br>Email: <a href="mailto:arun.idevs@gmail.com">arun.idevs@gmail.com</a></p>"""),
]
legal("privacy.html", f"Privacy Policy | {NAME}", "What {NAME} collects, what stays on your computer, and how your rights work.".replace("{NAME}", NAME), "Privacy Policy", UPDATED, [(i, t, b.replace("{NAME}", NAME)) for i, t, b in PRIVACY])

TERMS = [
 ("agree", "Using these terms", """<p>These terms are an agreement between you and Arun Datt Kaushik, who offers {NAME} ("we", "us"). By installing or using the app, the licence service, or this website, you accept them. If you use {NAME} for a company, you confirm you can accept these terms for that company.</p>"""),
 ("what", "What {NAME} is", """<p>{NAME} is desktop software for stock, billing, GST and accounts. It helps you prepare bills, records and reports. It is a tool: you decide what to enter and what to file.</p>"""),
 ("licence", "Your licence", """<p>We grant you a non-exclusive, non-transferable right to use the app on the number of computers your plan allows, for your own business, for the licence period you paid for, or during the free trial. You may not copy, resell, rent, reverse-engineer, or remove licence checks from the app, or share a licence key with people outside your business.</p>
 <p>A licence can be moved to another computer by removing the old one in the app or by asking us. A licence can be switched off if it is used against these terms, shared beyond its limit, or paid for by a payment that is reversed.</p>"""),
 ("trial", "Free trial", """<p>The trial lets you use the app before buying. Trial days are counted from the first start on a computer, and the licence service keeps the earliest start date it sees. When the trial ends, you will need a licence to keep creating records. Your data stays on your computer and you can still back it up.</p>"""),
 ("your-data", "Your data and your responsibility", """<p>Your business data belongs to you and is stored on your computer. We cannot see it, recover it, or restore it. You are responsible for:</p>
 <ul><li>taking regular backups and keeping them in a safe place;</li><li>keeping your computer, Windows account, and staff PINs secure;</li><li>the accuracy of what you enter, including GST rates, HSN codes, party details and stock;</li><li>checking bills, reports and returns before you print, share, or file them, and following the tax, drug and other laws that apply to your business.</li></ul>
 <p>Features that flag schedule drugs, expiry, credit limits or tax mismatches are aids. They do not replace your own compliance duties.</p>"""),
 ("payments", "Fees and payments", """<p>Fees are shown in rupees on the buy page for each plan and period, and may change for future purchases. Prices on the page at the time you pay apply to that purchase. Payments are handled by Razorpay. Taxes, including GST, are added where applicable. Renewals and upgrades extend your licence from its current end date.</p>"""),
 ("refunds", "Refunds and cancellation", """<p>You can try {NAME} free during the trial before you pay. Because the software is delivered digitally and a licence key is issued immediately, licence fees are <strong>not refundable</strong> once the key has been issued, except in these cases:</p>
 <ul><li>you were charged twice for the same purchase, or charged an amount different from the price shown. We refund the extra amount;</li><li>payment was taken but no licence key was issued and we cannot fix it within 7 days;</li><li>a refund is required by law.</li></ul>
 <p>To ask for a refund, write to <a href="mailto:arun.idevs@gmail.com">arun.idevs@gmail.com</a> within 7 days with your payment reference. Approved refunds go back to the original payment method and usually reach you within 5 to 10 working days, depending on your bank. Plans do not renew by themselves. You choose when to renew, so there is nothing to cancel. You can stop using {NAME} at any time.</p>"""),
 ("support", "Support and updates", """<p>We provide support by email and by the phone number you give us when you book a demo or buy. We may release updates that fix issues or add features. Some updates may be needed to keep the licence service working.</p>"""),
 ("ip", "Ownership", """<p>We own {NAME}, its design, and its code. You own your business data. Product names and trademarks of other companies belong to their owners, and we use them only to say what we work with.</p>"""),
 ("warranty", "No guarantee, and limit of liability", """<p>We work to make {NAME} accurate and reliable, but the software is provided "as is". We do not promise it will be error-free or always available, or that it fits every business's needs. To the extent the law allows, we are not liable for indirect or consequential loss, lost profits, lost data, penalties, or tax or legal consequences that result from using the software. Our total liability for any claim is limited to the fees you paid us for the licence in the 12 months before the claim.</p>
 <p>Nothing here limits liability that cannot be limited by law.</p>"""),
 ("ending", "Ending these terms", """<p>You can stop using {NAME} whenever you like. We may end or suspend a licence if you break these terms. After a licence ends, your data stays on your computer, and you can still open backups with a valid licence or trial.</p>"""),
 ("law", "Governing law", """<p>These terms follow the laws of India. Disputes will be handled by the courts that have jurisdiction in India. We would like to hear about a problem first, so please write to us and we will try to resolve it.</p>"""),
 ("changes", "Changes", """<p>We may update these terms. The date above shows the latest version. Using {NAME} after a change means you accept the updated terms.</p>"""),
 ("contact", "Contact", """<p>Arun Datt Kaushik, {NAME}<br>Email: <a href="mailto:arun.idevs@gmail.com">arun.idevs@gmail.com</a></p>"""),
]
legal("terms.html", f"Terms of Use | {NAME}", "Terms for using Ananya Inventory: licence, trial, your data, payments, refunds and support.", "Terms of Use", UPDATED, [(i, t.replace("{NAME}", NAME), b.replace("{NAME}", NAME)) for i, t, b in TERMS])

# ---------------------------------------------------------------- 404
nf = '''<section class="sec"><div class="wrap" style="display:grid;gap:20px;justify-items:start"><h1>Page not found</h1><p class="lead">That address does not exist. Go back to the home page or see the features.</p><div class="hero-cta"><a class="btn green" href="index.html">Home</a><a class="btn ghost" href="features.html">Features</a></div></div></section>'''
page("404.html", f"Page not found | {NAME}", "Page not found.", nf)

(ROOT / "assets" / "favicon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="7" fill="#14213d"/><text x="16" y="21.5" font-family="Arial,sans-serif" font-weight="700" font-size="14" text-anchor="middle" fill="#fff">A</text><circle cx="26" cy="26" r="3" fill="#5fd1a8"/></svg>')
(ROOT / "robots.txt").write_text("User-agent: *\nAllow: /\n")
(ROOT / ".nojekyll").write_text("")
print("built")
