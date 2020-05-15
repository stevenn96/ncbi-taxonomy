from classes.tree import TreeNode, Tree

tree = Tree()
tree.insert(1)
tree.insert(3, 1)
tree.insert(2, 1)
tree.insert(4, 2)
tree.insert(7, 2)
tree.insert(78, 7)
tree.insert(10, 3)
tree.insert(10, 3)

print(tree.print(tree.root, ''))

def find_lca(tree, n1, n2):
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

print(find_lca(tree, 4, 7))
print(find_lca(tree, 4, 1))
print(tree.ancestors(tree.root, 10))