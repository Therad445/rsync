#include <iostream>
#include <vector>


int MinKey(const std::vector<int>& key, const std::vector<bool>& visited)
{
	int min = 999, min_index{};

	for (int v = 0; v < key.size(); v++)
		if (!visited[v] && key[v] < min)
		{
			min = key[v];
			min_index = v;
		}

	return min_index;
}


void Print(const std::vector<int>& parents, const std::vector<std::vector<int>>& costs)
{
	int minCost = 0;
	std::cout << "Edge \tWeight\n";
	for (int i = 0; i < costs.size(); i++)
	{
		if (parents[i] == -1) continue;
		std::cout << parents[i] + 1 << " - " << i + 1 << "\t" << costs[i][parents[i]] << " \n";
		minCost += costs[i][parents[i]];
	}
}


void Prim(const std::vector<std::vector<int>>& costs, int& start)
{
	std::vector<int> parents(costs.size(), -1), distances(costs.size(), 999);
	std::vector<bool> visited(costs.size(), false);

	distances[start - 1] = 0;


	for (int x = 0; x < costs.size() - 1; x++)
	{
		int u = MinKey(distances, visited);

		visited[u] = true;

		for (int v = 0; v < costs.size(); v++)
			if (costs[u][v] != 0 && !visited[v] && costs[u][v] < distances[v])
			{
				parents[v] = u;
				distances[v] = costs[u][v];
			}
	}

	Print(parents, costs);
}


int main()
{
	std::vector<std::vector<int>> costs =
	{
		{ 0, 4, 6, 6, 8, 3, 0, 0 },
		{ 4, 0, 0, 0, 5, 0, 0, 0 },
		{ 6, 0, 0, 0, 2, 0, 0, 7 },
		{ 6, 0, 0, 0, 7, 1, 1, 0 },
		{ 8, 5, 2, 7, 0, 0, 2, 2 },
		{ 3, 0, 0, 1, 0, 0, 5, 0 },
		{ 0, 0, 0, 1, 2, 5, 0, 9 },
		{ 0, 0, 7, 0, 2, 0, 9, 0 }
	};

	int start = 8;
	Prim(costs, start);
	return 0;
}




