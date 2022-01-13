from trains.models import Train
from cities.models import City


def dfs_paths(graph, start, goal):
    """
    Function for searching all routes from one city to another.
    """
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next_ in graph[vertex] - set(path):
                if next_ == goal:
                    yield path + [next_]
                else:
                    stack.append((next_, path+[next_]))


def get_graph():
    qs = Train.objects.all()
    graph = {}
    for q in qs:
        graph.setdefault(q.from_city_id, set())
        graph[q.from_city_id].add(q.to_city_id)
    return graph


def get_routes(request, form) -> dict:
    context = {'form': form}
    graph = get_graph()
    data = form.cleaned_data
    from_city = data['from_city']
    to_city = data['to_city']
    cities = data['cities']
    travelling_time = data['travelling_time']
    all_ways = dfs_paths(graph, from_city.id, to_city.id)
    all_ways = list(all_ways)
    _cities = []
    if not len(all_ways):
        raise ValueError('Route does not find')
    if cities:
        _cities = [city.id for city in cities]
        right_ways = []
        city_names = []
        for route in all_ways:
            print(route)
            print(_cities)
            if all(city in route for city in _cities):
                right_ways.append(route)

            if not right_ways:
                for city in cities:
                    city_names.append(city.name)
                raise ValueError(
                    f'Does not find route throw {" ".join(city_names)} cities ')
    return context
