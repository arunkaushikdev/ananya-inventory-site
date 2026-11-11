(function () {
  var TO = "arun.idevs@gmail.com"; // form submissions are emailed here (via FormSubmit)
  document.documentElement.classList.add("js");

  // mobile menu
  var btn = document.querySelector(".menu-btn"), nav = document.querySelector(".nav");
  if (btn) btn.addEventListener("click", function () {
    var open = nav.classList.toggle("open");
    btn.setAttribute("aria-expanded", open);
  });

  // hero bill plays once
  var bill = document.querySelector(".bill");
  if (bill) requestAnimationFrame(function () { bill.classList.add("run"); });

  // demo dialog
  var dlg = document.getElementById("demo-dialog");
  document.querySelectorAll("[data-demo]").forEach(function (el) {
    el.addEventListener("click", function (e) {
      if (dlg && dlg.showModal) { e.preventDefault(); dlg.showModal(); var f = dlg.querySelector("input"); if (f) f.focus(); }
    });
  });
  if (dlg) {
    dlg.querySelector(".close").addEventListener("click", function () { dlg.close(); });
    dlg.addEventListener("click", function (e) { if (e.target === dlg) dlg.close(); });
  }

  // forms
  document.querySelectorAll("form[data-lead]").forEach(function (form) {
    var status = form.querySelector(".form-status");
    var submit = form.querySelector("button[type=submit]");
    function show(kind, text) { status.className = "form-status show " + kind; status.textContent = text; }
    function check(field) {
      var input = field.querySelector("input,select,textarea");
      var msg = field.querySelector(".msg");
      var ok = true, text = "";
      if (input.required && !input.value.trim()) { ok = false; text = "Enter " + field.dataset.name + "."; }
      else if (input.type === "email" && input.value && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(input.value)) { ok = false; text = "Enter a valid email, like name@shop.com."; }
      else if (input.name === "phone" && input.value && input.value.replace(/\D/g, "").length < 10) { ok = false; text = "Enter a 10-digit mobile number."; }
      field.classList.toggle("err", !ok);
      if (msg) msg.textContent = text;
      return ok;
    }
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var fields = form.querySelectorAll(".field"), good = true;
      fields.forEach(function (f) { if (!check(f)) good = false; });
      if (!good) { show("bad", "Fix the highlighted fields and send again."); var bad = form.querySelector(".err input,.err select"); if (bad) bad.focus(); return; }
      if (form.querySelector("[name=website]").value) return; // honeypot
      var data = new FormData(form);
      data.delete("website");
      data.append("_subject", "Inventory ERP demo request: " + (data.get("business") || data.get("name")));
      data.append("_template", "table");
      data.append("_captcha", "false");
      data.append("page", location.pathname);
      submit.disabled = true; var label = submit.textContent; submit.textContent = "Sending...";
      status.className = "form-status";
      fetch("https://formsubmit.co/ajax/" + TO, { method: "POST", headers: { Accept: "application/json" }, body: data })
        .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { if (!r.ok || j.success === "false") throw new Error(); }); })
        .then(function () { form.reset(); show("ok", "Thanks, " + (data.get("name") || "").split(" ")[0] + ". We got your details and will call you within one working day."); })
        .catch(function () { show("bad", "The form could not be sent. Email us at " + TO + " or try again in a minute."); })
        .then(function () { submit.disabled = false; submit.textContent = label; });
    });
    form.addEventListener("focusout", function (e) { var f = e.target.closest && e.target.closest(".field"); if (f) check(f); });
  });
})();
