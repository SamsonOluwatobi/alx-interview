#!/usr/bin/python3
'''A script that parses HTTP request logs and computes metrics.'''
import sys
import re

def print_statistics(total_file_size, status_codes_stats):
    '''Prints the accumulated statistics of the HTTP request log.'''
    print('File size: {:d}'.format(total_file_size))
    for status_code in sorted(status_codes_stats.keys()):
        count = status_codes_stats.get(status_code)
        if count > 0:
            print('{:s}: {:d}'.format(status_code, count))

def main():
    '''Main function that processes the input and computes metrics.'''
    line_count = 0
    total_file_size = 0
    status_codes_stats = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
    log_pattern = re.compile(
        r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'
    )

    try:
        for line in sys.stdin:
            match = log_pattern.match(line.strip())
            if match:
                status_code = match.group(1)
                file_size = int(match.group(2))
                
                # Accumulate file size
                total_file_size += file_size
                
                # Count status code occurrences
                if status_code in status_codes_stats:
                    status_codes_stats[status_code] += 1

                line_count += 1
                
                # Print stats every 10 lines
                if line_count % 10 == 0:
                    print_statistics(total_file_size, status_codes_stats)

    except KeyboardInterrupt:
        pass
    finally:
        # Print final statistics on interrupt or end of input
        print_statistics(total_file_size, status_codes_stats)

if __name__ == '__main__':
    main()
