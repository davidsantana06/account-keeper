from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declared_attr


class TimestampMixin:
    @declared_attr
    def created_at(cls):
        return Column(DateTime, nullable=False, default=datetime.now)

    @declared_attr
    def updated_at(cls):
        return Column(
            DateTime, nullable=False, default=datetime.now, onupdate=datetime.now
        )

    @property
    def age_in_seconds(self) -> float:
        return (datetime.now() - self.created_at).total_seconds()

    @property
    def age_in_minutes(self) -> float:
        return self.age_in_seconds / 60

    @property
    def age_in_hours(self) -> float:
        return self.age_in_minutes / 60

    @property
    def age_in_days(self) -> float:
        return self.age_in_hours / 24

    @property
    def age_in_weeks(self) -> float:
        return self.age_in_days / 7
