'''
calender, time for both of us
write algorithm that will take 2 people's calendars and return free slots of time that these 2 can have a meeting
calendars are lists of tuples of lists of lsits of length 2
'''

calendar1 = [['9:00', '10:30'],['12:00', '13:30'],['16:00', '18:00']]
dailyBounds1 = ['9:00', '20:00']
calendar2 = [['10:00', '11:30'],['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
dailyBounds2 = ['10:00', '18:30']
duration = 30

'''
c1s c2s c2e c1e
c1s c2s c1e c2e
c1s c1e c2s c2e - 
c2s c1s c1e c2e
c2s c1s c2e c1e
c2s c2e c1s c1e -

c1s dbs dbe c1e x
c1s dbs c1e dbe c1e -> dbe
c1s c1e dbs dbe x
dbs c1s c1e dbe dbs -> c1s , c1e -> dbe, split
dbs c1s dbe c1e
dbs dbe c1s c1e


'''

def compareTimes(t1, t2):
	
	h1, m1 = t1.split(':')
	h2, m2 = t2.split(':')

	m1  = int(h1)*60 + int(m1)
	m2  = int(h2)*60 + int(m2)
	if m1 == m2:
		return 0
	elif m1 < m2:
		return -1
	else:
		return 1

def minTime(t1, t2):
	if compareTimes(t1, t2) == -1:
		return t1
	else:
		return t2

def maxTime(t1, t2):
	if compareTimes(t1, t2) == 1:
		return t1
	else:
		return t2

def mergeCalendars(c1, c2):
	while len(c1) > 0:
		changed = False
		for j in range(len(c2)):
			# print('c1: ', c1)
			# print('c2: ', c2)
			c1start, c1end = c1[0]
			c2start, c2end = c2[j]

			# Not Connecting
			if compareTimes(c1end, c2start) == -1 or compareTimes(c2end, c1start) == -1:
				continue

			start = minTime(c1start, c2start)
			end = maxTime(c1end, c2end)

			# print('merging')
			# Connecting Times

			c1[0] = [start, end]
			c2.pop(j)
			changed = True
			break

		if not changed:
			c2.append(c1.pop(0))
	return c2


def findAvailableTimes(bounds, c):
	availableTimes = []
	# Start
	if compareTimes(bounds[0], c[0][0]) == -1:
		availableTimes.append([bounds[0], c[0][0]])

	i = 1
	while i < len(c):
		at = [c[i-1][1], c[i][0]] # available Times
		print(at)

		start = maxTime(at[0], bounds[0])
		end = minTime(at[1], bounds[1])
		availableTimes.append([start, end])
		i += 1

	# End
	if compareTimes(bounds[1], c[-1][1]) == 1:
		availableTimes.append([c[-1][1], bounds[1]])
	return availableTimes

bounds = [maxTime(dailyBounds1[0], dailyBounds2[0]), minTime(dailyBounds1[1], dailyBounds2[1])]

c2 = mergeCalendars(calendar1, calendar2)
print('bounds', bounds)
print('c2', c2)

c = findAvailableTimes(bounds, c2)
print('c', c)

