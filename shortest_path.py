from name import station_names, stations, lines_to_stations

def find_paths(start, end, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return [path]
    if start not in stations:
        return []
    paths = []
    for neighbor in stations[start]:
        if neighbor not in path: 
            new_paths = find_paths(neighbor, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

def find_short(start, end):
    all_paths = find_paths(start, end)
    if not all_paths:
        return []
    min_length = min(len(path) for path in all_paths)
    shortest_paths = [path for path in all_paths if len(path) == min_length]
    return shortest_paths


def turn_id(start, end):
    start_id = None
    end_id = None
    for id, name in station_names.items():
        if name == start:
            start_id = id
        if name == end:
            end_id = id
    return start_id, end_id


def find(start_id, end_id):   
    if start_id is None or end_id is None:
        print("輸入的車站名稱有誤，請確認後再試！")
    else:
        shortest_paths = find_short(start_id, end_id)
        for path in shortest_paths:
            path_names = [f"【{station_names[station]}】" for station in path]
            print("->".join(path_names))
