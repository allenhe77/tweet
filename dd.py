from datetime import datetime

# current date and time
now = datetime.now()

timestamp = datetime.timestamp(now)
tt = datetime.utcfromtimestamp(timestamp).strftime('%Y%m%d%H%M%S')
print(type(tt))
