class Network(list):

    def __init__(self):
        self.nodes = {}
        self.nodeCont = 0

    def add_node(self, node_str):
        if node_str not in self.nodes:
            self.nodes[node_str] = self.nodeCont
            self.nodeCont = self.nodeCont + 1
        return self.nodes[node_str]

    def __del__(self):
        del self.nodes

    class Component:
        def __init__(self, comp_type, high_str, low_str, value):
            self.comp_type = comp_type
            self.high_str = high_str
            self.low_str = low_str
            self.high_node = -1
            self.low_node = -1
            self.value = value

        def __repr__(self):
            return str(self.comp_type) + " " + self(self.high_node) + \
                   " " + str(self.low) + " " + self(self.value)

    def map_nodes(self, components):
        self.add_node('0')
        for comp in components:
            comp.high_node = self.add_node(comp.high_str)
            comp.low = self.add_node(comp.low_str)
        return components

    def parse_file(self, file_name):
        global vs_c, cs_c, r_c, c_c, i_c
        file = open(file_name, "r")
        components = []
        for line in file:
            parts = line.split()
            components.append(
                self.Component(parts[0][0].upper(), parts[1].upper(),
                               parts[2].upper(), float(parts[3])))
            '''
            if parts[0][0] == 'V':
                vs_c = vs_c + 1
            elif parts[0][0] == 'I' :
                cs_c = cs_c + 1
            elif parts [0][0] == 'R' :
                r_c = r_c + 1
            elif parts[0][0] == 'C' :
                c_c = c_c + 1
            elif parts[0][0] == 'L' :
                i_c = i_c + 1
            '''

        return components

