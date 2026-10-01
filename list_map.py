from name import station_names, stations, lines_to_stations

class Station:
    def __init__(self, sid, order_index):
        self.sid = sid 
        self.order_index = order_index 
        self.left = None
        self.right = None
        self.height = 1

class StationGroup:
    def insert_node(self, root, sid, order_index):
        if not root:
            return Station(sid, order_index)
        elif order_index < root.order_index:
            root.left = self.insert_node(root.left, sid, order_index)
        else:
            root.right = self.insert_node(root.right, sid, order_index)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balanceFactor = self.getBalance(root)

        if balanceFactor > 1 and order_index < root.left.order_index:
            return self.rightRotate(root)
        if balanceFactor > 1 and order_index > root.left.order_index:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balanceFactor < -1 and order_index > root.right.order_index:
            return self.leftRotate(root)
        if balanceFactor < -1 and order_index < root.right.order_index:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            if root.left:
                print('->', end="")
            print(f"【 {station_names[root.sid]} 】", end="")
            if root.right:
                print('->', end="")
            self.inorder(root.right)

    def getHeight(self, root):
        return root.height if root else 0

    def getBalance(self, root):
        return self.getHeight(root.left) - self.getHeight(root.right) if root else 0

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

class Line:
    def __init__(self, line_name):
        self.line_name = line_name
        self.stations_root = None
        self.left = None
        self.right = None

class MrtMap:
    def __init__(self):
        self.root = None

    def insert_line(self, root, line_name):
        if not root:
            return Line(line_name)
        elif line_name < root.line_name:
            root.left = self.insert_line(root.left, line_name)
        else:
            root.right = self.insert_line(root.right, line_name)
        return root

    def add_station(self, line_root, line_name, sid, order_index):
        line_node = self.search_line(line_root, line_name)
        if line_node:
            line_tree = StationGroup()
            line_node.stations_root = line_tree.insert_node(line_node.stations_root, sid, order_index)

    def search_line(self, root, line_name):
        if not root or root.line_name == line_name:
            return root
        if line_name < root.line_name:
            return self.search_line(root.left, line_name)
        return self.search_line(root.right, line_name)

    def list_stations(self, line_root, line_name):
        line_node = self.search_line(line_root, line_name)
        if line_node:
            print(f"〖 {line_name} 〗: ", end="")
            stationgroup = StationGroup()
            stationgroup.inorder(line_node.stations_root)
            print()

def makeMap():
    lines = MrtMap()
    root = None
    for line_name in lines_to_stations.keys():
        root = lines.insert_line(root, line_name)

    for line_name, station_ids in lines_to_stations.items():
        for order_index, station_id in enumerate(station_ids):
            lines.add_station(root, line_name, station_id, order_index)

    for line_name in lines_to_stations.keys():
        lines.list_stations(root, line_name)

def find_line(line_n):
    lines = MrtMap()
    root = None
    for line_name in lines_to_stations.keys():
        root = lines.insert_line(root, line_name)

    for line_name, station_ids in lines_to_stations.items():
        for order_index, station_id in enumerate(station_ids):
            lines.add_station(root, line_name, station_id, order_index)
    lines.list_stations(root, line_n)
