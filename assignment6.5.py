text = "X-DSPAM-Confidence:    0.8475"
text_find = text.find("0")
text_find1 = float(text[text_find:])
print(text_find1)
