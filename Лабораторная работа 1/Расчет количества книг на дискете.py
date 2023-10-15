totalMemory = 1.44 * 1024 * 1024
pages = 100
lines = 50
syllables = 25
symbolMemory = 4

answer = int(totalMemory // (symbolMemory * syllables * lines * pages))

print("Количество книг, помещающихся на дискету:", answer)
