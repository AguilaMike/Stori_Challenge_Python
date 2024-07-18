from abc import ABC, abstractmethod
from domain.entities import Account, Transaction

class TransactionRepository(ABC):
    @abstractmethod
    def save(self, transaction: Transaction):
        pass
    
    @abstractmethod
    def get_by_account_id(self, account_id: str) -> list[Transaction]:
        pass

class AccountRepository(ABC):
    @abstractmethod
    def save(self, account: Account):
        pass

    @abstractmethod
    def get_by_id(self, account_id: str) -> Account:
        pass