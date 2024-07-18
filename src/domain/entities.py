from dataclasses import dataclass
from datetime import datetime
from collections import defaultdict

@dataclass
class Transaction:
    id: int
    account_id: str
    date: datetime
    amount: float
    type: str  # "credit" o "debit"

@dataclass
class Account:
    id: str = "default_account"
    balance: float = 0
    transactions: list[Transaction] = None

    def process_transaction(self, transaction: Transaction):
        """Process a transaction and update the balance.

        Args:
            transaction (Transaction): Transaction to process.
        """
        
        if transaction.type == "credit":
            self.balance += transaction.amount
        elif transaction.type == "debit":
            self.balance -= transaction.amount
        self.transactions.append(transaction)
    
    def generate_sumary(self) -> dict:
        """Generate a summary .

        Returns:
            dict: A dictionary with the summary's information.
        """
        
        transactions_by_month = defaultdict(int)
        debit_amounts_by_month = defaultdict(list)
        credit_amounts_by_month = defaultdict(list)

        for transaction in self.transactions:
            date_str = transaction.date.strftime("%Y-%m-%d") 
            month = datetime.strptime(date_str, "%Y-%m-%d").strftime("%B")
            transactions_by_month[month] += 1
            
            if transaction.type == "debit":
                debit_amounts_by_month[month].append(transaction.amount)
            else:
                credit_amounts_by_month[month].append(transaction.amount)

        # Formateo de resultados
        formatted_transactions = {month: count for month, count in transactions_by_month.items()}
        
        # Asegurarse de no dividir por cero
        avg_debit = {month: -round(sum(amounts) / len(amounts), 2) if amounts else 0 
                    for month, amounts in debit_amounts_by_month.items()}
        avg_credit = {month: round(sum(amounts) / len(amounts), 2) if amounts else 0 
                    for month, amounts in credit_amounts_by_month.items()}

        summary_info = {
            "total_balance": round(self.balance, 2),  # Redondear a 2 decimales
            "transactions_by_month": formatted_transactions,
            "avg_debit": avg_debit,
            "avg_credit": avg_credit,
        }
        
        return summary_info