import re

with open('String.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')

vid = re.findall("\W*(http:\/\/eclassesbyravindra.com\/mod\/page\/view\.php\?id=\d\d\d\d)\W*", data)

result = []
for v in vid:
	result.append("".join(re.findall("\W*(\d\d\d\d)\W*", v)))

print (list(map(int, result)))