from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from collections import Counter # 次數統計
fontpath = "C:\Windows\Fonts\kaiu.ttf"  # 字型檔

# Read the whole text.
txtfile = "text.txt" # 剛才下載存的文字檔
text = open(txtfile, "r", encoding="utf-8").read()
#text = open(txtfile,"r").read()
text=text.split(" ")
dictionary = Counter(text)
freq = {}
for ele in dictionary:
    if ele in text:
        freq[ele] = dictionary[ele]
print(freq) # 計算出現的次數
# Generate a word cloud image
wordcloud = WordCloud(background_color="white", contour_width=3, contour_color='steelblue', font_path= fontpath).generate_from_frequencies(freq)

# 繪圖
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()