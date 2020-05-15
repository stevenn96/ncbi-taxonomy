class Node:
    def __init__(self, arr):
        self.tax_id = arr[0]
        self.parent_id = arr[1]
        self.rank = arr[2]
        self.embl_code = arr[3]
        self.division_id = arr[4]
        self.div_flag = arr[5]
        self.gc_id = arr[6]
        self.gc_flag = arr[7]
        self.mgc_id = arr[8]
        self.mgc_flag = arr[9]
        self.genbank_flag = arr[10]
        self.subtree_root_flag = arr[11]
        
    def print(self):
        print(self.tax_id, self.parent_id, self.rank)