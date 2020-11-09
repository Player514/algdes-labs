import java.util.LinkedList;
import java.util.Queue;

public class MaximumFlow {
    private boolean[] visited;
    private int maximumFlow;
    private Edge[] path;

    public int EdmondsKarp(Graph graph, int source, int sink){
        maximumFlow = 0;
        Graph residual = graph;
        
        while(augmentingPath(residual, source, sink)) { 
            int bottleneck = Integer.MAX_VALUE;
             
            for (int v = sink; v != source; v = path[v].getOtherVertice(v)) {
                bottleneck = Math.min(bottleneck, path[v].residualCapacityTo(v));
            }

            for (int v = sink; v != source; v = path[v].getOtherVertice(v)) {
                path[v].addResidualFlowTo(v, bottleneck);
            }  
            
            maximumFlow += bottleneck;
        }

        return maximumFlow;
    }
        
    private final boolean augmentingPath(Graph graph, int source, int sink){
        path = new Edge[graph.getNumberOfVertices()];
        visited = new boolean[graph.getNumberOfVertices()];
        
        Queue<Integer> q = new LinkedList<>();
        q.add(source);
        visited[source] = true;

        // BFS 
        while(!q.isEmpty()) {
            int v = q.poll(); 

            for(Edge e : graph.getAdjacent(v)) {
                int w = e.getOtherVertice(v);
                if(e.residualCapacityTo(w) > 0 && !visited[w]) {
                    path[w] = e; 
                    visited[w] = true;
                    q.add(w);
                }
            }
        }

        return visited[sink];
    }

    public boolean[] visited() {
        return this.visited;
    }
       
    public int flow() {
        return maximumFlow;
    }
    
    public boolean verticesInCut(int v) {
        return visited[v];
    } 
}