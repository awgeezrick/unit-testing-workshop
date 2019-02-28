
def remove_stop_words(str):
    stop_words = ['a', 'the', 'an']
    words = str.split()
    without_stop_words = [word for word in words if word not in stop_words]
    return ' '.join(without_stop_words)