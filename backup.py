import sys
import requests
import apache_log_parser

def fetch_log_entries(url):
    ex2 = requests.get(url)
    return ex2.text

def parse_logs(log_entries):
    # Parse log entries and return a list of dictionaries.
    parts = log_entries.split(" ")

    for i in
    # Extract and concatenate the date part
    date = parts[3] + ' ' + parts[4]
    # Extract and concatenate the request line
    request_line = ' '.join(parts[5:8])
    # Create the dictionary with structured data
    log_dict = {
        'IP': parts[0],
        'Identifier': parts[1],
        'UserID': parts[2],
        'Date': date,
        'Request': request_line,
        'Status': parts[8],
        'Size': parts[9],
        'Referer': parts[10],
        'UserAgent': ' '.join(parts[11:])
    }
    return log_dict

def analyze_logs(logs):
# Analyze logs to find specific user agent IP and the most popular status code.
# FIX ME


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    log_entries = fetch_log_entries(url)
    if log_entries:
        logs = parse_logs(log_entries)
        analysis = analyze_logs(logs)
        print("The IP of the user with user agent Chrome/38.0.855.0 is: " + str(analysis['IP for User Agent']))
        print("The most popular status code is: " + str(analysis['Most Popular Status']))
    else:
        print("Failed to fetch or parse logs.")
        