import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = open("A_Ultima_Cronica.txt", "r").read()

wc = WordCloud().generate(text)
plt.imshow(wc)
plt.axis("off")
plt.show()



