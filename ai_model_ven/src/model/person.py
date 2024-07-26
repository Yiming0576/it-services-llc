import attr
import uuid
from datetime import datetime

@attr.s
class Person:
    person_id: str = attr.ib(default=attr.Factory(lambda: uuid.uuid4().hex))
    first_name: str = attr.ib()
    last_name: str = attr.ib()
    birth_date: datetime = attr.ib(default=None)
    gender: str = attr.ib(default=None)
    address: str = attr.ib(default=None)

    def full_name(self) -> str:
        """Return the full name of the person."""
        return f"{self.first_name} {self.last_name}"
