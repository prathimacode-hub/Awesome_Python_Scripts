import sys
import nmap

def main():
    input_data = input("Please input hosts and ports (e.g., '192.168.1.1 80,443'): ")
    scan_row = input_data.strip().split()
    
    if len(scan_row) != 2:
        print("Error! Please provide both hosts and ports.")
        sys.exit(1)

    hosts = scan_row[0]
    ports = scan_row[1]
    
    try:
        nm = nmap.PortScanner()
    except nmap.PortScannerError as e:
        print(e)
        print("Nmap not found! Ensure that Nmap is installed.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        sys.exit(1)

    try:
        print(f"Scanning {hosts} on ports {ports}...")
        nm.scan(hosts=hosts, arguments=f'-v -sS -p {ports}')
    except Exception as e:
        print(f"Scan error: {str(e)}")
        sys.exit(1)

    for host in nm.all_hosts():
        print('-------------------------------------------')
        print(f'Host : {host} ({nm[host].hostname()})')
        print(f'State : {nm[host].state()}')

        for proto in nm[host].all_protocols():
            print('-------------------')
            print(f'Protocol : {proto}')
            ports = sorted(nm[host][proto].keys())
            for port in ports:
                state = nm[host][proto][port]['state']
                print(f'Port : {port}\tState : {state}')

if __name__ == "__main__":
    main()
