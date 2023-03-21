class Visitor:

    def __init__(self, n):
        if type(n) == str:
            self._name = n
        self._trips_list = []
        self._parks_set = set([])
    
    def get_name(self):
        return self._name
    def set_name(self, n):
        if type(n) == str:
            self._name = n
    
    def get_trips(self):
        return self._trips_list
    def set_trips(self, t):
        if type(t) == type(self._trip):
            self._trips_list = t
    def add_trip(self, t):
        self._trips_list.append(t)
    
    def trips(self):
        return self.get_trips()

    def nationalparks(self):
        return list(self._parks_set)

    def add_park(self, p):
        self._parks_set.add(p)

    name = property(get_name, set_name)
    visitor = property(get_trips, set_trips)