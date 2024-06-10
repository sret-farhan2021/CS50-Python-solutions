months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]

def date(date):
    if "/" in date:
        date=date.strip(" ")
        date_parts = date.split("/")
        year = date_parts[-1]
        month = date_parts[0]
        day = date_parts[1]

        if month in months:
            return None

        list = [year,month,day]
        return list

    elif "," in date:
        date_parts = date.split(",")
        year = date_parts[-1].strip(" ")
        date_parts = date_parts[0]
        month,day = date_parts.split()

        if day in months:
            return None

        month = str(months.index(month) + 1).strip(" ")
        list=[year,month,day]
        return list
    return None

while True:
    var = input("Enter date:")
    date1=date(var)

    if date1:
        year = date1[0]
        month = date1[1]
        day = date1[2]

        int_month = int(month)
        int_day = int(day)

        if int_month<=12 and int_month>=1 and int_day>=1 and int_day<=31:
            print(f"{year}-{month.zfill(2)}-{day.zfill(2)}")
            break
