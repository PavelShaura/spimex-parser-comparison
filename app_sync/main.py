import time

from app_sync.parser.scrapping import scrape_reports
from app_sync.db.database import Base, Session, engine
from app_sync.db.repository import TradeResultRepository
from app_sync.db.save_data import save_data_to_db
from app_sync.db.models import TradeResult


def create_tables(engine_db):
    print("Creating tables...")
    Base.metadata.create_all(engine_db)


def main():
    start_time = time.time()

    print("Starting main process...")
    report_data = scrape_reports()
    save_data_to_db(report_data)
    print("Main process finished.")

    with Session() as session:
        repository = TradeResultRepository(session)

        record_count = repository.get_record_count()
        print(f"Total records: {record_count}")

        max_volume_trade = repository.get_max_volume_trade()
        print(f"Max volume trade: {max_volume_trade}")

        unique_exchange_product_ids = repository.get_unique_exchange_product_ids()
        print(f"Unique exchange product IDs: {unique_exchange_product_ids}")

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"\n Общее время синхронного парсера : {execution_time:.2f} seconds")


if __name__ == "__main__":
    create_tables(engine)
    main()