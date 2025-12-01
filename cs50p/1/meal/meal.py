"""
Program prompts the user for a time and outputs whether it's breakfast time,
lunch time, or dinner time. If it's not time for a meal, don't output anything at all.
Assume that the user's input will be formatted in 24-hour time as #:## or ##:##.
And assume that each meal's time range is inclusive. For instance, whether it's 7:00,
7:01, 7:59, or 8:00, or anytime in between, it's time for breakfast.
"""
def main():
    time = input("What time is it? ")
    time = convert(time)
    if time >= 7 and time <= 8:
        print("breakfast time")
    if time >= 12 and time <= 13:
        print("lunch time")
    if time >= 18 and time <= 19:
        print("dinner time")


def convert(time):
    """
    Function converts time, a str in 24-hour format, to the corresponding number of hours as a float.
    For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes),
    convert should return 7.5 (i.e., 7.5 hours).
    """
    hours, minutes = time.split(":")
    if minutes.endswith("p.m."):
        minutes = minutes.removesuffix(" p.m.")
        hours = int(hours) + 12
    else:
        minutes = minutes.removesuffix(" a.m.")
    minutes = int(minutes) / 60
    return(int(hours) + minutes)

if __name__ == "__main__":
    main()