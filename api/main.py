"""
LITTLE BLUEPRINT - REST API Service
FastAPI endpoints powering the Web-to-App Onboarding Quiz and Mobile Client.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict, Any

from core.blueprint import BlueprintGenerator

app = FastAPI(
    title="Little Blueprint API",
    description="Your Child's Inborn Nature, Decoded. Powered by Neuro-Vedic Astrological Intelligence.",
    version="1.0.0"
)

generator = BlueprintGenerator()

class ChildProfileRequest(BaseModel):
    child_name: str = Field(..., example="Lucas")
    birth_iso: str = Field(..., example="2022-06-15T14:30:00Z")
    latitude: float = Field(..., example=37.7749)
    longitude: float = Field(..., example=-122.4194)

class SynastryRequest(BaseModel):
    child_name: str = Field(..., example="Lucas")
    child_birth_iso: str = Field(..., example="2022-06-15T14:30:00Z")
    child_latitude: float = Field(..., example=37.7749)
    child_longitude: float = Field(..., example=-122.4194)
    parent_name: str = Field(..., example="Emma")
    parent_birth_iso: str = Field(..., example="1991-04-10T08:15:00Z")
    parent_latitude: float = Field(..., example=37.7749)
    parent_longitude: float = Field(..., example=-122.4194)

@app.get("/")
def root():
    return {
        "app": "Little Blueprint",
        "tagline": "Your Child's Inborn Nature, Decoded.",
        "status": "online",
        "version": "1.0.0"
    }

@app.post("/api/blueprint/child")
def get_child_blueprint(req: ChildProfileRequest):
    try:
        birth_dt = datetime.fromisoformat(req.birth_iso.replace("Z", "+00:00"))
        blueprint = generator.generate_child_blueprint(
            child_name=req.child_name,
            birth_datetime=birth_dt,
            latitude=req.latitude,
            longitude=req.longitude
        )
        return {"status": "success", "data": blueprint}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/blueprint/synastry")
def get_parent_child_synastry(req: SynastryRequest):
    try:
        child_dt = datetime.fromisoformat(req.child_birth_iso.replace("Z", "+00:00"))
        parent_dt = datetime.fromisoformat(req.parent_birth_iso.replace("Z", "+00:00"))
        synastry = generator.generate_parent_child_synastry(
            child_name=req.child_name,
            child_birth=child_dt,
            child_lat=req.child_latitude,
            child_lon=req.child_longitude,
            parent_name=req.parent_name,
            parent_birth=parent_dt,
            parent_lat=req.parent_latitude,
            parent_lon=req.parent_longitude
        )
        return {"status": "success", "data": synastry}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/blueprint/daily-sensory/{child_id}")
def get_daily_sensory_score(child_id: str):
    # Simulated daily sensory score algorithm based on transit moon
    return {
        "child_id": child_id,
        "date": datetime.utcnow().strftime("%Y-%m-%d"),
        "sensory_overload_risk_score": 68,
        "alert_level": "Moderate Stimulation",
        "recommendation": "Transit Moon enters high sensory degree. Avoid crowded indoor play spaces between 2:00 PM - 5:00 PM; prioritize sensory grounding through bath play or clay.",
        "bedtime_soothing_ritual": "5 minutes of quiet dim lighting + foot reflexology touch."
    }
