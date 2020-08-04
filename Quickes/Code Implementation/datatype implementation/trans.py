from googletrans import Translator 
transulator = Translator()
print(transulator.translate("hello",dest='ur').text)