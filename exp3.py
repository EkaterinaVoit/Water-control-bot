import schedule
import time

time_in = input()
def job():
    print("I'm working...")

#schedule.every(1).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("12:14").do(job)
#schedule.every().monday.do(job)
schedule.every().saturday.at(time_in).do(job)
#schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)