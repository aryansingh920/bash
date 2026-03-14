import re
from collections import Counter

def get_top_404_hosts(file_path, top_k=5):
    """
    Parses a large log file to find the most frequent 404 offenders.
    NASA Format: 199.120.110.21 - - [01/Jul/1995:00:00:01 -0400] "GET /pub/winvn/readme.txt HTTP/1.0" 404 0
    """
    
    ip_pattern = r'(^[^.]+(\.[^.]+)+)\s-\s-'
    date_pattern = r'\s-\s-\s\[(\d{2}/[a-zA-Z]+/\d{4})((:\d{2}){3})\s-(\d{4})\]'
    request_pattern = r'\"([A-Z]+) \(/\S*) (HTTP\/1\.[0-2])\"'
    status_pattern = r'\s([2-5]\d{2})\s(\d+|-)$'
    
    
    counts = Counter()
    i=0
    try:

        with open(file_path, 'r', encoding='latin-1') as file:
            for line in file:
                ip_search = re.findall(ip_pattern,line)
                status_size_pattern = re.findall(status_pattern,line)
                if(len(ip_search)):
                    host = ip_search[0][0]
                    # print(host)
                    status = status_size_pattern[0][0]
            
                    
                    if(status == "404"):
                        # print(host)
                        counts[host] += 1
            # while(i <= 10000):
            #     break    
                    
                # --- END CODE ---
        print(counts.most_common(5))
        # Extract the Top K results
        return counts.most_common(top_k)

    except FileNotFoundError:
        print("File not found. Check your path!")
        return []


if __name__ == "__main__":
    # Update this to your local path
    LOG_FILE_PATH = "/Users/aryansingh/Documents/bash/script/logs/NASA_access.log"

    results = get_top_404_hosts(LOG_FILE_PATH)

    print(f"{'Host/IP Address':<30} | {'404 Count'}")
    print("-" * 45)
    for host, count in results:
        print(f"{host:<30} | {count}")
