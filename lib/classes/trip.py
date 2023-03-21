
class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self._visitor = visitor
        self._national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        visitor.add_trip(self)
        national_park.add_trip(self)
        national_park.add_visitor(visitor)
        visitor.add_park(national_park)
        
    def get_visitor(self):
        return self._visitor

    def set_visitor(self, v):
        if type(v) == type(self._visitor):
            self._visitor = v
        else:
            print("invalid argument for set_vistitor")

    def get_park(self):
        return self._national_park

    def set_park(self, p):
        if type(p) == type(self.national_park):
            self._national_park = p
        else:
            print("invalid argument for set_vistitor")

    national_park = property(get_park, set_park)
    visitor = property(get_visitor, set_visitor)