import pandas as pd
from django.core.management.base import BaseCommand
from stocks.models import Stock

class Command(BaseCommand):
    help = 'Load stock data from CSV file into the database'

    def handle(self, *args, **options):
        file_path = 'D:/stockProject/stockMarket/stock_market_data.csv'  # Update with your actual file path

        try:
            # Read CSV into a DataFrame
            df = pd.read_csv(file_path)

            # Clean numeric fields by removing commas
            numeric_fields = ['high', 'low', 'open', 'close', 'volume']
            for field in numeric_fields:
                df[field] = df[field].str.replace(',', '')

            # Iterate over DataFrame rows to populate Stock model
            for index, row in df.iterrows():
                Stock.objects.create(
                    date=row['date'],
                    trade_code=row['trade_code'],
                    high=float(row['high']),   # Convert to float after cleaning
                    low=float(row['low']),     # Convert to float after cleaning
                    open=float(row['open']),    # Convert to float after cleaning
                    close=float(row['close']),  # Convert to float after cleaning
                    volume=int(row['volume'])   # Convert to int after cleaning
                )

            self.stdout.write(self.style.SUCCESS('Data loaded successfully'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {file_path}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))