wakeTime = str(raw_input('Please input the wake time for the alarm in format HH:MM: \n '))
sleepTime = str(raw_input('Please input the sleep time for the alarm in format HH:MM: (Default 16 hours from wakeTime) \n '))

wakeTime = wakeTime.split(':')

if sleepTime == '':
    sleepTime = int(wakeTime[0]) + 16
else:
    sleepTime = sleepTime.split(':')

print('1/8: ' + str(int(wakeTime[0]) + 2) + ':' + wakeTime[1])
print('2/8: ' + str(int(wakeTime[0]) + 4) + ':' + wakeTime[1])
print('3/8: ' + str(int(wakeTime[0]) + 6) + ':' + wakeTime[1])
print('4/8: ' + str(int(wakeTime[0]) + 8) + ':' + wakeTime[1])
print('5/8: ' + str(int(wakeTime[0]) + 10) + ':' + wakeTime[1])
print('6/8: ' + str(int(wakeTime[0]) + 12) + ':' + wakeTime[1])
print('7/8: ' + str(int(wakeTime[0]) + 14) + ':' + wakeTime[1])
print('8/8: ' + str(int(wakeTime[0]) + 16) + ':' + wakeTime[1])