from datetime import datetime

birthday = datetime(1998, 12, 17)
birthday = datetime.strptime('17 Dec 1998', '%d %b %Y')
birthday_string = datetime.strftime(birthday, '%d %B %Y')
birthday_weekday = birthday.strftime('%A')

now = datetime.now()
days_lived = '{:,}'.format((now - birthday).days)
ninety = datetime(1998+90, 12, 17)
to_ninety = '{:,}'.format((ninety - now).days)

my_birthday_sentence = 'I was born on {birthday}, on a {weekday}.'.format(birthday = birthday_string, weekday = birthday_weekday)
days_lived_sentence = "I've been around for {days} days.".format(days = days_lived)
to_ninety_sentence = "If I'm lucky enough to live to ninety, I'll have {days} days left!".format(days = to_ninety)
my_timely_message = ' '.join([my_birthday_sentence, days_lived_sentence, to_ninety_sentence])
print(my_timely_message)