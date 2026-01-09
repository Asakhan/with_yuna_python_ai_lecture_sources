from __future__ import annotations
from dataclasses import dataclass

@dataclass
class UserFacingError(Exception):
    message: str
    exit_code: int = 2

    def __str__(self) -> str:
        return self.message