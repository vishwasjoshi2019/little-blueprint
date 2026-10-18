# 🌿 LITTLE BLUEPRINT
> **Your Child's Inborn Nature, Decoded.**  
> *The Anti-Anxiety Parenting Engine Powered by Neuro-Vedic Astrological Intelligence.*

---

## 📖 Overview
**LITTLE BLUEPRINT** translates high-precision astronomical calculations (Sidereal Moon Nakshatras, 5th House, and Divisional Charts) into modern, actionable child developmental psychology for affluent parents in Tier-1 markets (US, UK, Canada, Australia, and Germany).

It solves the primary parental pain points:
1. **Sensory Overload & Meltdowns:** Knowing how your child self-soothes based on their Moon Nakshatra.
2. **Parent-Child Clashes:** Real-time word-for-word gentle parenting scripts when parental cognitive speed clashes with child temperament.
3. **Inborn Learning Modalities:** Pinpointing whether the child learns best via tactile, visual, STEM-analytical, or artistic modalities.
4. **Physical Keepsakes:** Automated 42-page custom linen-bound hardcover book for baby showers and 1st birthdays.

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
* [LITTLE BLUEPRINT Master PRD](LITTLE_BLUEPRINT_PRD.md)
* [Master Venture Ideas Pipeline](../MASTER_IDEAS_PIPELINE.md)
