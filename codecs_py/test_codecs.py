import codecs

def test_hex():
    en = codecs.encode(['0','2'], 'dex_codec')
    print(en)
    de = en.decode("ISO-8859-1")
    print(de)
    return en

print(test_hex())
print('')