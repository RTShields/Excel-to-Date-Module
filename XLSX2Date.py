# A simple script for MS Excel writers to converte dates
# to numerics and visa versa. Generally to be imported 
# as "xtd" or "xd"

def double_digits(num,cond = True):
    if len(str(num)) < 2:
        r_num = '0' + str(num)
        return r_num
    elif num > 99:
        c_num = str(num)
        if cond == True:
            return c_num[2:]
        else:
            return c_num
    else:
        return str(num)

def X2D(data, form = 1, doubling = True):
    # Take the ##### number and conver it to readable date format
    # Easily calculate the year
    years = int(data / 365.25) + 1900

    # ### Get the Month 
    if years % 4 == 0:
        months = [31,29,31,30,31,30,31,31,30,31,30,31]  # Jan - Dec # of days for non leap year
    else:
        months = [31,28,31,30,31,30,31,31,30,31,30,31]  # Jan - Dec # of days for non leap year

    m_totals = []  # Accuring days within the month
    mt = 0
    for c in range(len(months)):
        mt += months[c]
        m_totals.append(mt)

    days_to_count = int(data - ((years - 1900) * 365.25))

    counter = 0
    for m in range(len(months)):
        if counter + months[m] < days_to_count:
            counter += months[m]
        else:
            month = m + 1
            break

    # Calculate the number of days left
    if month == 1:
        day = days_to_count
    else:
        day = days_to_count - m_totals[m-1]


    # Check for doubling
    if doubling is True:
        MM = double_digits(month)
        DD = double_digits(day)
        YY = double_digits(years)
    else:
        MM = str(month)
        DD = str(day)
        YY = str(years)

    # ### Grab the format number and return said string
    if form == 1:  # MM/DD/YYYY
        string = MM + '/' + DD + '/' + double_digits(years,False)
    elif form == 2:  # MM/DD/YY
        string = MM + '/' + DD + '/' + double_digits(years,True)
    elif form == 3:  # YYYY/MM/DD
        string = double_digits(years,False) + '/' + MM + '/' + DD
    else:  # YY/MM/DD
        string = double_digits(years,True) + '/' + MM + '/' + DD


    return string


def D2X(data):
    # Ex. Day 1 equals 1/1/1900,):

    if data.find('/') != -1:
        # ### Find the slashes to split up the date 
        slashes = []
        for char in range(len(data)):
            if data[char] == '/':
                slashes.append(char)

        # ### Make sure there are two /'s
        if len(slashes) < 2:
            print('Error: invalid format.')
            return
        else:
            # ### Separate date string into components
            part1 = data[:slashes[0]]
            part2 = data[slashes[0] + 1:slashes[1]]
            part3 = data[slashes[1]+1:]
            if len(part1) < 3 and int(part1) < 31:  # Make sure this isn't a disguised year format
                MM = int(part1)
                DD = int(part2)
                YY = int(part3)
            else:
                YY = int(part1)
                MM = int(part2)
                DD = int(part3)

            # ### Calculator how many days in YY Years
            years_to_days = int((YY - 1900) * 365.25)


            # ### Calculate how many days in in the months leading up to given date
            if YY % 4 == 0:
                months = [31,29,31,30,31,30,31,31,30,31,30,31]  # Jan - Dec # of days for non leap year
            else:
                months = [31,28,31,30,31,30,31,31,30,31,30,31]  # Jan - Dec # of days for non leap year

            months_to_days = 0
            for m in range(MM-1):
                months_to_days += months[m]

            # ### Give final number out
            days_total = years_to_days + months_to_days + DD
            return readout

    else:
        print('Error: invalid format.')
        return
