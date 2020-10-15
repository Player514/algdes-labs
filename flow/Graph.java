import java.util.ArrayList;

class Graph {
    private final int numOfVertices;
    private int numOfEdges;
    private ArrayList<ArrayList<Edge>> graph;
    
    Graph(int V) {
        this.numOfVertices = V;
        graph = new ArrayList<>(V);

        for(int i = 0; i < V; ++i) {
            graph.add(new ArrayList<>());
        }    
    }

    void addEdge(Edge e) {
        graph.get(e.fromVertice()).add(e);
        graph.get(e.toVertice()).add(e);
        numOfEdges++;
    }
    
    Iterable<Edge> getAdjacent(int v) {
        return graph.get(v);
    }
    
    Iterable<Edge> edges() {
        ArrayList<Edge> list = new ArrayList<>(numOfVertices);
        for(int i = 0; i < numOfVertices; ++i){
            for(Edge e: graph.get(i)) {
                list.add(e);
            }         
        }

        return list;        
    }
    
    int getNumberOfVertices() {
        return numOfVertices;
    };
    
    int getNumberOfEdges() {
        return numOfEdges;
    };
}