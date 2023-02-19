words = ['how', 'much', 'is[br]', 'the', 'fish[br]', 'no', 'really']

words = [w.replace('[br]', '<br />') for w in words]
print(words)