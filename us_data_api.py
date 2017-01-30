from flask import Flask, jsonify
import yfq
app = Flask(__name__)

@app.route("/api/v1/price/<symbol>")
def price_json(symbol):
    price = yfq.get_price(symbol)
    return jsonify(price)

@app.route("/api/v1/change/<symbol>")
def change_json(symbol):
    change = yfq.get_change(symbol)
    return jsonify(change)

@app.route("/api/v1/volume/<symbol>")
def volume_json(symbol):
    vol = yfq.get_volume(symbol)
    return jsonify(vol)

@app.route("/api/v1/avg_daily_volume/<symbol>")
def avg_daily_volume_json(symbol):
    avg = yfq.get_avg_daily_volume()

@app.route("/api/v1/stock_exchange/<symbol>")
def stock_exchange_json(symbol):
    ex = yfq.get_stock_exchange(symbol)
    return jsonify(ex)

@app.route("/api/v1/market_cap/<symbol>")
def market_cap_json(symbol):
    mcap = yfq.get_market_cap(symbol)
    return jsonify(mcap)

@app.route("/api/v1/book_value/<symbol>")
def book_value_json(symbol):
    bval = yfq.get_book_value(symbol)
    return jsonify(bval)

@app.route("/api/v1/ebitda/<symbol>")
def ebitda_json(symbol):
    ebitda = yfq.get_ebitda(symbol)
    return jsonify(ebitda)

@app.route("/api/v1/dividend_per_share/<symbol>")
def dividend_per_share_json(symbol):
    divps = yfq.get_dividend_per_share(symbol)
    return jsonify(divps)

@app.route("/api/v1/dividend_yield/<symbol>")
def dividend_yield_json(symbol):
    divyield = yfq.get_dividend_yield(symbol)
    return jsonify(divyield)

@app.route("/api/v1/earnings_per_share/<symbol>")
def earnings_per_share_json(symbol):
    eps = yfq.get_earnings_per_share(symbol)
    return jsonify(eps)

@app.route("/api/v1/52_week_high/<symbol>")
def week_high_52(symbol):
    bar = yfq.get_52_week_high(symbol)
    return jsonify(bar)

@app.route("/api/v1/52_week_low/<symbol>")
def week_low_52_json(symbol):
    bar = yfq.get_52_week_low(symbol)
    return jsonify(bar)

@app.route("/api/v1/50_day_moving_avg/<symbol>")
def day_moving_avg_50_json(symbol):
    bar = yfq.get_50day_moving_avg(symbol)
    return jsonify(bar)

@app.route("/api/v1/200_day_moving_avg/<symbol>")
def day_moving_avg_200_json(symbol):
    bar = yfq.get_200day_moving_avg(symbol)
    return jsonify(bar)

@app.route("/api/v1/price_earnings_ratio/<symbol>")
def price_earnings_ratio_json(symbol):
    bar = yfq.get_price_earnings_ratio(symbol)
    return jsonify(bar)

@app.route("/api/v1/price_earnings_growth_ratio/<symbol>")
def price_earnings_growth_ratio_json(symbol):
    bar = yfq.get_price_earnings_growth_ratio(symbol)
    return jsonify(bar)

@app.route("/api/v1/price_sales_ratio/<symbol>")
def price_sales_ratio_json(symbol):
    bar = yfq.get_price_sales_ratio(symbol)
    return jsonify(bar)

@app.route("/api/v1/price_book_ratio/<symbol>")
def price_book_ratio_json(symbol):
    bar = yfq.get_price_book_ratio(symbol)
    return jsonify(bar)

@app.route("/api/v1/short_ratio/<symbol>")
def short_ratio_json(symbol):
    bar = yfq.get_short_ratio(symbol)
    return jsonify(bar)

@app.route("/api/v1/historical/<symbol>/<int:start_date>/<int:end_date>")
def historical_price_json(symbol):
    try:
        bar = yfq.get_historical_prices(symbol, start_date, end_date)
    except urllib.error.HTTPError as e:
        bar = "stock not found"
    return jsonify(bar)

if __name__ == "__main__":
    app.run(port=8080, debug=True)
