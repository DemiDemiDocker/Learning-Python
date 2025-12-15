import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')  # Overwrite the line each second
        time.sleep(1)
        t -= 1

    print("Fire in the hole!!")

user_input = input("Enter the time (format: MM:SS or just minutes): ")

# Check if input contains a colon (MM:SS format)
if ':' in user_input:
    parts = user_input.split(':')
    minutes = int(parts[0])
    seconds = int(parts[1])
    total_seconds = minutes * 60 + seconds
else:
    # If no colon, treat as minutes only
    minutes = int(user_input)
    total_seconds = minutes * 60

countdown(total_seconds)