import ticket_number_reader

class LotteryResults:
	def __init__(self):
		self.tickets = None

	def get_winnings(self, winning_numbers):
		if not self.tickets:
			raise Exception('Ticket Numbers Not Set.')

		total_prize = 0
		for ticket in self.tickets:
			total_prize += self.get_winnings_for_single_ticket(ticket, winning_numbers)
		return total_prize

	def get_winnings_for_single_ticket(self, ticket_numbers, winning_numbers):
		ticket_normal_numbers = ticket_numbers[:-1]
		ticket_powerball = ticket_numbers[-1]

		winning_normal_numbers = winning_numbers[:-1]
		winning_powerball = winning_numbers[-1]

		matching_powerball = self.matching_powerball(ticket_powerball, winning_powerball)
		matching_normal_numbers = self.matching_normal_numbers(ticket_normal_numbers, winning_normal_numbers)
		prize = self.get_prize(matching_normal_numbers, matching_powerball)
		if prize:
			print '%s: $%s' % (ticket_numbers, prize)
		return prize

	def matching_normal_numbers(self, ticket_normal_numbers, winning_normal_numbers):
		count = 0
		for winning_number in winning_normal_numbers:
			count += ticket_normal_numbers.count(winning_number)
		return count

	def matching_powerball(self, ticket_powerball, winning_powerball):
		if ticket_powerball == winning_powerball:
			return 1
		return 0

	def get_prize(self, matching_normal_numbers, matching_powerball):
		if matching_normal_numbers == 5 and matching_powerball == 1:
			return 800000000
		elif matching_normal_numbers == 5 and matching_powerball == 0:
			return 1000000
		elif matching_normal_numbers == 4 and matching_powerball == 1:
			return 50000
		elif matching_normal_numbers == 4 and matching_powerball == 0:
			return 100
		elif matching_normal_numbers == 3 and matching_powerball == 1:
			return 100
		elif matching_normal_numbers == 3 and matching_powerball == 0:
			return 7
		elif matching_normal_numbers == 2 and matching_powerball == 1:
			return 7
		elif matching_normal_numbers == 1 and matching_powerball == 1:
			return 4
		elif matching_normal_numbers == 0 and matching_powerball == 1:
			return 4
		else:
			return 0

	def set_tickets(self, tickets):
		self.tickets = tickets

	def print_tickets(self):
		for ticket in self.tickets:
			print ticket


lottery_reader = LotteryResults()

def print_tickets_test():
	print 'Current Tickets:'
	lottery_reader.print_tickets()
	print ''

def print_winnings_test(winning_numbers):
	print 'Winning Numbers:\n', winning_numbers, '\n'
	total_winnings = lottery_reader.get_winnings(winning_numbers)
	print '\nTotal Prize:\n$%s' % total_winnings

def get_prize_test():
	print lottery_reader.get_prize(3, 1)
	print lottery_reader.get_prize(0, 0)
	print lottery_reader.get_prize(4, 1)

def load_lottery_tickets(tickets_file):
	tickets = ticket_number_reader.get_numbers_from_file(tickets_file)
	lottery_reader.set_tickets(tickets)

def run_jan_9_drawing():
	load_lottery_tickets('ticket_numbers_combined.txt')
	winning_numbers = [32,16,19,57,34,13]
	print_winnings_test(winning_numbers)

def run_jan_13_drawing():
	load_lottery_tickets('ticket_numbers_jan_13.txt')
	winning_numbers = [4,8,19,27,34,10]
	print_winnings_test(winning_numbers)

def main():
	#run_jan_9_drawing()
	run_jan_13_drawing()
	#print_tickets_test()
	#get_prize_test()
	#winning_numbers = [1, 2, 3, 4, 5, 6]
	#winning_numbers = [2, 11, 47, 62, 63, 17]
	
if __name__ == '__main__':
	main()