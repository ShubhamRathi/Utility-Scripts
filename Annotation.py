import pandas as pd
from difflib import SequenceMatcher
# Trim ACTORS_INVOLVED
df = pd.read_csv('Venu.csv')
inp = "y"
for index, row in df.iterrows():
	if inp == "y":
		r = row['ACTORS_INVOLVED'].split(",")
		# print r
		for n,i in enumerate(r):
			if (i.startswith('IGO') or i.startswith('NGO')):
				r[n]=i[0:6]
			else:
				r[n]=i[0:3]
		# print r
		df.set_value(index, 'ACTORS_INVOLVED', ','.join(r))
		# inp = raw_input("Continue?\n")
# ------------------------
#count = 0
for index1, row1 in df.iterrows():
	s1=row1['ACTORS_INVOLVED'].split(",")
	print "__________________________________________  "+str(int(101+index1))+"  ________________"
	print s1
	print "ID: "+ str(row1['ID'])	
	print "TOPIC: "+ str(row1['TOPIC'])
	print "SENTENCE: "+str(row1['SENTENCE'])
	print "______________________________________________________________________________________"
	print "\n\n"
	inp = ''
	for index2, row2 in df.iterrows():
		if index1 != index2:
			if inp == '':
				s2=row2['ACTORS_INVOLVED'].split(",")
				# if ((set(s1) == set(s2)) and (row1['LOCATION']==row2['LOCATION'] or row1['LOCATION_CITIES']==row2['LOCATION_CITIES'] or row1['LOCATION_STATES']==row2['LOCATION_STATES'] or row1['LOCATION_COUNTRIES']==row2['LOCATION_COUNTRIES'])): # Full Coreference
				# 	#count = count + 1
				# 	print s2
				# 	print "#"+str(int(101+index2))
				# 	print "ID: "+row2['ID']
				# 	print "TOPIC: "+str(row2['TOPIC'])
				# 	print "SENTENCE: "+row2['SENTENCE']
				if ((set(s1) != set(s2)) and (len(set(s1).intersection(s2))>0)): # Mixed Event
					#count = count + 1
					ratio = SequenceMatcher(None, row2['SENTENCE'], row1['SENTENCE']).ratio()
					if (ratio > 0.7):
						print ratio
						print s2
						print "#"+str(int(101+index2))
						print "ID: "+row2['ID']
						print "TOPIC: "+str(row2['TOPIC'])
						print "SENTENCE: "+row2['SENTENCE']
						inp=raw_input("Continue?\n")
#print count
