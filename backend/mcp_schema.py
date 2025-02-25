from pydantic import BaseModel
from typing import Optional

class DisasterEvent(BaseModel):
    id: str
    type: str  # e.g., "earthquake", "flood", "fire"
    location: dict  # GeoJSON format { "type": "Point", "coordinates": [lng, lat] }
    severity: Optional[str] = "unknown"  # Mild, Moderate, Severe
    timestamp: str  # ISO format