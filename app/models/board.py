from app import db
from app.models.card import Card


class Board(db.Model):
    board_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    owner = db.Column(db.String, nullable=False)
    cards = db.relationship("Card", back_populates="board")

    def to_dict(self):
        return {
            "board_id": self.board_id,
            "title": self.title,
            "owner": self.owner,
            # "cards": self.cards
        }

    @classmethod
    def from_dict(cls, request_data):
        new_board = cls(
            title=request_data["title"],
            owner=request_data["owner"]
        )

        return new_board
