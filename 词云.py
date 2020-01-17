import wordcloud
import sys
w = wordcloud.WordCloud(font_path="C:\Windows\Fonts\微软雅黑\msyh.ttc")
text = '李白 李信 韩信'
w.generate(text)
w.to_file(sys.path[0] + '/wordcloud.png')