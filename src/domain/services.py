from .entities import Account, Transaction
from .repositories import AccountRepository, TransactionRepository
from config import config

class TransactionService:
    def __init__(self, file_reader, email_sender, account_repository: AccountRepository=None, transaction_repository: TransactionRepository=None):
        self.file_reader = file_reader
        self.email_sender = email_sender
        self.account_repository = account_repository
        self.transaction_repository = transaction_repository
        
    def process_transactions(self, account_id: str):
        transactions_data: list[Transaction] = self.file_reader.read_transactions(account_id)
        account = Account()
        if self.account_repository:
            account = self.account_repository.get_by_id(account_id) or Account()  # Obtiene o crea una cuenta
            
        for transaction in transactions_data:
            account.process_transaction(transaction)
            
        self.account_repository.save(account)
        if self.transaction_repository:
            self.transaction_repository.save(transactions_data)
        
        summary_info = account.generate_sumary()
        self.email_sender.send_summary(config.EMAIL_TO, summary_info)