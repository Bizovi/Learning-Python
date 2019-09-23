from typing import (
	Tuple, NamedTuple, List,
	Optional, Dict
)


class SpendResult(NamedTuple):
	is_successful: bool
	balance: int


class Account:
	"""
	An account can spend or credit funds
	An account maintains a balance
	"""
	def __init__(self, name: str, initial_balance: int) -> None:
		self.name = name
		self.initial_balance = initial_balance

	def credit(self, value: int) -> bool:
		if value <= 0:
			return False
		self.initial_balance += value
		return True

	def spend(self, value: int) -> SpendResult:
		if value <= 0:
			return SpendResult(False, self.initial_balance)
		if self.initial_balance < value:
			return SpendResult(False, self.initial_balance)
		self.initial_balance -= value
		return SpendResult(True, self.initial_balance)


class Customer:
	"""
	# A customer has one or more amounts
	# A customer can spend money or credit from an account
	"""
	def __init__(self, name: str) -> None:
		self.name = name
		self.accounts: List[Account] = []
		self.primary_account_name: Optional[str] = None

	def find_account_by_name(self, name: str) -> Optional[Account]:
		for account in self.accounts:
			if account.name == name:
				return account
		return None

	def add_account(self, account: Account) -> None:
		self.accounts.append(account)

	@property
	def primary_account(self) -> Optional[Account]:
		if self.primary_account_name is None:
			return None
		return self.find_account_by_name(self.primary_account_name)



class Bank:
	"""
	# A bank has many customers
	# A bank can be used to transact between customers
	"""
	def __init__(self) -> None:
		self.name_to_customer: Dict[str, Customer] = {}

	def add_customer(self, customers: List[Customer]) -> List[bool]:
		result = []
		for customer in customers:
			if customer.name in self.name_to_customer:
				result.append(False)
			else:
				self.name_to_customer[customer.name] = customer
				result.append(True)
		return result

	def transfer_funds(self, customer_name_from: str, customer_name_to: str, value: int) -> bool:
		if customer_name_from not in self.name_to_customer or customer_name_to not in self.name_to_customer:
			return False

		primary_account_from = self.name_to_customer[customer_name_from].primary_account
		primary_account_to = self.name_to_customer[customer_name_to].primary_account

		if primary_account_from is None or primary_account_to is None:
			return False

		if primary_account_from.spend(value).is_successful:
			primary_account_to.credit(value)
			return True
		return False


def main():
	pass


if __name__ == "__main__":
	main()
