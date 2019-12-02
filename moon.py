import collections

Mars_time = collections.namedtuple('Mars_time',['hour','minute'])

class Moon:

    def __init__(self, hour_rise, minute_rise, hour_set, minute_set, name):

        self.name = name
        self.time_rise = Mars_time(hour_rise,minute_rise)
        self.time_set = Mars_time(hour_set,minute_set)

    def __repr__(self):
        return f'---{self.name}---\nTime rise {self.time_rise.hour}:{self.time_rise.minute}\nTime set {self.time_set.hour}:{self.time_set.minute}\n'

    def time_to_minutes(self,time):
        return time.hour*100 + time.minute
    
    def get_time_rise_minutes(self):
        return self.time_rise.hour*100 + self.time_rise.minute
    
    def get_time_set_minutes(self):
        return self.time_set.hour*100 + self.time_set.minute
    
    def calculate_overlap_time(self,moon2):
        MARS_MAX_TIME = 2500
        
        moon1 = self
        moon1_time_set, moon1_time_rise = moon1.get_time_set_minutes(), moon1.get_time_rise_minutes()
        moon2_time_set, moon2_time_rise = moon2.get_time_set_minutes(), moon2.get_time_rise_minutes()

        if moon1_time_rise==0 and moon1_time_rise==moon1_time_set and moon2_time_set==moon1_time_set and moon2_time_rise==moon2_time_set:
            return MARS_MAX_TIME
            
        if moon1_time_rise == moon2_time_set or moon2_time_rise==moon1_time_set:
            return 1
        
        
        #Wenn Monde vor Mitternacht aufgehen und nach Mitternacht untergehen, dann wird auf die Untergangszeit die max Marszeit dazuaddiert
        if moon1_time_rise>moon1_time_set:
            moon1_time_set = moon1_time_rise + moon1_time_set + (MARS_MAX_TIME - moon1_time_rise)
        if moon2_time_rise>moon2_time_set:
            moon2_time_set = moon2_time_rise + moon2_time_set + (MARS_MAX_TIME - moon2_time_rise)


        list_moon1 = [ x % MARS_MAX_TIME for x in range(moon1_time_rise,moon1_time_set)]
        list_moon2 = [ x % MARS_MAX_TIME for x in range(moon2_time_rise,moon2_time_set)]
        list_both = set(list_moon1) & set(list_moon2)
        return len(list_both)
