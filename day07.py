import numpy as np

BAG = re.compile('([0-9 ]*)([a-z]+ [a-z]+) bag')

def is_empty(first, *content):
    return first[1].startswith('no other')

def parse_graph(filename):

    with open(filename) as handle:
        rules = handle.readlines()

    # parse bags and contents
    bags, contents = [], []
    for rule in rules:
        bag, *content = BAG.findall(rule)
        bags.append(bag[1])
        contents.append(content if not is_empty(*content) else [])

    # represent 'bag contains other bags' as graph
    graph = np.zeros((len(bags), len(bags)), dtype=int)
    for i, content in enumerate(contents):
        for count, name in content:
            graph[i, bags.index(name)] = count

    return graph, bags

def fetch_containers(node, graph, containers):
    for parent in np.nonzero(graph[:, node])[0]:
        containers.add(parent)
        fetch_containers(parent, graph, containers)

def count_content(node, graph):
    count = 1
    for child in np.nonzero(graph[node])[0]:
        count += graph[node, child] * count_content(child, graph)
    return count
        
if __name__ == '__main__':

    filename = 'input07.txt'
    graph, bags = parse_graph(filename)
    target = bags.index('shiny gold')

    # part 1    
    containers = set()
    fetch_containers(target, graph, containers)
    print('part 1:', len(containers))

    # part 2: subtract count of bag itself
    print('part 2:', count_content(target, graph) - 1) 
