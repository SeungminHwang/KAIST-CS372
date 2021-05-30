import tagnode

class TagTree(object):
    def __init__(self):
        self.root = tagnode.Node("Root")    
    def print(self):
        print(self.root.tag)
        self.print_helper(self.root, '-')
    def print_helper(self, node, dashes):
        if node.children == []:
            pass
        for child in node.children:
            print(dashes + child.tag)
            self.print_helper(child, dashes + '-')
    def __str__(self):
        return str(self.root)
    def add_tag_seq(self, tag_seq):
        curr_node = self.root
        for tag in tag_seq:
            next_node = curr_node.goto_next(tag)
            curr_node = next_node
    
    # def tag_seq_query(tag_seq: tag list)
    # return true for tag_seq exists in tagtree
    # return false for tag_seq doesn't exist  
    def tag_seq_query_helper(self, curr_node, tag_seq):
        if len(tag_seq) == 0:
            return True
        for tag in tag_seq:
            if curr_node.checkout(tag):
                next_node = curr_node.goto_next(tag)
                return self.tag_seq_query_helper(next_node, tag_seq[1:])
            else:
                return False 
    def tag_seq_query(self, tag_seq):
        return self.tag_seq_query_helper(self.root, tag_seq)
        #curr_node = self.root
        
    
        
        