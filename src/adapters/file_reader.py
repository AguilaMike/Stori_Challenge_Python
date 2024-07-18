import csv
from datetime import datetime
from domain.entities import Transaction

class CSVFileAdapter:
    def __init__(self, file_path: str):
        self.file_path = file_path
        
    def read_transactions(self, account_id: str) -> list[Transaction]:
        transactions = []
        with open(self.file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Saltar encabezados
            for row in reader:
                id, date_str, amount_str = row
                id = int(id)
                date = datetime.strptime(date_str, '%Y-%m-%d').date()
                amount = float(amount_str)
                type = "credit" if amount > 0 else "debit"
                transactions.append(Transaction(id, account_id, date, abs(amount), type))
        return transactions