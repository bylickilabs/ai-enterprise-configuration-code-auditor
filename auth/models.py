# auth/models.py
from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    username: str
    role: str
    token: str
    created_at: datetime
    active: bool = True
