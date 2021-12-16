from timeit import default_timer as timer

start = timer()
# ...
end = timer()
print(end - start)
                h, rem = divmod((t1 - t2), 3600)
                m, sec = divmod(rem, 60)
                print("-> Time taken for previous transfer: {:0>2}:{:0>2}:{:0>2}".format(int(h), int(m), int(sec)))




def findDay(date):
    day, month, year = (int(i) for i in date.split(' '))   
    born = datetime.date(year, month, day)
    return born.strftime("%A")





def findDay(date):
    day, month, year = (int(i) for i in date.split(' '))   
    dayNumber = calendar.weekday(year, month, day)
    days =["Monday", "Tuesday", "Wednesday", "Thursday",
                         "Friday", "Saturday", "Sunday"]
    return (days[dayNumber])
