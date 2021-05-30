from khaiii import KhaiiiApi
api = KhaiiiApi()

sent = "(버전 1.0) 한국어 예문 문법성(수용성)을 언어 사용자가 평가한 정보가 포함된 말뭉치입니다."


for word in api.analyze(sent):
    print(word)
