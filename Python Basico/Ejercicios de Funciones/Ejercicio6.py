def sort_words(text):
    words = text.split("-")
    words.sort()
    return "-".join(words)

#Esto de investigar como funcionan las built-in functions, es genial.

result = sort_words("python-variable-function-computer-monitor")
print(result)