def num_of_words(text):
	words = text.split()
	return len(words)
	
def num_of_chars(text):
	lower = text.lower()
	char_dict = {}
	for char in lower:
		if char not in char_dict:
			char_dict[char] = 1
		else:
			char_dict[char] += 1
	return char_dict
