#!/usr/bin/env python3
"""Generate static HTML study-guide pages from data/courses.json (source of truth)."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "courses.json"
FONTS = (
    "https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;"
    "9..144,600;9..144,700&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;1,400&display=swap"
)


def esc(s) -> str:
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def load() -> dict:
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))


def progress_of(course: dict) -> tuple[int, int, int]:
    lessons = course.get("lessons") or []
    total = len(lessons)
    done = sum(1 for l in lessons if l.get("status") in ("complete", "skipped"))
    pct = int(round(100 * done / total)) if total else 0
    return done, total, pct


def chip(status: str) -> str:
    label = {
        "complete": "Complete",
        "in-progress": "In progress",
        "not-started": "Not started",
        "skipped": "Skipped",
    }.get(status, status.replace("-", " ").title())
    cls = {
        "complete": "complete",
        "in-progress": "progress",
        "not-started": "not-started",
        "skipped": "not-started",
    }.get(status, "")
    return f'<span class="chip {cls}">{esc(label)}</span>'


def shell(title: str, root: str, body: str, description: str = "") -> str:
    desc = description or "Study guides for Global Life University — for learning and sermon prep."
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{FONTS}" rel="stylesheet">
  <link rel="stylesheet" href="{root}css/styles.css">
  <script>
    try {{
      var t = localStorage.getItem("glu-theme");
      if (t === "dark" || t === "light") document.documentElement.setAttribute("data-theme", t);
      else if (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches)
        document.documentElement.setAttribute("data-theme", "dark");
    }} catch (e) {{}}
  </script>
</head>
<body data-root="{root}">
  <a class="skip" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="nav-inner">
      <a class="brand" href="{root}index.html"><span class="mark">G</span> GLU Study</a>
      <ul class="nav-links">
        <li><a class="nav-text" href="{root}index.html#courses">Courses</a></li>
        <li><button type="button" class="icon-btn nav-search" id="search-open" aria-label="Search" title="Search">Search</button></li>
        <li><button type="button" class="icon-btn" id="theme-toggle" aria-label="Toggle dark mode"></button></li>
      </ul>
    </div>
  </header>
  <main id="main">{body}</main>
  <footer class="site-footer">
    <div class="wrap footer-inner">
      <span>GLU Study · notes for Jay-R · Global Life University</span>
      <span>No login · study guides for learning and sermon prep</span>
    </div>
  </footer>
  <div class="search-overlay" id="search-overlay" aria-hidden="true">
    <div class="search-box" role="dialog" aria-label="Search lessons">
      <input id="search-input" type="search" placeholder="Search courses, lessons, study guides…" autocomplete="off">
      <div class="search-results" id="search-results"></div>
    </div>
  </div>
  <script src="{root}js/courses-data.js"></script>
  <script src="{root}js/app.js"></script>
</body>
</html>
"""


def render_table(fig: dict) -> str:
    heads = "".join(f"<th>{esc(h)}</th>" for h in fig.get("headers") or [])
    rows = []
    for row in fig.get("rows") or []:
        rows.append("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in row) + "</tr>")
    cap = f"<p class='topic'>{esc(fig.get('caption', ''))}</p>" if fig.get("caption") else ""
    return (
        f'{cap}<div style="overflow:auto"><table class="gospel-table">'
        f'<thead><tr>{heads}</tr></thead><tbody>{"".join(rows)}</tbody></table></div>'
    )


def big_ideas_of(lesson: dict) -> list:
    ideas = lesson.get("bigIdeas")
    if ideas:
        return list(ideas)
    return list(lesson.get("takeaways") or [])


def summary_of(lesson: dict) -> str:
    if lesson.get("summary"):
        return str(lesson["summary"])
    topic = (lesson.get("topic") or "").strip()
    takes = lesson.get("takeaways") or []
    first = (takes[0] if takes else "").strip()
    if topic and first:
        t = topic if topic.endswith(".") else topic + "."
        return f"{t} {first}"
    return topic or first or ""


def is_miss_why(why: str) -> bool:
    import re
    w = why or ""
    # Word-boundary so "Missionary" etc. do not false-positive on "Miss"
    return bool(re.search(r"\bMiss\b", w) or re.search(r"\bPartial\b", w))


def count_quiz_items(lesson: dict) -> int:
    sections = lesson.get("quizSections") or []
    if sections:
        return sum(len(sec.get("quiz") or []) for sec in sections)
    return len(lesson.get("quiz") or [])


def qa_items_html(quiz: list) -> str:
    blocks = []
    for i, item in enumerate(quiz, 1):
        ans = (item.get("answer") or "").strip()
        cls = "true" if ans.lower() == "true" else "false" if ans.lower() == "false" else ""
        why = item.get("why") or ""
        miss = is_miss_why(why)
        miss_chip = '<span class="chip miss">Miss / partial</span>' if miss else ""
        why_html = f'<span class="why">{esc(why)}</span>' if why else ""
        blocks.append(
            f'<article class="qa-item{" miss-item" if miss else ""}">'
            f'<p class="qa-q">{i}. {esc(item.get("q", ""))}</p>'
            f'<div class="qa-a"><span class="ans {cls}">{esc(ans)}</span>'
            f"{miss_chip}{why_html}</div></article>"
        )
    return '<div class="qa">' + "".join(blocks) + "</div>"


def quiz_inner_html(lesson: dict) -> str:
    note = lesson.get("quizWordingNote")
    note_html = f'<p class="note">{esc(note)}</p>' if note else ""
    sections = lesson.get("quizSections") or []
    quiz = lesson.get("quiz") or []
    empty = lesson.get("quizEmpty")
    if not sections and not quiz:
        msg = empty or "Waiting on Jaira’s full pack"
        detail = lesson.get("quizEmptyDetail") or (
            "Full question text is not in this pack yet. Quizzes will land here as soon as "
            "the wording is confirmed — we will not invent answers."
        )
        return f'{note_html}<div class="empty"><strong>{esc(msg)}</strong>{esc(detail)}</div>'
    if sections:
        parts = [note_html]
        for sec in sections:
            title = sec.get("title") or "Quiz"
            score = sec.get("score")
            head = f'<h3 class="qa-section">{esc(title)}'
            if score is not None:
                attempts = sec.get("attempts", 1)
                head += f' <span>· {esc(score)}% · {esc(attempts)} attempt</span>'
            head += "</h3>"
            parts.append(head + qa_items_html(sec.get("quiz") or []))
        return "".join(parts)
    score = lesson.get("quizScore")
    score_html = ""
    if score is not None:
        attempts = lesson.get("quizAttempts", 1)
        score_html = (
            f'<p class="topic">Quiz score: <strong>{esc(score)}%</strong> · '
            f"{esc(attempts)} attempt</p>"
        )
    return note_html + score_html + qa_items_html(quiz)


def essay_html(lesson: dict) -> str | None:
    essays = lesson.get("essays") or []
    if not essays:
        return None
    parts = []
    for es in essays:
        body = esc(es.get("summary", "")).replace("\n", "<br>")
        parts.append(
            f'<article class="essay"><h3>{esc(es.get("theme", "Essay theme"))}</h3>'
            f'<p>{body}</p></article>'
        )
    return "".join(parts)


def glance_chips(lesson: dict) -> str:
    chips = [chip(lesson.get("status", ""))]
    score = lesson.get("quizScore")
    if score is not None:
        chips.append(f'<span class="chip complete">Quiz {esc(score)}%</span>')
    for sec in lesson.get("quizSections") or []:
        if sec.get("score") is not None:
            title = sec.get("title") or "Section"
            short = title if len(title) <= 28 else title[:26] + "…"
            chips.append(
                f'<span class="chip">{esc(short)} · {esc(sec["score"])}%</span>'
            )
    return "".join(chips)


def section_panel(label: str, heading: str, body: str, sid: str = "") -> str:
    id_attr = f' id="{esc(sid)}"' if sid else ""
    return (
        f'<section class="panel"{id_attr}>'
        f'<div class="panel-label">{esc(label)}</div>'
        f"<h2>{esc(heading)}</h2>"
        f"{body}</section>"
    )


def glance_html(lesson: dict) -> str:
    summary = summary_of(lesson)
    intro = lesson.get("introCard") or ""
    intro_html = f'<p class="glance-note">{esc(intro)}</p>' if intro else ""
    body = (
        f'<div class="glance">'
        f'<p class="glance-summary">{esc(summary)}</p>'
        f'<div class="meta-row">{glance_chips(lesson)}</div>'
        f"{intro_html}</div>"
    )
    return section_panel("At a glance", "Summary", body, "glance")


def ideas_html(lesson: dict) -> str | None:
    ideas = big_ideas_of(lesson)
    if not ideas:
        return None
    lis = "".join(f"<li>{esc(t)}</li>" for t in ideas)
    extra = ""
    if lesson.get("figure"):
        extra = render_table(lesson["figure"])
    body = f'<ul class="idea-list">{lis}</ul>{extra}'
    return section_panel("Big ideas", "What to teach and remember", body, "ideas")


def glossary_html(lesson: dict) -> str | None:
    gloss = lesson.get("glossary") or []
    if not gloss:
        return None
    cards = []
    for g in gloss:
        cards.append(
            f'<article class="glossary-card"><h3>{esc(g.get("term", ""))}</h3>'
            f'<p>{esc(g.get("meaning", ""))}</p></article>'
        )
    body = f'<div class="glossary-grid">{"".join(cards)}</div>'
    return section_panel("Key terms", "People, places, and words that matter", body, "glossary")


def outline_html(lesson: dict) -> str | None:
    outline = lesson.get("outline") or []
    if not outline:
        return None
    lis = "".join(f"<li>{esc(item)}</li>" for item in outline)
    body = f'<ol class="outline-list">{lis}</ol>'
    return section_panel("Structure", "Outline / timeline", body, "outline")


def must_know_html(lesson: dict) -> str | None:
    facts = lesson.get("mustKnow") or []
    if not facts:
        return None
    rows = "".join(
        f"<tr><th scope='row'>{esc(f.get('label', ''))}</th>"
        f"<td>{esc(f.get('value', ''))}</td></tr>"
        for f in facts
    )
    body = (
        f'<div style="overflow:auto"><table class="facts-table">'
        f"<tbody>{rows}</tbody></table></div>"
    )
    return section_panel("Must remember", "Facts to keep straight", body, "facts")


def compare_html(lesson: dict) -> str | None:
    blocks = lesson.get("compare") or []
    if not blocks:
        return None
    cards = []
    for b in blocks:
        pts = "".join(f"<li>{esc(p)}</li>" for p in b.get("points") or [])
        cards.append(
            f'<article class="compare-card"><h3>{esc(b.get("title", ""))}</h3>'
            f'<ul>{pts}</ul></article>'
        )
    body = f'<div class="compare-grid">{"".join(cards)}</div>'
    return section_panel("Compare", "Side-by-side contrasts", body, "compare")


def pulpit_html(lesson: dict) -> str | None:
    hooks = lesson.get("pulpit") or []
    if not hooks:
        return None
    lis = "".join(f"<li>{esc(h)}</li>" for h in hooks)
    body = f'<ul class="pulpit-list">{lis}</ul>'
    return section_panel("For the pulpit", "Sermon hooks", body, "pulpit")


def drill_html(lesson: dict) -> str:
    n = count_quiz_items(lesson)
    sections = lesson.get("quizSections") or []
    quiz = lesson.get("quiz") or []
    has_content = bool(sections or quiz)
    # Open only when few items; long quizzes stay closed
    open_attr = " open" if has_content and n and n <= 8 else ""
    inner = quiz_inner_html(lesson)
    count_bit = f" · {n} items" if has_content and n else ""
    return f"""<section class="panel" id="quiz">
  <div class="panel-label">Quiz drill</div>
  <details class="drill"{open_attr}>
    <summary>Quiz drill / review · open to practice{count_bit}</summary>
    <div class="drill-body">{inner}</div>
  </details>
</section>"""


def essays_panel(lesson: dict) -> str | None:
    body = essay_html(lesson)
    if body is None:
        return None
    return section_panel("Essay themes", "If you preach or review", body, "essays")


def quick_review_html(lesson: dict) -> str | None:
    items = lesson.get("quickReview") or []
    if not items:
        # Fall back to first 5 takeaways / big ideas as flash facts
        ideas = big_ideas_of(lesson)[:5]
        if not ideas:
            return None
        items = ideas
    lis = "".join(f"<li>{esc(t)}</li>" for t in items)
    return (
        f'<aside class="quick-review" id="review">'
        f'<div class="panel-label">Quick review</div>'
        f"<h2>Flash facts</h2>"
        f'<ul>{lis}</ul></aside>'
    )


def study_next(course: dict) -> dict | None:
    for les in course.get("lessons") or []:
        st = les.get("status")
        if st in ("skipped", "complete"):
            continue
        if st in ("not-started", "in-progress") or not st:
            return les
    return None


def index_page(data: dict) -> str:
    cards = []
    for course in data["courses"]:
        done, total, pct = progress_of(course)
        cert = (
            '<span class="chip cert">Certificate unlocked</span>'
            if course.get("certificateUnlocked")
            else '<span class="chip">Certificate locked</span>'
        )
        cards.append(
            f"""<a class="card" href="courses/{esc(course['id'])}.html">
  <div class="card-kicker"><span>Course {esc(course['code'])}</span>{chip(course.get('status',''))}</div>
  <h2>{esc(course['title'])}</h2>
  <p class="topic">{esc(course.get('blurb',''))}</p>
  <div class="progress-label"><span>{done} of {total} lessons</span><span>{pct}%</span></div>
  <div class="progress" aria-hidden="true"><span style="width:{pct}%"></span></div>
  <div class="meta-row">{cert}<span class="chip">{total} lessons</span></div>
</a>"""
        )
    body = f"""
  <section class="hero wrap">
    <div class="eyebrow">Global Life University</div>
    <h1>GLU Study — notes for Jay-R</h1>
    <p class="lede">Study guides for learning and sermon prep. Warm, clear, dense, and scannable — ready for the desk and the pulpit.</p>
    <p class="epigraph">“Your word is a lamp to my feet and a light to my path.”<cite>Psalm 119:105</cite></p>
  </section>
  <section class="wrap" id="courses">
    <div class="section-head">
      <div>
        <h2>Courses</h2>
        <p>GLU courses on the desk right now. Open a card, then a lesson study guide.</p>
      </div>
    </div>
    <div class="cards">
      {''.join(cards)}
    </div>
  </section>"""
    return shell("GLU Study — Global Life University notes for Jay-R", "", body)


def course_page(course: dict) -> str:
    done, total, pct = progress_of(course)
    nxt = study_next(course)
    study_next_html = ""
    if nxt:
        study_next_html = (
            f'<p class="study-next">Study next: '
            f'<a href="../lessons/{esc(nxt["id"])}.html">'
            f'Lesson {esc(nxt["number"])} — {esc(nxt["title"])}</a></p>'
        )
    elif pct >= 100:
        study_next_html = (
            '<p class="study-next">Study next: '
            '<span>All lessons complete or skipped — review any guide below.</span></p>'
        )
    rows = []
    for les in course.get("lessons") or []:
        score = les.get("quizScore")
        score_chip = (
            f'<span class="chip complete">Quiz {esc(score)}%</span>'
            if score is not None
            else ""
        )
        rows.append(
            f"""<a class="lesson-row" href="../lessons/{esc(les['id'])}.html">
  <div class="num">{esc(les['number'])}</div>
  <div>
    <h3>{esc(les['title'])}</h3>
    <p>{esc(les.get('topic') or '')}</p>
  </div>
  <div class="chips">{chip(les.get('status',''))}{score_chip}</div>
</a>"""
        )
    cert = (
        '<span class="chip cert">Certificate unlocked</span>'
        if course.get("certificateUnlocked")
        else '<span class="chip">Certificate locked</span>'
    )
    total_line = ""
    if course.get("courseTotal") is not None:
        total_line = (
            f'<span class="chip complete">Course total {esc(course["courseTotal"])}%</span>'
        )
    body = f"""
  <div class="wrap page-hero">
    <nav class="crumbs"><a href="../index.html">Home</a> · Course {esc(course['code'])}</nav>
    <div class="eyebrow">Course {esc(course['code'])}</div>
    <h1>{esc(course['title'])}</h1>
    <p class="lede">{esc(course.get('blurb',''))}</p>
    <div class="meta-row">{chip(course.get('status',''))}{cert}{total_line}<span class="chip">{done} of {total} lessons</span></div>
    <p class="progress-label" style="margin-top:1rem;max-width:24rem"><span>Progress</span><span>{pct}%</span></p>
    <div class="progress" style="max-width:24rem"><span style="width:{pct}%"></span></div>
    {study_next_html}
  </div>
  <section class="wrap lesson-list">{''.join(rows)}</section>"""
    return shell(f"{course['title']} · GLU Study", "../", body, course.get("blurb", ""))


def lesson_page(course: dict, lesson: dict, prev_l: dict | None, next_l: dict | None) -> str:
    pager_l = (
        f'<a href="{esc(prev_l["id"])}.html"><span>Previous</span> {esc(prev_l["title"])}</a>'
        if prev_l
        else "<span></span>"
    )
    pager_r = (
        f'<a class="right" href="{esc(next_l["id"])}.html"><span>Next</span> {esc(next_l["title"])}</a>'
        if next_l
        else "<span></span>"
    )

    parts = [
        glance_html(lesson),
        ideas_html(lesson),
        glossary_html(lesson),
        outline_html(lesson),
        must_know_html(lesson),
        compare_html(lesson),
        pulpit_html(lesson),
        drill_html(lesson),
        essays_panel(lesson),
        quick_review_html(lesson),
    ]
    sections = "".join(p for p in parts if p)

    body = f"""
  <div class="read page-hero">
    <nav class="crumbs"><a href="../index.html">Home</a> · <a href="../courses/{esc(course['id'])}.html">{esc(course['title'])}</a> · Lesson {esc(lesson['number'])}</nav>
    <div class="eyebrow">Lesson {esc(lesson['number'])} · Course {esc(course['code'])}</div>
    <h1>{esc(lesson['title'])}</h1>
    <p class="lede">{esc(lesson.get('topic') or '')}</p>
    <div class="meta-row">{glance_chips(lesson)}</div>
  </div>
  <div class="read">
    {sections}
    <nav class="pager">{pager_l}{pager_r}</nav>
  </div>"""
    desc = summary_of(lesson) or lesson.get("topic", "")
    return shell(f"{lesson['title']} · {course['title']}", "../", body, desc)


def main() -> None:
    data = load()
    (ROOT / "js").mkdir(exist_ok=True)
    (ROOT / "courses").mkdir(exist_ok=True)
    (ROOT / "lessons").mkdir(exist_ok=True)
    js = "window.GLU_DATA = " + json.dumps(data, ensure_ascii=False) + ";\n"
    (ROOT / "js" / "courses-data.js").write_text(js, encoding="utf-8")
    (ROOT / "index.html").write_text(index_page(data), encoding="utf-8")
    count_c = count_l = 0
    for course in data["courses"]:
        (ROOT / "courses" / f"{course['id']}.html").write_text(
            course_page(course), encoding="utf-8"
        )
        count_c += 1
        lessons = course.get("lessons") or []
        for i, lesson in enumerate(lessons):
            prev_l = lessons[i - 1] if i else None
            next_l = lessons[i + 1] if i + 1 < len(lessons) else None
            (ROOT / "lessons" / f"{lesson['id']}.html").write_text(
                lesson_page(course, lesson, prev_l, next_l), encoding="utf-8"
            )
            count_l += 1
    print(f"Wrote index + {count_c} courses + {count_l} lessons")


if __name__ == "__main__":
    main()
