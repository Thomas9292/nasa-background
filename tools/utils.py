def parse_str_to_date(date):
    """ Given a date which is a string, will attempt to parse it by first splitting the string on its non numeric characters,
    and then by partitioning YYYYMMDD from the string. """
    import re
    from datetime import datetime
    date_str_arr = list(filter(lambda x: x.isdigit(), re.split(r"(\d+)", date)))
    if len(date_str_arr) != 3:
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
