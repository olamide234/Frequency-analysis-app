from collections import Counter
print('Welcome to the Frequency Analysis App')
#removing non-letters
non_letters=['1','2','3','4','5','6','7','8','9','0',' ','!','@','#','$','%','^','&','*','(',')','_','-','+','=',':',';','?','"','>','<',',','.','/','|']
#information for phrase 1
phrase_1 = input('Enter a word or phrase to count the occurrence of each letter: ').lower().strip()

for non_letter in non_letters:
    phrase_1 = phrase_1.replace(non_letter, '')
total_occurrences= len(phrase_1)

#creating a counter object to tally the number of each letter
letter_count = Counter(phrase_1)
print('\nHere is the frequency analysis from phrase: ')
print('\nLetter\t\tOccurrence\tPercentage')

for key, value in sorted(letter_count.items()):
    percent = value/total_occurrences*100
    percent = round(percent,2)
    print(key + '\t\t' + str(value) + '\t\t' + str(percent) + '%')

#make a list of highest occurrence to lowest
ordered_letter_count= letter_count.most_common()
phrase_1_ordered_letters =[]
for pair in ordered_letter_count:
    phrase_1_ordered_letters.append(pair[0])
print('\nLetter ordered from highest occurrence to lowest: ')
for letter in phrase_1_ordered_letters:
    print(letter, end=(''))

#information for phrase 2
phrase_2 = input('Enter a word or phrase to count the occurrence of each letter: ').lower().strip()

for non_letter in non_letters:
    phrase_2 = phrase_2.replace(non_letter, '')
total_occurrences= len(phrase_2)

#creating a counter object to tally the number of each letter
letter_count = Counter(phrase_2)
print('\nHere is the frequency analysis from phrase: ')
print('\nLetter\t\tOccurrence\tPercentage')

for key, value in sorted(letter_count.items()):
    percent = value/total_occurrences*100
    percent = round(percent,2)
    print(key + '\t\t' + str(value) + '\t\t' + str(percent) + '%')

#make a list of highest occurrence to lowest
ordered_letter_count= letter_count.most_common()
phrase_1_ordered_letters =[]
for pair in ordered_letter_count:
    phrase_1_ordered_letters.append(pair[0])
print('Letter ordered from highest occurrence to lowest: ')
for letter in phrase_1_ordered_letters:
    print(letter, end=(' '))