#!/usr/bin/env python3

import re
import itertools
import copy

ROLLNUM_REGEX = "201[0-9]{4}"

class Graph(object):
    name = "Lakshya A Agrawal"
    email = "lakshya18242@iiitd.ac.in"
    roll_num = "2018242"

    def __init__ (self, vertices, edges):
        """
        Initializes object for the class Graph

        Args:
            vertices: List of integers specifying vertices in graph
            edges: List of 2-tuples specifying edges in graph
        """

        self.vertices = vertices
        
        ordered_edges = list(map(lambda x: (min(x), max(x)), edges))
        
        self.edges    = ordered_edges
        self.dist_from_point={}
        
        self.validate()

    def validate(self):
        """
        Validates if Graph if valid or not

        Raises:
            Exception if:
                - Name is empty or not a string
                - Email is empty or not a string
                - Roll Number is not in correct format
                - vertices contains duplicates
                - edges contain duplicates
                - any endpoint of an edge is not in vertices
        """

        if (not isinstance(self.name, str)) or self.name == "":
            raise Exception("Name can't be empty")

        if (not isinstance(self.email, str)) or self.email == "":
            raise Exception("Email can't be empty")

        if (not isinstance(self.roll_num, str)) or (not re.match(ROLLNUM_REGEX, self.roll_num)):
            raise Exception("Invalid roll number, roll number must be a string of form 201XXXX. Provided roll number: {}".format(self.roll_num))

        if not all([isinstance(node, int) for node in self.vertices]):
            raise Exception("All vertices should be integers")

        elif len(self.vertices) != len(set(self.vertices)):
            duplicate_vertices = set([node for node in self.vertices if self.vertices.count(node) > 1])

            raise Exception("Vertices contain duplicates.\nVertices: {}\nDuplicate vertices: {}".format(vertices, duplicate_vertices))

        edge_vertices = list(set(itertools.chain(*self.edges)))

        if not all([node in self.vertices for node in edge_vertices]):
            raise Exception("All endpoints of edges must belong in vertices")

        if len(self.edges) != len(set(self.edges)):
            duplicate_edges = set([edge for edge in self.edges if self.edges.count(edge) > 1])

            raise Exception("Edges contain duplicates.\nEdges: {}\nDuplicate vertices: {}".format(edges, duplicate_edges))

    def min_dist(self, start_node, end_node, visited=[], explored=[], unvisited=[], dist=0):
        '''
        Finds minimum distance between start_node and end_node

        Args:
            start_node: Vertex to find distance from

           end_node: Vertex to find distance to

        Returns:
            An integer denoting minimum distance between start_node
            and end_node
        '''
        print("in " + str(dist)+" visited " + str(visited))
        if start_node in self.dist_from_point:
            if end_node in self.dist_from_point[start_node]:
                return(self.dist_from_point[start_node][end_node])
        if dist==0:
            unvisited=copy.deepcopy(self.vertices)
            if not (start_node in self.dist_from_point):
                self.dist_from_point[start_node]={}
            unvisited.remove(start_node)
            visited=[]
            explored=[]
            visited.append(start_node)
            return(self.min_dist(start_node, end_node, visited, explored, unvisited, dist+1))
        else:
            to_rem_vis=[]
            to_add_vis=[]
            #print("visited " + str(visited))
            for i in visited:
                #print("Exploring "+str(i))
                #print("going through "+str(i))
                to_rem_un=[]
                for j in unvisited:
                    if (min(i,j), max(i, j)) in self.edges:
                        #print("Visiting " + str(j))
                        #print("distance of "+str(j) + " " + str(dist))
                        if not j in self.dist_from_point[start_node]:
                            self.dist_from_point[start_node][j]=dist
                        to_rem_un.append(j)
                        to_add_vis.append(j)
                        #print("visited "+str(j))
                for t in to_rem_un:
                    unvisited.remove(t)
                to_rem_vis.append(i)
                explored.append(i)
                #print("Explored " + str(i))
            for z in to_rem_vis:
                visited.remove(z)
            for a in to_add_vis:
                visited.append(a)
            return(self.min_dist(start_node, end_node, visited, explored, unvisited, dist+1))
    def all_shortest_paths(self, start_node, end_node):
        """
        Finds all shortest paths between start_node and end_node

        Args:
            start_node: Starting node for paths
            end_node: Destination node for paths

        Returns:
            A list of path, where each path is a list of integers.
        """
        min_dis_bw_points=self.min_dist(start_node, end_node)
        return(self.all_paths(start_node, end_node, min_dis_bw_points))
    def neighbours(self, node):
        a=[]
        for i in self.edges:
            if node==i[0]:
                a.append(i[1])
            elif node==i[1]:
                a.append(i[0])
        return(a)

    def all_paths(self, start_node, end_node, distance, paths=[], visited=[], explored=[], unvisited=[], dist=-1):
        """
        Finds all paths from node to destination with length = dist

        Args:
            node: Node to find path from
            destination: Node to reach
            dist: Allowed distance of path
            path: path already traversed

        Returns:
            List of path, where each path is list ending on destination

            Returns None if there no paths
        """
        #print("in " + str(dist))
        #print("visited " + str(visited))
        if dist>(distance-1):
            a=[]
            for i in paths:
                if i[-1]==end_node:
                    a.append(i)
            if len(a)==0:
                return(None)
            return(a)
        if dist==-1:
            unvisited=copy.deepcopy(self.vertices)
            unvisited.remove(start_node)
            visited=[]
            explored=[]
            visited.append(start_node)
            new_paths=[[start_node]]
            return(self.all_paths(start_node, end_node, distance, new_paths, visited, explored, unvisited, dist+1))
        else:
            to_rem_vis=[]
            to_add_vis=[]
            #print("visited " + str(visited))
            new_paths=[]
            for i in visited:
                print("checking for neighbours of "+str(i))
                print(paths)
                list_of_neighbours=self.neighbours(i)
                #print("neighbours of "+str(i)+" "+str(list_of_neighbours))
                to_rem_un=[]
                for neighbour in list_of_neighbours:
                    neigh_rev=self.neighbours(neighbour)
                    for neighbour_of_neighbour in neigh_rev:
                        for path in paths:
                            if path[-1]==neighbour_of_neighbour:
                                if not neighbour in path:
                                    if not path+[neighbour] in new_paths:
                                        new_paths.append(path+[neighbour])
                    if neighbour in unvisited:
                        to_rem_un.append(neighbour)
                        to_add_vis.append(neighbour)
                #print("Exploring "+str(i))
                #print("going through "+str(i))
                for t in to_rem_un:
                    unvisited.remove(t)
                to_rem_vis.append(i)
                explored.append(i)
                #print("Explored " + str(i))
            for z in to_rem_vis:
                visited.remove(z)
            for a in to_add_vis:
                visited.append(a)
            #print("in "+ str(dist) + " paths " + str(new_paths))
            return(self.all_paths(start_node, end_node, distance, new_paths, visited, explored, unvisited, dist+1))

    def betweenness_centrality(self, node):
        """
        Find betweenness centrality of the given node

        Args:
            node: Node to find betweenness centrality of.

        Returns:
            Single floating point number, denoting betweenness centrality
            of the given node
        """

        raise NotImplementedError

    def top_k_betweenness_centrality(self):
        """
        Find top k nodes based on highest equal betweenness centrality.

        
        Returns:
            List a integer, denoting top k nodes based on betweenness
            centrality.
        """

        raise NotImplementedError

if __name__ == "__main__":
    vertices = [1, 2, 3, 4, 5, 6]
    edges    = [(1, 2), (1, 5), (2, 3), (2, 5), (3, 4), (4, 5), (4, 6)]

    graph = Graph(vertices, edges)
