def tsp(graph, visited, curr_pos, n, count, cost, ans):
    if count == n:
        if graph[curr_pos][0] > 0:
            ans[0] = min(ans[0], cost + graph[curr_pos][0])
        return

    for city in range(n):
        if not visited[city] and graph[curr_pos][city] > 0:
            visited[city] = True

            tsp(graph, visited, city, n, count + 1,
                cost + graph[curr_pos][city], ans)

            visited[city] = False


def main():
    n = int(input("Enter number of cities: "))

    graph = []
    print("Enter cost adjacency matrix:")

    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    visited = [False] * n
    visited[0] = True
    ans = [float('inf')]

    tsp(graph, visited, 0, n, 1, 0, ans)

    if ans[0] == float('inf'):
        print("No valid tour exists")
    else:
        print("Minimum travelling cost:", ans[0])


main()
