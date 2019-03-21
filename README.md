# nodemetrics
python module to calculate betweenness centrality of nodes in undirected un-weighted graphs.
To use, import nodemetrics.
The module defines a Graph class, which can be initialized with 2 arguments:

vertices: List of integers specifying vertices in graph

edges: List of 2-tuples specifying edges in graph

The following methods are defined:
>
        min_dist(start_node, end_node)
        Finds minimum distance between start_node and end_node

        Args:
            start_node: Vertex to find distance from

            end_node: Vertex to find distance to

        Returns:
            An integer denoting minimum distance between start_node
            and end_node


>
        all_shortest_paths(start_node, end_node):
        Finds all shortest paths between start_node and end_node

        Args:
            start_node: Starting node for paths
            end_node: Destination node for paths

        Returns:
            A list of path, where each path is a list of integers.
 
 >
        neighbours(self, node):
        From the graph, returns a list of neighbours for the given node


>
        all_paths(start_node, end_node, distance)
        Finds all paths from node to destination with length = distance

        Args:
            node: Node to find path from
            destination: Node to reach
            dist: Allowed distance of path
            path: path already traversed

        Returns:
            List of path, where each path is list ending on destination

            Returns None if there no paths
            
>

        betweenness_centrality(node):
        Find betweenness centrality of the given node

        Args:
            node: Node to find betweenness centrality of.

        Returns:
            Single floating point number, denoting standardized betweenness centrality
            of the given node

To run the tests, execute the unit test file by:
```
python3 nodemetrics_test.py
```
