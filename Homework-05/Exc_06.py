def is_spam_words(text, spam_words, space_around=False):
    for spam_words in text:
        if not space_around:
            spam_words = spam_words.lower()
            text = text.lower()
        if spam_words in text:
            
