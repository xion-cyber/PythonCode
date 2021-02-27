from word_count import count_words

file_path = 'text_files\\alice.txt'
with open(file_path,'r') as file_object:
    contents = file_object.read()
words = contents.lower().count('alice')
print(words)
