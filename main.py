from dateutil.easter import *
import datetime
if __name__ == "__main__":
    now = datetime.datetime.now()
    easter = easter(now.year)
    print(f"Hello world. Today is {now.strftime('%Y-%m-%d')}. The easter in this year is on {easter.strftime('%Y-%m-%d')}")
