class Node(object):
    def __init__(self, tag):
        self.tag = tag
        self.children = []
    def __eq__(self, x):
        return self.tag == x
    def add_child(self, obj):
        self.children.append(obj)
        return self.children[-1]
    def goto_next(self, query_tag):
        for child in self.children:
            if(query_tag == child.tag):
                return child
        return self.add_child(Node(query_tag))
    def __str__(self):
        output_str = ""
        for child in self.children:
            output_str += child.tag + " "
        return output_str#"Node: " + self.tag
    def checkout(self, tag):
        for child in self.children:
            #print(tag, child.tag)
            if(tag == child.tag):
                return True
        return False
'''
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
 '''  