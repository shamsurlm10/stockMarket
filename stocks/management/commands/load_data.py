import csv
from django.core.management.base import BaseCommand
from stocks.models import Stock

class Command(BaseCommand):
    help = 'Load stock data from CSV file into the database'

    def handle(self, *args, **options):
        file_path = 'D:/stockProject/stockMarket/stock_market_data.csv'  # Update with your actual file path

        with open(file_path, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                Stock.objects.create(
                    date=row['date'],
                    trade_code=row['trade_code'],
                    high=row['high'],
                    low=row['low'],
                    open=row['open'],
                    close=row['close'],
                    volume=row['volume']
                )

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))