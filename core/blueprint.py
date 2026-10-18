"""
LITTLE BLUEPRINT - Profile & Report Generator
Combines raw ephemeris output with the Neuro-Vedic translation dictionaries
to generate the complete Inborn Child Blueprint and Parent-Child Synastry.
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional

from core.ephemeris import EphemerisEngine, ZODIAC_ELEMENTS

DATA_DIR = Path(__file__).parent.parent / "data"

class BlueprintGenerator:
    def __init__(self):
        self.engine = EphemerisEngine()
        self.nakshatras_db = self._load_json(DATA_DIR / "nakshatras.json").get("nakshatras", [])
        self.learning_db = self._load_json(DATA_DIR / "learning_styles.json").get("learning_modalities", [])
        self.scripts_db = self._load_json(DATA_DIR / "gentle_scripts.json").get("parent_child_scripts", [])

    def _load_json(self, path: Path) -> Dict[str, Any]:
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def generate_child_blueprint(
        self,
        child_name: str,
        birth_datetime: datetime,
        latitude: float,
        longitude: float
    ) -> Dict[str, Any]:
        """
        Generates the comprehensive Inborn Child Blueprint.
        """
        astro_data = self.engine.calculate_moon_nakshatra(birth_datetime, latitude, longitude)
        nakshatra_name = astro_data["nakshatra_name"]
        element = astro_data["element"]

        # Match with translation dictionary
        matched_nakshatra = next(
            (n for n in self.nakshatras_db if n["name"].lower() == nakshatra_name.lower()),
            None
        )

        if not matched_nakshatra:
            # Fallback profile
            matched_nakshatra = {
                "archetype": "The Natural Explorer",
                "sensory_profile": {
                    "energy_type": f"Governed by {element} energy",
                    "sensory_triggers": ["Sudden disruptions", "Lack of physical comfort"],
                    "soothing_mechanisms": ["Gentle reassurance", "Predictable routine"]
                },
                "emotional_temperament": "Curious, responsive to environment, seeks connection.",
                "learning_modality": f"Thrives in environments balancing {element} strengths.",
                "parenting_key": "Observe their natural rhythm and support their self-soothing cues."
            }

        # Match learning modality by element
        matched_learning = next(
            (l for l in self.learning_db if l["element"].lower() == element.lower()),
            None
        )

        return {
            "child_name": child_name,
            "astronomical_profile": astro_data,
            "inborn_archetype": matched_nakshatra.get("archetype"),
            "sensory_profile": matched_nakshatra.get("sensory_profile"),
            "emotional_temperament": matched_nakshatra.get("emotional_temperament"),
            "learning_modality": {
                "overview": matched_nakshatra.get("learning_modality"),
                "cognitive_style": matched_learning.get("learning_style") if matched_learning else "Multimodal",
                "attention_span": matched_learning.get("attention_span") if matched_learning else "Normal",
                "ideal_schooling_environment": matched_learning.get("ideal_environment") if matched_learning else "Montessori / Adaptive",
                "recommended_extracurriculars": matched_learning.get("extracurricular_recommendations") if matched_learning else [],
                "parent_study_tip": matched_learning.get("parent_coaching_tip") if matched_learning else ""
            },
            "parenting_guidance": matched_nakshatra.get("parenting_key")
        }

    def generate_parent_child_synastry(
        self,
        child_name: str,
        child_birth: datetime,
        child_lat: float,
        child_lon: float,
        parent_name: str,
        parent_birth: datetime,
        parent_lat: float,
        parent_lon: float
    ) -> Dict[str, Any]:
        """
        Generates the Parent-Child Trigger & Harmony Diagnostic.
        """
        child_astro = self.engine.calculate_moon_nakshatra(child_birth, child_lat, child_lon)
        parent_astro = self.engine.calculate_moon_nakshatra(parent_birth, parent_lat, parent_lon)

        child_element = child_astro["element"]
        parent_element = parent_astro["element"]

        dynamic_key = f"{parent_element} Parent + {child_element} Child"

        # Check for gentle script match
        matched_script = None
        for script in self.scripts_db:
            if parent_element.lower() in script["dynamic_type"].lower() and child_element.lower() in script["dynamic_type"].lower():
                matched_script = script
                break

        # Calculate baseline compatibility score (0 to 100)
        # Elemental harmony matrix
        element_scores = {
            ("Fire", "Air"): 92, ("Air", "Fire"): 92,
            ("Earth", "Water"): 90, ("Water", "Earth"): 90,
            ("Fire", "Fire"): 85, ("Earth", "Earth"): 88,
            ("Air", "Air"): 86, ("Water", "Water"): 88,
            ("Fire", "Earth"): 72, ("Earth", "Fire"): 72,
            ("Fire", "Water"): 68, ("Water", "Fire"): 68,
            ("Earth", "Air"): 74, ("Air", "Earth"): 74,
            ("Air", "Water"): 70, ("Water", "Air"): 70
        }
        harmony_score = element_scores.get((parent_element, child_element), 78)

        return {
            "parent_name": parent_name,
            "child_name": child_name,
            "harmony_score": harmony_score,
            "dynamic_summary": f"Your {parent_element} nature interacts with your child's {child_element} emotional core.",
            "elemental_pairing": dynamic_key,
            "trigger_analysis": matched_script.get("trigger_point") if matched_script else "Pacing differences during transitions.",
            "why_the_clash_happens": matched_script.get("why_it_happens") if matched_script else "Different cognitive processing speeds.",
            "actionable_scripts": matched_script.get("word_for_word_script") if matched_script else {
                "step_1_pause": "Take a deep breath and lower your physical elevation to match their eye level.",
                "step_2_script": "'I see you are feeling big feelings. I am here with you while you reset.'",
                "step_3_physical_anchor": "Gentle, non-demanding presence."
            }
        }
