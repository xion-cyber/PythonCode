def count_words(file_path):
    """计算一个文本有多少单词"""
    try:
        with open(file_path,'r') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        # 计算文本有多少词
        words = contents.split()
        num_words = len(words)
        print("The file has about " + str(num_words) + " words.")
