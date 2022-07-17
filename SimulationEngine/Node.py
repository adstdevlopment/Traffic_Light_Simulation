from SimulationEngine.EngineObject import EngineObject


class Node(EngineObject):
    def __init__(self, id_node, x, y, type_cross, nodes, traffic_light):
        super().__init__()
        self.id = id_node
        self.x = x
        self.y = y
        self.type = type_cross
        self.nodes = nodes
        self.traffic_light = traffic_light
