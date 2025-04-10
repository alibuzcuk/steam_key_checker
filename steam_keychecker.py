import requests

def check_key(key):
    url = f"https://store.steampowered.com/account/redeem?key={key}"
    response = requests.get(url)
    if response.status_code == 200 and "This product key is already registered" in response.text:
        return True
    else:
        return False

def save_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data + '\n')

def check_keys_from_wordlist(wordlist_file, valid_file, invalid_file):
    valid_count = 0
    invalid_count = 0
    with open(wordlist_file, 'r') as file:
        keys = file.readlines()
    for key in keys:
        key = key.strip()
        if check_key(key):
            print(f"Valid Key: {key}")
            save_to_file(valid_file, key)
            valid_count += 1
        else:
            print(f"Invalid Key: {key}")
            save_to_file(invalid_file, key)
            invalid_count += 1
    print(f"\nValid keys: {valid_count}")
    print(f"Invalid keys: {invalid_count}")

wordlist_file = 'wordlist.txt'
valid_file = 'valid_keys.txt'
invalid_file = 'invalid_keys.txt'

check_keys_from_wordlist(wordlist_file, valid_file, invalid_file)
