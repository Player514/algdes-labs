class Edge {
    private final int v, w;
    private final int capacity;
    private int flow;
    
    Edge(int v, int w, int capacity){
        this.v = v;
        this.w = w;
        this.capacity = capacity;
    }

    public int getSource() {
        return v;
    }

    public int getDestination() {
        return w;
    }
    
    public int fromVertice() {
        return v;
    }
    
    public int toVertice() {
        return w;
    }
    
    public int getOtherVertice(int v) { 
        return (v == this.v) ? w : this.v;
    }

    double capacity() {
        return capacity;
    }
    
    int getFlow() {
        return flow;
    }
    
    int residualCapacityTo(int v) {
        if(v == this.w) {
            return capacity - flow;
        }
        else {
            return flow;
        }       
    }
    void addResidualFlowTo(int v, double f) {
        if(v == this.w) { 
            flow += f;
        }
        else {
            flow -= f;
        }         
    }
}