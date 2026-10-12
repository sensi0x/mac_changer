# MAC Changer

A Python command-line utility for changing and verifying the MAC address of a network interface on Linux using the `ip` command.

## Features

- Select a network interface.
- Specify a custom MAC address.
- Validate MAC address format before execution.
- Bring the selected interface down before applying the change.
- Bring the interface back up after the requested change.
- Retrieve and verify the current MAC address.
- Handle command execution and operating system errors.

## Requirements

- Python 3
- Linux
- The `ip` utility, commonly provided by `iproute2`
- Appropriate privileges to modify network interface settings

## Usage

### Display Help

```bash
python3 mac_changer.py -h
```

### Change a MAC Address

```bash
sudo python3 mac_changer.py -i eth0 -m 02:11:22:33:44:55
```

Replace `eth0` with your actual network interface and use a MAC address appropriate for your authorized test environment.

## Example Output

```text
[+] Requested MAC change for eth0 to 02:11:22:33:44:55
[+] MAC address changed successfully: 02:11:22:33:44:55
```

The output above is illustrative; actual results depend on the system and interface configuration.

## How It Works

1. Parses the interface and requested MAC address from command-line arguments.
2. Validates the MAC address format.
3. Uses the Linux `ip link` command to bring the interface down.
4. Requests the MAC address change and brings the interface back up.
5. Reads the interface configuration and compares the current MAC address with the requested value.

## Limitations

- Designed for Linux systems using `iproute2`.
- Interface drivers and hardware may restrict MAC address changes.
- Network management services may restore the original MAC address.
- Successful command execution does not guarantee that the address remains changed.
- Changing a MAC address does not provide anonymity or guarantee access to a network.

## Responsible Use

Use this tool only on devices and networks you own or have explicit authorization to administer. Avoid impersonating other devices or bypassing network access controls.

## Author

SENSI0X
