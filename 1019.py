N = int(input())
seconds = N%60
if (seconds<60):
	seconds = seconds
else:
	seconds = seconds - 60

minutes = int(N/60)
hours = int(minutes/60)

if(minutes < 60):
	minutes = minutes
else:
	minutes = minutes%60
hours = str(hours)
minutes = str(minutes)
seconds = str(seconds)
print(hours+':'+minutes+':'+seconds)