import sys
from stats import num_of_words, num_of_chars, dict_to_sorted

def get_book_text(book_path):
	with open(book_path) as f:
		file_contents = f.read()
	return file_contents

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	
	book_path = sys.argv[1]
	text = get_book_text(book_path)
	num_words = num_of_words(text)
	num_chars = num_of_chars(text)
	sorted_chars = dict_to_sorted(num_chars)
	
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")	
	for item in sorted_chars:
		if not item["char"].isalpha():
			continue
		print(f"{item["char"]}: {item["num"]}")
				
	print("============= END ===============")

main()
