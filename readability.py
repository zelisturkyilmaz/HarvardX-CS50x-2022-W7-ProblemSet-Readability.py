from cs50 import get_string

text = get_string("Text: ")

count_letters = 0
count_words = 1
count_sent = 0

for i in text:
    if i.isalpha():
        count_letters += 1
    if i == " ":
        count_words += 1
    if i == "." or i == "!" or i == "?":
        count_sent += 1

l = count_letters / count_words * 100
s = count_sent / count_words * 100

index = round(0.0588 * l - 0.296 * s - 15.8)
if index < 1:
    print("Before Grade 1")
elif index > 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")