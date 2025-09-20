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
	
def sort_on(items):
	return items["num"]
	
def dict_to_sorted(char_dict):
	sorted_list = []
	for chars in char_dict:
		sorted_list.append({"char": chars, "num": char_dict[chars]})
	sorted_list.sort(reverse = True, key=sort_on)
	return sorted_list
