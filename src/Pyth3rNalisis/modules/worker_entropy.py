import math
from collections import Counter

def calculate_entropy(data):
    if not data:
        return 0
    entropy = 0
    counter = Counter(data)
    length = len(data)
    for count in counter.values():
        p_x = count / length
        entropy += - p_x * math.log2(p_x)
    max_entropy = math.log2(length)  # Maximum possible entropy
    return entropy, max_entropy


def check_entropy(file_path):
    with open(file_path, 'rb') as f:
        file_data = f.read()
    entropy, max_entropy = calculate_entropy(file_data)
    entropy_percentage = (entropy / max_entropy) * 100 if max_entropy > 0 else 0

    # Color coding based on entropy percentage
    if 85 < entropy_percentage:
        color = '\033[91m'  # Red for high entropy (suspicious)
    elif 70 < entropy_percentage:
        color = '\033[93m'  # Yellow for moderate entropy (potentially suspicious)
    else:
        color = '\033[92m'  # Green for low entropy (less suspicious)

    reset_color = '\033[0m'

    print(f"File Entropy: {entropy:.2f} | {color}{entropy_percentage:.2f}%{reset_color}")
      