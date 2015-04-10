def the_sum(list):
	sum=0
	for x in range (0,len(list)):
		sum+=list[x]
	return (sum)
def average(list):
	avrg=totalsum(list)/10
	return (avrg)

def standardeviation(list):
	std= statistics.stdev(list)
	return (std)

list=[]

x=0

while(x<10):

	num=(float(input("Write some numbers for the list:")))
	list.append(num)
	x=x+1

tsum = the_sum(list)
avr = average(list)
stan = standardeviation(list)

print("The sum of the list is:",tsum)
print("The average of the list is:",avr)
print("The standard deviation of the list is:",stan)
