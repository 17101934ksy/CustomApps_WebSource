import json

def mailpass() :
    data = {
        'name': 'mail',
        'prov': 'pass'
    }
    json_data = json.dumps(data)
    return json_data

def mailfail() :
    data = {
        'name': 'mail',
        'prov': 'fail'
    }
    json_data = json.dumps(data)
    return json_data