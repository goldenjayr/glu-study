# GLU Study

Static **study guides** for **Jay-R** — Global Life University courses, written for learning and sermon prep.

## Open the site

**Local server (preferred):**

```bash
cd /workspace/glu-study
./serve.sh
# or: python3 -m http.server 8787 --bind 0.0.0.0
```

Then open **http://localhost:8787/** (or this machine’s URL on port **8787**).

Pages also work as files (`index.html`) if you do not need search’s JSON extras — search and data live in `js/courses-data.js`, so file:// is fine for reading.

## Layout

```
glu-study/
  index.html              Home — course cards
  css/styles.css
  js/app.js               Search + dark mode
  js/courses-data.js      Generated copy of the JSON (do not edit by hand)
  data/courses.json       SOURCE OF TRUTH
  courses/*.html          One page per course
  lessons/*.html          One page per lesson
  generate.py             Rebuilds HTML + js/courses-data.js from the JSON
  serve.sh
```

After you edit `data/courses.json`, run:

```bash
python3 generate.py
```

## JSON shape (for later Jaira packs)

```json
{
  "courses": [{
    "id": "ot-survey-1",
    "code": 50,
    "title": "Old Testament Survey 1",
    "status": "complete | in-progress | not-started",
    "certificateUnlocked": true,
    "courseTotal": 100,
    "blurb": "One-line pastoral summary",
    "lessons": [{
      "id": "ot-1",
      "number": 1,
      "title": "…",
      "topic": "one-line topic",
      "quizScore": 100,
      "quizAttempts": 1,
      "status": "complete | in-progress | not-started",
      "summary": "2-3 sentences at a glance",
      "bigIdeas": ["crisp teaching bullets"],
      "glossary": [{"term": "…", "meaning": "who/what + why it matters"}],
      "outline": ["ordered structure points"],
      "mustKnow": [{"label": "Author", "value": "…"}],
      "compare": [{"title": "…", "points": ["…"]}],
      "pulpit": ["sermon hooks"],
      "quickReview": ["flash facts"],
      "takeaways": ["pastor-friendly bullets (fallback for bigIdeas)"],
      "quiz": [{"q": "full question", "answer": "True", "why": "short why"}],
      "essays": [{"theme": "…", "summary": "…"}],
      "quizWordingNote": "Question wording reconstructed from session notes.",
      "quizEmpty": "Waiting on Jaira’s full pack",
      "quizEmptyDetail": "…"
    }]
  }]
}
```

### Lesson study-guide sections (page order)

1. At a glance · 2. Big ideas · 3. Glossary · 4. Outline · 5. Must-know facts · 6. Compare · 7. For the pulpit · 8. Quiz drill (in `<details>`) · 9. Essay themes (if any) · 10. Quick review

- Optional fields hide when empty. Missing `bigIdeas` → `takeaways`. Missing `summary` → `topic` + first takeaway.
- Empty `quiz` → placeholder UI (do **not** invent Q&A). Essay panel omitted when `essays` is empty.
- `quizScore: null` when the quiz is not done.
- Optional `figure`: `{ "caption", "headers": [], "rows": [[]] }`. Optional `introCard` under At a glance.

## Design

Cream / parchment, deep navy, muted gold. Fraunces headings, Source Sans 3 body. Dark mode toggle (saved in `localStorage`, respects `prefers-color-scheme` on first visit). Sticky nav: **GLU Study · Courses · Search**.

## Status snapshot (this build)

| Course | Code | Status | Certificate | Full quiz Q&A |
|---|---|---|---|---|
| Old Testament Survey 1 | 50 | Complete 100% | Unlocked | L1–L6 full quiz Q&A. L1 & L3 exact Moodle; L2, L4, L5, L6 reconstructed from session notes. |
| Old Testament Survey 2 | 54 | Complete 99% | Unlocked | L7–L12 full Q&A (L11 90%). |
| Survey of Theology 1 | 52 | Complete 100% | Unlocked | L1–L6. L2 & L3 labeled reconstructed from session notes. |
| Survey of Theology 2 | 56 | Complete | Unlocked | L7–L12 full Q&A. Course total 96%. |
| Survey of Theology 3 | 57 | Complete 98% | Unlocked | L1–L6 full Q&A. Course total 98%; certificate unlocked (cmid 2158). BIB 205. |
| The Book of Acts | 60 | Complete 98% | Locked | L1–L3 + Final (93.33%). Reports/Project skipped. Cert not unlocked. Third Mill. |
| Apologetics 2 | 65 | Complete 98% | Unlocked | L7–L12 full Q&A + essays. Course total 98%; certificate unlocked (cmid 2164). BIB 222 / DOCX. |
| Church History 2 | 66 | In progress 88% | Locked | L7–L11 full Q&A + essays. L12 empty. Cert cmid 2165 locked until final. Continues CH1 as L7–12. |
| New Testament Survey 1 | 51 | Complete 99% | Unlocked | L1–L6 full Q&A; complete; certificate unlocked; course total 99% (John was 90%). |
| New Testament Survey 2 | 55 | Complete 94% | Locked (no cert module) | L7–L12 full Q&A (L9 60%, L10–11 90%, L12 100%). |
| Survey of Basic Christian Life 2 | 59 | Complete 100% | Unlocked | L7–L12 full Q&A. Course total 100%. |
| The Four Gospels | 64 | Complete 94% | Locked (no cert module visible) | L1-L5 + Final Exam. L6 reading reports skipped. |
| Apologetics 1 | 62 | Complete 100% | Unlocked | L1–L6 full Q&A. Course total 100%; certificate unlocked (cmid 2109). |
| Church History 1 | 63 | Complete 98% | Unlocked | L1–L6 full Q&A. Course total 98%; certificate unlocked (cmid 2108). HIS 402. |
