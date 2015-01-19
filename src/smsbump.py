import urllib
import json

_resp = ''


def _getApiUrl(method, apikey):
    return 'http://api.smsbump.com/' + method + '/' + apikey + '.json'


def _send_single(
    apikey,
    fromName,
    toNumber,
    message,
    callback,
    ):
    global _resp

    params = urllib.urlencode({'from': fromName, 'to': toNumber,
                              'message': message})
    request = urllib.urlopen(_getApiUrl('send', apikey), params)
    _resp = request.read()

    if hasattr(callback, '__call__'):
        callback(json.loads(_resp))


def send(
    apikey=None,
    fromName='',
    toNumber=None,
    message=None,
    callback=None,
    ):
    if None in [apikey, toNumber, message]:
        raise TypeError('apikey, toNumber and message cannot be None')

    if len([x for x in [apikey, toNumber, message] if x]) != 3:
        raise ValueError('apikey, toNumber and message must be strings and cannot be empty'
                         )

    if isinstance(toNumber, basestring):
        _send_single(apikey, fromName, toNumber, message, callback)
    elif isinstance(toNumber, (list, tuple)):

        for x in toNumber:
            _send_single(apikey, fromName, x, message, callback)


def estimate(
    apikey=None,
    toNumber=None,
    message=None,
    callback=None,
    ):
    global _resp

    if None in [apikey, toNumber, message]:
        raise TypeError('apikey, toNumber and message cannot be None')

    if len([x for x in [apikey, toNumber, message] if x]) != 3:
        raise ValueError('apikey, toNumber and message must be strings and cannot be empty'
                         )

    params = urllib.urlencode({'to': toNumber, 'message': message})
    request = urllib.urlopen(_getApiUrl('estimate', apikey), params)
    _resp = request.read()

    resp = json.loads(_resp)
    if hasattr(callback, '__call__'):
        callback(resp)
    else:
        return resp


def balance(apikey=None, callback=None):
    if None in [apikey]:
        raise TypeError('apikey cannot be None')

    request = urllib.urlopen(_getApiUrl('balance', apikey))
    _resp = request.read()

    resp = json.loads(_resp)
    if hasattr(callback, '__call__'):
        callback(resp)
    else:
        return resp


def getResponse():
    return _resp



			