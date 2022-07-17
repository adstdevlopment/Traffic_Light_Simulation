from DataManagement.Importer import Importer


class Simulation:
    def __init__(self):
        self.importer = Importer()
        self.list_city = []
        self.list_thread_vehicles = []

    def start(self):
        self.generate_cities()

    def generate_cities(self):
        self.importer.import_cities()
        self.list_city = self.importer.list_city
