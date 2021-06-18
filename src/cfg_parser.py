import nltk
from khaiii import KhaiiiApi
api = KhaiiiApi()


success = 0
fail = 0

CFG_str = """
S -> 주어 목적어 서술어_종결형
S -> 주어 서술어_종결형
S -> 주어 부사어 서술어_종결형
S -> 주어 보어 서술어_종결형
S -> 주어 목적어 부사어 서술어_종결형
주어 -> 체언 JKS | 체언 JX
목적어 -> 체언 JKO | 체언 JX 
체언 -> NNG | NNP | NNB | NP | NR 
서술어 -> 기본_서술어 | 본용언 보조용언 | 본용언 보조용언 보조용언
서술어_종결형 -> 서술어 EF
기본_서술어 -> 동사 | 동사 EP | 동사 EP EP | 형용사 | 형용사 EP | 형용사 EP EP | 체언 VCP | 체언 VCN | 체언 VCP EF | 체언 VCN EF
동사 -> VV
형용사 -> VA
본용언 -> 기본_서술어 EC
보조용언 -> VX | VX EP | VX EC | VX EP EC
SF -> '.'
"""

#grammar = nltk.CFG.fromstring(CFG_str)


# data aquisition(correct sentence (train))
filename = "./dev/train_correct_1.txt"
f = open(filename, 'r', encoding='utf-8')

tag_seq_list = []
for line in f.readlines():
    sent, tags_str = line.split(';')
    #tag_seq = tags_str.split(',')[:-1]
    #tag_seq_list.append(tag_seq)
    
    sentence = []
    print(sent, end=" ")
    
    for word in api.analyze(sent):
        word_str = str(word)
        raw_word, tagged_words_raw = word_str.split('\t')
        tagged_words = tagged_words_raw.split('+')
        #print(tagged_words)
        
        for tw in tagged_words:
            w, t = tw.split('/')
            t = t.replace(" ", "")
            w = w.replace(" ", "")
            CFG_str += t + " -> '" + w + "'\n"
            
            sentence.append(w)
            
            '''
            temp = tw.replace("/", " -> ")
            temp = temp.replace(" ", "")
            print(temp)
            CFG_str += temp + "\n"'''
    
    grammar = nltk.CFG.fromstring(CFG_str)
    #print(sentence)
    rd_parser = nltk.RecursiveDescentParser(grammar)
    status = False
    
    sent = ['그', '가', '팔', '을', '뻗', '는다']
    #print(sent == sentence[:-1])
    #print(CFG_str)
    for tree in rd_parser.parse(sentence[:-1]):
        status = True
        print(tree)
    if status:
        success += 1
        print("Success", end=" ")
        print(success)
        
    else:
        fail += 1
        print("Failed", end=" ")
        print(fail)
        
        