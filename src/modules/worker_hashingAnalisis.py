import hashlib
import os
import sys
import requests
from tabulate import tabulate
import modules.module_log as module_log

def calculate_hash(file_path, hash_type='sha256'):
    hash_func = getattr(hashlib, hash_type)()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hash_func.update(chunk)
    except Exception as e:
        module_log.critical('An error has occured, not able to calculate hash, quitting.')
        sys.exit(1)  # Exit the program with a non-zero status to indicate an error
    return hash_func.hexdigest()

def MalwareBazaar(file_hash):
    url = 'https://mb-api.abuse.ch/api/v1/'
    data = {'query': 'get_info', 'hash': file_hash}

    response = requests.post(url, data=data)
    result = response.json()

    if result['query_status'] == 'ok':
        return True
    else:
        return False
    
def VirusTotal(file_hash):
    api_key = os.getenv('VirusTotal_API_Key')
    if api_key is None:
        module_log.warning("Could not find 'VirusTotal_API_Key' as an environment variable. Skipping check.")
        return False
    url = f'https://www.virustotal.com/vtapi/v2/file/report?apikey={api_key}&resource={file_hash}'

    response = requests.get(url)
    result = response.json()

    if result['response_code'] == 1:
        if result['positives'] > 0:
            return True
        else:
            return False
    else:
        return False

def HybridAnalisis(file_hash):
    api_key = os.getenv('HybridAnalisis_API_Key')
    if api_key is None:
        module_log.warning("Could not find 'HybridAnalisis_API_Key' as an environment variable. Skipping check.")
        return False

    headers = {
    'User-Agent': 'Falcon Sandbox',
    'api-key': api_key
    }
    url = f'https://www.hybrid-analysis.com/api/v2/search/hash/{file_hash}'

    response = requests.get(url, headers=headers)
    result = response.json()

    if response.status_code == 200 and result:
        return True
    else:
        return False

def MalShare(file_hash):
    api_key = os.getenv('MalShare_API_Key')
    if api_key is None:
        module_log.warning("Could not find 'MalShare_API_Key' as an environment variable. Skipping check.")
        return False

    url = f'https://malshare.com/api.php?api_key={api_key}&action=search&query={file_hash}'

    response = requests.get(url)
    result = response.json()

    if result:
        return True
    else:
        return False
    
def check_Against_Public_DB(file_hash):

    #Checking against MalwareBazaar
    MalwareBazaar_found = MalwareBazaar(file_hash)
    
    #Checking against VirusTotal
    VirusTotal_found = VirusTotal(file_hash)
    
    #Checking against HybridAnalisis
    HybridAnalisis_found = HybridAnalisis(file_hash)

    #Checking against MalShare
    MalShare_found = MalShare(file_hash)

    return MalwareBazaar_found, VirusTotal_found, HybridAnalisis_found, MalShare_found

def perform_hashing_analisis(file_path):
    file_hash = calculate_hash(file_path)
    MalwareBazaar_found, VirusTotal_found, HybridAnalisis_found, MalShare_found = check_Against_Public_DB(file_hash)

    def color_boolean(value):
        if value:
            return "\033[91mTrue\033[0m"  # Red for True
        else:
            return "\033[92mFalse\033[0m"  # Green for False

    data = [
    ["MalwareBazaar", color_boolean(MalwareBazaar_found)],
    ["VirusTotal", color_boolean(VirusTotal_found)],
    ["HybridAnalysis", color_boolean(HybridAnalisis_found)],
    ["MalShare", color_boolean(MalShare_found)]
    ]

    # Printing the table
    print(tabulate(data, headers=["Database", "Found"], tablefmt="grid"))