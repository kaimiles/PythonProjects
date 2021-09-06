max_mins = 60
timelist = []
addtimelist = []
daylist = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def add_time(inputtime, addedtime, day = ''):
    [starttime, ampm] = inputtime.split()
    [hour, mins] = starttime.split(':')
    [addhour, addmins] = addedtime.split(':')

    assert hour.isnumeric() and mins.isnumeric(), 'Enter valid time'
    assert int(hour) <= 24 and int(mins) <= max_mins, 'Enter valid time'

    newhour = int(hour) + int(addhour)
    newmins = int(mins) + int(addmins)

    if newmins >= max_mins:
        newhour = newhour + 1
        newmins = newmins - 60

    if newmins < 10:
        newmins = "{:0>2d}".format(newmins)

    if newhour < 24:
        newhour = newhour % 12
    elif newhour >= 24:
        Newhour = newhour % 24
        dayAfter = newhour // 24

    ampm = 'PM' if newhour >= 12 else 'AM'

    if day:
        index = daylist.index(day.lower().capitalize())
        weekDay = daylist[index + dayAfter] if dayAfter else day
        weekDay = weekDay.lower().capitalize()
        if dayAfter == 1:
            weekDay = weekDay + '(next day)'
        else:
            weekDay + '(' + str(dayAfter) + 'days later)'

        new_time = str(Newhour) + ':' + str(newmins) + ' ' + ampm
        if weekDay:
            new_time = new_time + ',' + weekDay
        elif dayAfter:
            new_time = new_time + '(next day)' if dayAfter == 1 else weekDay + '(' + dayAfter + 'days later)'

    new_time = print(new_time)
    return new_time


add_time("3:43 PM", "48:20", "tueSday")
