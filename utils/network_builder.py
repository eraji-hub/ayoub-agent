import networkx as nx
from pyvis.network import Network

def build_network(analysis_text):
    """
    بناء شبكة علاقات بسيطة من النص (يمكن تطوير لاحقاً)
    الآن: مجرد مثال بسيط مع عقد افتراضية
    """
    G = nx.Graph()
    # مثال: العقد والعلاقات (يمكن تطوير تحليل LLM لاستخراجها تلقائياً)
    G.add_node("Company")
    G.add_node("Founder1")
    G.add_node("Partner1")
    G.add_edge("Company", "Founder1")
    G.add_edge("Company", "Partner1")

    net = Network(notebook=False, height="500px", width="100%")
    net.from_nx(G)
    file_name = "network.html"
    net.save_graph(file_name)
    return file_name
