import json
from datetime import date, datetime
from decimal import Decimal

DATE_FORMAT = "date(%Y,%m,%d)"
DATETIME_FORMAT = "datetime(%Y,%m,%d,%H,%M,%S,%f)"

class ExtendJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime(DATETIME_FORMAT)
        elif isinstance(obj, date):
            return obj.strftime(DATE_FORMAT)
        elif isinstance(obj, Decimal):
            # don't really care
            return float(obj)

        return super(ExtendJSONEncoder, self).default(obj)

def datetime_parser(dct):
    for k, s in dct.items():
        if isinstance(s, basestring):
            try:
                dct[k] = datetime.strptime(s, DATE_FORMAT).date()
            except Exception as e:
                pass

            try:
                dct[k] = datetime.strptime(s, DATETIME_FORMAT)
            except Exception as e:
                pass

    return dct

def dump(obj, **kwargs):
    return json.dump(obj, cls=ExtendJSONEncoder, **kwargs)

def dumps(obj, **kwargs):
    return json.dumps(obj, cls=ExtendJSONEncoder, **kwargs)

def loads(s, **kwargs):
    return json.loads(s, object_hook=datetime_parser, **kwargs)

def load(fp, **kwargs):
    return json.load(fp, object_hook=datetime_parser, **kwargs)
