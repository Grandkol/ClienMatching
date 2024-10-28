from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column
from typing_extensions import Union

from models import Base


class User(Base):
    avatar: Mapped[str] = mapped_column(nullable=True)
    gender: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[Union[str, None]] = mapped_column(nullable=False)
    last_name: Mapped[Union[str, None]] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)

    def __init__(
        self, first_name: str, last_name: str
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name


    def __repr__(self) -> str:
        return f"<User {self.first_name}>"