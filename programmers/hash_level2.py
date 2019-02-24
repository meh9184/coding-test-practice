def solution(phone_book):
    phone_book.sort(key=len)

    for i, phone1 in enumerate(phone_book):
        for phone2 in phone_book[i+1:]:
            if isPrefix(phone1, phone2):
                return False

    return True

def isPrefix(str1, str2):
    return str2.startswith(str1)



# phone_book = ['119', '97674223', '1195524421']

phone_book = ["113", "12340", "123440", "12345", "98346"]

print(solution(phone_book))
