from __future__ import print_function
from os import getenv
import sys

"""def env_var(name):
    value = getenv(name, None)

    if value is None:
        print("You must set the environment variable", name, file = sys.stderr)
        sys.exit(1)
    
    return value"""

def extract_error(response):
    for response_part in response['messages']:
        if response_part['status'] != '0':
            return response_part['error-text']
