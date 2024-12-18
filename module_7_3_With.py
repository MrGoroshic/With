class WordsFinder:
    def __init__(self, *file_name):
        self.file_name = list(file_name)

    def get_all_words(self):
        all_words = {}
        symbol = [',', '.', '=', '!', '?', ';', ':']
        for current_file in self.file_name:
            with open(current_file, encoding="utf-8") as file:
                file_contents = file.read().lower()
                for sym in symbol:
                    file_contents = file_contents.replace(sym, "")
                file_contents = file_contents.split()
                all_words[current_file] = file_contents
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        found_word = {}
        found = False
        for key, value in all_words.items():
            for val in value:
                if val == word.lower():
                    found = True
            if found:
                found_word[key] = value.index(word.lower())+1
                found = False
            else:
                if len(found_word) == 0:
                    return "The word was not found"
                else:
                    return found_word
        return found_word

    def count(self, word):
        all_words = self.get_all_words()
        found_word = {}
        count = 0
        for key, value in all_words.items():
            for val in value:
                if val == word.lower():
                    count += 1
            found_word[key] = count
            count = 0
        return found_word


finder1 = WordsFinder('mod_7_3.txt')
print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))