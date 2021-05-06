"""
You are given a list of projects and a list of dependencies
(which is a list of pairs of projects, where the second project is dependent on the first project).
All of a project's dependencies must be built before the project is.
Find a build order that will allow the projects to be built. If there is no valid build order, return an error.
"""


def createGraph(projects, dependencies):
    projectGraph = {}
    for project in projects:
        projectGraph[project] = []
    for pairs in dependencies:
        projectGraph[pairs[0]].extend(pairs[1])
    return projectGraph


project = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a','d'), ('f','b'), ('b','d'), ('f','a'), ('d','c')]


def projectWithDependencies(graph):
    pwd = set()
    for project in graph:
        pwd = pwd.union(set(graph[project]))
    return pwd


def projectWithoutDependencies(pwd, graph):
    pwod = set()
    for project in graph:
        if project not in pwd:
            pwod.add(project)
    return pwod


def findBuildOrder(projects, dependencies):
    build_order = []
    graph = createGraph(projects, dependencies)
    while graph:
        pwd = projectWithDependencies(graph)
        pwod = projectWithoutDependencies(pwd, graph)
        if pwod is None:
            raise ValueError("There is a cycle in build order.")
        for independentProjects in pwod:
            build_order.append(independentProjects)
            del graph[independentProjects]
    return build_order
