#!/usr/bin/env python3
import json
from pathlib import Path

def q(text, answer, why):
    return {"q": text, "answer": answer, "why": why}

def e(theme, summary):
    return {"theme": theme, "summary": summary}

NOTE = "Question wording reconstructed from session notes."

data = {
  "meta": {
    "title": "GLU Study",
    "student": "Jay-R",
    "updated": "2026-08-29"
  },
  "courses": []
}

# ── OT Survey 1 ──────────────────────────────────────────────
ot = {
  "id": "ot-survey-1",
  "code": 50,
  "title": "Old Testament Survey 1",
  "status": "complete",
  "certificateUnlocked": True,
  "courseTotal": 100,
  "blurb": "From creation’s aftermath to Solomon’s wisdom — the first sweep of Israel’s story, ready for review and preaching.",
  "lessons": [
    {
      "id": "ot-1",
      "number": 1,
      "title": "Introduction to the Old Testament",
      "topic": "Survey overview of OT structure and themes — the story that prepares the way for Christ.",
      "quizScore": 100,
      "quizAttempts": 1,
      "status": "complete",
      "takeaways": [
        "The Old Testament is one unfolding story: creation, covenant, failure, and promise — God preparing a people and a Savior.",
        "It is not a random shelf of books. Law, history, poetry, and prophecy each have a voice, and together they preach the same faithful Lord.",
        "When you preach the OT, watch for covenant, sacrifice, kingship, land, and remnant hope. Every one of those roads runs toward Jesus.",
        "The God of Abraham is not a different God from the Father of our Lord. These pages still form a people for His glory."
      ],
      "introCard": "This lesson is a survey doorway: how the Old Testament is put together, what its big themes are, and why the church still needs it. The quiz is complete at 100%; the full Moodle wording is not in this pack yet.",
      "quiz": [],
      "quizEmpty": "Full Q&A not in this pack — asking Jaira to pull from grade review.",
      "quizEmptyDetail": "Quiz 1 is complete (10/10, 100%). Exact question text was not in this pack. We will not invent stems from memory.",
      "essays": [],
      "essayEmpty": "Essay themes not in this pack yet",
      "essayEmptyDetail": "Waiting on Jaira’s full pack for the Lesson 1 essay prompts."
    },
    {
      "id": "ot-2",
      "number": 2,
      "title": "Noah through Joseph",
      "topic": "Genesis 7–50: after the flood, through Abraham’s family, to Joseph in Egypt.",
      "quizScore": 100,
      "quizAttempts": 1,
      "status": "complete",
      "quizWordingNote": NOTE,
      "takeaways": [
        "After the flood, God does not start from nothing — the Noahic covenant continues the Edenic story with new mercy (and a bow in the cloud).",
        "Babel is judgment and mission at once: confused languages scatter the nations so that one day every tongue will praise the Lord.",
        "Abraham is called so that all families of the earth will be blessed. Christianity, Judaism, and Islam all look back to him — but the gospel keeps the promise through Isaac, not through our shortcuts.",
        "Ishmael is a warning for the pulpit: helping God along is not great faith. Waiting on the promise is.",
        "Isaac and Joseph both preach Christ in type — the beloved son, the one who goes down and is raised up for the saving of many. Rebekah, coming to the son, is a picture of the church.",
        "Job sits early in this world — older than the Greek tragedies — and teaches us to speak of suffering without cheap answers."
      ],
      "quiz": [
        q("The Noahic Covenant was a continuation of the Edenic covenant with added aspects.", "True", "God does not discard the first story; He carries it forward with new terms of mercy after the flood."),
        q("The confusion of languages at the Tower of Babel resulted in the dissemination of people throughout the earth.", "True", "Judgment scattered the nations — the map of the world begins here."),
        q("The Ebla texts, found in Syria and dating to the time of Abraham, indicated that Sodom was a real place.", "True", "The patriarchal stories sit in real geography, not in myth."),
        q("Abraham is identified as the father of three great religions.", "True", "Judaism, Christianity, and Islam all look back to Abraham — preach the promise with that in view."),
        q("When Abraham obeyed God, God gave him the Abrahamic Covenant.", "True", "The covenant meets a man on the road of obedience, not on the sofa of delay."),
        q("The birth of Ishmael showed Abraham’s great faith.", "False", "Ishmael is the fruit of a shortcut. Great faith waits for Isaac."),
        q("Abraham was never outside the will of God.", "False", "Egypt, Hagar, and half-truths about Sarah are in the record. Grace keeps the promise anyway."),
        q("Isaac is a type of the church.", "False", "Isaac is a type of Christ; Rebekah, coming to him, is a type of the church."),
        q("Joseph is a type of the church.", "False", "Joseph is a type of Christ — rejected, suffered, raised to save many (Genesis 50:20)."),
        q("The book of Job was penned soon after the Greek tragedies.", "False", "Job is earlier — before 1400 BC — not a late echo of Greece.")
      ],
      "essays": [
        e("Abraham’s five tests", "Walk the tests as a pastoral map: leave, let Lot choose, refuse Sodom’s spoils, send Ishmael, and offer Isaac. Faith is proven on the road, not in the brochure. Each test asks whether the promise is enough."),
        e("Joseph as a type of Christ", "Beloved of the father, hated by his brothers, sold, falsely accused, raised to the right hand, and the savior of the hungry. Preach the type with a light touch — Joseph points; Jesus fulfills."),
        e("Types in Genesis 24", "Abraham’s servant seeks a bride for the son. Rebekah leaves her world to meet Isaac. It is a quiet picture of the Father sending, the Spirit seeking, and the church coming to Christ.")
      ]
    },
    {
      "id": "ot-3",
      "number": 3,
      "title": "Exodus and the wilderness",
      "topic": "The call of Moses, the offerings of Leviticus, and Moses’ death on Nebo.",
      "quizScore": 100,
      "quizAttempts": 1,
      "status": "complete",
      "takeaways": [
        "Exodus 3–4 is a pastor’s mirror: Moses offers five excuses, and God answers with His name, His presence, and His patience — not with a pep talk.",
        "The five Levitical offerings (burnt, meal, peace, sin, trespass) are not museum pieces. They still preach Christ: whole devotion, daily life, fellowship, guilt, and the wrong we have done to others.",
        "The wilderness is where redeemed people learn to live. Manna, water, and a lingering God train a complaining church.",
        "Moses dies on Nebo for Meribah — he struck the rock. Leaders are not above the Word they preach. The promise still stands; the servant still answers to God."
      ],
      "quiz": [],
      "quizEmpty": "Exact Moodle wording not in this pack — asking Jaira.",
      "quizEmptyDetail": "Quiz 3 is complete (10/10, 100%). Exact true/false stems were not in this pack, so they are not reconstructed here.",
      "essays": [
        e("The call of Moses", "Five excuses, one holy God. Reluctance is not disqualifying if it ends in obedience. The bush still burns for servants who feel too slow of speech."),
        e("The sacrifices", "Burnt, grain/meal, peace, sin, and trespass — five windows on the cross. Use them to teach worship, fellowship, and atonement without flattening every detail into an allegory."),
        e("Moses’ untimely death", "Meribah: he struck the rock and misrepresented God. Nebo is grace and grief together — he sees the land he will not enter. Authority in ministry is a trust, not a trophy.")
      ]
    },
    {
      "id": "ot-4",
      "number": 4,
      "title": "Joshua and Judges",
      "topic": "Victory and fulfillment in Joshua; the cycle of compromise in Judges; Ruth’s redemption.",
      "quizScore": 100,
      "quizAttempts": 1,
      "status": "complete",
      "quizWordingNote": NOTE,
      "takeaways": [
        "Joshua’s theme is fulfillment and victory — God keeping the land-promise. Judges’ theme is the warning against compromise. Do not swap the banners.",
        "Rahab is spared. Faith can hang a scarlet cord in a collapsing city. The gospel has always made room for unlikely family.",
        "Caleb asks for Hebron at eighty-five. Age is not a disqualification when the promise still stands.",
        "The judges are not stained-glass saints. God delivers through imperfect people — and the refrain “everyone did what was right in his own eyes” still preaches.",
        "Ruth teaches the doctrine of redemption: a kinsman who can, who will, and who pays. Boaz is a window; Christ is the door.",
        "Incomplete obedience in Joshua becomes next generation’s snare. Finish the work God actually assigned."
      ],
      "quiz": [
        q("The theme of Joshua is a warning against compromise.", "False", "That warning belongs to Judges. Joshua is fulfillment and victory."),
        q("Israel entered a death pact of capital punishment.", "True", "Joshua 1:18 — whoever rebels against the command shall be put to death. The conquest is not casual."),
        q("Rahab was executed by stoning.", "False", "Rahab was spared. Faith brought her into Israel’s story — and into Messiah’s line."),
        q("The altar on Mount Ebal was built of precision-cut stone.", "False", "It was uncut stones. Worship is received, not manufactured to our taste."),
        q("Caleb conquered Hebron at the age of 85.", "True", "A whole heart at eighty-five still takes mountains."),
        q("The author of Judges was Moses.", "False", "Samuel is identified as the author, not Moses."),
        q("The judges were all men of uncompromising character.", "False", "The book’s theme includes their imperfections. God uses cracked vessels."),
        q("Gideon was the most inferior of his father’s house.", "True", "God delights to save through the least, so the glory stays His."),
        q("Samson was a Nazarite.", "True", "Set apart from the womb — and still a warning about wasted strength."),
        q("The book of Ruth teaches the doctrine of redemption.", "True", "The kinsman-redeemer is the pastoral heart of the story.")
      ],
      "essays": [
        e("Ai", "Jericho’s victory, then Ai’s defeat — hidden sin in the camp, overconfidence, and a God who will not be used. Restoration comes through confession and a second, obedient battle."),
        e("Gideon", "The least in his house, too many soldiers, a fleece, and a God who reduces the army so Israel cannot boast. Courage is not the absence of fear; it is obedience with trembling."),
        e("Ruth, Boaz, and the kinsman-redeemer", "Nearness, ability, willingness, and the public price. Preach redemption as personal and costly — then name the greater Boaz.")
      ]
    },
    {
      "id": "ot-5",
      "number": 5,
      "title": "Saul and David",
      "topic": "From failing judges to a king like the nations — then a shepherd after God’s heart.",
      "quizScore": 100,
      "quizAttempts": 1,
      "status": "complete",
      "quizWordingNote": NOTE,
      "takeaways": [
        "The line of the judges grows weaker while the oppressors grow stronger. When leadership thins, God’s people start asking for a king like everybody else.",
        "Samuel is prophet, priest, and judge — not king. Keep the offices straight when you preach 1 Samuel.",
        "Saul looks the part and lives by excuses. Appearance is not anointing. A congregation can want a tall king and still miss God’s man.",
        "David is anointed long before Saul dies. God’s choice often runs ahead of the public calendar.",
        "David ruled forty years — and he sinned. Greatness in Scripture includes repentance, not a clean press kit. The Davidic covenant still points to a forever King.",
        "The witch of Endor is not a curiosity for Halloween sermons. It is a man at the end of himself, and even the darkness shrieks."
      ],
      "quiz": [
        q("Each judge became weaker, while the oppressors became stronger.", "True", "The book winds down; the need for a true king winds up."),
        q("Eli was a strong, disciplined leader.", "False", "Eli’s house is a study in indulgence, not discipline."),
        q("Samuel was prophet, priest, and king.", "False", "Prophet, priest, and judge — not king. The crown is not his."),
        q("Israel wanted a king so they could be like the other nations.", "True", "The motive is conformity, not covenant. That still preaches."),
        q("Saul had many excuses.", "True", "Blame-shifting is the soundtrack of a rejected king."),
        q("Whether Saul was saved or lost is debated.", "True", "Hold the debate humbly; do not build a whole system on a silence."),
        q("David was anointed as soon as Saul died.", "False", "David was anointed earlier, while Saul still sat on the throne."),
        q("The witch of Endor was delighted.", "False", "She shrieked. This is terror, not a séance souvenir."),
        q("David ruled for 40 years.", "True", "Forty years of real reign — triumph, sin, and covenant mercy."),
        q("David never sinned.", "False", "Bathsheba, Uriah, the census — and a psalm of repentance. Preach the whole man.")
      ],
      "essays": [
        e("Samuel", "The last judge, a praying prophet, a disappointed mentor to Saul, and the anointer of David. Leadership that listens to God outlasts leadership that listens to the crowd."),
        e("Was Saul saved or lost?", "The text leaves room for debate. Use it to teach holy caution: fruit, obedience, and the danger of a heart that will not return — without pretending we sit in the final chair of judgment."),
        e("David’s greatness and the Davidic covenant", "A shepherd, a singer, a sinner, a king. 2 Samuel 7 is sermon gold: God builds the house. The forever throne is not David’s achievement; it is God’s promise, kept in Christ.")
      ]
    },
    {
      "id": "ot-6",
      "number": 6,
      "title": "Solomon and the poetic books",
      "topic": "Wisdom on the throne, a temple raised, and the poetry that teaches us to live and to pray.",
      "quizScore": 100,
      "quizAttempts": 1,
      "status": "complete",
      "quizWordingNote": NOTE,
      "takeaways": [
        "God offered Solomon anything in a dream — and wisdom was the right ask. Gifts still reveal what we think a throne is for.",
        "Solomon wrote three books and still drifted. A divided heart can preach Proverbs in the morning and gather horses by night.",
        "Job asks what suffering is for. Psalms give the church a voice. Proverbs is skill for ordinary Tuesdays. Ecclesiastes says life without God is vanity. Song of Solomon is communion, not Ecclesiastes wearing cologne.",
        "Not all the Psalms are David’s, and their themes walk in step with the Torah’s movement. Use that when you plan a series.",
        "There is more than one kind of biblical poetry. Read laments as laments, wisdom as wisdom, and love songs as love songs.",
        "Adonijah’s rebellion and death are a hard footnote: the kingdom is not seized; it is given."
      ],
      "quiz": [
        q("Job explains the purpose of suffering.", "True", "Not every why is answered, but the book will not let suffering be meaningless or cruelly simple."),
        q("Ecclesiastes explains communion with God.", "False", "Communion is the Song of Solomon. Ecclesiastes asks about purpose — and finds vanity under the sun."),
        q("There is more than one type of poetry in the Bible.", "True", "The course names four types. Do not flatten the Psalter into one mood."),
        q("All of the Psalms were written by David.", "False", "David wrote many, not all. Asaph, the sons of Korah, Moses, and others also sing."),
        q("The themes of the Psalms reflect the progression of the Torah.", "True", "The five books of Psalms walk with the five books of Moses — a gift for series preaching."),
        q("God offered Solomon anything in a dream.", "True", "1 Kings 3. What we would ask still reveals us."),
        q("Adonijah was executed for rebellion.", "True", "The kingdom is not taken by a feast and a claim."),
        q("Solomon wrote three books.", "True", "Proverbs, Ecclesiastes, and Song of Songs — wisdom’s three notes."),
        q("Proverbs emphasizes principles for everyday life.", "True", "Street-level holiness: tongue, work, friends, anger, and the fear of the Lord."),
        q("Ecclesiastes teaches that life without God is vanity, and the search is endless.", "True", "Under the sun, the well is empty. Preach it to restless people, then walk them back to the fear of God.")
      ],
      "essays": [
        e("Four types of poetry", "Name the kinds and read each on its own terms — so a lament is not preached as a pep talk, and a proverb is not treated like a legal promise."),
        e("Psalms and the Torah in parallel", "Five movements matching five books. Creation and walk, deliverance, holiness, wilderness, and homecoming — a ready skeleton for a Psalter series."),
        e("Solomon: greatness, strengths, and weaknesses", "Wisdom, temple, international glory — and multiplied horses, wives, and a heart turned. Gifts without a guarded heart become a slow funeral. Christ is the greater Son of David who does not drift.")
      ]
    }
  ]
}

# ── Theology 1 ───────────────────────────────────────────────
th = {
  "id": "theology-1",
  "code": 52,
  "title": "Survey of Theology 1",
  "status": "complete",
  "certificateUnlocked": True,
  "courseTotal": 100,
  "blurb": "From prolegomena to the Person of Christ — doctrine that helps a pastor worship, preach, and care for the flock.",
  "lessons": [
    {
      "id": "th-1",
      "number": 1,
      "title": "Introduction — belief about God / prolegomena",
      "topic": "The Bible’s story, what doctrine is for, and the blueprint that goes before the rest of theology.",
      "quizScore": 100,
      "quizAttempts": 1,
      "status": "complete",
      "takeaways": [
        "The Bible is 66 books, many authors, about 1,600 years — and one story: God revealing Himself and redeeming people (Hebrews 1:1–2). Christianity is Jesus Christ.",
        "Doctrine is not a cold hobby. It is teaching that meets people at the point of need — a wrench that actually turns, not a trophy on the shelf.",
        "The gospel is good news as a proposition (Christ died, was buried, rose — 1 Corinthians 15) and as a Person received (John 1:12). Do not separate relationship from truth.",
        "Prolegomena means “the word that goes before” — the blueprint. We assume God exists and speaks, that truth does not contradict itself, and that the last step of communication is worship (John 4:24).",
        "Test doctrine by consistency, correspondence, relevance, Christ’s centrality, and thoroughness. Towns maps eleven divisions, not twenty-two."
      ],
      "quiz": [
        q("The Bible is made up of 77 books.", "False", "Sixty-six books. Do not let a number error become a pulpit error."),
        q("Christian doctrine speaks to the point of need.", "True", "Theology that never lands in a life is not yet ready to preach."),
        q("God’s greatest way to communicate was through His Son.", "True", "Hebrews 1 — the final Word is a Person."),
        q("The first step in communication between God and man is worship.", "False", "Worship is the final step, not the first. We hear, then we bow."),
        q("The content of Christian doctrine is God’s good news.", "True", "Doctrine carries the gospel; it is not a rival to the gospel."),
        q("Prolegomena means “to go before.”", "True", "It is the porch of the house — what must be said before the rooms."),
        q("A presupposition is a self-evident truth.", "True", "We all start somewhere. Name your starting place honestly."),
        q("The first presupposition is that there is a God who has revealed Himself.", "True", "We do not guess God into being; He speaks."),
        q("The first test used to verify doctrine is reliable eyewitnesses.", "False", "The first test is consistency. Eyewitnesses matter, but they are not the first sieve here."),
        q("Dr. Towns sees 22 divisions of theology and doctrine.", "False", "Eleven divisions: from prolegomena through eschatology.")
      ],
      "essays": [
        e("Prolegomena", "The word that goes before: God exists and reveals Himself; laws are constant; we can know what we observe; truth does not contradict itself; the mind receives what is logical. Build the house on that porch."),
        e("Five tests of doctrine", "Consistency, correspondence to reality, relevance to need, centrality of Christ, and thoroughness. A sermon can be clever and still fail these tests."),
        e("Eleven divisions of theology", "Prolegomena, bibliology, theology proper, Christology, pneumatology, anthropology, hamartiology, soteriology, angelology, ecclesiology, eschatology — a map so you do not preach only your favorite room.")
      ]
    },
    {
      "id": "th-2",
      "number": 2,
      "title": "Contents of the Bible",
      "topic": "Revelation, inspiration, inerrancy, and the eight words for how we handle Scripture.",
      "quizScore": 100,
      "quizAttempts": 1,
      "status": "complete",
      "quizWordingNote": NOTE,
      "takeaways": [
        "Eight words keep a pastor honest with the Book: revelation, inspiration, inerrancy, preservation, canonicity, illumination, interpretation, application.",
        "Revelation is God unveiling Himself — not merely handing us ideas. General revelation (nature, conscience, history) and special revelation (Scripture and Christ) both matter, and they are not the same gift.",
        "Inspiration (theopneustos, God-breathed) is the Spirit guiding the writing. Revelation gives the truth; inspiration guards the writing. Mix them up and you will preach fog.",
        "We trust this Book because it uniquely reveals Christ, says “Thus saith the Lord” more than a thousand times, carries fulfilled prophecy (the Dead Sea Scrolls still preach), converts sinners, and tells the truth about its heroes’ sins.",
        "Illumination is the Spirit helping us understand; application is actually doing the Word (James 1:22). Interpretation without obedience is unfinished discipleship."
      ],
      "quiz": [
        q("The redemption message meets the needs of sinful men.", "True", "The Bible is not a riddle for the clever; it is rescue for the guilty."),
        q("Inerrancy means the Bible is accurate, reliable, authoritative, and without error.", "True", "A high view of Scripture is a pastoral comfort, not a hobbyhorse."),
        q("The Bible is essentially a story of thoughts about God.", "False", "It is a record of God’s acts — He does, then He speaks."),
        q("Revelation means God unveils Himself to His people.", "True", "God is not a puzzle we invented; He pulls back the veil."),
        q("There is general revelation and special (specific) revelation.", "True", "The sky preaches; the Son and the Scriptures save and specify."),
        q("The Bible is God’s Word because of the unique revelation of Christ.", "True", "The Book’s center is a Person."),
        q("God’s truthfulness would demand that He remain incognito.", "False", "Because He is true, He reveals Himself. Hiddenness is not His last word."),
        q("Over 1,000 times the authors claim the message is from God.", "True", "“Thus saith the Lord” is not a decoration; it is a claim."),
        q("The Dead Sea Scrolls show that prophecies pre-date their fulfillment.", "True", "The promise was written before the empty tomb, not after."),
        q("Each book was written by a human author guided by the Holy Spirit.", "True", "Real men, real style, one divine Author.")
      ],
      "essays": [
        e("Fourteen methods of revelation", "Visions, dreams, nature, biography, sermons, face to face, writing on stone, object lessons, parables, inner compulsion, history, angels, research, and Jesus Himself — God is not limited to one microphone."),
        e("The unity of Scripture despite many authors", "About forty writers across about 1,600 years, and one story. That unity is itself a reason to trust, and a reason to preach the whole counsel."),
        e("Christ’s deity claims — liar, lunatic, or Lord", "He does not leave us the option of a merely nice teacher. The claims force a decision; the pulpit should too.")
      ]
    },
    {
      "id": "th-3",
      "number": 3,
      "title": "Accuracy and inspiration of Scripture",
      "topic": "God-breathed words, inerrancy, faulty theories, and a closed canon.",
      "quizScore": 100,
      "quizAttempts": 1,
      "status": "complete",
      "quizWordingNote": NOTE,
      "takeaways": [
        "Inspiration is the Spirit’s superintending work so that writers wrote what God wanted, without error. Theopneustos in 2 Timothy 3:16 means God-breathed — life in the words.",
        "Four qualities to keep straight: inspired men (borne along, 2 Peter 1:21), inspired writers (God used personality and style), inspired words (verbal, not ideas only), inspired results (inerrancy and authority).",
        "Name the faulty views so you can smell them in a conversation: intuition, conceptual, illumination-only, partial, limited (“only the religious bits”), dictation, and KJV-only inspiration of a translation.",
        "We hold inerrancy because Scripture claims it, Jesus treated it as final truth (“It is written”), and God cannot lie. Reliability is also backed by history, archaeology, and prophecy.",
        "The autographs are gone; thousands of manuscripts remain. Textual criticism, rightly used, aims to recover the original wording — not to unseat the Word."
      ],
      "quiz": [
        q("The word theopneustos appears in 2 Timothy 3:16.", "True", "God-breathed. That one word carries a pulpit’s confidence."),
        q("The author was guided to write what God wanted.", "True", "Superintendence, not religious guesswork."),
        q("God gave the thoughts but not the words.", "False", "Verbal inspiration: the words matter, not only the vibe."),
        q("Conceptual inspiration means God inspired the ideas.", "True", "That is a real view — and a faulty one. Ideas without words will not hold a church."),
        q("Limited inspiration means Scripture is authoritative only in religious dogma.", "True", "George Eldon Ladd’s kind of limit. It carves the Bible into “safe” and “skippable.”"),
        q("Some dismiss passages as morally objectionable.", "True", "People still edit God. The pastor’s job is not to help them."),
        q("The prophets never claimed to speak the words of God.", "False", "They claimed it constantly. That is why “thus saith the Lord” lands with weight."),
        q("Jesus appealed to the authority of the Word as final truth.", "True", "“It is written” is how the Lord Himself argued."),
        q("Parts of Daniel are in Chaldean.", "True", "The Book is at home in history and language, not in a fog."),
        q("Textual criticism aims to recover the wording of the autographs.", "True", "A servant task: get back to what was written, not replace it.")
      ],
      "essays": [
        e("Definition and four qualities of inspiration", "Men borne along, writers as themselves, words as God’s, results as inerrant and authoritative. Keep all four or the doctrine tilts."),
        e("The Bible’s own arguments for inerrancy", "Self-witness, the character of God, and the Lord’s own use of Scripture. We do not prop the Book up with mood; it claims what it is."),
        e("How Jesus treated Scripture", "He quoted it as final, lived under it, and fulfilled it. A church that shrugs at the Book is not following this Jesus.")
      ]
    },
    {
      "id": "th-4",
      "number": 4,
      "title": "Nature of God",
      "topic": "God’s nature and attributes — and the wrong views that quietly wreck a Christian life.",
      "quizScore": 100,
      "quizAttempts": 1,
      "status": "complete",
      "takeaways": [
        "A wrong view of God always multiplies problems in daily Christian living (Tozer). What you believe about God will leak into prayer, marriage, money, and preaching.",
        "Nature is who God is; attributes are the rays of that sun. Do not preach attributes as spare parts you can rearrange.",
        "Seven terms for His nature: Spirit, Person, Life, self-existent, immutable, unlimited by time and space, and unity — one God. The Trinity is not three gods.",
        "Holiness, love, and goodness are absolute attributes (God alone in that fullness). Omniscience, omnipresence, and omnipotence are comparative — we have a drop; He has the sea.",
        "God has never learned. He is present everywhere at all times. Omnipotence still has limits of character: He cannot lie, sin, or stop being who He is.",
        "Most religions paint God as an impersonal force. The gospel gives us a living Lord with intellect, emotion, and will."
      ],
      "quiz": [
        q("The wrong view of God will always cause a multitude of problems in the daily life of a Christian.", "True", "Theology leaks. Bad doctrine makes anxious disciples."),
        q("While the nature of God defines His existence, the attributes of God reflect His nature.", "True", "The sun and its light — do not confuse them, and do not divide them."),
        q("The term “personal” when used to define God means that He is immaterial, incorporeal, and invisible.", "False", "That describes God as Spirit. Personal means intellect, emotion, and will."),
        q("Most religions of the world portray God as an impersonal being or force.", "True", "The gospel is startling: God speaks, loves, and comes near."),
        q("God is the source of all life.", "True", "We do not lend Him breath; He lends us ours."),
        q("God is limited in space and time.", "False", "He is not a larger creature. He fills heaven and earth."),
        q("Holiness, love, and goodness are comparative attributes of God.", "False", "They are absolute. Comparative attributes are omniscience, omnipresence, omnipotence."),
        q("Love is the opposite of selfishness.", "True", "Preach love as holy self-giving, not as sentiment."),
        q("God has never learned.", "True", "Omniscience is not a good student; it is a perfect mind."),
        q("God is present everywhere at all times.", "True", "Omnipresence is comfort for the hospital room and warning for the secret sin.")
      ],
      "essays": [
        e("God is Spirit", "Immaterial, invisible, living. We worship in spirit and truth because He is not a statue and not a mood."),
        e("Eleven erroneous views of God", "Atheism, agnosticism, materialism, animism, polytheism, henotheism, tritheism, dualism, pantheism, idealism, deism — a pastoral checklist for the ideas already sitting in the pews."),
        e("Six principal attributes", "Absolute: holiness, love, goodness. Comparative: omniscience, omnipresence, omnipotence. Keep the pairs straight when you teach.")
      ]
    },
    {
      "id": "th-5",
      "number": 5,
      "title": "The Trinity and the works of God",
      "topic": "One God in three Persons, the law of God, decrees, and the three primary names.",
      "quizScore": 100,
      "quizAttempts": 1,
      "status": "complete",
      "takeaways": [
        "The members of the Trinity are equal in nature, distinct in person, and subordinate in duties. We worship one God, not three. Tritheism and modalism both miss the glory.",
        "The word Trinity is not in the Bible; the truth is. The Old Testament points (Elohim, “let Us,” holy-holy-holy). The New Testament shows it in the open at Jesus’ baptism.",
        "Works that only God can do involve all three Persons — creation, the cross, the resurrection, inspiration, indwelling. Never preach a Lone Ranger God.",
        "The law reflects God’s attributes. The rule of law presupposes objective truth. Pantheism turns God into an inanimate force in nature; Scripture will not.",
        "God has revealed three primary names in the Old Testament, not six: Elohim, Jehovah (Yahweh), and Adonai. Names are revelation, not nicknames.",
        "Calvinistic language about decrees stresses that they are all-encompassing. Handle the mystery with worship: God rules, and we remain accountable."
      ],
      "quiz": [
        q("The members of the Trinity are equal in nature, distinct in person, and subordinate in duties.", "True", "Equal in deity; distinct in person; ordered in mission. Hold all three lines."),
        q("The Trinity means three Gods.", "False", "Christians are monotheists. Hear, O Israel: the LORD is one."),
        q("The Old Testament points to the Trinity.", "True", "Hints and plural unity — not a full Nicene paragraph, but not silence either."),
        q("The Trinity was revealed at the baptism of Jesus.", "True", "The Son in the water, the Spirit as a dove, the Father’s voice. Go to the Jordan."),
        q("All three persons of divinity are involved in works that only God can do.", "True", "Creation, Calvary, and new birth are triune works."),
        q("The law is a reflection of God’s attributes.", "True", "Holy, just, and good — because He is."),
        q("The “rule of law,” by its very nature, presupposes objective truth for it to be reliable to rightly order society.", "True", "If law is only power, the strongest always wins."),
        q("Pantheism is the ideology teaching that God is an inanimate force within nature and controls all things through the laws of nature.", "True", "Pantheism dissolves the distinction between Creator and creation."),
        q("The Calvinistic understanding of decrees teaches that they are all-encompassing because they control everything that comes to pass.", "True", "That is the claim of that tradition. Teach it accurately even when you linger over the mystery."),
        q("God has revealed His six primary names in the Old Testament.", "False", "Three primary names: Elohim, Jehovah, Adonai.")
      ],
      "essays": [
        e("What is the Trinity?", "One divine nature, three real Persons — Father, Son, and Spirit — neither confounding the persons nor dividing the substance. Use the baptism, the benediction, and the Great Commission."),
        e("Biblical words for decree", "Predestine, foreknowledge, elect, call, purpose, will, counsel, good pleasure. The vocabulary is worship language before it is a debate team."),
        e("Three primary names", "Elohim (the strong God, plural majesty), Jehovah/Yahweh (I AM, the covenant Name), Adonai (Master). Capitalization in the KJV is a preaching tool if you explain it.")
      ]
    },
    {
      "id": "th-6",
      "number": 6,
      "title": "The Person of Christ",
      "topic": "The Son’s deity, eternal generation, offices, virgin birth, kenosis, and hypostatic union.",
      "quizScore": 100,
      "quizAttempts": 1,
      "status": "complete",
      "takeaways": [
        "Jesus is the second Person of the Trinity — equal with the Father in essence, subordinate in office as the Sent One. He accepted worship. The New Testament ascribes creation to Him.",
        "Eternal generation: He has always been the Son. He did not become Son at baptism or resurrection. Christophanies are pre-incarnate appearances (the Angel of the LORD).",
        "Three anointed offices: Prophet (speaks), Priest (sacrifice and intercession), King. Oil pictures the Spirit; Christ means Anointed One. Do not give the priest’s work to the prophet.",
        "The virgin birth is necessary for His sinlessness (Genesis 3:15; Isaiah 7:14). Liberal theology does not require it; the gospel does. Joseph was not His biological father.",
        "Kenosis (Philippians 2:7) is self-emptying: veiled glory, accepted human limits, surrendered independent use of comparative attributes — not a surrender of deity.",
        "Hypostatic union (Chalcedon): one Person, two natures, fully God and fully man, without mixture or separation. Tempted for real, yet without sin. That is the Christ we preach."
      ],
      "quiz": [
        q("Jesus never allowed people to worship Him.", "False", "He received worship. A mere rabbi would have stopped it."),
        q("The New Testament authors ascribe the work of creation to Christ.", "True", "John 1:3; Colossians 1:16 — the carpenter is the Maker."),
        q("Jesus has always been the Son of God.", "True", "Eternal Sonship. The manger is not His beginning."),
        q("A Christophany was a pre-incarnate appearance of Jesus Christ.", "True", "The Angel of the LORD is not a footnote; it is the Son before Bethlehem."),
        q("The three anointed offices of Jesus Christ are prophet, priest, and king.", "True", "Speak, sacrifice, reign — the whole Christ for the whole church."),
        q("The prophet fulfilled his office by offering sacrifices and making intercession.", "False", "That is the priest. Keep the offices clean in the pulpit."),
        q("Even those embracing a liberal theological posture affirm the absolute necessity of believing in the virgin birth of Jesus Christ.", "False", "Liberalism often shrugs. We cannot."),
        q("Jesus was the biological son of his father, Joseph.", "False", "Joseph is legal father, not biological. The conception is of the Holy Spirit."),
        q("Part of Jesus’ self-emptying was His surrender of the independent use of His comparative attributes.", "True", "Kenosis is veiling and dependence, not subtraction of deity."),
        q("Jesus is totally God and totally human at the same time.", "True", "One Person, two natures. If either is lost, so is our salvation.")
      ],
      "essays": [
        e("Threefold offices", "Prophet to our ignorance, Priest to our guilt, King to our rebellion. Preach all three or the congregation gets a partial Jesus."),
        e("False views of kenosis", "He did not empty Himself of being God. He veiled glory, took servant form, and refused independent use of attributes that are His by nature."),
        e("Biblical testimony for the virgin birth", "Genesis 3:15, Isaiah 7:14, the infancy narratives, and the need for a sinless last Adam. This is gospel structure, not seasonal decoration.")
      ]
    }
  ]
}

# ── NT Survey 1 ──────────────────────────────────────────────
nt = {
  "id": "nt-survey-1",
  "code": 51,
  "title": "New Testament Survey 1",
  "status": "in-progress",
  "certificateUnlocked": False,
  "blurb": "The silent years, four portraits of one Lord, and the church on mission — Lessons 1–4 complete; John and Acts still on the desk.",
  "lessons": [
    {
      "id": "nt-1",
      "number": 1,
      "title": "Introduction to the New Testament",
      "topic": "Four Gospels at a glance, the 400 silent years, and a world prepared for the Savior.",
      "quizScore": 100,
      "quizAttempts": 1,
      "status": "complete",
      "takeaways": [
        "The Old Testament is the New Testament concealed; the New Testament is the Old Testament revealed. Everything points to Christ (Luke 24:44).",
        "Gospel means good news. The four Gospels are persuasive histories written by the evangelists — Jesus did not write them, and we do not need Him to have written them in order to trust them.",
        "Matthew: tax collector, Jew, apostle — to the Jews — Christ as King — key word Kingdom — Lion. Mark: with Peter — to Romans — Christ as Servant — immediately — Ox. Luke: physician, Greek, with Paul — to Greeks — perfect Man — Son of Man — Man. John: fisherman, apostle — to the whole world — Christ is God — believe and life — Eagle.",
        "The 400 silent years were not empty years: Babylon, Persia, Greece (Septuagint, 285 BC, Hebrew into Greek), Maccabees, Rome. Herod was crowned by Julius Caesar. Pax Romana paved roads for preachers.",
        "Pharisees (“to separate”) and Sadducees stood opposite each other. It was the Sadducees who denied the supernatural — a detail that still saves you from mixing the parties in a sermon."
      ],
      "figure": {
        "caption": "Four Gospels at a glance",
        "headers": ["Gospel", "Author", "Audience", "Theme", "Key word", "Symbol"],
        "rows": [
          ["Matthew", "Tax collector, Jew, apostle", "Jews", "Christ as King", "Kingdom", "Lion"],
          ["Mark", "Jew/Roman, with Peter", "Romans", "Christ as Servant", "immediately", "Ox"],
          ["Luke", "Physician, Greek, with Paul", "Greeks", "Christ as perfect Man", "Son of Man", "Man"],
          ["John", "Fisherman, Jew, apostle", "Whole world", "Christ is God", "believe / life", "Eagle"]
        ]
      },
      "quiz": [
        q("Jesus wrote the New Testament.", "False", "The evangelists wrote the Gospels. Jesus is the subject, not the scribe."),
        q("Everything in the Gospels points to Jesus.", "True", "Luke 24:44 — law, prophets, and psalms find their yes in Him."),
        q("Matthew was a doctor.", "False", "Luke is the beloved physician. Matthew was a tax collector."),
        q("The key word in Matthew is Kingdom.", "True", "The King and His kingdom — that is Matthew’s drumbeat."),
        q("John was written to the entire world.", "True", "Not a house newsletter. “Whoever believes” is the horizon."),
        q("John includes the greatest number of parables.", "False", "John has none of the Synoptic parables. Luke has the most."),
        q("Luke is the most Jewish-oriented Gospel.", "False", "Matthew is the most Jewish Gospel. Luke writes with Greeks in view."),
        q("The Septuagint is the Hebrew Bible translated into Greek.", "True", "About 285 BC — God preparing a Greek-speaking world for a Greek New Testament."),
        q("Herod was crowned by Julius Caesar.", "True", "Rome’s politics become the cradle of the nativity story."),
        q("The Pharisees denied the supernatural.", "False", "The Sadducees denied the supernatural. Keep the parties straight.")
      ],
      "essays": [
        e("Four authors and their audiences", "Matthew to Jews (King), Mark to Romans (Servant), Luke to Greeks (perfect Man), John to the world (God the Son). Audience shapes emphasis without splitting Jesus into four."),
        e("Key word, verse, symbol, and emphasis compared", "Kingdom / Lion; immediately / Ox; Son of Man / Man; believe and life / Eagle. One Lord, four faithful portraits — preach them as harmony, not as rivals."),
        e("Seven course objectives", "A survey’s aim: know the lay of the land, the writers, the silent years, and how each book serves Christ and the church. Use the objectives as a checklist when you review.")
      ]
    },
    {
      "id": "nt-2",
      "number": 2,
      "title": "Matthew",
      "topic": "The most Jewish Gospel: Jesus the predicted King, the Baptist, the Mount, and the road to the cross.",
      "quizScore": 100,
      "quizAttempts": 1,
      "status": "complete",
      "takeaways": [
        "Matthew, the former tax collector, writes the most Jewish Gospel: Jesus is the promised King and Messiah. Key verse: Matthew 2:2 — “Where is He who has been born King of the Jews?”",
        "The wise men’s request threatened Herod. History has never agreed on the star. You can preach the worship without pretending the astronomy is settled.",
        "John the Baptist fulfills Isaiah. The high point of his ministry is baptizing Jesus — the Trinity at the Jordan, not the biggest crowd.",
        "Matthew’s own call was immediate and influenced others. Following Jesus in public still makes room for other feet.",
        "The Sermon on the Mount travels across culture and time. To bless is to add value to another’s life. The believer’s ultimate authority is God’s planned purpose — not mood, not majority.",
        "Expect opposition (Matthew 10). Jesus predicted His death and resurrection about twenty times, not three. The cross was not a surprise ending."
      ],
      "quiz": [
        q("The wise men’s request to see the baby born “King of the Jews” threatened Herod.", "True", "A rival king in Bethlehem is a political emergency in Jerusalem."),
        q("History has been in total agreement concerning the star which guided the worshippers to Jesus.", "False", "The star’s identity is disputed. Worship is not. Hold the story with honesty."),
        q("John the Baptist’s preaching fulfilled an Old Testament prediction.", "True", "Isaiah’s voice in the wilderness becomes flesh and locusts."),
        q("The high point of John the Baptist’s ministry was baptizing Jesus.", "True", "He must increase. The Jordan, not the crowds, is the peak."),
        q("Matthew’s willingness to follow Jesus influenced others to do the same.", "True", "Obedience is contagious. So is delay."),
        q("The Sermon on the Mount contains principles that can be applied across culture and across time.", "True", "Amazement, authority, and real happiness — not a first-century museum."),
        q("To “bless” means to add value to another’s life.", "True", "Blessing is not thin words; it is real good done to a real neighbor."),
        q("The planned purpose of God is the believer’s ultimate authority for life.", "True", "Not the loudest opinion in the room."),
        q("It is easier to endure when we are unaware of the opposition to our faith.", "False", "Jesus tells the truth about opposition so we can stand, not so we can nap."),
        q("Jesus only predicted His death and resurrection three times before He was actually crucified.", "False", "About twenty times — the cross was announced, not improvised.")
      ],
      "essays": [
        e("Who was John the Baptist?", "Wilderness prophet, Isaiah’s voice, forerunner, and the man who got to lower the King into the water. His joy was to decrease."),
        e("Seven questions and three principles from the Sermon on the Mount", "The sermon still asks how we live before the Father who sees in secret. Carry amazement at Jesus’ authority, the shape of true happiness, and a life aimed at God’s purpose."),
        e("Eight insights from Matthew 10", "Mission is not a picnic. Jesus prepares disciples for opposition, dependence, and courage. Negative preparation is still love.")
      ]
    },
    {
      "id": "nt-3",
      "number": 3,
      "title": "Mark",
      "topic": "John Mark, Peter’s interpreter, and the gospel of the Servant — immediately.",
      "quizScore": 100,
      "quizAttempts": 1,
      "status": "complete",
      "takeaways": [
        "Mark (John Marcus), Barnabas’ nephew, likely the young man who fled naked, wrote from Peter’s testimony. A restored helper can still write Scripture’s shortest Gospel.",
        "Mark presents Jesus as Servant in a gospel of deeds. Key verse: Mark 10:45. Key word: immediately. No genealogy, no birth narrative — a servant does not hand you a résumé.",
        "The “Long Day” (Mark 3:12–5:43) is packed with about ten events. It shows Jesus’ humanity and weariness. He is in control of Himself, not always of His circumstances.",
        "During that long day He preached a sermon with eight parables. His family did not demonstrate total support. Ministry can be lonely in your own house.",
        "The day ends with two contrasting miracles: the woman with the issue of blood and Jairus’ daughter — a long hemorrhage and a short life, both met by the Servant.",
        "Mark 4’s soils still preach: wayside, stony, thorns, good ground. The issue is not the Sower’s skill only; it is the heart that hears."
      ],
      "quiz": [
        q("Mark, only a boy during the ministry of Christ, wrote from the testimony of Peter.", "True", "Peter’s interpreter. Eyewitness preaching becomes written Gospel."),
        q("Mark was Barnabas’ nephew.", "True", "Family, failure at Perga, and later restoration — a pastoral subplot."),
        q("The book of Mark presents Jesus as a servant in a gospel of deeds.", "True", "Action more than speech. The Servant is busy with the Father’s will."),
        q("The key word in Mark is “immediately.”", "True", "Urgency is not hurry for its own sake; it is a Lord on the move."),
        q("The favorite name of the devil/demons for deity is “The Holy One of God.”", "True", "Hell knows His name. The question is whether the church will."),
        q("The “Long Day” in Mark demonstrated that Jesus was tireless.", "False", "It shows His humanity. He grew weary. That is good news for tired pastors."),
        q("Mark points out that Jesus was in control of Himself, but not necessarily His circumstances.", "True", "Self-control under pressure is holiness, not passivity."),
        q("During the “Long Day,” Jesus preached a sermon with eight parables.", "True", "Teaching packed into a crushing schedule — the Servant still opens His mouth."),
        q("During the “Long Day,” Jesus’ family demonstrated total support.", "False", "They misunderstood Him. Faithfulness is not always applauded at home."),
        q("The “Long Day” concludes with miracles where Jesus healed two people with two contrasting problems.", "True", "A twelve-year hemorrhage and a twelve-year-old girl — one Lord for both.")
      ],
      "essays": [
        e("The emphasis of Mark", "Jesus the Servant, deeds over pedigree, immediately, Mark 10:45 as the spine. Preach a Christ who came not to be served but to serve, and to give His life as a ransom."),
        e("Ten events of the Long Day", "A crushing sequence from confrontation to parables to storm to tombs to two healings. Use it to show both the press of need and the real humanity of Jesus."),
        e("The parables of Mark 4", "Four soils, and the company of kingdom parables. Hearing is not automatic. Ask the congregation which soil they are this week.")
      ]
    },
    {
      "id": "nt-4",
      "number": 4,
      "title": "Luke",
      "topic": "The beloved physician, the Son of Man, parables, prayer, and the Savior of the overlooked.",
      "quizScore": 100,
      "quizAttempts": 1,
      "status": "complete",
      "takeaways": [
        "Luke, “the beloved physician” (Colossians 4:14), likely a Gentile, writes careful history to Theophilus. Key word: Son of Man. Key verse: Luke 19:10 — the Son of Man came to seek and to save the lost.",
        "Zacharias and Elizabeth were righteous and still carried the stigma of childlessness. Gabriel (not Michael) announced both John and Jesus. God sees the quiet shame in a good home.",
        "Luke has more parables than any other Gospel. A parable is an earthly story with a heavenly meaning: one interpretation, many applications. Do not turn every detail into an allegory.",
        "Each parable has its own lesson. Miracle is truth in action; parable is truth in story. Use both in the pulpit without confusing them.",
        "The disciples asked to be taught to pray. The Lord’s Prayer is a pattern, not a spell. Prayer in Luke is a school, not a performance.",
        "Luke loves the outsider, the poor, women, and the lost. If your preaching never sounds like that, you are not yet preaching Luke."
      ],
      "quiz": [
        q("Luke’s vocation was that he was a rabbi.", "False", "He was a physician, not a rabbi. Colossians 4:14 still introduces him."),
        q("The key word (term) in Luke is “Son of Man.”", "True", "The human nature of the God-Man is Luke’s open secret."),
        q("Elizabeth had a stigma because she was childless.", "True", "Righteous and still carrying cultural shame. God writes John into that ache."),
        q("The angel Michael told Mary about the coming of Jesus.", "False", "It was Gabriel. Keep the messengers straight."),
        q("There are more parables in Luke than in any other Gospel.", "True", "Luke is a treasure chest for story-shaped preaching."),
        q("A parable is an earthly story with a heavenly meaning.", "True", "Down-to-earth, aimed at heaven — that is the form."),
        q("Each parable has its own lesson.", "True", "Do not mash them into one vague moral."),
        q("A parable has one interpretation, but many applications.", "True", "One center, many landing places. That frees the preacher and guards the text."),
        q("Jesus’ disciples asked Him to teach them to pray.", "True", "They did not ask first to preach. That should humble our seminaries and our Sundays."),
        q("The Lord’s Prayer is considered a model or pattern for praying.", "True", "A pattern to enter, not a formula to mutter.")
      ],
      "essays": [
        e("John’s birth in Luke", "Barren Elizabeth, doubting Zacharias, Gabriel’s word, muteness, and a boy set apart. God begins the Gospel in a priestly home that had stopped expecting."),
        e("Towns on parables", "Earthly story, heavenly meaning; one interpretation, many applications; don’t over-allegorize. A parable is a servant of one main truth."),
        e("The circumstances of Jesus’ birth", "Nazareth unlikely, census under Quirinius, manger, Simeon, growth in four areas (Luke 2:52), and the first recorded words at twelve. The Son of Man enters our mess without a palace.")
      ]
    },
    {
      "id": "nt-5",
      "number": 5,
      "title": "John",
      "topic": "The Gospel of belief and life — in progress; quiz not yet done.",
      "quizScore": None,
      "status": "in-progress",
      "takeaways": [
        "John writes so that we may believe that Jesus is the Christ, the Son of God, and that by believing we may have life. That purpose sentence is a preaching commission.",
        "This Gospel is for the whole world: Christ is God, the key words are believe and life, the symbol is the eagle. It is simple enough for a child and deep enough for a lifetime.",
        "The “I am” sayings and the signs are not decorations. They reveal who Jesus is and what He gives — bread, light, shepherd, resurrection, way, vine.",
        "Notes beyond this doorway are still on the way. Lesson 5 is in progress; the quiz has not been taken. Full Q&A will land when Jaira’s pack does."
      ],
      "quiz": [],
      "quizEmpty": "Waiting on Jaira’s full pack",
      "quizEmptyDetail": "Lesson 5 is in progress. The quiz has not been completed. We will not invent questions or answers.",
      "essays": [],
      "essayEmpty": "Waiting on Jaira’s full pack",
      "essayEmptyDetail": "Essay themes for John will be summarized here after the lesson pack arrives."
    },
    {
      "id": "nt-6",
      "number": 6,
      "title": "Acts",
      "topic": "The risen Lord at work through His church — not started.",
      "quizScore": None,
      "status": "not-started",
      "takeaways": [
        "Acts is Luke’s second volume: Jesus continues His work by the Spirit through the apostles and the church.",
        "The map runs from Jerusalem to the ends of the earth. The gospel crosses cultures because Christ is Lord of all.",
        "The church in Acts preaches, prays, suffers, and multiplies. That pattern is still a mirror for mission, unity, and courage.",
        "This lesson is not started. Full takeaways, quiz, and essays will be folded in when the pack arrives — nothing invented to fill the page."
      ],
      "quiz": [],
      "quizEmpty": "Waiting on Jaira’s full pack",
      "quizEmptyDetail": "Lesson 6 has not been started. Quiz questions will appear here after the pack, not before.",
      "essays": [],
      "essayEmpty": "Waiting on Jaira’s full pack",
      "essayEmptyDetail": "Essay themes for Acts will be summarized when Jaira sends the lesson pack."
    }
  ]
}

data["courses"] = [ot, th, nt]
out = Path("/workspace/glu-study/data/courses.json")
out.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("wrote", out, "bytes", out.stat().st_size, "courses", len(data["courses"]))
for c in data["courses"]:
    print(c["id"], "lessons", len(c["lessons"]), "status", c["status"])
