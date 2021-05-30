import csv
from khaiii import KhaiiiApi
api = KhaiiiApi()


filename = "./../../data/NIKL_CoLA_in_domain_dev.tsv"

f = open(filename, 'r', encoding='utf-8')
reader = csv.reader(f, delimiter='\t')


sents_true = []
sents_false = []
for line in reader:
    if(line[1] == '1'):
        sent = line[3]
        sents_true.append(sent)
    if(line[1] == '0'): # wrong sentence
        sent = line[3]
        sents_false.append(sent)

f.close()


# sent + tag (for tag tree) - correct
f = open("train_sent_correct.txt", 'w')
for sent in sents_true:
    tag_seq = []
    for word in api.analyze(sent):
        word_str = str(word)
        raw_word, tagged_words_raw = word_str.split('\t')
        tagged_words = tagged_words_raw.split('+')
        tags = [tw.split('/')[1] for tw in tagged_words]
        tag_seq += tags
    
    tag_seq_str = ""
    for tag in tag_seq:
        if(tag[-1] == ' '):
            tag = tag[:-1]
        tag_seq_str += (tag + ',')
    output_str = sent + ';' + tag_seq_str
    #print(output_str)
    f.write(output_str + '\n')
f.close()

# sent + tag (for tag tree) - incorrect
f = open("train_sent_incorrect.txt", 'w')
for sent in sents_false:
    tag_seq = []
    for word in api.analyze(sent):
        word_str = str(word)
        raw_word, tagged_words_raw = word_str.split('\t')
        tagged_words = tagged_words_raw.split('+')
        tags = [tw.split('/')[1] for tw in tagged_words]
        tag_seq += tags
    
    tag_seq_str = ""
    for tag in tag_seq:
        if(tag[-1] == ' '):
            tag = tag[:-1]
        tag_seq_str += (tag + ',')
    output_str = sent + ';' + tag_seq_str
    #print(output_str)
    f.write(output_str + '\n')
f.close()