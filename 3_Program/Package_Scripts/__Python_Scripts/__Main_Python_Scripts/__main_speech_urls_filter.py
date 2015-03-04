
def filterSpeechURL():
	import csv 
	with open('speechurls.csv', 'rU') as f:
		for row in csv.reader(f):

			#Filter President Obama
			if 'remarks-president' in row[0]:
				with open('__president_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'weekly-address' in row[0]:
				with open('__president_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'letter' in row[0]:
				with open('__president_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'statement-president' in row[0]:
				with open('__president_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'president-obama' in row[0]:
				with open('__president_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'excerpts-president' in row[0]:
				with open('__president_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))


			#Filter First Lady
			elif 'remarks-first-lady' in row[0]:
				with open('__first-lady_urls.csv', 'a') as f2: f2.write("{}\n".format(row[0]))


			#Filter VP
			elif 'vice-president' in row[0]:
				with open('__vice_president_urls.csv', 'a') as f2: f2.write("{}\n".format(row[0]))


			#Filter Jill Biden
			elif 'jill' in row[0]:
				with open('__second-lady_urls.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'dr-biden' in row[0]:
				with open('__second-lady_urls.csv', 'a') as f2: f2.write("{}\n".format(row[0]))


			#Filter Everthing Else
			else:
				with open('__other_urls.csv', 'a') as f2: f2.write("{}\n".format(row[0]))

filterSpeechURL()
