mydata = {"time":{"updated":"Jul 2, 2024 10:47:18 UTC","updatedISO":"2024-07-02T10:47:18+00:00","updateduk":"Jul 2, 2024 at 11:47 BST"},"disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org","chartName":"Bitcoin","bpi":{"USD":{"code":"USD","symbol":"&#36;","rate":"62,703.122","description":"United States Dollar","rate_float":62703.1221},"GBP":{"code":"GBP","symbol":"&pound;","rate":"49,634.726","description":"British Pound Sterling","rate_float":49634.7255},"EUR":{"code":"EUR","symbol":"&euro;","rate":"58,542.08","description":"Euro","rate_float":58542.0802}}}

n = mydata.keys()
print(n)

print(n.__len__())

print(mydata["disclaimer"])

print(mydata["chartName"])

print(mydata["bpi"]["USD"]["rate_float"])

print(mydata["bpi"]["GBP"]["rate_float"])

print(mydata["bpi"]["EUR"]["rate_float"])
