(function () {
  var root = document.body.getAttribute("data-root") || "";
  var THEME_KEY = "glu-theme";

  function preferredTheme() {
    try {
      var saved = localStorage.getItem(THEME_KEY);
      if (saved === "light" || saved === "dark") return saved;
    } catch (e) {}
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light";
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    var btn = document.getElementById("theme-toggle");
    if (btn) {
      btn.setAttribute("aria-pressed", theme === "dark" ? "true" : "false");
      btn.setAttribute("aria-label", theme === "dark" ? "Switch to light mode" : "Switch to dark mode");
      btn.title = theme === "dark" ? "Light mode" : "Dark mode";
      btn.innerHTML = theme === "dark" ? sunIcon() : moonIcon();
    }
  }

  function moonIcon() {
    return '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M21 14.3A8.5 8.5 0 1 1 9.7 3 7 7 0 0 0 21 14.3z"/></svg>';
  }
  function sunIcon() {
    return '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>';
  }
  function searchIcon() {
    return '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.2-3.2"/></svg>';
  }

  applyTheme(preferredTheme());

  var themeBtn = document.getElementById("theme-toggle");
  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      var next = document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
      try { localStorage.setItem(THEME_KEY, next); } catch (e) {}
      applyTheme(next);
    });
  }

  var searchBtn = document.getElementById("search-open");
  if (searchBtn) searchBtn.innerHTML = searchIcon();
  if (themeBtn && !themeBtn.innerHTML.trim()) applyTheme(preferredTheme());

  var overlay = document.getElementById("search-overlay");
  var input = document.getElementById("search-input");
  var results = document.getElementById("search-results");

  function href(path) {
    return root + path;
  }

  function openSearch() {
    if (!overlay) return;
    overlay.classList.add("open");
    overlay.setAttribute("aria-hidden", "false");
    if (input) {
      input.value = "";
      renderResults("");
      setTimeout(function () { input.focus(); }, 20);
    }
  }
  function closeSearch() {
    if (!overlay) return;
    overlay.classList.remove("open");
    overlay.setAttribute("aria-hidden", "true");
  }

  if (searchBtn) searchBtn.addEventListener("click", openSearch);
  if (overlay) {
    overlay.addEventListener("click", function (e) {
      if (e.target === overlay) closeSearch();
    });
  }
  document.addEventListener("keydown", function (e) {
    if ((e.key === "k" && (e.metaKey || e.ctrlKey)) || (e.key === "/" && e.target === document.body)) {
      e.preventDefault();
      openSearch();
    }
    if (e.key === "/" && !/input|textarea/i.test((e.target.tagName || ""))) {
      e.preventDefault();
      openSearch();
    }
    if (e.key === "Escape") closeSearch();
  });

  function data() {
    return (window.GLU_DATA && window.GLU_DATA.courses) || [];
  }

  function haystack(lesson, course) {
    var parts = [
      course.title, course.id, String(course.code),
      lesson.title, lesson.topic || "", lesson.summary || ""
    ];
    (lesson.takeaways || []).forEach(function (t) { parts.push(t); });
    (lesson.bigIdeas || []).forEach(function (t) { parts.push(t); });
    (lesson.outline || []).forEach(function (t) { parts.push(t); });
    (lesson.pulpit || []).forEach(function (t) { parts.push(t); });
    (lesson.quickReview || []).forEach(function (t) { parts.push(t); });
    (lesson.glossary || []).forEach(function (g) {
      parts.push(g.term || "", g.meaning || "");
    });
    (lesson.mustKnow || []).forEach(function (f) {
      parts.push(f.label || "", f.value || "");
    });
    (lesson.compare || []).forEach(function (c) {
      parts.push(c.title || "");
      (c.points || []).forEach(function (pt) { parts.push(pt); });
    });
    (lesson.quiz || []).forEach(function (q) {
      parts.push(q.q || "", q.answer || "", q.why || "");
    });
    (lesson.quizSections || []).forEach(function (sec) {
      parts.push(sec.title || "");
      (sec.quiz || []).forEach(function (q) {
        parts.push(q.q || "", q.answer || "", q.why || "");
      });
    });
    (lesson.essays || []).forEach(function (es) {
      parts.push(es.theme || "", es.summary || "");
    });
    return parts.join(" ").toLowerCase();
  }

  function renderResults(q) {
    if (!results) return;
    q = (q || "").trim().toLowerCase();
    if (!q) {
      results.innerHTML = '<div class="search-empty">Search courses, lessons, study guides, and quiz text.</div>';
      return;
    }
    var hits = [];
    data().forEach(function (course) {
      if ((course.title + " " + course.code).toLowerCase().indexOf(q) !== -1) {
        hits.push({
          href: href("courses/" + course.id + ".html"),
          title: course.title,
          sub: "Course " + course.code
        });
      }
      (course.lessons || []).forEach(function (lesson) {
        if (haystack(lesson, course).indexOf(q) !== -1) {
          hits.push({
            href: href("lessons/" + lesson.id + ".html"),
            title: lesson.title,
            sub: course.title + " · Lesson " + lesson.number
          });
        }
      });
    });
    if (!hits.length) {
      results.innerHTML = '<div class="search-empty">No matches for “' + q.replace(/</g, "&lt;") + '”.</div>';
      return;
    }
    results.innerHTML = hits.slice(0, 24).map(function (h) {
      return '<a class="search-hit" href="' + h.href + '"><strong>' + h.title + "</strong><small>" + h.sub + "</small></a>";
    }).join("");
  }

  if (input) {
    input.addEventListener("input", function () { renderResults(input.value); });
  }
})();
