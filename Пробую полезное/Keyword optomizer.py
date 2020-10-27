# новый оптимизатор ключевых слов
keywords = input()
keywords = keywords.replace("?", "й") # исправляет иногда возникающую ошибку при которой  "й" отображается как "?"
keywords = keywords.replace(",", "*")
keywords = keywords.replace("|", "*")
keywords = keywords.replace(";", "*")
keywords = keywords.replace("  ", "*")
keywords = keywords.replace(" ", "*")
keywords = keywords.replace(".", "*")
b = set(keywords.split("*"))
b = sorted(b)
print(", ".join(b))
