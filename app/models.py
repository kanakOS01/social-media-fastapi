from .database import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Boolean, text
from sqlalchemy.types import TIMESTAMP


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String)
    content: Mapped[str] = mapped_column(String)
    published: Mapped[bool] = mapped_column(Boolean, server_default="TRUE")
    created_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True), server_default=text("now()")
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, title={self.title!r}, content={self.content!r}, published={self.published!r})"
