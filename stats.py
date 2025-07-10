def get_num_words(text):
    words = text.split()
    count = 0
    for w in words:
        count += 1
    #print(f"{count} words found in the document")
    return count

def get_char_num(text):
    low = text.lower()
    chars = {}
    for l in low:
        if l not in chars:
            chars[l] = 0
        chars[l] += 1
    return chars

def sort_dict(dict):
    a = "char"
    b = "num"

    dlist = []
    for d in dict:
        i = dict[d]
        dlist.append({a: d, b: i})

    def sort_on(dict):
        for d in dict:
            k = dict[d]
        return k

    dlist.sort(reverse=True, key=sort_on)
    return dlist
