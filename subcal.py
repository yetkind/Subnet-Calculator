
import ipaddress
import math

def analyze_network(ip_cidr):
    try:
        network = ipaddress.ip_network(ip_cidr, strict=False)
    except ValueError as e:
        print(f"Error: {e}")
        return

    print(f"\nAnalyzing Network: {ip_cidr}")
    print(f"  Network Address : {network.network_address}")
    print(f"  Subnet Mask     : {network.netmask}")
    print(f"  CIDR Notation   : /{network.prefixlen}")
    print(f"  Broadcast Addr  : {network.broadcast_address}")
    print(f"  Usable Hosts    : {network.num_addresses - 2}")
    print(f"  Wildcard Mask   : {ipaddress.IPv4Address(int(network.hostmask))}")
    hosts = list(network.hosts())
    if hosts:
        print(f"  First Host      : {hosts[0]}")
        print(f"  Last Host       : {hosts[-1]}")
    else:
        print("  No usable hosts in this subnet.")
    print(f"  Next Subnet     : {network.broadcast_address + 1}")
    print("-" * 50)

def calculate_subnet_mask(required_subnets, required_hosts, start_network='0.0.0.0/0'):
    # Determine host bits so that 2^h - 2 ≥ required_hosts
    host_bits = math.ceil(math.log2(required_hosts + 2))
    cidr = 32 - host_bits
    usable_per = 2 ** host_bits - 2

    print(f"\nTo get ≥{required_subnets} subnets with ≥{required_hosts} hosts each from {start_network}:")
    print(f"  Subnet Mask     : {ipaddress.IPv4Network('0.0.0.0/'+str(cidr)).netmask}")
    print(f"  CIDR Notation   : /{cidr}")
    print(f"  Usable Hosts/Sub: {usable_per}")
    print(f"  (Each is a /{cidr} network.)")
    print("-" * 50)

    # 
        # Parse the network (must include CIDR)
    try:
        pool = ipaddress.ip_network(start_network, strict=False)
    except ValueError as e:
        print(f"Error with start network: {e}")
        return

    # Generate subnets from the pool
    sub_iter = pool.subnets(new_prefix=cidr)
    sub_iter = pool.subnets(new_prefix=cidr)

    for i in range(1, required_subnets + 1):
        try:
            sn = next(sub_iter)
        except StopIteration:
            print(f"Only {i-1} subnets available; cannot produce more.")
            break

        hosts = list(sn.hosts())
        first = hosts[0] if hosts else None
        last  = hosts[-1] if hosts else None
        print(f"Subnet {i}:")
        print(f"  Network Addr : {sn.network_address}")
        print(f"  Broadcast    : {sn.broadcast_address}")
        print(f"  First Host   : {first}")
        print(f"  Last Host    : {last}")
        print(f"  Next Subnet  : {sn.broadcast_address + 1}")
        print("-" * 50)

def main():
    while True:
        print("\nSubnet Calculator Menu:")
        print("1. Analyze a network (IP/CIDR)")
        print("2. Calculate subnets & hosts requirements")
        print("3. Exit")
        choice = input("Enter choice (1-3): ")

        if choice == '1':
            ip_cidr = input("Enter IP/CIDR (e.g. 192.168.1.0/24): ")
            analyze_network(ip_cidr)
        elif choice == '2':
            try:
                rs = int(input("Required subnets: "))
                rh = int(input("Hosts per subnet: "))
                start = input("Starting network (e.g. 10.0.0.0/16) or press Enter for 0.0.0.0/0: ") or '0.0.0.0/0'
                calculate_subnet_mask(rs, rh, start)
            except ValueError:
                print("Please enter valid integers.")
        elif choice == '3':
            print("Goodbye.")
            break
        else:
            print("Invalid choice; try again.")

if __name__ == "__main__":
    main()
