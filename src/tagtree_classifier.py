import tagnode
import tagtree

# data aquisition(correct sentence (train))
filename = "./dev/train_sent_correct.txt"
f = open(filename, 'r', encoding='utf-8')

tag_seq_list = []
for line in f.readlines():
    sent, tags_str = line.split(';')
    tag_seq = tags_str.split(',')[:-1]
    tag_seq_list.append(tag_seq)
    

# Build Tag-Tree
tag_tree = tagtree.TagTree()
#print(tag_tree)
for tag_seq in tag_seq_list:
    curr_node = tag_tree.root
    for tag in tag_seq:
        next_node = curr_node.goto_next(tag)
        curr_node = next_node
#tag_tree.print()





# data aquisition(incorrect sentence (train))
filename = "./dev/train_sent_incorrect.txt"
f = open(filename, 'r', encoding='utf-8')
tag_seq_list_incorrect = []
for line in f.readlines():
    sent, tags_str = line.split(';')
    tag_seq = tags_str.split(',')[:-1]
    tag_seq_list_incorrect.append(tag_seq)

correct_cnt = 0
incorrect_cnt = 0
for tag_seq in tag_seq_list_incorrect[:100]:
    if tag_tree.tag_seq_query(tag_seq):
        correct_cnt +=1
    else:
        incorrect_cnt += 1

print(correct_cnt, incorrect_cnt)
print("----------------------")

for tag_seq in tag_seq_list[:10]:
    print(tag_tree.tag_seq_query(tag_seq))


tag_tree = tagtree.TagTree()
tag_tree.add_tag_seq(['A', 'B', 'C'])
tag_tree.add_tag_seq(['A', 'B', 'D'])
tag_tree.print()

print(tag_tree.tag_seq_query(['A', 'B', 'C', 'E']))