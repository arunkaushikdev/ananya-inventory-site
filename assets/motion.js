(function () {
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var inr = function (n) { return n.toLocaleString("en-IN", { minimumFractionDigits: 2, maximumFractionDigits: 2 }); };
  var inr0 = function (n) { return n.toLocaleString("en-IN", { maximumFractionDigits: 0 }); };

  // header gets a shadow once you scroll
  var head = $(".site-head");
  function onScroll() { if (head) head.classList.toggle("scrolled", window.scrollY > 8); }
  window.addEventListener("scroll", onScroll, { passive: true }); onScroll();

  function visibleWatcher(el, on, off) {
    if (!el || !("IntersectionObserver" in window)) { on && on(); return; }
    new IntersectionObserver(function (es) { es.forEach(function (e) { e.isIntersecting ? on && on() : off && off(); }); }, { threshold: 0.35 }).observe(el);
  }
  function countTo(el, to, dur, fmt) {
    if (reduce) { el.textContent = fmt(to); return; }
    var t0 = performance.now();
    (function step(t) {
      var p = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - p, 3);
      el.textContent = fmt(to * e);
      if (p < 1) requestAnimationFrame(step);
    })(t0);
  }

  // ---------------------------------------------------------- hero: three different bills
  var bills = [
    { tab: "Pharmacy", shop: "Sharma Medical Store", no: "SALE-00418", tag: "Local sale · GST 12%", rate: 12, kind: "local", col: "Batch / Exp",
      rows: [["Paracetamol 500mg", "HSN 3004", "B2291 · 08/27", 10, 312], ["Azithromycin 250mg", "HSN 3004 · Sch H", "AZ118 · <span class='exp-soon'>02/27</span>", 6, 468], ["ORS Powder", "HSN 3004", "OR771 · 11/27", 12, 216], ["Cetirizine 10mg", "HSN 3004", "CT405 · 05/28", 20, 180]] },
    { tab: "Retail", shop: "Verma General Store", no: "SALE-02107", tag: "Local sale · GST 5%", rate: 5, kind: "local", col: "Pack",
      rows: [["Basmati Rice", "HSN 1006", "5 kg", 2, 640], ["Sunflower Oil", "HSN 1512", "1 L", 6, 930], ["Tea Leaf", "HSN 0902", "500 g", 3, 540], ["Sugar", "HSN 1701", "1 kg", 10, 440]] },
    { tab: "Distributor", shop: "Mehta Electricals, Kanpur", no: "SALE-00093", tag: "Central sale · IGST 18%", rate: 18, kind: "central", col: "Pack",
      rows: [["LED Bulb 9W", "HSN 8539", "Box of 10", 120, 9600], ["Extension Board 4-way", "HSN 8536", "Each", 40, 7200], ["Switch 6A", "HSN 8536", "Box of 20", 200, 5000]] }
  ];
  var bill = $(".bill"), wrap = $(".bill-wrap"), tabs = $$(".bill-tabs button"), cur = 0, timer = null, auto = true;

  function renderBill(i, animate) {
    var b = bills[i]; cur = i;
    var taxable = b.rows.reduce(function (a, r) { return a + r[4]; }, 0);
    var tax = taxable * b.rate / 100, total = Math.round(taxable + tax);
    $(".bill-top strong", bill).textContent = b.shop;
    $(".bill-top > div > span", bill).textContent = "Tax Invoice " + b.no + " · 11 Nov 2026";
    $(".bill-tag", bill).textContent = b.tag;
    $("thead th:nth-child(2)", bill).textContent = b.col;
    $("tbody", bill).innerHTML = b.rows.map(function (r, k) {
      return "<tr style='--i:" + k + "'><td>" + r[0] + "<span class='sub'>" + r[1] + "</span></td><td>" + r[2] + "</td><td class='r num'>" + r[3] + "</td><td class='r num'>₹" + inr(r[4]) + "</td></tr>";
    }).join("");
    var taxLabel = b.kind === "central" ? "IGST " + b.rate + "%" : "SGST " + b.rate / 2 + "% + CGST " + b.rate / 2 + "%";
    $(".bill-foot", bill).innerHTML =
      "<div style='--j:0'><span>Taxable value</span><span class='num'>₹" + inr(taxable) + "</span></div>" +
      "<div style='--j:1'><span>" + taxLabel + "</span><span class='num'>₹" + inr(tax) + "</span></div>" +
      "<div class='total' style='--j:2'><span>Invoice total</span><span class='num' data-total='" + total + "'>₹" + inr(total) + "</span></div>";
    tabs.forEach(function (t, k) { t.setAttribute("aria-selected", k === i); t.classList.toggle("on", k === i); });
    bill.style.setProperty("--n", b.rows.length);
    bill.classList.remove("run"); void bill.offsetWidth; bill.classList.add("run");
    var tot = $("[data-total]", bill);
    if (animate && !reduce) { tot.textContent = "₹0.00"; setTimeout(function () { countTo(tot, total, 900, function (v) { return "₹" + inr(v); }); }, 700 + b.rows.length * 380); }
    var st = $(".stamp", bill); if (st) { st.style.animationDelay = (0.7 + b.rows.length * 0.42 + 1.1) + "s"; }
  }
  function next() { renderBill((cur + 1) % bills.length, true); }
  function play() { stop(); if (auto && !reduce) timer = setInterval(next, 7200); }
  function stop() { if (timer) clearInterval(timer); timer = null; }

  if (bill && wrap) {
    renderBill(0, true);
    tabs.forEach(function (t, k) { t.addEventListener("click", function () { auto = false; stop(); renderBill(k, true); }); });
    play();
    document.addEventListener("visibilitychange", function () { document.hidden ? stop() : play(); });
    // gentle tilt following the pointer (mouse only)
    if (!reduce && window.matchMedia("(hover: hover) and (pointer: fine)").matches) {
      wrap.addEventListener("pointermove", function (e) {
        var r = wrap.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
        bill.style.transform = "perspective(1100px) rotateY(" + (x * 5) + "deg) rotateX(" + (-y * 4) + "deg)";
      });
      wrap.addEventListener("pointerleave", function () { bill.style.transform = ""; });
    }
  }

  if (reduce) return;

  // ---------------------------------------------------------- scroll reveals
  if ("IntersectionObserver" in window) {
    var sel = ".sec-head, .row, .seg, .panel, .split .copy, .split > .checks, .facts > div, .cta .wrap > *, .proof .wrap > div, .contact-side > *, .form-card, .prose > p";
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { threshold: 0.12, rootMargin: "0px 0px -6% 0px" });
    $$(sel).forEach(function (el) {
      var sibs = el.parentElement ? Array.prototype.filter.call(el.parentElement.children, function (c) { return c.matches(sel); }) : [el];
      el.style.setProperty("--d", Math.min(sibs.indexOf(el), 4) * 80 + "ms");
      el.classList.add("reveal"); io.observe(el);
    });
  }

  // ---------------------------------------------------------- batch picker plays itself
  var picker = $(".panel[aria-label='Batch picker example']");
  if (picker) {
    var prow = $$("tbody tr", picker), pt = null;
    var seq = [0, 1, 2], run = function (k) {
      prow.forEach(function (r, i) { r.classList.toggle("sel", i === seq[k]); });
      picker.classList.toggle("done", k === seq.length - 1);
      pt = setTimeout(function () { run(k === seq.length - 1 ? 0 : k + 1); }, k === seq.length - 1 ? 3400 : 1100);
    };
    visibleWatcher(picker, function () { if (!pt) run(0); }, function () { clearTimeout(pt); pt = null; prow.forEach(function (r) { r.classList.remove("sel"); }); });
  }

  // ---------------------------------------------------------- credit bar fills when seen
  var credit = $(".credit");
  if (credit) visibleWatcher(credit, function () {
    if (credit.classList.contains("go")) return; credit.classList.add("go");
    countTo($(".credit-used", credit), 16370, 1200, function (v) { return "₹" + inr0(v); });
  });

  // ---------------------------------------------------------- shortcut keys press one after another
  var kl = $(".kbd-line");
  if (kl) {
    var spans = $$("span", kl), ki = 0, kt = null;
    var press = function () { spans.forEach(function (s, i) { s.classList.toggle("on", i === ki); }); ki = (ki + 1) % spans.length; kt = setTimeout(press, 1300); };
    visibleWatcher(kl, function () { if (!kt) press(); }, function () { clearTimeout(kt); kt = null; spans.forEach(function (s) { s.classList.remove("on"); }); });
  }

  // ---------------------------------------------------------- mobile sticky call to action
  var cta = $(".m-cta");
  if (cta && !document.getElementById("contact")) {
    var foot = $(".site-foot"), nearFoot = false, dlg = $("#demo-dialog");
    var upd = function () { cta.classList.toggle("show", window.scrollY > 520 && !nearFoot && !(dlg && dlg.open)); };
    if (foot && "IntersectionObserver" in window) new IntersectionObserver(function (es) { nearFoot = es[0].isIntersecting; upd(); }).observe(foot);
    window.addEventListener("scroll", upd, { passive: true }); upd();
    if (dlg) dlg.addEventListener("close", upd);
  }
})();
