# 🌿 LITTLE BLUEPRINT
> **Your Child's Inborn Nature, Decoded.**  
> *The Anti-Anxiety Parenting Engine Powered by Neuro-Vedic Astrological Intelligence.*

---

## 📖 Overview
**LITTLE BLUEPRINT** is a parent-only product (ages 0–8, hero 1–5) that translates sidereal natal math into a child’s sensory, emotional, and learning profile — plus word-for-word clash scripts. It is not adult life-astrology and not a medical tool.

Primary pain points:
1. **Sensory overload & meltdowns** — how this child self-soothes
2. **Parent–child clashes** — why you trigger each other, and the exact script
3. **Inborn learning modality** — tactile, visual, STEM-analytical, or artistic

V1 scope, non-goals, and screens: [LITTLE_BLUEPRINT_PRD.md](LITTLE_BLUEPRINT_PRD.md). Keepsake book, Doula AI, and registry gifting are later phases.

---

## 🗂️ Project Structure

```
AstroApp/
├── api/
│   └── main.py              # FastAPI REST endpoints (/api/blueprint/child, /synastry, /daily-sensory)
├── core/
│   ├── ephemeris.py         # Sidereal Lahiri calculation engine (Swiss Ephemeris + fallback)
│   └── blueprint.py         # Profile & synastry generator engine
├── data/
│   ├── nakshatras.json      # 27 Nakshatras mapped to sensory & emotional profiles
│   ├── learning_styles.json # Cognitive styles & extracurricular recommendations
│   └── gentle_scripts.json  # Tantrum de-escalation scripts by elemental clash
├── docs/
│   └── LITTLE_BLUEPRINT_PRD.md # Master Product Requirements Document
├── requirements.txt         # Backend Python dependencies
├── IDEAS.md                 # Strategic market comparison of spiritual tech verticals
└── README.md
```

---

## 🚀 Quickstart & Testing

### 1. Test the Core Calculation Engine Directly:
```bash
python3 -c "
from datetime import datetime, timezone
from core.blueprint import BlueprintGenerator

bg = BlueprintGenerator()
print(bg.generate_child_blueprint(
    child_name='Lucas',
    birth_datetime=datetime(2022, 6, 15, 14, 30, tzinfo=timezone.utc),
    latitude=37.7749,
    longitude=-122.4194
))
"
```

### 2. Run the REST API:
```bash
pip3 install -r requirements.txt
uvicorn api.main:app --reload --port 8000
```
Then visit `http://127.0.0.1:8000/docs` to test the interactive Swagger documentation.

---

## 📄 Key Documentation
* [LITTLE BLUEPRINT V1 PRD (source of truth)](LITTLE_BLUEPRINT_PRD.md)
* [Master Venture Ideas Pipeline](../MASTER_IDEAS_PIPELINE.md)
