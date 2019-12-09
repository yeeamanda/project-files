import search1
import search2
import search3

def test_cleanme():
	assert cleanMe('.Cory Booker') == 'Cory Booker'
	assert cleanMe('Cory Booker?') == 'Cory Booker'
def test_search1():
    assert runSearch1('Cory Booker') ==('Session: ' + '113'+
                        '\n\tFacebook Account: '+ 'None'+
                        '\n\t' + 'Title: ' + 'Senator, 2nd Class' +
                        'Date of Birth: ' + '1969-04-27'+'\n\t' +
                        'Url: ' + 'https://www.booker.senate.gov'+'\n\t' +
                        'State: '+ 'NJ'+'\n\t'+
                        "In Office: "+ 'False'+'\n' + 'Session: ' + '114'+
                        '\n\tFacebook Account: '+ 'None'+
                        '\n\t' + 'Title: ' + 'Senator, 2nd Class' +
                        'Date of Birth: ' + '1969-04-27'+'\n\t' +
                        'Url: ' + 'https://www.booker.senate.gov'+'\n\t' +
                        'State: '+ 'NJ'+'\n\t'+
                        "In Office: "+ 'False'+'\n'+'Session: ' + '115'+
                        '\n\tFacebook Account: '+ 'None'+
                        '\n\t' + 'Title: ' + 'Senator, 2nd Class' +
                        'Date of Birth: ' + '1969-04-27'+'\n\t' +
                        'Url: ' + 'https://www.booker.senate.gov'+'\n\t' +
                        'State: '+ 'NJ'+'\n\t'+
                        "In Office: "+ 'False'+'\n' + 'Session: ' + '116'+
                        '\n\tFacebook Account: '+ 'None'+
                        '\n\t' + 'Title: ' + 'Senator, 2nd Class' +
                        'Date of Birth: ' + '1969-04-27'+'\n\t' +
                        'Url: ' + 'https://www.booker.senate.gov'+'\n\t' +
                        'State: '+ 'NJ'+'\n\t'+
                        "In Office: "+ 'True'+'\n')

def test_search2():
	assert get_district('MD') != 1
	assert get_district('WY') == 1

if __name__ == '__main__':
	test_cleanme()
	test_search1()
	test_search2()

