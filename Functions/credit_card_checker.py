import re

is_grouping = re.compile('^(?:.{4}\-){3}.{4}$').match
is_consecutive = re.compile('(.)\1{3}').search
is_valid = re.compile('^[456]\d{15}$').match

for _ in range(int(input())):
    card_no = input()
    if is_grouping(card_no):
        card_no = card_no.replace('-', '')
    if is_valid(card_no) and not is_consecutive(card_no):
        print('Valid')
    else:
        print('Invalid')