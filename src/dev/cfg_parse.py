import nltk
grammar = nltk.CFG.fromstring("""
S -> 주어 목적어 서술어_종결형
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
NP -> '그'
JKS -> '가'
NNG -> '팔'
JKO -> '을'
VV -> '뻗'
EF -> '는다'
""")
sent = ['그', '가', '팔', '을', '뻗', '는다']
rd_parser = nltk.RecursiveDescentParser(grammar)
for tree in rd_parser.parse(sent):
    print(tree)