from sqlalchemy.orm import Session
from sqlalchemy import select, func

from app_sync.db.models import TradeResult


class TradeResultRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_record_count(self) -> int:
        result = self.session.execute(select(func.count(TradeResult.id)))
        count = result.scalar_one()
        return count

    def get_max_volume_trade(self) -> TradeResult:
        result = self.session.execute(
            select(TradeResult).order_by(TradeResult.volume.desc()).limit(1)
        )
        max_volume_trade = result.scalar_one()
        return max_volume_trade

    def get_unique_exchange_product_ids(self) -> list[str]:
        result = self.session.execute(
            select(TradeResult.exchange_product_id).distinct()
        )
        unique_ids = [row[0] for row in result.fetchall()]
        return unique_ids
