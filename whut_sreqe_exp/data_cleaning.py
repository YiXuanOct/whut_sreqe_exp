import jieba
from wordcloud import WordCloud

text = ' '.join(jieba.cut(open('../data/算法工程师.txt', 'r', encoding='utf-8').read()))
stopwords = open('../data/cn_stopwords.txt', 'r', encoding='utf-8').read().split('\n')
stopwords.extend(
    ['岗位', '任职', '要求', '良好', '经验', '熟练', '使用', '具备', '优先', '了解', '项目', '管理', '负责', '工作',
     '相关', '公司', '产品', '五险', '一金', '熟悉', '业务', '部门', '一定',
     '岗位职责', '五险一金'])

wc = WordCloud(
    font_path='../data/round.ttf',
    width=1920,
    height=1080,
    background_color='white',
    stopwords=set(stopwords),
)
wc.generate(text)
wc.to_file('../data/算法工程师.png')
