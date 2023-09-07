import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

api_key = os.getenv('6LeVHLkUAAAAAC16N9EasV6cFfStTFaG9wF3tpOj', 'c08a94ac3b58ce18f575e00cfe44d27f')

solver = TwoCaptcha(api_key)

try:
    result = solver.recaptcha(
        sitekey='6LeVHLkUAAAAAC16N9EasV6cFfStTFaG9wF3tpOj',
        url='https://app.clickadilla.com/register')

except Exception as e:
    sys.exit(e)

else:
    print('solved: ' + str(result))
