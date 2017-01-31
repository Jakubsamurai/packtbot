import urllib.request, urllib.parse, urllib.error
import datetime



def get_historical_prices(symbol, start_date, end_date):
    """
    Get historical prices for the given ticker symbol.
	Date format is 'YYYYMMDD'
	All parameters are strings
	Returns a nested list.
	"""
	url = 'http://ichart.yahoo.com/table.csv?s=%s&' % symbol + \
		'd=%s&' % str(int(end_date[4:6]) - 1) + \
		'e=%s&' % str(int(end_date[6:8])) + \
		'f=%s&' % str(int(end_date[0:4])) + \
		'g=d&' + \
		'a=%s&' % str(int(start_date[4:6]) - 1) + \
		'b=%s&' % str(int(start_date[6:8])) + \
		'c=%s&' % str(int(start_date[0:4])) + \
		'ignore=.csv'
	days = urllib.request.urlopen(url).readlines()
	data = []
	for day in days:
		data.append(day[:-1].decode().split(','))
	return data