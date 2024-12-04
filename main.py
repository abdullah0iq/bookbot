def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path).lower()
    text_report_printer(book_path,text)
    


def text_report_printer(path , text):
    print(f"--- Begin report of {path} ---")
    print(f"{words_counter(text)} words found in the document\n")
    chars_counter = char_counter_dic(text)
    
    for t in chars_counter:
        print(f"The '{t[0]} character was found {t[1]} times")
    print("--- End report ---")


def char_counter_dic(text):
    chars = {}
    for c in text :
        if c.isalpha():
            if c in chars :
                chars[c] +=1
            else :
                chars[c] =0
    chars = sorted(chars.items() , key=lambda item: item[1] , reverse=True)
    return chars


def words_counter(content):
    return len(content.split())



def get_book_text(path):
    with open(path) as f:
        return f.read()

main()