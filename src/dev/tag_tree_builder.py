class Node(object):
    def __init__(self, tag):
        self.tag = tag
        self.children = []
    def __eq__(self, x):
        return str(self.tag == x)
    
    def add_child(self, obj):
        self.children.append(obj)
        return self.children[-1]
    def goto_next(self, query_tag):
        for child in self.children:
            if(query_tag == child.tag):
                return child
        return self.add_child(Node(query_tag))
    def __str__(self):
        # fix it!
        output_str = str(self.tag) + '\n'
        return output_str
    def print(self):
        print(self.tag)
        self.str_helper(self, '-')
    def str_helper(self, node, dashes):
        if node.children == []:
            pass#print(dashes + node.tag)
        for child in node.children:
            print(dashes + child.tag)
            self.str_helper(child, dashes + '-')
        
    


filename = "./train_sent_correct.txt"
f = open(filename, 'r', encoding='utf-8')

# data aquisition
tag_seq_list = []
for line in f.readlines():
    sent, tags_str = line.split(';')
    tags = tags_str.split(',')[:-1]
    #print(tags)
    tag_seq_list.append(tags)



tag_tree = Node("Root")
for tag_seq in tag_seq_list:
    curr_node = tag_tree
    print(tag_seq)
    for tag in tag_seq:
        next_node = curr_node.goto_next(tag)
        curr_node = next_node

tag_tree.print()