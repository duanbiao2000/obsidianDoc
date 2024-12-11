### 图（Graph）

图是由顶点（Vertex）和边（Edge）组成的集合。顶点代表实体，边代表实体之间的关系。图可以是有向的（有向图，Directed Graph）或无向的（无向图，Undirected Graph），并且可以是加权的（Weighted Graph）或无权的（Unweighted Graph）。图的常见类型包括树（作为特殊类型的图）、图的连通性（Connectivity）、最短路径问题（如Dijkstra算法、Floyd-Warshall算法）等。
#### 邻接矩阵
![image.png](https://cdn.jsdelivr.net/gh/duanbiao2000/BlogGallery@main/picture/20240722121504.png)
使用邻接矩阵表示图时，我们可以直接访问矩阵元素以获取边，因此增删查改操作的效率很高，时间复杂度均为 𝑂(1) 。然而，矩阵的空间复杂度为 𝑂(𝑛2) ，内存占用较多。
#### 邻接表
![image.png](https://cdn.jsdelivr.net/gh/duanbiao2000/BlogGallery@main/picture/20240722121617.png)
**邻接表结构与哈希表中的“链式地址”非常相似，因此我们也可以采用类似的方法来优化效率**。比如当链表较长时，可以将链表转化为 AVL 树或红黑树，从而将时间效率从 𝑂(𝑛) 优化至 𝑂(log⁡𝑛) ；还可以把链表转换为哈希表，从而将时间复杂度降至 𝑂(1) 。

表 9-1   现实生活中常见的图

||顶点|边|图计算问题|
|---|---|---|---|
|社交网络|用户|好友关系|潜在好友推荐|
|地铁线路|站点|站点间的连通性|最短路线推荐|
|太阳系|星体|星体间的万有引力作用|行星轨道计算|

[[[哈希集合]]]

#### 图的最短路径问题（使用 Dijkstra 算法）

```python
import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = [w]
        else:
            self.graph[u].append(w)
        # 如果是无向图，需要添加反向边
        if v not in self.graph:
            self.graph[v] = [w]
        else:
            self.graph[v].append(w)

    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        pq = [(0, src)]

        while pq:
            u = heapq.heappop(pq)[1]
            for v in self.graph[u]:
                if dist[u] + self.graph[u][v] < dist[v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    heapq.heappush(pq, (dist[v], v))

        return dist

# 创建一个图并添加边
g = Graph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 3)
g.add_edge(1, 3, 1)
g.add_edge(1, 2, 2)
g.add_edge(2, 4, 5)
g.add_edge(2, 3, 8)
g.add_edge(3, 5, 7)
g.add_edge(4, 3, 9)
g.add_edge(4, 5, 2)

# 计算从顶点 0 到其他顶点的最短路径
shortest_distances = g.dijkstra(0)
print("Shortest distances from vertex 0 are:", shortest_distances)
```

这些代码示例展示了如何在 Python 中实现基本的树和图算法。在实际应用中，你可能需要根据具体问题调整算法的细节。例如，Dijkstra 算法在处理带有负权重边的图时可能不会给出正确的结果，这种情况下你可能需要使用 Bellman-Ford 算法。

 这段代码是 Dijkstra 算法的一部分，用于在图中找到从源顶点到所有其他顶点的最短路径。Dijkstra 算法是一种贪心算法，它通过维护一个优先队列（在这里使用 Python 的 `heapq` 模块实现）来确保每次从队列中取出的都是当前已知最短路径的顶点。这里是代码的详细解释：

1. `while pq:`：这是一个循环，它会一直执行，直到优先队列为空。优先队列 `pq` 存储了所有待处理的顶点及其到源顶点的当前最短距离。

2. `u = heapq.heappop(pq)[1]`：从优先队列中弹出当前距离最短的顶点。`heapq.heappop()` 返回的是优先队列中的最小元素，这里我们只关心顶点（索引为 1），因为优先队列中的元素是成对的，第一个元素是距离，第二个元素是顶点。

3. `for v in self.graph[u]:`：遍历与顶点 `u` 相邻的所有顶点 `v`。`self.graph[u]` 是一个列表，包含了所有与顶点 `u` 直接相连的顶点的权重。

4. `if dist[u] + self.graph[u][v] < dist[v]:`：检查通过顶点 `u` 到达顶点 `v` 的路径是否比已知的最短路径更短。这里 `dist[u]` 是从源顶点到顶点 `u` 的最短距离，`self.graph[u][v]` 是从顶点 `u` 到顶点 `v` 的边的权重。

5. `dist[v] = dist[u] + self.graph[u][v]`：如果通过顶点 `u` 到达顶点 `v` 的路径更短，更新 `dist[v]` 的值。

6. `heapq.heappush(pq, (dist[v], v))`：将顶点 `v` 和它的新最短距离重新加入到优先队列中，以便后续处理。

这个循环会一直执行，直到所有顶点都被处理过，此时 `dist` 数组将包含从源顶点到图中所有其他顶点的最短路径长度。这个过程确保了每次都是考虑了最新信息的最短路径，从而保证了最终结果是全局最优的。 