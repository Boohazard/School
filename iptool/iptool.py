import subprocess

if __name__ == '__main__':
    process = subprocess.run(['ipconfig', '/all'], capture_output=True)

    for full_line in process.stdout.splitlines():
            if b"Ethernet " in full_line:
                bytes_line_dirty = full_line.split(b"'")[0]
                line_dirty = bytes_line_dirty.decode()
                ethernet = line_dirty.strip()
                print(ethernet)

            elif b"IPv4 Address" in full_line:
                bytes_line_dirty = full_line.split(b":")[1]
                line_dirty = bytes_line_dirty.decode()
                line = line_dirty.strip()
                ip_address = line.split("(")[0]
                print("Je IP-adres is: " + ip_address)

            elif b"Physical Address" in full_line:
                bytes_line_dirty = full_line.split(b":")[1]
                line_dirty = bytes_line_dirty.decode()
                mac_address = line_dirty.strip()
                print("Je MAC-adres is: " + mac_address)

            elif b"Subnet Mask" in full_line:
                bytes_line_dirty = full_line.split(b":")[1]
                line_dirty = bytes_line_dirty.decode()
                sub_mask = line_dirty.strip()
                print("Je Subnet Mask is: " + sub_mask)

            elif b"Default Gateway" in full_line:
                bytes_line_dirty = full_line.split(b":")[1]
                line_dirty = bytes_line_dirty.decode()
                def_gateway = line_dirty.strip()
                print("Je Gateway is: " + def_gateway)

            elif b"DHCP Server" in full_line:
                bytes_line_dirty = full_line.split(b":")[1]
                line_dirty = bytes_line_dirty.decode()
                dhcp = line_dirty.strip()
                print("Je DHCP server is: " + dhcp)

            elif b"DNS Servers" in full_line:
                bytes_line_dirty = full_line.split(b":")[1]
                line_dirty = bytes_line_dirty.decode()
                dns = line_dirty.strip()
                print("Je DNS server is: " + dns)
                print("\n")




