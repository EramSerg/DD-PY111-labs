from typing import Union

import networkx as nx


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    return nx.shortest_path_length(graph, source=0, target=(len(graph)-1), weight="weight")  #TODO c помощью функции из модуля networkx найти стоимость кратчайшего пути до последней лестницы


def create_graph(stairway):
    G = nx.DiGraph()
    graph_value = []

    for index, value in enumerate(stairway):
        if index <= len(stairway) - 1:
            graph_value.append((index, index + 1, value))
        if index <= len(stairway) - 2:
            graph_value.append((index, index + 2, stairway[index+1]))

    G.add_weighted_edges_from(graph_value)
    return G


if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = create_graph(stairway)
    print(stairway_path(stairway_graph))  # 72
