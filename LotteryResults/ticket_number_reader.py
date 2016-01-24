class TicketNumberReader:
	def __init__(self):
		pass

	def get_numbers_from_file(self, file_name):
		tickets_file = open(file_name)
		tickets = []
		for ticket in tickets_file:
			if ticket.rstrip() == '':
				continue
			ticket_numbers_str = ticket.rstrip().split()
			ticket_numbers = [int(ticket_number) for ticket_number in ticket_numbers_str]
			tickets.append(ticket_numbers)

		tickets_file.close()
		return tickets

instance = None

def create_instance(function):
	global instance
	if not instance:
		instance = TicketNumberReader()
	return function

@create_instance
def get_numbers_from_file(file_name):
	return instance.get_numbers_from_file(file_name)

def main():
	#print get_numbers_from_file('ticket_numbers.txt')
	print get_numbers_from_file('ticket_numbers_combined.txt')

if __name__ == '__main__':
	main()