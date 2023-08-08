# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main

print(
  'The starting time must include hour:minute PM/AM.\nFor example "4:55 PM" or "12:08 AM").'
)
start_time = input('What is the starting time?  ')
weekday = input('Day of the week? ')
duration = input(
  'Duration? (How many hours and minutes after the starting time) ')
print(add_time(start_time, duration, weekday))

# Run unit tests automatically
# main(module='test_module', exit=False)
