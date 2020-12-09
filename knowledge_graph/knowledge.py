from suggestion import Suggestion


class KnowledgeGraph:
    MAX_DEPTH = 2

    def __init__(self, term):
        self.__term = term.lower()
        self.__nodes = [term]
        self.__edges = []
        self.__build_graph(term)

    def __build_graph(self, term, depth=0):
        if depth == self.MAX_DEPTH:
            return
        suggestions = Suggestion(term).get_suggestion()
        for suggestion in suggestions:
            if " vs " not in suggestion:
                continue
            first_word, second_word = suggestion.split(" vs " , maxsplit=1)
            if second_word not in self.__nodes:
                self.__nodes.append(second_word)
                edge = (first_word, second_word)
                reversed_edge = (second_word, first_word)
                if edge not in self.__edges and reversed_edge not in self.__edges:
                    self.__edges.append(edge)
                self.__build_graph(second_word, depth=depth + 1)

    @property
    def nodes(self):
        return self.__nodes

    @property
    def edges(self):
        return self.__edges

if __name__ == "__main__":
    graph = KnowledgeGraph("python")
    print(graph.nodes)
    print(graph.edges)
