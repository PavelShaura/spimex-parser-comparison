from app_sync.db.database import Session
from app_sync.db.models import TradeResult


def save_data_to_db(data):
    print("Saving data to database...")
    with Session() as session:
        try:
            for item in data:
                trade_result = TradeResult(
                    exchange_product_id=item["exchange_product_id"],
                    exchange_product_name=item["exchange_product_name"],
                    delivery_basis_name=item["delivery_basis_name"],
                    volume=item["volume"],
                    total=item["total"],
                    count=item["count"],
                    date=item["date"],
                )
                session.add(trade_result)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e