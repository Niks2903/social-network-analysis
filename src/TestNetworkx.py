import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame


if __name__ == "__main__":
    df = pd.read_csv("NetworkPulwama.csv")
    # location_array = []plt.show()
    # for i in df.index:
    #     location_array.append(df.at[i, "Location"])
    # location_array.append("Mumbai")
    # print(location_array)
    g = nx.Graph()
    for i in range(df.__len__()):
        g.add_edge(df.at[i, "Source"], df.at[i, "Destination"])
    pos = nx.spring_layout(g)
    betCent = nx.betweenness_centrality(g, normalized=True, endpoints=True)
    node_color = [20000.0 * g.degree(v) for v in g]
    node_size = [v * 10000 for v in betCent.values()]
    plt.figure(figsize=(50, 50))
    nx.draw_networkx(g, pos=pos, with_labels=False,
                     node_color=node_color,
                     node_size=node_size)
    nx.draw_networkx_labels(g, pos=pos, font_color="grey", font_size=1)
    print(sorted(betCent, key=betCent.get, reverse=True)[:5])
    plt.axis('off')
    # nx.draw_shell(g, with_labels=True)
    plt.savefig("Graph.svg", dpi=1500)
    plt.show()

