from classes.node import Node

nodes = {}

print("Loading nodes from file")
with open('taxdump/nodes.dmp') as f:
    for line in f:
        formatted_input = line.split('\t|\t')
        nodes[formatted_input[0]] = Node(formatted_input)
print("Loading completed")

def getPath(id):
    if id not in nodes:
        return []
    currentNode = nodes[id]
    res = [currentNode.tax_id]
    while(currentNode.rank_lv > 0):
        res.append(currentNode.parent_id)
        currentNode = nodes[currentNode.parent_id]
    return res

def find_lca(n1, n2):
    n1_path = getPath(n1)
    n2_path = getPath(n2)
    if len(n1_path) == 0 or len(n2_path) == 0:
        return None
    
    for p in n1_path:
        if p in n2_path:
            return p

    return None

while True:
    input1 = input('Enter first node tax_id (enter q to exit): ')
    if input1.lower() == 'q':
        break
    input2 = input('Enter second node tax_id (enter q to exit): ')
    if input2.lower() == 'q':
        break
    res = find_lca(input1, input2)
    print('The lowest common ancestor of', input1, 'and', input2, 'is', res)