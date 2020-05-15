from random_word import RandomWords

r = RandomWords()
print(r.get_random_word())
word = str(r.get_random_word())
print(type(word))

for i in range(3):
    # print(r.get_random_word(hasDictionaryDef="true", includePartOfSpeech='noun',
                            # minLength=5, maxLength=10, minDictionaryCount=5))
    print(r.get_random_word(hasDictionaryDef="true", includePartOfSpeech='noun', maxLength=5))

