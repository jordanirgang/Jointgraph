import server.py

class (server.Server):
    def __init__(self,server_ip="",server_port=8080,config_file="robot_urdf.xml"):
        super().__init__(server_ip,server_port)
        self.graph = make_urdf_graph(config_file)
    
