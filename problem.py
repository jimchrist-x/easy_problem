import sys

tries = 1

while 1:
	try:
		
		user_in = int(input('\n number needs to be shown: 1010101\n' + 'Your number: '))
		answer = user_in * 10001




		
		if answer == 1010101:
			print('The answer is: ' + str(answer) + '\nis right!')
			print('You tried ' + str(tries), 'times')
			tries = 1
		elif user_in == 1:
			print('Number 1 is not an option')
		else:
			print('The answer: ' + str(answer) + '\nis wrong!')
			tries += 1
			
				

	except KeyboardInterrupt:
		print('\n\nnever give up!')
		sys.exit()
	except ValueError:
		print('Only numbers you cheater!')


