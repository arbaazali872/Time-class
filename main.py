class Time:
    def __init__(self,hours, minutes, seconds):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds
    def display(self):
        print(f'{self.hours} hrs and {self.minutes} mins and {self.seconds} seconds')
    def addTime(self,  second):
        n_sec= self.seconds + second.seconds
        n_minutes= self.minutes + second.minutes
        n_hours= self.hours + second.hours
        if n_sec>=60:
            #if sum of seconds goes beyond 60 we will add 1 into minute and update second
            # to the diffrence of sum of seonds and 60
            n_minutes+=1
            n_sec-=60
        if n_minutes>=60:
            # if sum of minutes goes beyond 60 we will add 1 into hours and update second
            # to the diffrence of sum of minutes and 60
            n_hours+=1
            n_minutes-=60
        return f'{n_hours} hrs and {n_minutes} mins and {n_sec} seconds'
    def DisplaySecond(self):
        new_sec=self.seconds
        new_sec+= self.minutes * 60
        new_sec+= self.hours * 3600
        return f'{new_sec} seconds'


t1=Time(2,50,10)
t1.display()
t2=Time(1,20,5)

print(t1.addTime(t2))
#to check the seconds in our time
t3=Time(1,2,0)
print(t3.DisplaySecond())
