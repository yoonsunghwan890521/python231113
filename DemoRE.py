#DemoRE.py
#정규표현식을 사용하는 경우

import re

#일반적인 검색
result = re.search("[0-9]*th", "35th")
print(result)
print(result.group())

#정확하게 일치
result = re.match("[0-9]*th", "35th")
print(result)
print(result.group())


print("[0-9]*th")

result = re.search("\d{4}", "올해는 2023년")
print(result.group())

result = re.search("\d{5}", "올해는 51200")
print(result.group())



#chatgpt 결과
import re

def is_valid_email(email):
    # Define the regular expression pattern for a valid email address
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Use the search() function to check if the email matches the pattern
    match = re.search(pattern, email)
    
    # If a match is found, the email is valid; otherwise, it's not
    return bool(match)

# Test 10 email addresses
emails_to_test = [
    'user@example.com',
    'john.doe@gmail.com',
    'invalid.email',
    'missing@at-symbol.com',
    'special!char@example.com',
    'user@subdomain.domain.com',
    'user123@123.com',
    'user@.com',
    '@missingusername.com',
    'user@missingtld.'
]

for email in emails_to_test:
    if is_valid_email(email):
        print(f'{email} is a valid email address.')
    else:
        print(f'{email} is NOT a valid email address.')



