#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

#define edge pair<int, int>

class Graph {
private:
    vector<pair<int, edge> > G;  // graph
    vector<pair<int, edge> > T;  // mst
    int* parent;
    int V;  // number of vertices/nodes in graph
public:
    Graph(int V);
    void AddWeightedEdge(int u, int v, int w);
    int find_set(int i);
    void union_set(int u, int v);
    void kruskal();
    void print();
};
Graph::Graph(int V) 
{
    this->V = V;
    parent = new int[V];

    for (int i = 0;i < V; i++)
        parent[i] = i;

    G.clear();
    T.clear();
}
void Graph::AddWeightedEdge(int u, int v, int w) {
    G.push_back(make_pair(w, edge(u, v)));
}
int Graph::find_set(int i) {
    if (i == parent[i])
        return i;
    else
        return find_set(parent[i]);
}

void Graph::union_set(int u, int v) {
    parent[u] = parent[v];
}
void Graph::kruskal() {
    int i, uRep, vRep;
    sort(G.begin(), G.end());  // increasing weight
    for (i = 0; i < G.size(); i++) {
        uRep = find_set(G[i].second.first);
        vRep = find_set(G[i].second.second);
        if (uRep != vRep) {
            T.push_back(G[i]);  // add to tree
            union_set(uRep, vRep);
        }
    }
}
void Graph::print() {
    cout << "Edge :" << " Weight" << endl;
    for (int i = 0; i < T.size(); i++) {
        cout << T[i].second.first << " - " << T[i].second.second << " : "
            << T[i].first;
        cout << endl;
    }
}
int main() {
    Graph g(9);
    g.AddWeightedEdge(1, 2, 4);
    g.AddWeightedEdge(1, 3, 6);
    g.AddWeightedEdge(1, 4, 6);
    g.AddWeightedEdge(1, 5, 8);
    g.AddWeightedEdge(1, 6, 3);
    g.AddWeightedEdge(2, 1, 4);
    g.AddWeightedEdge(2, 5, 5);
    g.AddWeightedEdge(3, 1, 6);
    g.AddWeightedEdge(3, 5, 2);
    g.AddWeightedEdge(3, 8, 7);
    g.AddWeightedEdge(4, 1, 6);
    g.AddWeightedEdge(4, 5, 7);
    g.AddWeightedEdge(4, 6, 1);
    g.AddWeightedEdge(4, 7, 1);
    g.AddWeightedEdge(5, 1, 8);
    g.AddWeightedEdge(5, 2, 6);
    g.AddWeightedEdge(5, 3, 2);
    g.AddWeightedEdge(5, 4, 7);
    g.AddWeightedEdge(5, 7, 2);
    g.AddWeightedEdge(5, 8, 2);
    g.AddWeightedEdge(6, 1, 3);
    g.AddWeightedEdge(6, 4, 1);
    g.AddWeightedEdge(6, 7, 5);
    g.AddWeightedEdge(7, 4, 1);
    g.AddWeightedEdge(7, 5, 2);
    g.AddWeightedEdge(7, 6, 5);
    g.AddWeightedEdge(7, 8, 9);
    g.AddWeightedEdge(8, 3, 7);
    g.AddWeightedEdge(8, 5, 2);
    g.AddWeightedEdge(8, 7, 9);

    g.kruskal();
    g.print();
    return 0;
}