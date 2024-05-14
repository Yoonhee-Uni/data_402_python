from csv_intro import *
import csv

# def test_add():
#     actual = add(2, 2)
#     expected = 4
#     assert actual == expected

def test_read():
    actual = read_file('user_details.csv')
    expected = [['Alasdair', 'Beeckx', 'abeeckx0@un.org'], ['Saunder', 'Murname', 'smurname1@ftc.gov'], ['Julissa', 'Spriddle', 'jspriddle2@chicagotribune.com'], ['Bernadene', 'Peak', 'bpeak3@fc2.com'], ['Cass', 'Bernardeschi', 'cbernardeschi4@technorati.com'], ['Aggi', 'Lipson', 'alipson5@ucoz.ru'], ['Trescha', 'Damato', 'tdamato6@skyrock.com'], ['Dav', 'Headon', 'dheadon7@ted.com'], ['Nealson', 'Janeway', 'njaneway8@360.cn'], ['Laney', 'Trobey', 'ltrobey9@eventbrite.com']]
    assert actual == expected

def test_read2():
    actual = read_file('user_details.csv')[0]
    expected = ['Alasdair', 'Beeckx', 'abeeckx0@un.org']
    assert actual == expected


