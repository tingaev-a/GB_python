

with open('original.txt') as text:
    line = text.readline()


with open('tanslate.txt', 'a+') as tr_text:
    for item in line:
        if '1' in item:
            item = item.replace('One', '����')
        elif '2' in item:
            item = item.replace('Two', '���')
        elif '3' in item:
            item = item.replace('Three', '���')
        elif '4' in item:
            item = item.replace('Four', '������')
        tr_text.write(item)
