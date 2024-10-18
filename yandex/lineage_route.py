# ['Moscow', 'Tbilisi']                         -> ['Moscow', 'Tbilisi']
# ['Belgrade', 'Moscow] ['Yerevan', 'Moscow]    -> ['Yerevan', 'Moscow', 'Belgrade']

class Flight:
    def __init__(self, origin, dest):
        self.origin = origin
        self.dest = dest


def find_route(flights):
    answer = []
    origin_dest = find_origin_dest(flights)
    answer.append(origin_dest[0])
    groups = create_groups(flights)

    current = origin_dest[0]
    visited = set()

    while current != origin_dest[1]:
        flights = groups[current]
        for flight in flights:
            key = str(sorted(flight.dest + flight.origin))
            if key not in visited:
                if flight.origin == current:
                    current = flight.dest
                    answer.append(current)
                    visited.add(key)
                else:
                    if flight.dest == current:
                        current = flight.origin
                        answer.append(current)
                        visited.add(key)

    return answer

def find_origin_dest(flights):
    cites = {}
    answer = []
    for flight in flights:
        origin = flight.origin
        if origin not in cites:
            cites[origin] = 1
        else:
            cites[origin] += 1
        dest = flight.dest
        if dest not in cites:
            cites[dest] = 1
        else:
            cites[dest] += 1

    for city, count in cites.items():
        if count == 1:
            answer.append(city)
    return answer

def create_groups(flights):
    groups = {}
    for flight in flights:
        origin = flight.origin
        if origin not in groups:
            groups[origin] = [flight]
        else:
            groups[origin].append(flight)
        dest = flight.dest
        if dest not in groups:
            groups[dest] = [flight]
        else:
            groups[dest].append(flight)
    return groups