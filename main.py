# imports
import sys
from stats import get_num_words
from stats import get_char_num
from stats import sort_dict

if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    book = get_book_text(sys.argv[1])
    print(book)

file = get_book_text(sys.argv[1])
chara = get_char_num(file)
sort = sort_dict(chara)
words = get_num_words(file)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
print(f"Found {words} total words")
print("--------- Character Count -------")
for so in sort:
    al = so["char"]
    if al.isalpha() == True:
        alpha = so["char"]
        numa = so["num"]
        print(f"{alpha}: {numa}")
print("============= END ===============")
