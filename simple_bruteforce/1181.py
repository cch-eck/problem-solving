n = int(input())
words = {input().strip() for _ in range(n)}  
sorted_words = sorted(words, key=lambda x: (len(x), x))
print("\n".join(sorted_words))