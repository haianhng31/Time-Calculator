def add_time(start, duration, weekday = False):
  # Take out the start time 
  start_comp = start.replace(":"," ").split()
  start_hour = int(start_comp[0])
  start_minute = int(start_comp[1])
  start_daytime = start_comp[2]
  
  if start_daytime == "PM":
    start_hour += 12 

  # Take out the duration time 
  dur_comp = duration.split(":")
  dur_hour = int(dur_comp[0])
  dur_minute = int(dur_comp[1])
  dur_day = dur_hour//24
  
  # Calculate the end time 
  end_hour = start_hour + dur_hour%24
  if end_hour >= 24:
    dur_day += 1
    end_hour -= 24
  
  end_minute = start_minute + dur_minute
  if end_minute >= 60:
    end_hour += 1
    end_minute -= 60 
    if end_hour >= 24:
      dur_day += 1
      end_hour -= 24

  if end_hour == 0:
    end_daytime = 'AM'
    end_hour = 12
  elif end_hour<12:
    end_daytime = 'AM'
  elif end_hour == 12:
    end_daytime = 'PM'
  elif end_hour >12:
    end_daytime = 'PM'
    end_hour -= 12
  

  # Convert to strings 

  end_minute = str(end_minute)
  if len(end_minute) < 2:
    end_minute = "".join([str(0),end_minute])

  if dur_day > 1:
    end_day = '('+ str(dur_day) + ' days later)'
  if dur_day == 1:
    end_day = '(next day)'

  # Calculate days in week 
  weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  if weekday: 
    for i in range(len(weekdays)):
      if weekdays[i].lower() == weekday.lower():
        end_weekday = weekdays[(i+dur_day)%7]
        end_weekday = ', ' + end_weekday
  
  new_time = str(end_hour) + ':' + str(end_minute) + ' ' + end_daytime

  if weekday: 
    new_time = "".join([new_time,end_weekday])
  if dur_day != 0:
    new_time = " ".join([new_time,end_day])
    
  return new_time
    