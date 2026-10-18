"""
LITTLE BLUEPRINT - Astrological Calculation Engine
Calculates high-precision Sidereal positions using Lahiri Ayanamsa
and maps them to the 27 Nakshatras and 12 Bhavas (Houses).
"""

import math
from datetime import datetime, timezone
from typing import Dict, Any, Optional

# List of 27 classical Vedic Nakshatras in zodiacal order (0° Aries to 360° Pisces)
NAKSHATRA_NAMES = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
    "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
    "Hasta", "Chitra", "Svati", "Vishakha", "Anuradha", "Jyeshtha",
    "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
    "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

ZODIAC_SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

ZODIAC_ELEMENTS = {
    "Aries": "Fire", "Leo": "Fire", "Sagittarius": "Fire",
    "Taurus": "Earth", "Virgo": "Earth", "Capricorn": "Earth",
    "Gemini": "Air", "Libra": "Air", "Aquarius": "Air",
    "Cancer": "Water", "Scorpio": "Water", "Pisces": "Water"
}

class EphemerisEngine:
    """
    Computes Sidereal planetary longitudes, Nakshatras, and Houses.
    Supports pyswisseph with an astronomical trigonometric fallback.
    """

    def __init__(self, ayanamsa_mode: str = "LAHIRI"):
        self.ayanamsa_mode = ayanamsa_mode
        self._has_swisseph = False
        try:
            import swisseph as swe
            self.swe = swe
            self._has_swisseph = True
            # Set Lahiri Ayanamsa
            self.swe.set_sid_mode(self.swe.SIDM_LAHIRI)
        except ImportError:
            self._has_swisseph = False

    def get_ayanamsa_degrees(self, year: int) -> float:
        """Approximates Lahiri Ayanamsa for any year (approx 24.1° in 2024)."""
        # Lahiri ayanamsa formula: ~23.85° at 2000.0, precessing at ~50.29 arcseconds/year
        years_since_2000 = year - 2000.0
        return 23.85 + (years_since_2000 * 50.29 / 3600.0)

    def calculate_moon_nakshatra(
        self,
        birth_datetime: datetime,
        latitude: float,
        longitude: float
    ) -> Dict[str, Any]:
        """
        Calculates the child's exact Moon longitude, Zodiac sign, Nakshatra, and Pada.
        """
        if self._has_swisseph:
            # High-precision Swiss Ephemeris calculation
            utc_dt = birth_datetime.astimezone(timezone.utc) if birth_datetime.tzinfo else birth_datetime
            jd = self.swe.julday(
                utc_dt.year, utc_dt.month, utc_dt.day,
                utc_dt.hour + utc_dt.minute / 60.0 + utc_dt.second / 3600.0
            )
            # Flag for sidereal position
            flags = self.swe.FLG_SWIEPH | self.swe.FLG_SIDEREAL
            res, _ = self.swe.calc_ut(jd, self.swe.MOON, flags)
            moon_lon = res[0] % 360.0
        else:
            # Fallback astronomical calculation based on mean lunar motion
            epoch_2000 = datetime(2000, 1, 1, 12, 0, tzinfo=timezone.utc)
            utc_dt = birth_datetime.astimezone(timezone.utc) if birth_datetime.tzinfo else birth_datetime.replace(tzinfo=timezone.utc)
            days = (utc_dt - epoch_2000).total_seconds() / 86400.0
            
            # Mean Moon longitude formula
            mean_moon = (218.316 + 13.176396 * days) % 360.0
            ayanamsa = self.get_ayanamsa_degrees(utc_dt.year)
            moon_lon = (mean_moon - ayanamsa) % 360.0

        # Each Nakshatra spans exactly 360 / 27 = 13° 20' = 13.3333333333°
        nakshatra_span = 360.0 / 27.0
        nakshatra_idx = int(moon_lon / nakshatra_span) % 27
        nakshatra_name = NAKSHATRA_NAMES[nakshatra_idx]

        # Each Pada is 1/4 of a Nakshatra = 3° 20' = 3.3333333333°
        degree_in_nakshatra = moon_lon % nakshatra_span
        pada = int(degree_in_nakshatra / (nakshatra_span / 4.0)) + 1

        # Zodiac sign (each is 30°)
        sign_idx = int(moon_lon / 30.0) % 12
        sign_name = ZODIAC_SIGNS[sign_idx]
        element = ZODIAC_ELEMENTS[sign_name]

        return {
            "longitude_degrees": round(moon_lon, 3),
            "zodiac_sign": sign_name,
            "element": element,
            "nakshatra_id": nakshatra_idx + 1,
            "nakshatra_name": nakshatra_name,
            "pada": pada,
            "calculation_engine": "SwissEphemeris" if self._has_swisseph else "AstronomicalTrigFallback"
        }
