import csv
from khaiii import KhaiiiApi
api = KhaiiiApi()


filename = "./../../data/NIKL_CoLA_in_domain_dev.tsv"

f = open(filename, 'r', encoding='utf-8')
reader = csv.reader(f, delimiter='\t')


sents = []
for line in reader:
    #print(line[3])
    sent = line[3]
    sents.append(sent)

f.close()

f = open("output.txt", 'w')
for sent in sents:
    f.write("--------------------\n")
    for word in api.analyze(sent):
        f.write(str(word) + '\n')

f.close()