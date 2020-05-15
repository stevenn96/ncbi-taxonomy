from classes.node import Node
from classes.tree import TreeNode, Tree

tree = Tree()
nodes = {}

# load taxonomy data to dictionary
print("Loading nodes from file")
with open('taxdump/nodes.dmp') as f:
    for line in f:
        formatted_input = line.split('\t|\t')
        nodes[formatted_input[0]] = Node(formatted_input)
print("Loading completed")

# function to get a node path from the dictionary
def getPath(id):
    if id not in nodes:
        return []
    currentNode = nodes[id]
    res = [currentNode.tax_id]
    while(currentNode.tax_id != currentNode.parent_id):
        res.append(currentNode.parent_id)
        currentNode = nodes[currentNode.parent_id]
    return res

# function to find lca based on a dictionary list
def find_lca(n1, n2):
    n1_path = getPath(n1)
    n2_path = getPath(n2)
    if len(n1_path) == 0 or len(n2_path) == 0:
        return None
    print(n1_path, n2_path)
    for p in n1_path:
        if p in n2_path:
            return p

    return None

# function to find lca based on a n ary tree
def find_lca2(tree, n1, n2):
    _, n1_path = tree.search(tree.root, n1)
    _, n2_path = tree.search(tree.root, n2)
    if n1_path is None:
        print('Node ', n1, ' doesn\'t exist')
        return None

    if n2_path is None:
        print('Node ', n2, ' doesn\'t exist')
        return None

    n1_path = n1_path.split(',')
    n2_path = n2_path.split(',')

    if len(n1_path) == 0 or len(n2_path) == 0:
        return None

    print(n1_path, n2_path)
    for p in n1_path:
        if p in n2_path:
            return p

# populate tree
# this will take a very long time since inserting to n-ary tree will do a search then insert O(n)
for i in nodes:
    path = getPath(i)
    path.reverse()
    print(len(nodes) - int(i))
    for node in path:
       tree.insert(nodes[node].tax_id, nodes[node].parent_id, nodes[node].rank)

# ask for input for calling lca
# change find_lca to find_lca2 for using tree implementation instead of dictionary
while True:
    input1 = input('Enter first node tax_id (enter q to exit): ')
    if input1.lower() == 'q':
        break
    input2 = input('Enter second node tax_id (enter q to exit): ')
    if input2.lower() == 'q':
        break
    res = find_lca(input1, input2)
    print('The lowest common ancestor of', input1, 'and', input2, 'is', res)