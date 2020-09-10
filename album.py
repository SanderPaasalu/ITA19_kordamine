class Album:
    # Loodud klass album ja sellele antud klassi omadus
    # ja koht kuhu saab laule panna
    def __init__(self, pealkiri, laulja, aasta):
        self.pealkiri = pealkiri
        self.laulja = laulja
        self.aasta = aasta
        self.laulud = []
