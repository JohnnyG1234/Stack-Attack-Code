from datetime import datetime

now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

other = datetime.now().time()

print(other)
