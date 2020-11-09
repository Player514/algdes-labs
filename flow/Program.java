import java.util.Arrays;
import java.util.HashMap;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Map;
import java.util.Map.Entry;


public class Program {  
	static int s = -1;
	static int t = -1;
	static int numOfVertices = -1;
    
    public static void main(String[] args) throws Exception {
		Map<Integer, String> vertexNames = new HashMap<>();
		ArrayList<int[]> arcs = new ArrayList<>();
		
		readFile("rail.txt", vertexNames, arcs);

        Graph graph = new Graph(numOfVertices);
        
		for(int[] arc : arcs) {
			System.out.println("Inserted the following edge into the graph: " + arc[0] + " " + arc[1] + " " + arc[2]);
			
			// Change -1 capacity to highest possible integer value when reading a -1
			graph.addEdge(new Edge(arc[0], arc[1], (arc[2] ==- 1 ? Integer.MAX_VALUE : Integer.valueOf(arc[2]) )));			
			graph.addEdge(new Edge(arc[1], arc[0], (arc[2] ==- 1 ? Integer.MAX_VALUE : Integer.valueOf(arc[2]) )));
		}

		System.out.println("____________________________________________________");
		System.out.println("Vertices in graph: " + graph.getNumberOfVertices());
		System.out.println("Edges in graph: " + graph.getNumberOfEdges() + " (Including backward edges)");

        MaximumFlow karp = new MaximumFlow();
		System.out.println("Maximum flow in graph: " + karp.EdmondsKarp(graph, s,t));
		
		System.out.println();
        System.out.println("Minimum cut vertices: ");

        for (int i = 0; i < graph.getNumberOfVertices(); ++i) {
            if (karp.visited()[i]) {
				System.out.print(i + " ");
			}
        }

        System.out.println();
        System.out.println("Flow from minimum cut vertices: ");
        
        for (int i = 0; i < graph.getNumberOfVertices(); ++i) {
        	if (karp.verticesInCut(i)) {
        		for (Edge edge : graph.getAdjacent(i)) {
        			if (edge != null && !karp.verticesInCut(edge.getDestination()) && edge.getFlow() > 0) {
            		  System.out.println(edge.getSource() + " " + edge.getDestination() + " " + edge.getFlow());        		
        			}
        		}
        	}
		}
		
		System.out.println();
		
        // Max flow when reducing flow from vertice 4W, 48, 49. 
        reducedFlow(vertexNames,arcs,"4W","48","49", 0);
          
    }

    private static void reducedFlow(Map<Integer,String> nodeNames,ArrayList<int[]> arcList,String fromName, 
        String targetVertexOne,String targetVertexTwo,int targetFlow) {

        int from = getEdgeIndexByName(fromName,nodeNames);
        int to48 = getEdgeIndexByName(targetVertexOne,nodeNames);
        int to49 = getEdgeIndexByName(targetVertexTwo,nodeNames);
        
        arcList.forEach(arr -> {if(arr[0] == from && arr[1] == to48){arr[2] = targetFlow;}});
        arcList.forEach(arr -> {if(arr[0] == from && arr[1] == to49){arr[2] = targetFlow;}});

        Graph graphReducedFlow = new Graph(nodeNames.keySet().size());
        
        for (int[] arc : arcList) {
		// Change -1 capacity to highest possible integer value when reading a -1
            graphReducedFlow.addEdge(new Edge(arc[0], arc[1], (arc[2] ==- 1 ? Integer.MAX_VALUE : Integer.valueOf(arc[2]) )));			
            graphReducedFlow.addEdge(new Edge(arc[1], arc[0], (arc[2] ==- 1 ? Integer.MAX_VALUE : Integer.valueOf(arc[2]) )));
        }
    
        MaximumFlow reducedFlow = new MaximumFlow();
        System.out.println("Reduced maximum flow value = " + reducedFlow.EdmondsKarp(graphReducedFlow, s,t));

    }
       
	private static int getEdgeIndexByName(String name, Map<Integer, String> nodeNames) {
		for (Entry<Integer, String> entry : nodeNames.entrySet()) {
	        if (entry.getValue().equals(name)) {
	            return entry.getKey();
	        }
        }
        
	    return -1;
	}

	private static void readFile(String filename, Map<Integer, String> vertexNames, ArrayList<int[]> arcList) throws Exception {
		File file = new File(filename);
		InputStream stream = new FileInputStream(file);
		BufferedReader reader = new BufferedReader(new InputStreamReader(stream));

		String line;
		String status = "numOfVertices";

		int numOfArcs = -1;	
		int vertexIndex = -1;
		int arcIndex = -1;

		while ((line = reader.readLine()) != null) {
			if (status.startsWith("numOfVertices")) {
				numOfVertices = Integer.parseInt(line);
				status = "vertexNames";
				continue;
			}

			if (status.startsWith("vertexNames") && vertexIndex < numOfVertices) {
				vertexNames.put(++vertexIndex, line);
				if (line.equalsIgnoreCase("origins"))
					s = vertexIndex;

				if (line.equalsIgnoreCase("destinations"))
					t = vertexIndex;

				if (vertexIndex == numOfVertices - 1) {
					status = "numOfArcs";
				}
				continue;
			}

			if (status.startsWith("numOfArcs")) {
				numOfArcs = Integer.parseInt(line);
				status = "arcList";
				continue;
			}

			if (status.startsWith("arcList") && arcIndex < numOfArcs) {
				int[] intArray = Arrays.asList(line.trim().split(" ")).stream().mapToInt(Integer::parseInt).toArray();
				arcList.add(intArray);
				arcIndex++;
				continue;
			}
		}

		reader.close();
	}
}
