#!/usr/bin/env python3
"""Dense study-guide enrichment for all lessons with pack data.
Restructures existing takeaways/essays/quiz only — never invents quiz or lectures.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "courses.json"

STOP = {
    "The", "This", "That", "These", "Those", "When", "Then", "After", "Before",
    "With", "From", "Into", "God", "Lord", "Jesus", "Christ", "Spirit", "Bible",
    "Scripture", "Old", "New", "Testament", "True", "False", "Moodle", "Jay",
    "Lesson", "Quiz", "Essay", "One", "Two", "Three", "Four", "Five", "Six",
    "Seven", "Eight", "Nine", "Ten", "His", "Her", "Their", "They", "And", "But",
    "For", "Not", "Also", "Still", "Even", "Only", "Each", "Every", "Both",
    "Some", "Many", "Most", "All", "Any", "Our", "Your", "Its", "Who", "What",
    "Where", "Why", "How", "Church", "Gospel", "Word", "Father", "Son", "Holy",
    "People", "Israel", "Jews", "Gentiles", "Acts", "Paul", "Peter", "John",
    "Matthew", "Mark", "Luke", "Genesis", "Exodus", "There", "Here", "Thus",
    "Therefore", "However", "Because", "While", "Since", "Under", "Over",
    "About", "Among", "Between", "Through", "Without", "Within", "Toward",
}


def crisp(s: str, n: int = 140) -> str:
    s = re.sub(r"\s+", " ", (s or "")).strip()
    if len(s) <= n:
        return s
    cut = s[:n].rsplit(" ", 1)[0]
    return cut.rstrip(".,;:") + "…"


def sentences(text: str) -> list[str]:
    return [p.strip() for p in re.split(r"(?<=[.!?])\s+", (text or "").strip()) if p.strip()]


def quiz_items(lesson: dict) -> list[dict]:
    items = list(lesson.get("quiz") or [])
    for sec in lesson.get("quizSections") or []:
        items.extend(sec.get("quiz") or [])
    return items


def miss_items(lesson: dict) -> list[dict]:
    out = []
    for q in quiz_items(lesson):
        why = q.get("why") or ""
        if "Miss" in why or "Partial" in why:
            out.append(q)
    return out


def pack_blob(lesson: dict) -> str:
    parts = []
    parts.extend(lesson.get("takeaways") or [])
    for e in lesson.get("essays") or []:
        parts.append(e.get("theme") or "")
        parts.append(e.get("summary") or "")
    for q in quiz_items(lesson):
        parts.append(q.get("why") or "")
    parts.append(lesson.get("topic") or "")
    return "\n".join(p for p in parts if p)


def is_thin(lesson: dict) -> bool:
    status = lesson.get("status")
    takes = lesson.get("takeaways") or []
    essays = lesson.get("essays") or []
    quiz = quiz_items(lesson)
    if status in ("empty", "not-started"):
        return True
    if status == "skipped" and len(takes) <= 2 and not essays and not quiz:
        return True
    if not takes and not essays and not quiz:
        return True
    return False


def build_summary(lesson: dict) -> str:
    existing = (lesson.get("summary") or "").strip()
    if existing and 2 <= len(sentences(existing)) <= 4 and len(existing) >= 80:
        return existing
    topic = (lesson.get("topic") or "").strip()
    takes = lesson.get("takeaways") or []
    essays = lesson.get("essays") or []
    sents: list[str] = []
    if topic:
        sents.append(topic if topic.endswith((".", "!", "?")) else topic + ".")
    if takes:
        first = takes[0].strip()
        if not sents or first[:50] not in sents[0]:
            sents.append(first if first.endswith((".", "!", "?")) else first + ".")
    if essays and len(sents) < 3:
        themes = "; ".join(e.get("theme", "") for e in essays[:3] if e.get("theme"))
        if themes:
            sents.append(f"Essay work covers {themes}.")
    elif len(sents) < 2 and len(takes) > 1:
        second = takes[1].strip()
        sents.append(second if second.endswith((".", "!", "?")) else second + ".")
    return " ".join(sents[:3]).strip() or existing or topic or (takes[0] if takes else "")


def build_big_ideas(lesson: dict) -> list[str]:
    existing = lesson.get("bigIdeas") or []
    takes = lesson.get("takeaways") or []
    essays = lesson.get("essays") or []
    if 5 <= len(existing) <= 8 and all(len(x) > 20 for x in existing):
        return list(existing)[:8]
    ideas: list[str] = []
    for t in existing or takes:
        t = (t or "").strip()
        if t and t not in ideas:
            ideas.append(t)
    for e in essays:
        if len(ideas) >= 8:
            break
        theme = (e.get("theme") or "").strip()
        summary = (e.get("summary") or "").strip()
        if theme and summary:
            bullet = f"{theme}: {crisp(summary, 150)}"
            if bullet not in ideas:
                ideas.append(bullet)
        elif theme and theme not in ideas:
            ideas.append(theme)
    if len(ideas) < 5:
        for q in quiz_items(lesson):
            if q.get("answer") == "True" and q.get("why"):
                ideas.append(crisp(q["why"], 150))
            if len(ideas) >= 5:
                break
    return ideas[:8]


def extract_colon_lists(text: str) -> list[tuple[str, list[str]]]:
    results = []
    for m in re.finditer(r"([^:\n]{8,80}):\s*([^.\n]{15,220})", text):
        head, body = m.group(1).strip(), m.group(2).strip()
        parts = re.split(r",\s*|\s+and\s+|\s*;\s*|\s+[—–]\s*", body)
        parts = [p.strip(" .") for p in parts if len(p.strip(" .")) > 1]
        if 3 <= len(parts) <= 12:
            results.append((head, parts))
    return results


def outline_quality(o: list) -> int:
    if not o or len(o) < 2:
        return 0
    short = sum(1 for x in o if len(str(x)) < 12 and str(x)[:1].islower())
    if short >= max(2, len(o) // 2):
        return 0
    return len(o)


def build_outline(lesson: dict) -> list[str] | None:
    existing = lesson.get("outline") or []
    if outline_quality(existing) >= 3:
        return list(existing)
    essays = lesson.get("essays") or []
    takes = lesson.get("takeaways") or []
    outline: list[str] = []
    for e in essays:
        theme = (e.get("theme") or "").strip()
        if theme:
            outline.append(theme)
    blob = "\n".join(takes)
    for head, parts in extract_colon_lists(blob):
        hl = head.lower()
        if any(
            k in hl
            for k in (
                "chronolog", "sayings", "steps", "stages", "journey", "order",
                "structure", "divisions", "expressions", "views", "reasons",
                "traits", "characteristics", "walk",
            )
        ):
            if len(parts) >= 4:
                return parts[:10]
    if not outline and takes:
        outline = [crisp(t, 90) for t in takes[:6]]
    return outline[:10] if outline else None


def meaning_for(term: str, lesson: dict, blob: str) -> str | None:
    # Fast local patterns only — no catastrophic backtracking
    esc = re.escape(term)
    for pat in (
        rf"{esc}\s+means?\s+([^.!\n]{{8,140}})",
        rf"{esc}\s*[—–=]\s*([^.!\n]{{8,140}})",
        rf"{esc}\s*\(([^)]{{8,100}})\)",
        rf"{esc}\s*:\s*([^.!\n]{{8,140}})",
    ):
        m = re.search(pat, blob, flags=re.I)
        if m:
            meaning = m.group(1).strip(" \"“”'.,;:")
            if len(meaning) > 8:
                return crisp(meaning, 160)
    # First sentence containing the term (simple scan)
    low = term.lower()
    for sent in sentences(blob):
        if low in sent.lower() and 25 < len(sent) < 220:
            return crisp(sent, 160)
    for q in quiz_items(lesson):
        why = q.get("why") or ""
        if low in why.lower() and len(why) > 15:
            return crisp(why, 160)
    for e in lesson.get("essays") or []:
        summ = e.get("summary") or ""
        if low in summ.lower():
            return crisp(summ, 160)
    return None


def build_glossary(lesson: dict) -> list[dict] | None:
    existing = lesson.get("glossary") or []
    if existing and len(existing) >= 3:
        return list(existing)

    blob = pack_blob(lesson)
    scores: dict[str, int] = {}

    for m in re.finditer(r"[“\"]([^”\"]{2,40})[”\"]", blob):
        term = m.group(1).strip()
        if 2 <= len(term) <= 40:
            scores[term] = scores.get(term, 0) + 4

    for m in re.finditer(r"\b([A-Za-z][A-Za-z\-]*(?:ology|ism))\b", blob):
        scores[m.group(1)] = scores.get(m.group(1), 0) + 3

    for m in re.finditer(r"\b([A-Za-z][A-Za-z\-]+)\s*=\s*([^.!,\n]{3,50})", blob):
        scores[m.group(1)] = scores.get(m.group(1), 0) + 5

    # Proper names — count only, cap candidates
    for m in re.finditer(r"\b([A-Z][a-z]{2,}(?:\s+[A-Z][a-z]+){0,2})\b", blob):
        term = m.group(1)
        first = term.split()[0]
        if first in STOP or term in STOP:
            continue
        scores[term] = scores.get(term, 0) + 1

    ranked = sorted(scores.items(), key=lambda kv: (-kv[1], kv[0]))[:40]
    gloss: list[dict] = []
    seen: set[str] = set()
    for term, score in ranked:
        key = term.lower()
        if key in seen:
            continue
        if score < 2 and not re.search(r"(ology|ism)", term):
            continue
        meaning = meaning_for(term, lesson, blob)
        if not meaning:
            continue
        if meaning.lower().startswith(key) and len(meaning) < len(term) + 20:
            continue
        gloss.append({"term": term, "meaning": meaning})
        seen.add(key)
        if len(gloss) >= 8:
            break

    if len(gloss) < 3:
        # Essay-theme cards as reliable fallback (pack material only)
        for e in lesson.get("essays") or []:
            theme = (e.get("theme") or "").strip()
            summary = (e.get("summary") or "").strip()
            if not theme or not summary:
                continue
            term = theme.split("—")[0].split(":")[0].strip()
            if 3 < len(term) < 55 and term.lower() not in seen:
                gloss.append({"term": term, "meaning": crisp(summary, 160)})
                seen.add(term.lower())
            if len(gloss) >= 6:
                break

    # Key doctrine words from takeaways if still thin
    if len(gloss) < 3:
        for t in lesson.get("takeaways") or []:
            for m in re.finditer(
                r"\b(covenant|propitiation|redemption|reconciliation|justification|"
                r"sanctification|regeneration|inspiration|inerrancy|trinity|"
                r"atonement|substitution|remnant|synagogue|diaspora|septuagint|"
                r"pharisees|sadducees|prolegomena|pneumatology|christology|"
                r"bibliology|hamartiology|soteriology|angelology)\b",
                t,
                flags=re.I,
            ):
                term = m.group(1)
                key = term.lower()
                if key in seen:
                    continue
                meaning = meaning_for(term, lesson, blob) or crisp(t, 160)
                gloss.append({"term": term[0].upper() + term[1:], "meaning": meaning})
                seen.add(key)
                if len(gloss) >= 5:
                    break
            if len(gloss) >= 5:
                break

    return gloss if gloss else None


def build_must_know(lesson: dict) -> list[dict] | None:
    existing = lesson.get("mustKnow") or []
    if (
        existing
        and len(existing) >= 3
        and all(isinstance(x, dict) and x.get("label") and x.get("value") for x in existing)
    ):
        return list(existing)

    rows: list[dict] = []
    if lesson.get("quizScore") is not None:
        attempts = lesson.get("quizAttempts")
        val = f"{lesson['quizScore']}%"
        if attempts:
            val += f" ({attempts} attempt{'s' if attempts != 1 else ''})"
        rows.append({"label": "Quiz score", "value": val})

    text = "\n".join(
        list(lesson.get("takeaways") or [])
        + [(e.get("summary") or "") for e in (lesson.get("essays") or [])]
    )
    patterns = [
        ("Author", re.compile(r"(?:wrote by|written by|author(?:ed)?(?:\s+is|\s+was)?)\s+([A-Z][^.]{3,70})", re.I)),
        ("Audience", re.compile(r"(?:audience[:\s]+|written to(?:\s+the)?)\s*([^.]{3,70})", re.I)),
        ("Date", re.compile(r"(\d{2,4}\s*(?:BC|AD|A\.D\.|B\.C\.)[^.]{0,30})", re.I)),
        ("Purpose", re.compile(r"(?:purpose|aim|goal)\s*(?:is|:)\s*([^.]{8,90})", re.I)),
        ("Key word", re.compile(r"key word\s*(?:is|:)?\s*[“\"']?([^.”\"',\n]{2,40})", re.I)),
        ("Portrait", re.compile(r"Christ as ([^—\n,.]{3,40})", re.I)),
    ]
    for label, cre in patterns:
        m = cre.search(text)
        if m and not any(r["label"] == label for r in rows):
            rows.append({"label": label, "value": crisp(m.group(1).strip(" :—–"), 120)})

    for t in (lesson.get("takeaways") or [])[:3]:
        tl = t.lower()
        label = "Key claim"
        if "covenant" in tl:
            label = "Covenant"
        elif "reject" in tl or "false" in tl:
            label = "Reject"
        elif "preach" in tl:
            label = "Preach"
        val = crisp(t, 140)
        if not any(r["value"] == val for r in rows):
            rows.append({"label": label, "value": val})
        if len(rows) >= 7:
            break

    for i, q in enumerate(miss_items(lesson)[:3], 1):
        rows.append(
            {
                "label": f"Miss drill {i}",
                "value": crisp(f"{q.get('answer')}: {q.get('q','')} — {q.get('why','')}", 160),
            }
        )

    if existing and len(rows) < 3:
        for row in existing:
            if row not in rows:
                rows.append(row)

    return rows[:8] if rows else None


def build_compare(lesson: dict) -> list[dict] | None:
    existing = lesson.get("compare") or []
    if existing and isinstance(existing, list) and existing and isinstance(existing[0], dict):
        return list(existing)

    blocks: list[dict] = []
    takes = lesson.get("takeaways") or []
    essays = lesson.get("essays") or []

    for t in takes:
        if " vs " in t.lower():
            parts = re.split(r"\s+vs\.?\s+", t, flags=re.I)
            if len(parts) == 2:
                blocks.append(
                    {"title": "Contrast", "points": [crisp(parts[0], 100), crisp(parts[1], 100)]}
                )
        elif " — not " in t:
            a, b = t.split(" — not ", 1)
            blocks.append({"title": "Clarify", "points": [crisp(a, 100), "Not: " + crisp(b, 100)]})

    for e in essays:
        theme = e.get("theme") or ""
        summary = e.get("summary") or ""
        tl = theme.lower()
        if any(k in tl for k in ("theor", "view", "contrast", "compar", "vs", "reject", "false")):
            points: list[str] = []
            lists = extract_colon_lists(summary)
            if lists:
                points = [crisp(p, 90) for p in lists[0][1][:6]]
            else:
                m = re.search(r"(?:theories|views|reject(?:ed)?)\s*:?\s*([^.]+)", summary, re.I)
                if m:
                    parts = re.split(r",\s*|\s*;\s*|\s+and\s+", m.group(1))
                    points = [crisp(p, 80) for p in parts if len(p.strip()) > 2][:8]
            if len(points) >= 2:
                blocks.append({"title": theme, "points": points})

    # Pharisees / Sadducees — simple non-backtracking search
    blob = pack_blob(lesson)
    if "Pharisee" in blob and "Sadducee" in blob:
        ph = next((s for s in sentences(blob) if "Pharisee" in s), None)
        sa = next((s for s in sentences(blob) if "Sadducee" in s), None)
        if ph and sa and ph != sa:
            blocks.append(
                {"title": "Pharisees and Sadducees", "points": [crisp(ph, 120), crisp(sa, 120)]}
            )

    for t in takes:
        if "Matthew:" in t and "Mark:" in t:
            parts = re.findall(r"((?:Matthew|Mark|Luke|John)\s*:[^.]+)", t)
            if len(parts) >= 2:
                blocks.append(
                    {"title": "Four Gospels at a glance", "points": [crisp(p, 110) for p in parts]}
                )

    essay_blob = "\n".join(takes + [e.get("summary", "") for e in essays])
    for head, parts in extract_colon_lists(essay_blob):
        hl = head.lower()
        if any(k in hl for k in ("view", "theor", "expression", "reject", "false")):
            if len(parts) >= 2:
                blocks.append({"title": crisp(head, 60), "points": [crisp(p, 90) for p in parts[:8]]})

    seen: set[str] = set()
    out: list[dict] = []
    for b in blocks:
        title = b.get("title", "")
        if title in seen or len(b.get("points") or []) < 2:
            continue
        seen.add(title)
        out.append(b)
        if len(out) >= 3:
            break
    return out or None


def build_pulpit(lesson: dict) -> list[str] | None:
    existing = lesson.get("pulpit") or []
    if existing and len(existing) >= 2:
        return list(existing)[:4]

    hooks: list[str] = []
    sources = list(lesson.get("takeaways") or [])
    for e in lesson.get("essays") or []:
        if e.get("summary"):
            sources.append(e["summary"])
    preach_keys = (
        "preach", "pulpit", "sermon", "pastoral", "for the church",
        "when you teach", "when you preach",
    )
    for src in sources:
        for sent in sentences(src):
            sl = sent.lower()
            if any(k in sl for k in preach_keys):
                h = crisp(sent, 160)
                if h not in hooks:
                    hooks.append(h)
    tone_keys = (
        "watch", "hold", "reject", "do not", "keep", "let", "name", "walk",
        "test", "remember", "cling", "faith", "hope", "love", "cross",
        "gospel", "christ", "kingdom",
    )
    if len(hooks) < 2:
        for t in (lesson.get("takeaways") or [])[:5]:
            if any(k in t.lower() for k in tone_keys):
                base = crisp(t, 130)
                if base not in hooks:
                    hooks.append(base)
            if len(hooks) >= 3:
                break
    if len(hooks) < 2:
        topic = lesson.get("topic") or lesson.get("title") or ""
        if topic:
            hooks.append(crisp(f"Keep this lesson’s center clear for the people: {topic}", 160))
        if lesson.get("takeaways"):
            hooks.append(crisp(lesson["takeaways"][0], 150))
    return hooks[:4] if hooks else None


def build_quick_review(lesson: dict) -> list[str] | None:
    existing = lesson.get("quickReview") or []
    facts: list[str] = []
    for q in miss_items(lesson):
        facts.append(crisp(f"Miss: {q.get('answer')} — {q.get('q')}", 120))
    for t in lesson.get("takeaways") or []:
        facts.append(crisp(t, 110))
        if len(facts) >= 8:
            break
    if len(facts) < 5:
        for q in quiz_items(lesson):
            if q.get("answer") == "True":
                facts.append(crisp(q.get("q"), 110))
            elif q.get("answer") == "False":
                facts.append(crisp(f"False: {q.get('q')}", 110))
            if len(facts) >= 5:
                break
    out: list[str] = []
    seen: set[str] = set()
    for f in facts:
        k = f.lower()[:50]
        if k in seen:
            continue
        seen.add(k)
        out.append(f)
        if len(out) >= 5:
            break
    if len(out) < 5:
        for f in existing:
            k = f.lower()[:50]
            if k not in seen:
                out.append(f)
                seen.add(k)
            if len(out) >= 5:
                break
    return out[:5] if out else None


def thin_enrich(lesson: dict) -> None:
    topic = lesson.get("topic") or lesson.get("title") or "This lesson"
    status = lesson.get("status") or "not-started"
    if status == "skipped":
        summary = f"{topic}. Skipped in this pack — waiting on fuller notes before dense enrichment."
    elif status in ("empty", "not-started"):
        summary = f"{topic}. Not started / empty in this pack — enrichment waiting on takeaways and quiz data."
    else:
        summary = f"{topic}. Minimal pack data so far — enrichment left thin."
    lesson["summary"] = summary
    takes = lesson.get("takeaways") or []
    if takes:
        lesson["bigIdeas"] = takes[:5]
        lesson["quickReview"] = [crisp(t, 100) for t in takes[:5]]
    else:
        lesson["bigIdeas"] = [summary]
        lesson["quickReview"] = [
            f"Status: {status}",
            "No takeaways in pack yet",
            "No quiz stems to drill",
            "No essays yet",
            "Revisit when pack arrives",
        ]
    for k in ("glossary", "outline", "mustKnow", "compare", "pulpit"):
        if not lesson.get(k):
            lesson[k] = None


def classify(lesson: dict) -> str:
    needed = ["summary", "bigIdeas", "glossary", "outline", "mustKnow", "pulpit", "quickReview"]
    has = {k: bool(lesson.get(k)) for k in needed}
    if is_thin(lesson) and not all(has.values()):
        # If thin path left dense fields empty → THIN
        if not (has["glossary"] and has["outline"] and has["mustKnow"] and has["pulpit"]):
            return "THIN"
    if all(has.values()):
        return "FULL"
    if sum(has.values()) >= 3:
        return "PARTIAL"
    return "THIN"


def enrich_lesson(lesson: dict, course_id: str) -> str:
    if is_thin(lesson):
        thin_enrich(lesson)
        return "THIN"

    # Keep Gospels FULL enrichment intact
    if course_id == "four-gospels" and all(
        lesson.get(k)
        for k in ("summary", "bigIdeas", "glossary", "outline", "mustKnow", "pulpit", "quickReview")
    ):
        return "FULL"

    lesson["summary"] = build_summary(lesson)
    lesson["bigIdeas"] = build_big_ideas(lesson)

    gloss = build_glossary(lesson)
    if gloss:
        lesson["glossary"] = gloss

    outline = build_outline(lesson)
    if outline:
        lesson["outline"] = outline

    mk = build_must_know(lesson)
    if mk:
        lesson["mustKnow"] = mk

    cmp_ = build_compare(lesson)
    if cmp_:
        lesson["compare"] = cmp_

    pulpit = build_pulpit(lesson)
    if pulpit:
        lesson["pulpit"] = pulpit

    qr = build_quick_review(lesson)
    if qr:
        lesson["quickReview"] = qr

    return classify(lesson)


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    report = {"FULL": [], "PARTIAL": [], "THIN": []}
    needed = ["summary", "bigIdeas", "glossary", "outline", "mustKnow", "pulpit", "quickReview"]

    for course in data["courses"]:
        for lesson in course["lessons"]:
            cat = enrich_lesson(lesson, course["id"])
            # Reclassify from final fields
            cat = classify(lesson)
            has = {k: bool(lesson.get(k)) for k in needed}
            report[cat].append(
                {
                    "course": course["id"],
                    "courseTitle": course["title"],
                    "id": lesson["id"],
                    "number": lesson.get("number"),
                    "title": lesson["title"],
                    "status": lesson.get("status"),
                    "fields": has,
                    "hasCompare": bool(lesson.get("compare")),
                    "missing": [k for k, v in has.items() if not v],
                }
            )

    data["meta"]["updated"] = "2026-09-04"
    DATA.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Write markdown report
    lines = [
        "# GLU Study enrichment report",
        "",
        f"Updated: 2026-09-04 (Asia/Manila)",
        "",
        "## Counts",
        "",
        f"- **FULL**: {len(report['FULL'])} (summary + bigIdeas + glossary + outline + mustKnow + pulpit + quickReview)",
        f"- **PARTIAL**: {len(report['PARTIAL'])}",
        f"- **THIN**: {len(report['THIN'])}",
        f"- **Total lessons**: {sum(len(report[k]) for k in report)}",
        "",
    ]
    for cat in ("FULL", "PARTIAL", "THIN"):
        lines.append(f"## {cat}")
        lines.append("")
        if not report[cat]:
            lines.append("_None_")
            lines.append("")
            continue
        by_course: dict[str, list] = {}
        for r in report[cat]:
            by_course.setdefault(r["courseTitle"], []).append(r)
        for ctitle, items in by_course.items():
            lines.append(f"### {ctitle}")
            lines.append("")
            for r in items:
                num = r.get("number")
                label = f"L{num}" if num is not None else r["id"]
                extra = ""
                if cat == "PARTIAL":
                    extra = f" — missing: {', '.join(r['missing'])}"
                elif cat == "THIN":
                    extra = f" — status={r['status']}"
                cmp = " · compare ✓" if r.get("hasCompare") else ""
                lines.append(f"- `{r['id']}` {label}: {r['title']}{extra}{cmp}")
            lines.append("")

    report_path = ROOT / "enrichment-report.md"
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    Path("/tmp/enrich_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(f"FULL={len(report['FULL'])} PARTIAL={len(report['PARTIAL'])} THIN={len(report['THIN'])}")
    print(f"report={report_path}")
    if report["PARTIAL"]:
        print("PARTIAL details:")
        for r in report["PARTIAL"]:
            print(f"  {r['course']} {r['id']} missing={r['missing']}")
    if report["THIN"]:
        print("THIN details:")
        for r in report["THIN"]:
            print(f"  {r['course']} {r['id']} status={r['status']}")


if __name__ == "__main__":
    main()
