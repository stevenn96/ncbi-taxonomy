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

        # map the ranks to integers
        if self.rank == 'species':
            self.rank_lv = 7
        elif self.rank == 'genus':
            self.rank_lv = 6
        elif self.rank == 'family':
            self.rank_lv = 5
        elif self.rank == 'order':
            self.rank_lv = 4
        elif self.rank == 'class':
            self.rank_lv = 3
        elif self.rank == 'phylum':
            self.rank_lv = 2
        elif self.rank == 'kingdom':
            self.rank_lv = 1
        elif self.rank == 'superkingdom':
            self.rank_lv = 0
        else:
            self.rank_lv = -1
        
    def print(self):
        print(self.tax_id, self.parent_id, self.rank)