from adapters.file_reader import CSVFileAdapter
from adapters.email_sender import SMTPEmailSender
from adapters.database import SQLiteTransactionRepository, SQLiteAccountRepository, initialize_database
from domain.services import TransactionService
from config import config

def main():
    file_reader = CSVFileAdapter("data/transactions.csv")
    email_sender = SMTPEmailSender(config.EMAIL_HOST, config.EMAIL_PORT, config.EMAIL_USER, config.EMAIL_PASSWORD)
    initialize_database(config.DATABASE_URL)
    transaction_repository = SQLiteTransactionRepository(config.DATABASE_URL)
    account_repository = SQLiteAccountRepository(config.DATABASE_URL)
    transaction_service = TransactionService(file_reader, email_sender, account_repository, transaction_repository)

    try:
        transaction_service.process_transactions("default_account")
    except Exception as e:
        # Manejo de errores
        print(f"Error al procesar las transacciones: {e}")

if __name__ == "__main__":
    main()