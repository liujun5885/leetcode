// Package critical_connections_in_a_network Package graph https://leetcode-cn.com/problems/critical-connections-in-a-network/
package critical_connections_in_a_network

func buildGraph(connections [][]int) map[int][]int {
	graph := map[int][]int{}

	for _, conn := range connections {
		graph[conn[0]] = append(graph[conn[0]], conn[1])
		graph[conn[1]] = append(graph[conn[1]], conn[0])
	}

	return graph
}

func dfs(cur int, tag int, parent int, nodeVsTag map[int]int, graph map[int][]int, result *[][]int) int {
	nodeVsTag[cur] = tag

	for _, i := range graph[cur] {
		if i == parent {
			continue
		}
		var newTag int
		if nodeVsTag[i] == 0 {
			newTag = dfs(i, nodeVsTag[cur]+1, cur, nodeVsTag, graph, result)
		} else {
			newTag = nodeVsTag[i]
		}

		if newTag < nodeVsTag[cur] {
			nodeVsTag[cur] = newTag
		}
	}
	if nodeVsTag[cur] > nodeVsTag[parent] {
		*result = append(*result, []int{cur, parent})
	}

	return nodeVsTag[cur]
}

func criticalConnections(n int, connections [][]int) [][]int {
	graph := buildGraph(connections)
	nodeVsTag := map[int]int{}
	for i := 0; i < n; i++ {
		nodeVsTag[i] = 0
	}
	var result [][]int
	dfs(0, 1, 0, nodeVsTag, graph, &result)

	return result
}
