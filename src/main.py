from src.config.config import get_database_config
from src.service.gold_service import GoldService
from src.service.raw_service import RawService
from src.service.silver_service import print_dataframe


def main():


    raw_service = RawService()
    raw_service.download_dataset()

    print_dataframe()

    gold_service = GoldService(get_database_config())
    gold_service.main()

if __name__ == "__main__":
    main()