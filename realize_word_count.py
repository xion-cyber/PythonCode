from word_count import count_words

file_path = 'text_files\\'
file_names = ['alice.txt','saddhartha.txt','little_women.txt']
for file_name in file_names:
    file_paths = file_path + file_name
    count_words(file_paths)