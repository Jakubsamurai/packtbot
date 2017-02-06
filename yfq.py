#!/usr/bin/env python
#
#  Copyright (c) 2007-2008, Corey Goldberg (corey@goldb.org)
#
#  license: GNU LGPL
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.

#	Author:		notes.angelo@gmail.com
#	License:	GPL V3
#	compatible with Python 3

# only works for US stocks

import urllib.request, urllib.parse, urllib.error


"""
This is the "yfq" module.

This module provides a Python API for retrieving stock data from Yahoo Finance.

sample usage:
>>> import yfq
>>> yfq.get_price('GOOG+APPL')
{'GOOG': '486.35', 'AAPL': '249.10'}
"""


def __request(symbol, stat):
	url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (symbol, stat)
	return urllib.request.urlopen(url).read().decode().strip().strip('"')


def get_all(symbol):
	"""
	Get all available quote data for the given ticker symbol.

	Returns a dictionary.
	"""
	url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=l1c1va2xj1b4j4dyekjm3m4rr5p5p6s7' % symbol
	temp = urllib.request.urlopen(url).readlines()
	keys = ['price', 'change', 'volume', 'avg_daily_volume', 'stock_exchange', \
		'market_cap', 'book_value', 'ebitda', 'dividend_per_share', \
		'dividend_yield', 'earning_per_share', '52_week_high', '52_week_low', \
		'50day_moving_avg', '200day_moving_avg', 'price_earnings_ratio', \
		'price_earnings_growth_ratio', 'price_sales_ratio', 'price_book_ratio', 'short_ratio']
	tkrs = symbol.split('+')
	data = {}
	for c in range(len(tkrs)):
		data[tkrs[c]] = dict(zip(keys, temp[c].decode().split(',')))
	return data


def get_price(symbol):
	return dict(zip(symbol.split('+'), __request(symbol, 'l1').split('\r\n')))


def get_change(symbol):
	return dict(zip(symbol.split('+'), __request(symbol, 'c1').split('\r\n')))


def get_volume(symbol):
	return dict(zip(symbol.split('+'), __request(symbol, 'v').split('\r\n')))


def get_avg_daily_volume(symbol):
	return dict(zip(symbol.split('+'), __request(symbol, 'a2').split('\r\n')))


def get_stock_exchange(symbol):
	return dict(zip(symbol.split('+'), __request(symbol, 'x').split('\r\n')))


def get_market_cap(symbol):
	return dict(zip(symbol.split('+'), __request(symbol, 'j1').split('\r\n')))


def get_book_value(symbol):
	return dict(zip(symbol.split('+'), __request(symbol, 'b4').split('\r\n')))


def get_ebitda(symbol):
	return dict(zip(symbol.split('+'), __request(symbol, 'j4').split('\r\n')))


def get_dividend_per_share(symbol):
	return dict(zip(symbol.split('+'), __request(symbol, 'd').splir('\r\n')))


def get_dividend_yield(symbol):
	return dict(zip(symbol.split('+'), __request(symbol, 'y').split('\r\n')))


def get_earnings_per_share(symbol):
	return dict(zip(symbol.split('+'), __request(symbol, 'e').split('\r\n')))


def get_52_week_high(symbol):
	return dict(zip(symbol.split('+'), __request(symbol, 'k').split('\r\n')))


def get_52_week_low(symbol):
	return dict(zip(symbol.split('+'), __request(symbol, 'j').split('\r\n')))


def get_50day_moving_avg(symbol):
	return dict(zip(symbol.split('+'), __request(symbol, 'm3').split('\r\n')))


def get_200day_moving_avg(symbol):
	return dict(zip(symbol.split('+'), __request(symbol, 'm4').split('\r\n')))


def get_price_earnings_ratio(symbol):
	return dict(zip(symbol.split('+'), __request(symbol, 'r').split('\r\n')))


def get_price_earnings_growth_ratio(symbol):
	return dict(zip(symbol.split('+'), __request(symbol, 'r5').split('\r\n')))


def get_price_sales_ratio(symbol):
	return dict(zip(symbol.split('+'), __request(symbol, 'p5').split('\r\n')))


def get_price_book_ratio(symbol):
	return dict(zip(symbol.split('+'), __request(symbol, 'p6').split('\r\n')))


def get_short_ratio(symbol):
	return dict(zip(symbol.split('+'), __request(symbol, 's7').split('\r\n')))


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
