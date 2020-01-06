def parse_str_to_date(date):
    """ Given some date as a string, will attempt to parse it to a date, if it can be split into
    3 or more sections of numeric characters seperated by non-numeric characters. Otherwise, it will
    check if there are exactly eight digits: if so, it will split the string into YYYYMMDD compontents.
    Otherwise, it will fail. """
    import re
    from datetime import datetime
    date_str_arr = list(filter(lambda x: x.isdigit(), re.split(r"(\d+)", date)))
    if len(date_str_arr) < 3:
        date_str = "".join(date_str_arr)
        if len(date_str) != 8:
            raise ValueError("Insufficient digits to reconstruct a YYYY-mm-dd date")
        else:
            date_str_arr.clear()
            date_str_arr.append(date_str[:4])
            date_str_arr.append(date_str[4:6])
            date_str_arr.append(date_str[6:])

    date = datetime.strptime("-".join(date_str_arr[:3]), "%Y-%m-%d")
    return date
