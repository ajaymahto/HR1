m = int(raw_input().strip())
english_news = set(map(int, raw_input().strip().split()))
n = int(raw_input().strip())
french_news = set(map(int, raw_input().strip().split()))
#union
print len(english_news | french_news)
print len(english_news.union(french_news))
#intersection
print len(english_news.intersection(french_news))
#difference
print len(english_news.difference(french_news))
print len(english_news - french_news)
#symmetric_difference
print len(english_news.symmetric_difference(french_news))
print len(english_news ^ french_news)