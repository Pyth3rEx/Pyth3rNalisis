import re
from tabulate import tabulate

try:
    import Pyth3rNalisis.modules.module_log as module_log
except:
    import modules.module_log as module_log

def find_regex_matches(text_data, pattern):
    return re.findall(pattern, text_data)

def check_for_IPv4(text_data):
    pattern = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    matches = find_regex_matches(text_data, pattern)
    return matches

def check_for_IPv6(text_data):
    pattern = r'\b(?:' \
              r'([0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}|' \
              r'([0-9A-Fa-f]{1,4}:){1,7}:|' \
              r'([0-9A-Fa-f]{1,4}:){1,6}:[0-9A-Fa-f]{1,4}|' \
              r'([0-9A-Fa-f]{1,4}:){1,5}(:[0-9A-Fa-f]{1,4}){1,2}|' \
              r'([0-9A-Fa-f]{1,4}:){1,4}(:[0-9A-Fa-f]{1,4}){1,3}|' \
              r'([0-9A-Fa-f]{1,4}:){1,3}(:[0-9A-Fa-f]{1,4}){1,4}|' \
              r'([0-9A-Fa-f]{1,4}:){1,2}(:[0-9A-Fa-f]{1,4}){1,5}|' \
              r'[0-9A-Fa-f]{1,4}:((:[0-9A-Fa-f]{1,4}){1,6})|' \
              r':((:[0-9A-Fa-f]{1,4}){1,7}|:)|' \
              r'fe80:(:[0-9A-Fa-f]{0,4}){0,4}%[0-9a-zA-Z]{1,}|' \
              r'::(ffff(:0{1,4}){0,1}:){0,1}' \
              r'((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}' \
              r'(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|' \
              r'([0-9A-Fa-f]{1,4}:){1,4}:' \
              r'((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}' \
              r'(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])' \
              r')\b'
    matches = find_regex_matches(text_data, pattern)
    return matches

def check_for_eMail(text_data):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return find_regex_matches(text_data, pattern)

def check_for_domain(text_data):
    pattern = r'\b(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+(?:[A-Z|a-z]{2,})\b'
    return find_regex_matches(text_data, pattern)

def openForStatic(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    return data

def check_CommandAndControl(file_path):
    data = openForStatic(file_path)

    # Convert binary data to a string
    try:
        text_data = data.decode('utf-8')  # Decode using UTF-8 encoding
    except UnicodeDecodeError:
        text_data = data.decode('latin-1')  # Use a fallback encoding if UTF-8 fails
    except Exception as e:
        module_log.critical(f'Cannot decode data: {e}')
        return

    ipv4_addresses = check_for_IPv4(text_data)
    ipv6_addresses = check_for_IPv6(text_data)
    emails = check_for_eMail(text_data)
    domains = check_for_domain(text_data)

    # Create a single-line entry for each type
    results = [
        ['IPv4', ', '.join(ipv4_addresses)],
        ['IPv6', ', '.join(ipv6_addresses)],
        ['Email', ', '.join(emails)],
        ['Domain', ', '.join(domains)]
    ]

    headers = ['Type', 'Matches']
    print(tabulate(results, headers=headers, tablefmt="fancy_grid"))