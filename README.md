# Taxonomy
A simple console driven application to find the least common ancestor of 2 nodes.

Data is populated to a dictionary of objects based on taxonomy dump from NCBI (nodes.dmp)

## Requirements
Make sure you have the taxdump files from NCBI in the same directory with this project.

./taxdump/nodes.dmp -- required

## Usage

```bash
python main.py
```
main.py is a console driven application, it has 2 different implementations of finding least common ancestor

find_lca(node1, node2) will find the least common ancestor for dictionary based tree
find_lca2(tree, node1, node2) will find the least common ancestor for a pointer based n-ary tree

## Notes
Populating the pointer based n-ary tree will take a long time due to the nature of inserting to a tree. Inserting to a tree will cause the class to iterate through the corresponding parent and then add the new node after it has found the parent. This will take O(n) time  in the worst case, given n is the number of nodes in the set.

Comparing this implementation to a dictionary, insertion will take constant time O(1) as we hash all the tax_id and attach it to a Node object. This will result in a dictionary based tree where we can have constant random access to any node.
