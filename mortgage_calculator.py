import csv
from time import sleep
import sys
import argparse
 
class Mortgage:

	"""
	mortgage and personal loan calculator interest calculator using fixed rates
	"""

	def __init__(self, principle, rate, years=30):
		self.principle = principle
		self.rate = rate
		self.years = years
		self.payment = 0

	def down_payment(self, percentage):
		money_down = self.principle * (percentage / 100)
		self.principle -= money_down

	# monthly payment function
	def monthly_payment(self):
		fixed_rate = (self.rate / 100) / 12
		term = 12 * self.years
		self.payment = (self.principle * (1 + fixed_rate) ** term * fixed_rate) // ((1 + fixed_rate) ** term - 1)
		return self.payment

	# remaining balance function, input number of payments made
	def balance(self, payments_made):
		fixed_rate = self.rate / 100 / 12 + 1
		term = self.years * 12
		bal_form = ((fixed_rate ** term) - (fixed_rate ** payments_made)) / (fixed_rate ** term - 1)
		remaining_balance = self.principle * bal_form
		return remaining_balance


class PersonalLoan:

	"""simple interest formuala, using number of months"""

	def __init__(self, principle, rate, term_in_months):
		self.rate = rate / 100
		self.principle = principle
		self.term_in_months = term_in_months
		self.payoff_amount = 0
		self.payment = 0

	def total_loan_payoff(self):
		time_months = self.term_in_months / 12
		self.payoff_amount = self.principle * (1 + self.rate * time_months)
		return self.payoff_amount

	def view_interest_amount(self):
		return self.principle - self.payoff_amount

	def monthly_payment(self):
		self.payment = self.payoff_amount / self.term_in_months
		return self.payment


class Borrower:

	"""user's loan information"""

	def __init__(self):
		self.loan_info = {'Loan Type': None, 'Rate': None, 'Monthly Payment': None, 'Term': None, 'Principle': None}

	def __repr__(self) -> str:
		return " Terminal Program ".center(50, "*")

	def input_loan_info(self):
		print(" Enter Loan Information ".center(50, "*"))
		print("\n\n")
		self.loan_info['Loan Type'] = input("Type of Loan (mortgage or personal): ")
		if self.loan_info['Loan Type'].lower() != 'mortgage' and self.loan_info['Loan Type'].lower() != 'personal':
			raise ValueError("Wrong Loan Option")
		self.loan_info['Rate'] = float(input("Interest Rate: "))
		try:
			self.loan_info['Term'] = int(input("Loan Term (personal=months | mortgage=years): "))
			self.loan_info['Principle'] = int(input("Loan Amount: "))
		except ValueError:
			print("Value must be an integer")
			sys.exit(1)

	def append_monthly_payment(self, monthly_payment):
		self.loan_info['Monthly Payment'] = monthly_payment

	# round monthly payment to format from float value
	def output_to_csv(self,file_name):
		with open(f"{file_name}.csv", "w", encoding='UTF-8') as file:
			fields = ['Loan Type', 'Rate', 'Monthly Payment', 'Term', 'Principle']
			output = csv.DictWriter(file, fieldnames=fields)
			output.writeheader()
			self.loan_info['Monthly Payment'] = round(self.loan_info['Monthly Payment'], 2)
			loan_list = [self.loan_info]
			for item in loan_list:
				output.writerow(item)

terminal_prompt = """
                

                      _                
 /|/|   __/_ _ _ _   / )_ /_   /__/  _ 
/   |()/ /(/(/(/(-  (__(/(( (/((//()/  
         _/  _/                        
____                __                 
 /  _ _ _  '  _ /  /__)_   _ _ _ _     
(  (-/ //)//)(/(  /   / ()(// (///)    
                         _/            

 
"""

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-o", "--output", action="store_true", help="output to a csv file")
	args = parser.parse_args()
	user = Borrower()
	print(user)
	for text in terminal_prompt:
		print(text, end="", flush=True)
		sleep(0.01)
	user.input_loan_info()
	if user.loan_info['Loan Type'].lower() == 'mortgage':
		mortgage_loan = Mortgage(user.loan_info['Principle'], user.loan_info['Rate'], user.loan_info['Term'])
		money_down_percentage = int(input("Down Payment Percentage: "))
		if money_down_percentage < 0 or money_down_percentage > 100:
			raise ValueError("Enter integer between 0 and 100")
		mortgage_loan.down_payment(money_down_percentage)
		mortgage_payment = mortgage_loan.monthly_payment()
		user.append_monthly_payment(mortgage_payment)
		print("Monthly Payment --> {:.2f}\n\n".format(mortgage_payment))
		view_balance_remaining = input("View mortgage balance(y/n): ")
		if view_balance_remaining.lower() == 'y':
			try:
				num_paymets = int(input("How many payments have been made: "))
				bal = mortgage_loan.balance(num_paymets)
				print(f"Your mortgage balance is {bal:.2f}")
			except ValueError:
				print("Value must be an integer")
				sys.exit(1)
	else:
		personal_loan = PersonalLoan(user.loan_info['Principle'], user.loan_info['Rate'], user.loan_info['Term'])
		personal_loan_payoff = personal_loan.total_loan_payoff()
		personal_loan_interest = personal_loan.view_interest_amount()
		personal_loan_payment = personal_loan.monthly_payment()
		user.append_monthly_payment(personal_loan_payment)
		print(f"Total Payoff Amount --> {personal_loan_payoff:.2f}")
		print(f"Interest Amount --> {personal_loan_interest:.2f}")
		print(f"Monthly Payment --> {personal_loan_payment:.2f}\n\n")
	if args.output:
		output_filename = input("Output Filename: ")
		user.output_to_csv(output_filename)
	print("Exiting...")
if __name__ == '__main__':
	main()
sys.exit(0)
