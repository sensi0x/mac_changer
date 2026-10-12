
import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option(
        "-i", "--interface",
        dest="network_interface",
        help="Network interface to change"
    )

    parser.add_option(
        "-m", "--mac",
        dest="new_mac",
        help="New MAC address"
    )

    options, arguments = parser.parse_args()

    if not options.network_interface:
        parser.error("[-] Network interface is required")

    if not options.new_mac:
        parser.error("[-] New MAC address is required")

    if not re.fullmatch(
        r"(?:[0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}",
        options.new_mac
    ):
        parser.error("[-] Invalid MAC address format")

    return options


def run_command(command):
    subprocess.run(command, check=True)


def mac_changer(network_interface, new_mac):
    try:
        run_command(["ip", "link", "set", "dev",
                     network_interface, "down"])

        run_command(["ip", "link", "set", "dev",
                     network_interface, "address", new_mac])

        run_command(["ip", "link", "set", "dev",
                     network_interface, "up"])

        print(
            "[+] Requested MAC change for "
            + network_interface + " to " + new_mac
        )

    except subprocess.CalledProcessError as error:
        print("[-] Failed to change MAC address:", error)
        raise


def get_mac(network_interface):
    result = subprocess.run(
        ["ip", "link", "show", "dev", network_interface],
        capture_output=True,
        text=True,
        check=True
    )

    match = re.search(
        r"\blink/ether\s+([0-9a-fA-F]{2}(?::[0-9a-fA-F]{2}){5})",
        result.stdout
    )

    if match:
        return match.group(1)

    return None


if __name__ == "__main__":
    options = get_arguments()

    try:
        mac_changer(
            options.network_interface,
            options.new_mac
        )

        current_mac = get_mac(options.network_interface)

        if current_mac and current_mac.lower() == options.new_mac.lower():
            print(
                "[+] MAC address changed successfully: "
                + current_mac
            )
        else:
            print("[-] MAC address verification failed.")
            print("Current MAC:", current_mac)

    except (subprocess.CalledProcessError, OSError) as error:
        print("[-] Error:", error)
