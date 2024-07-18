import sqlite3
from domain.repositories import TransactionRepository, AccountRepository
from domain.entities import Account, Transaction

def initialize_database(db_path):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS accounts (
                id TEXT PRIMARY KEY,
                balance REAL
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_id TEXT,
                date TEXT,
                amount REAL,
                type TEXT,
                FOREIGN KEY (account_id) REFERENCES accounts (id)
            )
            """
        )
        cursor.execute(
            """
            DELETE FROM transactions
            """
        )
        cursor.execute(
            """
            DELETE FROM accounts
            """
        )            
        conn.commit()

class SQLiteTransactionRepository(TransactionRepository):
    def __init__(self, db_path):
        self.db_path = db_path

    def save(self, transactions: list[Transaction]):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.executemany(
                "INSERT INTO transactions (account_id, date, amount, type) VALUES (?, ?, ?, ?)",
                [(t.account_id, t.date, t.amount, t.type) for t in transactions],
            )
            conn.commit()
    
    def get_by_account_id(self, account_id: str) -> list[Transaction]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, account_id, date, amount, type FROM transactions WHERE account_id = ?", (account_id,))
            rows = cursor.fetchall()
            return [Transaction(id=row[0], account_id=row[1], date=row[2], amount=row[3], type=row[4]) for row in rows]

class SQLiteAccountRepository(AccountRepository):
    def __init__(self, db_path):
        self.db_path = db_path
        self._transaction_repository = SQLiteTransactionRepository(db_path)

    def save(self, account: Account):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT OR REPLACE INTO accounts (id, balance) VALUES (?, ?)", (account.id, account.balance,))
            conn.commit()

    def get_by_id(self, account_id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT balance FROM accounts WHERE id = ?", (account_id,))
            row = cursor.fetchone()
            account = Account(id=account_id, balance=row[0]) if row else Account(id=account_id)
            account.transactions = self._transaction_repository.get_by_account_id(account_id)
            return account