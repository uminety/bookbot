from stats import num_of_words
from stats import num_of_chars

def get_book_text(book_path):
	with open(book_path) as f:
		file_contents = f.read()
	return file_contents

def main():
	text = get_book_text("./books/frankenstein.txt")
	num_words = num_of_words(text)
	print(f"{num_words} words found in the document")
	num_chars = num_of_chars(text)
	for char in num_chars:
		quantity = num_chars[char]
		print(f"\'{char}\': {quantity}")

main()
