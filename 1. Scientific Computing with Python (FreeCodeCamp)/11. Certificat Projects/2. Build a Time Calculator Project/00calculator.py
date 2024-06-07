def add_time(start, duration, day=None):
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    lower_week = [word.lower() for word in week]
  
    start_time = ''
    start_hour = ''
    start_minutes = ''
    start_period = ''
  
    duration_hour = ''
    duration_minutes = ''
  
    period = ''
    message = ''

    start_time, start_period = start.split()
    start_hour, start_minutes = map(int,start_time.split(":"))

    duration_hour, duration_minutes = map(int,duration.split(":"))

    if start_period == 'PM' and start_hour != 12:
        start_hour += 12
    elif start_period == 'AM' and start_hour == 12:
        start_hour = 0

    final_hour = start_hour + duration_hour
    final_minutes = start_minutes + duration_minutes

    days = final_hour / 24
    
    if final_minutes >= 60:
        final_hour += final_minutes // 60
        final_minutes = int(final_minutes % 60)

    if final_hour == 0:
        period = 'AM'
        final_hour += 12
    elif final_hour < 12:
        period = 'AM'
    elif final_hour == 12:
        period = 'PM'

    elif final_hour > 12:
        if (final_hour // 12) % 2 == 0:
            period = 'AM'
        elif (final_hour // 12) % 2 != 0:
            period = 'PM'
        final_hour = int(final_hour % 12)
    
    if period == 'AM' and final_hour == 00:
        final_hour += 12

    if day:
        index = lower_week.index(day.lower())
        if days < 1:
            message = f', {week[index]}'
        elif round(days) == 1:
            message = f', {week[index + 1]} (next day)'
        else:
            index = (index + round(days) % 7) % len(week)
            message = f', {week[index]} ({round(days)} days later)'
    else:
        if days < 1:
            message = ''
        elif round(days) == 1:
            message = f' (next day)'
        else:
            message = f' ({round(days)} days later)'

    new_time = f'{final_hour}:{final_minutes:02} {period}{message}'

    return new_time
