import os
from concurrent.futures import ThreadPoolExecutor

# Sensitive keywords to search
KEYWORDS = ["password", "secret", "token", "apikey"]

# File extensions to scan (optional optimization)
VALID_EXT = (".txt", ".log", ".conf", ".ini", ".py", ".json", ".xml")


def search_file(file_path):
    results = []
    try:
        with open(file_path, "r", errors="ignore") as f:
            for lineno, line in enumerate(f, 1):
                for keyword in KEYWORDS:
                    if keyword.lower() in line.lower():
                        snippet = line.strip()
                        results.append(
                            f"{file_path} | Line {lineno} | {snippet}"
                        )
    except:
        pass
    return results


def get_all_files(root_dir):
    file_list = []
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(VALID_EXT):
                file_list.append(os.path.join(root, file))
    return file_list


def main():
    # Option 1: interactive input
    # directory = input("Enter directory to scan: ")

    # Option 2: hardcoded folder path (replace with your folder)
    directory = r"C:\codepoduh"

    files = get_all_files(directory)
    print(f"Scanning {len(files)} files...\n")

    with ThreadPoolExecutor(max_workers=8) as executor:
        results = executor.map(search_file, files)

    # Print matches
    for file_result in results:
        for match in file_result:
            print(match)


if __name__ == "__main__":
    main()
