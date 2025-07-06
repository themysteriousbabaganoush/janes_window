__title__ = "Janes Window"
__version__ = "1.0"
__author__ = "Chairman Hellsing & Mun"


import subprocess
import os
import tempfile
import platform
from datetime import datetime
import time

def print_ascii_girl():
    art = r'''
..............................-@@@@@@@@@@@@@..............................
..........................@@@@@@@@@@@@@@@@@@@@@-#.........................
.......................@@@@@@@@@@@@@@@@@@@@@@@@@@@.#......................
.....................+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##....................
...................:#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:@@@.%..................
.................#..:-.+@@@@:@@@@@@@@@@@@@@@@@@@@.%@.:....................
................%@....=@@@@@@@@@@@@@@@@@@@@@@@@@@@..@..@-#%...............
...............*@.-..@=.@@@.@@@@@@@@@@@..@@@@@:=#::=.@@.@@@@..............
..............@@:@#.@@@@@@..@@:#@@:.@@@..@@@@@@@@@@#@@@@+@@@-.............
.............:@@@@.@@@@@@%@@@@@@@@@@@@@.@@@@@@.@@@@@@@@@@-@@-. ...........
..............@@-.@@@@@@@@@@@@@@@@@@@@@%@@@@@@..@@@@@@@@@@@@@+............
............#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@..-@@@@@@@@@@@@@............
............=@@@@@@@@@@@@@@@@@@@+:@@@@@@@@@@@....@@@@@@@@@@@@@@...........
............@@@@@@@@@@@@@@@@@@@=.@@@@@@@@@:@@@@+..@@@@@@@@@@@@@...........
...........-@@@@@@@@@@@@@@%@@=...@@@@@@@@@%@.......@@@@@@@@@@@@...........
...........@@@@@@@@@@@@@%-@@.....@@:@@@@@.@........:@@@@@@@@@@@...........
...........@@@@@@@@@@@@.%%.%+=...@+@@@.@.@...+%%....@@@@@@@@@@@#..........
...........@@@@@@@@@@=..@@@@@@@..=@@@.@.@...@@@@@@@:.@@@@@@@@@@#..........
..........@@@@@@@@@@@.@@=@@@@*@@...........@@@@@=@*@@@@@@@@@@@@@%.........
..........%@@@@@@@@@@*@=.@@@@@@.............@@@@@@.=@@@@@@@@@@@@..........
.........*.@@@@@@@@@@..#.=-*+=*.............+=**=#.+.@@@@@@@@@@@.@........
.........@.@@@@@@@@@@.....-@@@...............@@@=....@@@@@@@@@@@%.........
.........-.@@@@@@@@@@................................@@@@@@@@@@@@.#.......
........@.+@@@@@@@@@@@..:......................:.-:..@@@@@@@@@@@%@*.......
........@.@@@@@@@@@@@...............................:@@@@@@@@@@@@@........
........@.#@@@@@@@@@@@@.........=@@+===+@@@.........@@@@@@@@@@@@@.*+......
........:+.#@@@@@@@@@%@@.........=========. ......-@@@@@@@@@@@@@@.@+......
.......#.@.*@@@@@@@@@@@@@@........:=====#........@@@@@@@@@@@@@@@@.@@......
.......%.@.*@@@@@@@@@@@@@@@@*.................%@@@@@@@@@@@@@@@@@@.@@......
.......-...@@@@@@@@@@@@@@@@@@@@*...........#@@@@@@@@@@@@@@@@@@@@@.@@......
........@..@#@@@@@@@@@@@@@@@@@@%@@@.....@@@@=@@@@@@@@@@@@@@@@@@@@:@@......
........@..@.@@@@@@@@@@@@@@@@@@===@@@@@@@@==#@@@@@@@@@@@@@@@@@@@@@.%......
........@:.@+@@@@@@@@@@@@@@@@@@===-:+@@--=-=%@*@@@@@@@@@@@@@@@@.@@........
........::.@@@@@@@@@@@@@@@#+@@@....+=-:++=++=@@#%@@@@@@@@@@@@@:.@.-.......
............@@+@@@@@@@@%##+**-=.............+=@++**@@@@@@@@@@%@@%.........
.............@%@@@@@@@@@@+#*#*................#%##@@@@@@@@@@@#@%..........
.......@..#*#*%#@@@@@@@@###%##...............@=*+*#@@@@@@@@@**##+..@......
.....*@%#**=..+*+@@@@@@@@+*##%@..*.......*=..+%#*#@@@@@@@@+*=*..:+#*@@@...
....@...:=@+=*..+#*@@@@@@@+-=*+.............%%+*+@@@@@@@*#*@..*##@=...-#..
..@........-*@#=+..@+@%@@@@@@+@*..@:....%-.@#-+@@@@@@@+*#..@%%#@.....+....
    '''
    print(art)



def get_timestamp():
    return datetime.now().strftime("%m%d%y%H%M%S")

def create_logs_folder():
    os.makedirs("logs", exist_ok=True)

def select_hash_input_mode():
    print("\n[1] Paste comma-separated NT hashes")
    print("[2] Load NT hashes from file")
    choice = input("Select input mode [1/2]: ").strip()
    return choice

def get_hashes_from_paste():
    pasted_hashes = input("Paste NT hashes (comma-separated): ").strip()
    hash_lines = [h.strip() for h in pasted_hashes.split(",") if h.strip()]
    return hash_lines

def get_hashes_from_file():
    path = input("Enter path to NT hash file: ").strip()
    if not os.path.isfile(path):
        print("[!] Invalid file path.")
        return []
    with open(path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def save_hashes_to_temp_file(hash_lines):
    temp_file = tempfile.NamedTemporaryFile(mode='w+', delete=False)
    for line in hash_lines:
        temp_file.write(line + '\n')
    temp_file_path = temp_file.name
    temp_file.close()
    return temp_file_path

def choose_wordlist():
    system_os = platform.system().lower()
    wordlists = []
    if system_os == 'linux' and os.path.isdir('/usr/share/wordlists'):
        for fname in os.listdir('/usr/share/wordlists'):
            full_path = os.path.join('/usr/share/wordlists', fname)
            if os.path.isfile(full_path):
                wordlists.append(full_path)
    if wordlists:
        print("\nAvailable wordlists:")
        for i, wl in enumerate(wordlists):
            print(f"[{i+1}] {wl}")
        print(f"[{len(wordlists)+1}] Enter custom path")
        choice = input("Select wordlist: ").strip()
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(wordlists):
                return wordlists[choice - 1]
    return input("Enter path or filename of your wordlist: ").strip()

def get_custom_log_name(default_name):
    name = input("Enter custom log filename (or press Enter for default): ").strip()
    if name:
        if not name.lower().endswith(".log"):
            name += ".log"
        return os.path.join("logs", name)
    return os.path.join("logs", f"janes_2cents_{default_name}.log")

def run_john(hash_file, wordlist_path):
    print("\n[+] Launching John the Ripper...")
    try:
        process = subprocess.Popen([
            "john",
            "--format=NT",
            f"--wordlist={wordlist_path}",
            hash_file
        ])
        # Monitor loop (basic status updates)
        while process.poll() is None:
            print("[*] Cracking in progress... waiting 10 seconds")
            time.sleep(10)
        print("[+] John has finished cracking.\n")
    except Exception as e:
        print("[!] Error running John:", e)

def get_cracked_results(hash_file):
    try:
        result = subprocess.run(
            ["john", "--show", "--format=NT", hash_file],
            stdout=subprocess.PIPE, text=True
        )
        cracked_lines = []
        for line in result.stdout.strip().split('\n'):
            if ':' in line and not line.startswith(("Warning", "Note")):
                parts = line.split(':')
                if len(parts) >= 2:
                    cracked_lines.append(f"{parts[0]} : {parts[1]}")
        return cracked_lines
    except Exception as e:
        print("[!] Failed to get cracked results:", e)
        return []

def main():
    print_ascii_girl()
    print("\n=== Janes Window — NT Hash Decipher Engine ===")

    create_logs_folder()
    timestamp = get_timestamp()

    input_mode = select_hash_input_mode()
    if input_mode == '1':
        hash_lines = get_hashes_from_paste()
    elif input_mode == '2':
        hash_lines = get_hashes_from_file()
    else:
        print("[!] Invalid input mode selected.")
        return

    if not hash_lines:
        print("[!] No hashes provided.")
        return

    hash_file = save_hashes_to_temp_file(hash_lines)
    wordlist = choose_wordlist()
    if not os.path.isfile(wordlist):
        print("[!] Wordlist file not found.")
        return

    log_file = get_custom_log_name(timestamp)

    run_john(hash_file, wordlist)
    cracked = get_cracked_results(hash_file)

    if cracked:
        with open(log_file, 'w') as f:
            for line in cracked:
                f.write(line + '\n')
        print(f"[✓] Cracked hashes saved to: {log_file}")
    else:
        print("[!] No passwords cracked.")

    # Clean up
    os.remove(hash_file)

if __name__ == "__main__":
    main()
