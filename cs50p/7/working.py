import re


def main():
    print(convert(input("Hours: ").strip().lower()))


def convert(s):
    """
    Expects a str in either of the 12-hour formats below and returns the corresponding str in 24-hour format
    (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there
    will be a space before each. Assume that these times are representative of actual times,
    not necessarily 9:00 AM and 5:00 PM specifically.

    Raise a ValueError instead if the input to convert is not in either of those formats or if either
    time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start
    ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).
    """
    s = re.split(r" to ", s)
    if len(s) == 2:
        s = f"{convert_time(s[0])} to {convert_time(s[1])}"
    else:
        raise ValueError
    return(s)


def convert_time(time):
    """
    Converts one time into 24-Hour format
    """
    if not "am" in time and not "pm" in time:
        raise ValueError
    if "am" in time:
        time = re.split(r":", re.sub(r" am", "", time))
        if time[0] == "12":
            time[0] = "00"
        if len(time[0]) == 1:
            time[0] = "0" + time[0]
        if len(time) == 1:
            time.append("00")
        elif int(time[1]) < 10:
            time[1] = f"0{int(time[1])}"
        elif int(time[1]) >= 60:
            raise ValueError
    elif "pm" in time:
        time = re.split(r":", re.sub(r" pm", "", time))
        if 1 <= int(time[0]) <= 11:
            time[0] = int(time[0]) + 12
        if len(time) == 1:
            time.append("00")
        elif int(time[1]) < 10:
            time[1] = f"0{int(time[1])}"
        elif int(time[1]) >= 60:
            raise ValueError
    return f"{time[0]}:{time[1]}"


if __name__ == "__main__":
    main()
