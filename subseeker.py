from colorama import *
import argparse
import requests
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import RequestException

init(autoreset=True)

def banner():
    banner = """
        ███████╗██╗   ██╗██████╗ ███████╗███████╗███████╗██╗  ██╗
        ██╔════╝██║   ██║██╔══██╗██╔════╝██╔════╝██╔════╝██║ ██╔╝
        ███████╗██║   ██║██████╔╝███████╗█████╗  █████╗  █████╔╝
        ╚════██║██║   ██║██╔══██╗╚════██║██╔══╝  ██╔══╝  ██╔═██╗
        ███████║╚██████╔╝██████╔╝███████║███████╗███████╗██║  ██╗
        ╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                    # Coded By ACE Veen ~ Cyxna Team
    """
    print(Fore.RED + banner)

def find(subdomain, domain):
    try:
        req = requests.get("https://" + subdomain + "." + domain)
        if req.status_code == 200:
            print(Fore.LIGHTGREEN_EX + "[+] Subdomain --> " + "https://" + subdomain + "." + domain)
    except RequestException:
            pass

def main(args):
    domain = args.domain
    with open(args.wordlist, 'r') as f:
        wordlist = f.readlines()

    with ThreadPoolExecutor(max_workers=int(args.threads)) as executor:
        for word in wordlist:
            executor.submit(find, word.strip(), domain)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='SubSeek', description='Subdomain Finder Tool By ACEVeen', epilog='SubSeek @cyxnateam')

    parser.add_argument('-d', '--domain', required=True, help='Specify the domain to scan')
    parser.add_argument('-w', '--wordlist', required=True, help='Specify the wordlist file')
    parser.add_argument('-t', '--threads', required=True, help='Specify the threads')

    args = parser.parse_args()

    banner()
    main(args)
