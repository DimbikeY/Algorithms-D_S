from collections import defaultdict

graph = defaultdict(list)
digit = int(input())

def input_func(graph, digit):
    for i in range(digit):
        sentence = input().replace(":", "").split()
        if len(sentence) == 1 and not sentence[0] in list(graph.keys()):
            sentence[0]
        else:
            if len(sentence) > 1:
                for element in sentence[1:]:
                    graph[element].append(sentence[0])
    return graph

graph = input_func(graph, digit)
digit_end = int(input())

def output_making(digit_end, lst_output = []):
    for i in range(digit_end):
        lst_output.append(input())
    return lst_output

lst_output = output_making(digit_end)

def search_path(graph, start, end, path = []):
    path = path + [start]
    if start == end:
        return path
    if not graph[start]:
        return None
    for node in graph[start]:
        try:
            if not node in path:
                path = search_path(graph, node, end, path)
                if path:
                    return path
        except:
            path = search_path(graph, node, end, path = []) # Если path == None
            if path:
                return path
    return None

removed_elements = []

while lst_output:
    start = lst_output.pop(0)
    for end in lst_output:
        if search_path(graph, start, end):
            removed_elements.append(end)
            lst_output.remove(end)

for element in removed_elements:
    print(element)
