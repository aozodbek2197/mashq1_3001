# 1-masala
matn = input("Matn kiriting: ")
katta_harf = matn.title()
print(katta_harf)
# 2-masala
def qavs_alohida(text):
    result = []
    inside = False
    word = ""

    for char in text:
        if char == "(":
            inside = True
            word = ""
        elif char == ")":
            inside = False
            result.append(word)
        elif inside:
            word += char

    return result

print(qavs_alohida("Bu (birinchi) va (ikkinchi) qavs"))
# 3-masala
def email_tekshir(email):
    return "@" in email and "." in email.split("@")[-1]

print(email_tekshir("salom@gmail.com"))
print(email_tekshir("salomgmail.com"))
# 4-masala
def takrorlanuvch_harf(harf):
    result = ""
    for h in harf:
        if h not in result:
            result += h

    return result
print(takrorlanuvch_harf("harf"))
# 5-masala
def palindrom(text):
    tekshir = text.replace(" ", "").lower()
    return tekshir == tekshir[::-1]

print(palindrom("Aziz a Aziza"))
# 6-masala
def eng_kop_soz(text):
    words = text.lower().split()
    max_word = ""
    max_count = 0

    for word in words:
        count = words.count(word)
        if count > max_count:
            max_count = count
            max_word = word
    return max_word, max_count

print(eng_kop_soz("python yaxshi python zor python juda yaxshi"))
# 7-masala
def format(text):
    result = ""

    for i in range(0, len(text), 3):
        result += text[i:i+3] + "-"

    return result[:-1]

print(format("1234567890"))
