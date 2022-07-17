import json
import os

from Simulation.City import City
from SimulationEngine.Node import Node

os.chdir("D:/_PROJET/_SIMULATION/Feux rouges/CodeV2")


class Importer:
    def __init__(self):
        self.data_file = "data.json"
        self.data = None

        self.list_city = []

    def import_cities(self):
        with open(self.data_file) as json_file:
            self.data = json.load(json_file)
            for data in self.data["city"]:
                # Create the city
                self.list_city.append(City(data['name_city']))

                # Generate the city nodes
                for node_data in data['Nodes']:
                    self.list_city[-1].list_nodes.append(Node(node_data["id"],
                                                              node_data["x"],
                                                              node_data["y"],
                                                              node_data["type"],
                                                              node_data["nodes"],
                                                              node_data["traffic_light"]))
        return self.list_city
