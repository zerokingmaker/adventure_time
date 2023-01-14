class wrongspecialisationError(Exception):
    def __init__(self, specialisation):
        self.specialisation = specialisation
    
    def __str__(self):
        return 'Your specialization must be either mage or warior but you have : ' + self.specialisation 