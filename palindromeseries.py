cases = int(input())

for case in range(cases):
    
    word_count = int(input())
    words = [input() for _ in range(word_count)]

    result = True
    bad_nums = []
    for idx, word in enumerate(words):
        if word.lower() != word[::-1].lower():
            result = False
            bad_nums.append(str(idx+1))
    false_str = f" - {', '.join(bad_nums)}" if result == False else ''
    print(str(result) + false_str)