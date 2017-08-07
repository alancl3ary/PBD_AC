
changes_file = 'changes_python.log'

data = [line.strip() for line in open(changes_file, 'r')]

print(len(data))

sep = 72*'-'

commits = []
#current_commit = None
index = 0

while index < len(data):

	try:
		details = data[index + 1].split(' | ')
		#print details
		commits.append({'revision': details[0], 'author':details[1], 'date': details[2]})
		commits.append(commit)
		index = data.index(sep, index +1)
	except IndexError:
		break
		
#print len(commits)

output_file = 'changes.csv'
my_file = open(output_file, 'w')
my_file.write('Revision,Author,Date\n')
for details in commits:
	my_file.write(commit['revision'] + ',' + commit['author'] + ',"' + commit['data'] + '"\n ')
	#details[0].strip() + ',' + details[1].strip() + ',"' + details[2].strip() + '"\n')

my_file.close()

