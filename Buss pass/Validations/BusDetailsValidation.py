class BusDetailValidation:

    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def setBusDetails(self):
        details = {"Majastic_ksl": {"MKSL1": "10:00 AM", "MKSL2": "11:00", "MKSL3": "12:00"},
                   "Majastic_uttarahalli": {"MU1": "10:00 AM", "MU2": "11:00", "MU3": "12:00"},
                   "Majastic_kengeri": {"MK1": "10:00 AM", "MK2": "11:00", "MK3": "12:00"},
                   "electroniccity_ksl": {"EKSL1": "2:00 PM", "EKSL2": "2:30 PM", "EKSL3": "2:30 PM"},
                   "electroniccity_uttarahalli": {"EU1": "2:30 PM", "EU2": "2:30 PM", "EU3": "2:30 PM"},
                   "electroniccity_kengeri": {"EK1": "2:30 PM", "EK2": "2:30 PM", "EK3": "2:30 PM"},
                   "silkboard_kengeri": {"SK1": "2:00 PM", "SK2": "2:30 PM", "SK3": "2:30 PM"},
                   "silkboard_ksl": {"SKSL1": "10:00 AM", "SKSL2": "11:00", "SKSL3": "12:00"},
                   "silkboard_uttarahalli": {"SU1": "10:00 AM", "SU2": "11:00", "SU3": "12:00"}
                   }
        return details

    def validate(self):
        fetchFormat = self.source + "_" + self.destination
        details = self.setBusDetails()
        res = details.get(fetchFormat)
        return res



