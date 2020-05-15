class TreeNode:
    def __init__(self, tax_id, parent_id, rank):
        self.tax_id = tax_id
        self.parent_id = parent_id
        self.rank = rank
        #self.embl_code = arr[3]
        #self.division_id = arr[4]
        #self.div_flag = arr[5]
        #self.gc_id = arr[6]
        #self.gc_flag = arr[7]
        #self.mgc_id = arr[8]
        #self.mgc_flag = arr[9]
        #self.genbank_flag = arr[10]
        #self.subtree_root_flag = arr[11]
        self.children = []
        self.parent = []
        
    def add_child(self, node):
        self.children.append(node)

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def insert(self, new_node_id, parent_id=None, rank=None):
        # check for duplicates, we don't allow duplicates as tax_ids are unique
        node, _ = self.search(self.root, new_node_id)
        if node != None:
            return
        # create new node based on new_node_id
        new_node = TreeNode(new_node_id, parent_id, rank)
        # check if adding root node
        if parent_id == None or new_node_id == parent_id:
            self.root = new_node
        # else search for parrent node and append new node to its children
        else:
            parent_node, _ = self.search(self.root, parent_id)
            if not(parent_node):
                print('Parent not found, new node ', new_node_id, ' will be orphaned')
                return
            parent_node.children.append(new_node)
        self.size += 1

    # this function will search for node_id starting from node
    # it will return the node and the path to the node if found
    def search(self, node, node_id):
        # check if we have found the node
        if node == None:
            return None, None
        if node_id == None or node.tax_id == node_id:
            return node, str(node.tax_id)

        # recursively traverse through each node's children
        for child in node.children:
            child_node, path = self.search(child, node_id)
            if child_node:
                return child_node, path + ',' + str(node.tax_id)
        return None, None

    def print(self, node, string):
        if node == None:
            return ""
        string += str(node.tax_id) + '('
        for i in range(len(node.children)):
            child = node.children[i]
            string_end =  ',' if i < len(node.children) - 1 else ''
            string = self.print(child, string) + string_end
        string += ')'
        return string

    def ancestors(self, node, node_id):
        if node.tax_id == node_id:
            return str(node.tax_id)
        else:
            for child in node.children:
                res = self.ancestors(child, node_id)
                print(node.tax_id, node_id, res)
                if res:
                    return res + ',' + str(node.tax_id)
            return []