import sys
import requests
import apache_log_parser

def fetch_log_entries(url):
    text = requests.get(url)
    return text

def parse_logs(log_entries):
    # Parse log entries and return a list of dictionaries.
    with open("logs.txt", "w") as logs:
        logs.write(log_entries.text)

    # Prepare the parser
    line_parser = apache_log_parser.make_parser("%a %l %u %t \"%r\" %s %b \"%{Referer}i\" \"%{User-Agent}i\"")

    # List to hold parsed data
    entries = []
    try:
        file = open(logs.txt, 'r')
        for line in file:
            parsed_data = line_parser(line)
            entries.append(parsed_data)
    except:
        print("There was a problem parsing the file")
        sys.exit(1)
    finally:
        file.close()

    return log_entries

def analyze_logs(logs):
    # Analyze logs to find specific user agent IP and the most popular status code.

    # Iterate through the logs to find the entry with the desired user agent
    for log in logs:
        if log.get("user_agent") == "Chrome/38.0.855.0":
            print(f"IP Address: {log.get('ip')}")
            break

    status_count = {}
    for entry in logs:
        status = entry['status']
        if status in status_count:
            status_count[status] = status_count[status] + 1
        else:
            status_count[status] = 1

    most_occur = max(status_count.values())
    most_common_status_code = []
    for status in status_count.keys():
        if status_count[status] == most_occur:
            most_common_status_code.append(status)

    # Return a dictionary containing the result
    return {'Most Frequent Status Code': most_common_status_code, 'Number of Occurences': most_occur}


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
        