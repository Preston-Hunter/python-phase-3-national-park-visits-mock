from .trip import Trip

class NationalPark:

    def __init__(self, n):
        if type(n) == str:
            self._name = n
        self._trips_list = []
        self._visitors_set = set([])
    
    def get_name(self):
        return self._name
    def set_name(self, n):
        print("Im sorry Dave, I cant let you do that")

    def get_trips(self):
        return self._trips_list
    def set_trips(self, t):
        if type(t) == type(self._trip):
            self._trips_list = t
    def add_trip(self, t):
        self._trips_list.append(t)
    
    def trips(self):
        return self.get_trips()

    def visitors(self):
        return list(self._visitors_set)
    def add_visitor(self, v):
        self._visitors_set.add(v)

    name = property(get_name, set_name)