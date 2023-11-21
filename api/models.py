from datetime import datetime
from dataclasses import dataclass, field
from typing import Dict


@dataclass
class User:
    name: str
    email: str
    password: str
    created_at: datetime = datetime.now()
    updated_at: datetime = created_at

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "created_at": self.created_at.isoformat() if isinstance(self.created_at, datetime) else datetime.fromisoformat(self.created_at["$date"].replace("Z", "+00:00")),
            "updated_at": self.updated_at.isoformat() if isinstance(self.updated_at, datetime) else datetime.fromisoformat(self.updated_at["$date"].replace("Z", "+00:00")),
        }



@dataclass
class UserResponse(User):
    _id: Dict[str, str] = field(default_factory=dict)    

