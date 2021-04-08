import re

nomor = '08553 2597867'
regex = re.compile(r'\d{4} \d{4}')
mo = regex.findall(nomor)
print(mo)
