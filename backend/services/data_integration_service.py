import requests

def connect_to_iot_platform(platform_name, api_key, params):
    if platform_name == 'platform_a':
        url = 'https://api.platforma.com/data'
        headers = {'Authorization': f'Bearer {api_key}'}
        response = requests.get(url, headers=headers, params=params)
        return response.json()
    elif platform_name == 'platform_b':
        url = 'https://api.platformb.com/data'
        headers = {'X-API-Key': api_key}
        response = requests.post(url, json=params)
        return response.json()
    else:
        raise ValueError('Unsupported platform')