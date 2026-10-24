# Little Blueprint — Product Requirements Document

**Version:** 2.0 (decision-locked V1)  
**Status:** Source of truth  
**Last updated:** 21 October 2026  
**Replaces:** Vision PRD (full suite: Doula, keepsake book, Babylist, practitioner portal)

---

## 1. One-line product

Little Blueprint is a **parent-only app** that turns a child’s birth time and place into an **inborn sensory, emotional, and learning profile**, plus **word-for-word scripts** for parent–child clashes.

It is not a life-astrology product. It is not a medical product. It is not for the child to use.

**Tagline:** Understand your child’s inborn nature before the world tells them who to be.

---

## 2. Decisions locked

| Decision | Choice |
|---|---|
| Who it is for | Parents / legal guardians of children roughly **0–8 years** |
| Hero usage window | **1–5 years** (tantrums, sleep, sensory, transitions) |
| Newborn-only? | **No.** Newborn is the gift/acquisition moment; toddlers are retention. |
| Adult “know your life”? | **No.** Parent birth data is used only as a **clash mirror**. |
| What we sell | Clarity + tonight’s script, not fate or diagnosis |
| Public language | Parenting / nervous system / learning. **No kundali, dasha, or fortune-telling copy** on parent-facing screens |
| Account holder | Adult 18+ only. Child never creates an account or uses the app |
| V1 geography | English, Tier-1: US, UK, Canada, Australia (Germany later) |

Older research docs (`KINDRED_MASTER_PLAN.md`, `IDEAS.md`) are background. This file wins on product scope.

---

## 3. Problem

Affluent parents in Tier-1 markets are exhausted by one-size-fits-all advice. Child A sleeps; child B screams over sock seams. Gentle-parenting books work on the neighbor’s kid and fail on theirs.

That produces three feelings we design against:

1. **“Is my child broken?”** — fear of ADHD, sensory issues, “too intense”
2. **“I am a terrible parent”** — guilt after losing patience
3. **“Every method fails on *this* kid”** — decision fatigue

Generic leap apps (e.g. Wonder Weeks-style products) add a fourth failure: they warn that a stormy period is coming and give no agency. We do the opposite: **name the wiring, then give a 2-minute action.**

---

## 4. Audience

### Primary buyer
Parent (mostly mothers, ages ~26–42) in US / UK / CA / AU, household income roughly $120k+, already buying Lovevery, Hatch, Nanit, sleep consultants, Montessori toys.

### Jobs to be done
- Decode *this* child’s sensory and emotional wiring
- Know what to say in a tantrum without improvising
- Plan the day around overstimulation, not dread
- Stop blaming themselves for a pacing mismatch with the child

### Not a user
- The child
- Adults seeking career, dating, luck, or “life path”
- Clinicians as the primary customer in V1 (doula portal is later)

---

## 5. Positioning

**We are:** Lovevery-grade parenting utility with a hidden Vedic calculation engine.

**We are not:** Co-Star for babies, a kundali app, a diagnostic tool, or a milestone tracker.

**Engine vs. parent copy**

| Calculation (never the headline) | Parent-facing output |
|---|---|
| Moon Nakshatra (27 lunar mansions) | Emotional nervous system + self-soothe profile |
| 5th house / Mercury (V1: element + learning dictionary) | Learning modality |
| Lagna / Mars / Sun (V1: element + sensory dictionary) | Sensory threshold |
| Parent–child Moon/element pairing | Why you clash + 3-step script |
| Transit Moon (V1: simple daily score) | Today’s stimulation window + ritual |

Parent-facing screens use archetypes (“Sensory Sensor”, “Kinetic Pioneer”), not Nakshatra names, unless we later A/B a discreet “inborn type” label. Astrology vocabulary stays in logs, JSON, and internal admin.

---

## 6. Product principles

1. **Agency over dread.** Never forecast a doomed week. Always attach a doable action.
2. **Scripts over essays.** Exact words beat theory.
3. **Validation without diagnosis.** Reframe intensity; never claim ADHD/autism/SPD yes/no.
4. **Parent chart is a mirror.** No parent horoscope, luck score, or life reading.
5. **Minimum child data.** Nickname, birth date, birth time (optional), birth city. No photos, GPS, medical, or school records.
6. **Calm UI.** Warm oatmeal / terracotta / sage. Montessori, not crystals.

---

## 7. V1 success looks like

A parent can, in one sitting:

1. Enter one child + one parent
2. See a reveal that names the child’s wiring in plain language
3. Read a clash explanation that removes guilt
4. Leave with a script they can use **tonight**
5. Pay for annual access (or start a 3-day trial)

If those five steps work, the product is real. Everything else is amplification.

---

## 8. Scope by phase

### P0 — Must ship to charge money

| ID | Requirement | Notes |
|---|---|---|
| P0-1 | Web quiz funnel | See §9 |
| P0-2 | Child Blueprint | Archetype, sensory, emotion, learning, do-not-do |
| P0-3 | Harmony engine | One parent ↔ one child; score, trigger, 3-step script |
| P0-4 | Crisis scripts | At least 5 situations, profile-aware |
| P0-5 | Daily home | Score 0–100, one caution window, one 2-min ritual |
| P0-6 | Age-aware copy | Bands: 0–12 mo, 1–3 yr, 4–8 yr |
| P0-7 | Unknown birth time | Coarser profile + accuracy note; do not hard-fail |
| P0-8 | Auth (parent only) | Email / Apple / Google; 18+ attestation |
| P0-9 | Billing | 3-day trial → $79.99/yr; monthly $14.99 as anchor |
| P0-10 | Trust layer | Medical disclaimer, privacy, one-tap delete, COPPA posture |
| P0-11 | Language firewall | Block fate/medical/fortune copy in UI and any AI later |

### P1 — Keep them after the quiz (V1.5)

| ID | Requirement |
|---|---|
| P1-1 | Second parent / co-parent share (same child, second harmony) |
| P1-2 | Sibling add-on (+$29/yr) |
| P1-3 | Digital PDF dossier ($39) |
| P1-4 | Doula AI chat, grounded in this child’s JSON + scripts + disclaimer |
| P1-5 | iOS app (Expo) with daily home as default tab |

### P2 — Later (explicitly out of V1)

- Linen keepsake book / Gelato
- Babylist / Amazon registry
- Doula practitioner portal + affiliate
- Germany localization
- School-age extras beyond learning card
- Teen mode
- Push notifications beyond a single daily ritual reminder
- Full dasha / divisional-chart “growth seasons” as a parent-facing module

### Never in this product

- Adult life path, career, wealth, marriage, death
- Dating synastry as a product
- Daily horoscope for the parent
- Child-facing UI
- Photos, live location, medical records
- “Is my child gifted / delayed” scoring
- Milestone shaming or age-gated leap panic

---

## 9. User journeys

### 9.1 Acquisition — quiz (`trylittleblueprint.com`)

1. **Child** — first name or nickname, gender optional
2. **Birth** — date, time (or “I don’t know the time”), city (geocode to lat/lon + timezone)
3. **Parent** — name, birth date/time/city (time optional)
4. **Struggles** — pick up to 3: bedtime, tantrums / hitting, sensory (socks, noise, hair), picky eating, transitions / leaving the house
5. **Reveal (free hook)** — archetype + one clash sentence tied to a selected struggle
6. **Paywall** — annual (hero) vs monthly (anchor); trial terms in plain language

Reveal copy example (never “Rohini Moon” as the hook):

> Lucas is an inborn sensory processor. Fast, hurried talk can register as panic in his body. Tonight, drop to his eye level before you ask him to put shoes on.

### 9.2 Logged-in parent — daily use

- Open **Today**: score, caution window, ritual
- Open **Blueprint** when they feel “why is he like this?”
- Open **Harmony / Scripts** in a live conflict
- (P1) Open **Doula** at 2am

### 9.3 Gift / newborn (P2)

Shower book is a **channel**, not V1. V1 still accepts 0–12 month profiles so the quiz works for new babies.

---

## 10. Feature specs

### 10.1 Child Blueprint

**User story:** As an exhausted parent, I want to understand this child’s sensory and emotional wiring so I stop forcing methods that do not fit them.

**Must show**

- Inborn archetype badge + 2–3 sentence overview
- Sensory card: energy type, triggers, soothe list
- Emotional temperament (plain language)
- Learning modality: style, attention pattern, environment hint, play/extracurricular ideas (toned down for infants)
- Parenting key (one paragraph)
- Do-not-do list (3–5 tactics that backfire)
- Struggle-matched first card (from quiz picks)

**Age bands**

| Band | Emphasize | De-emphasize |
|---|---|---|
| 0–12 months | Sleep, soothe, overstimulation, feeding environment | School, extracurriculars, “hitting sibling” |
| 1–3 years | Tantrums, transitions, sensory clothing, bedtime | Career-of-the-child language |
| 4–8 years | Learning, focus, after-school load, sibling conflict | Newborn soothe as the lead |

**Accuracy states**

- Exact time: full sensory + emotional resolution
- Date + city only: element-level profile, banner: “Exact birth time makes clash scripts more precise”

### 10.2 Harmony

**User story:** As a parent who feels guilty, I want to see why this child triggers *me*, and the exact words to use.

**Must show**

- Harmony score 0–100 (element pairing; not a love score)
- Pairing label, e.g. “Fast-talking Air parent + Earth child”
- Trigger point + why it happens (pacing, volume, touch, logic-during-storm)
- 3-step crisis card:
  1. Body pause
  2. Word-for-word script
  3. Physical anchor (touch vs space, per profile)

V1 = one parent. P1 = add second adult.

### 10.3 Crisis scripts library

Minimum situations in P0:

1. Bedtime stall / won’t sleep
2. Hitting / aggressive burst
3. Clothing / sock / hair sensory
4. Leaving the park or playground
5. Grocery / public meltdown

Each script is keyed by **situation + parent element + child element** (fallback: situation + child archetype). Show 3 steps, not a blog post.

### 10.4 Daily sensory home

**User story:** I want to know when today is a high-stimulation day and what 2-minute thing to do — without dreading the week.

**Must show**

- Score 0–100 for today
- Alert level: Low / Moderate / High (no “storm” / “leap” language)
- One green window and one caution window (local time)
- One micro-ritual tailored to the child’s soothe list
- Disclaimer: educational, not medical, not predictive of behavior as fate

P0 may use a simplified transit-Moon + child-element heuristic (current API stub). Must not be a hardcoded 68 for every child.

### 10.5 Paywall & account

- Plans: Annual $79.99 (hero), Monthly $14.99 (anchor)
- 3-day trial; cancel anytime; auto-renew disclosed before Apple/Stripe confirm
- P0: one child included
- Settings: edit birth data, unknown-time toggle, delete account + all child records
- No child photos. No social feed.

### 10.6 Doula AI (P1 only)

- Inputs: parent message + child blueprint JSON + harmony JSON + approved script bank + medical disclaimer
- Outputs: calm 3-step advice; refuse diagnosis; refuse fortune-telling; refuse adult life questions
- Language firewall applied to every completion

---

## 11. Screen inventory (P0)

**Web quiz**

1. Landing
2. Child name
3. Birth details (+ unknown time)
4. Parent birth details
5. Struggles
6. Reveal
7. Paywall / trial
8. Account create (if not earlier)

**App or logged-in web (P0 may be web-only)**

1. Today (home)
2. Blueprint
3. Harmony
4. Scripts (situation list → crisis card)
5. Settings (privacy, delete, billing, disclaimers)

---

## 12. Content & language firewall

**Allowed:** nervous system, sensory, temperament, learning, pacing, scripts, “inborn,” “wiring,” “today’s stimulation.”

**Banned on parent-facing UI:** kundali, dasha, house lord, Rahu, Ketu, mangal, shani, “destined,” “soul contract,” marriage, money, death, “your child will become,” diagnosis, “this is ADHD,” crystal / tarot imagery.

**Required footer (Blueprint, Daily, Doula):**

> Little Blueprint is educational. It is not medical, pediatric, or psychiatric advice and is not a diagnosis of ADHD, autism, or sensory processing disorder. If you have concerns about your child’s development, talk to a qualified clinician.

Internal JSON may keep Nakshatra keys. APIs that the client renders must expose parent-safe fields (`archetype`, `sensory_profile`, …). Raw `astronomical_profile` must not be the primary UI payload.

---

## 13. Data model (logical)

**ParentAccount**  
`id`, email, auth_provider, created_at, locale, trial/subscription status, deletion_requested_at

**ChildProfile**  
`id`, account_id, nickname, birth_datetime (nullable time), timezone, lat, lon, birth_time_known (bool), age_band (derived), created_at

**ParentNatal (for harmony)**  
`id`, account_id, display_name, role (mom/dad/caregiver), birth_datetime, timezone, lat, lon, birth_time_known

**Derived (store or recompute)**  
blueprint_json, harmony_json, daily_score_json (cache by local date)

**Never store**  
photos, GPS traces, medical notes, school records, audio, child-authored content

**Retention**  
Parent may erase child + natal + derived records in one action. COPPA/GDPR-K: parent is the operator; child is not a user.

---

## 14. Analytics (P0)

Track object-action events (see `docs/ANALYTICS_EVENT_TAXONOMY.md`). Minimum:

- `quiz_started` / `quiz_step_completed`
- `child_profile_created` (`has_exact_time`, `age_band`)
- `blueprint_revealed`
- `paywall_viewed` / `trial_started` / `subscription_activated`
- `daily_score_checked`
- `crisis_script_viewed`

Do not send Nakshatra names to ad networks. Do not attach child nickname to advertising pixels.

**P0 funnel targets (directional)**

| Step | Target |
|---|---|
| Quiz start → complete | ≥ 65% |
| Reveal → trial | ≥ 12% |
| Trial → paid | measure; optimize copy before spend scale |
| D7 return (daily home) | leading retention indicator |

---

## 15. Monetization (V1)

| Offer | Price | Phase |
|---|---|---|
| Annual membership | $79.99/yr | P0 |
| Monthly membership | $14.99/mo | P0 |
| Extra child | +$29/yr | P1 |
| PDF dossier | $39 | P1 |
| Hardcover book | $89 | P2 |

No ads. No selling child data.

---

## 16. Technical requirements

### Current repo (as of this PRD)

- `core/ephemeris.py` — Lahiri sidereal Moon Nakshatra (Swiss Ephemeris + fallback)
- `core/blueprint.py` — child blueprint + parent–child elemental synastry
- `data/*.json` — nakshatras, learning styles, gentle scripts
- `api/main.py` — `POST /api/blueprint/child`, `POST /api/blueprint/synastry`, stub daily sensory

### P0 engineering work

- Replace daily stub with a real per-child calculation
- Age-band copy layer on blueprint
- Unknown-time path
- Parent-safe API responses (hide raw astronomy from default client payload)
- Situation-script endpoint
- Quiz web app + auth + Stripe/Apple + delete-my-data
- Geocode birth city → lat/lon/timezone
- Persistent profiles (Supabase or equivalent)

### Target stack

- Web quiz + P0 logged-in: Next.js
- P1 mobile: React Native / Expo
- Engine: existing Python FastAPI + `pyswisseph`
- Auth/DB: Supabase (Postgres)
- Payments: Stripe (web) / StoreKit (iOS later)
- AI (P1): LLM with cached child JSON + firewall system prompt — no training on child data

---

## 17. Design

Follow `docs/DESIGN_SYSTEM_TOKENS.md`.

- Canvas `#FDFBF7`, terracotta `#D97D64`, sage `#8A9A86`, charcoal `#2C2C2A`
- Display serif for emotional headlines; Inter / SF for UI
- Large daily score ring, short cards, one primary CTA per screen
- WCAG 2.2 AA for text contrast on oatmeal backgrounds

---

## 18. Compliance (P0 launch gate)

Must exist before paid traffic:

1. Medical / not-a-diagnosis disclaimer on reveal, blueprint, daily, paywall
2. Privacy policy: what is collected, what is never collected, no sale of child data
3. Terms: trial, auto-renew, cancellation
4. 18+ / parent-or-guardian checkbox
5. One-tap erasure
6. TLS in transit; encryption at rest for birth records
7. No third-party ads SDK on child-profile screens

Detail: `docs/TERMS_AND_PRIVACY_COMPLIANCE.md`.

---

## 19. Build sequence

1. Parent-safe blueprint + harmony APIs + unknown time + age bands  
2. Quiz + reveal + paywall (web)  
3. Scripts library + Today screen  
4. Auth, billing, delete, disclaimers  
5. Real daily score  
6. P1: co-parent, sibling, PDF, Doula, iOS  

Do not start the book, registry, or practitioner portal until the quiz converts and Today is used more than once.

---

## 20. Open questions (do not block P0)

1. Show a discreet type name (e.g. “Rohini-type sensor”) vs archetype-only?
2. Is P0 web-only, or web quiz + simple logged-in web app?
3. Exact birth-city geocoder (Google vs Mapbox vs GeoNames)?
4. Gender on quiz: omit vs optional for copy tone only (never for fate)?
5. When to introduce the second parent in the quiz vs after paywall?

---

## 21. Appendix — existing docs

| Doc | Role after this PRD |
|---|---|
| This file | Product source of truth |
| `docs/FEATURE_PSYCHOLOGY_SPEC.md` | Deeper feature psychology; trim anything that contradicts P2/never |
| `docs/MARKET_PSYCHOLOGY_RESEARCH.md` | Research background |
| `docs/MONETIZATION_GTM_STRATEGY.md` | GTM; book/Babylist/doula = P2 |
| `docs/DESIGN_SYSTEM_TOKENS.md` | Visual system |
| `docs/TERMS_AND_PRIVACY_COMPLIANCE.md` | Legal baseline |
| `docs/ANALYTICS_EVENT_TAXONOMY.md` | Event names |
| `IDEAS.md` | Other ventures — **not** this product |
| `KINDRED_MASTER_PLAN.md` | Retired brand exploration |
