import sys
import heapq


def print_solution(dist):
    print("Vertex tDistance from Source")
    for node in range(len(dist)):
        print(node, "t", dist[node])


def dijkstra(adj, src):
    # set up dist
    dist = [sys.maxsize] * len(adj)
    heap = []
    dist[src] = 0
    heapq.heappush(heap, (0, src))
    # iterate heap, and update dist
    while heap:
        d, curr = heapq.heappop(heap)
        # iterate adj of curr, and push if weight is good to push
        for i in range(len(adj[curr])):
            # push into heap, if weight is smaller than curr dist
            if adj[curr][i] > 0 and d + adj[curr][i] < dist[i]:
                dist[i] = d + adj[curr][i]
                heapq.heappush(heap, (d + adj[curr][i], i))
    return dist


if __name__ == "__main__":
    adj = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0],
    ]
    distance = dijkstra(adj, 0)
    print_solution(distance)
