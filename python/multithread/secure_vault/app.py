import os
from cryptography.fernet import Fernet
from datetime import datetime

# --- Configuration ---
VAULT_DIR = "/home/ec2-user/vault_files"
AUDIT_LOG = "/home/ec2-user/audit_logs.txt"

# Generate a Fernet key from a password (simple demo for hackathon)
def generate_key(password):
    # In real-world, use a proper key derivation function
    key = Fernet.generate_key()
    return Fernet(key)

# Logging function
def log_action(file_name, action, status):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(AUDIT_LOG, "a") as f:
        f.write(f"{timestamp} | {file_name} | {action} | {status}\n")

# Encrypt file
def encrypt_file(file_path, fernet):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        with open(file_path, "wb") as f:
            f.write(fernet.encrypt(data))
        log_action(file_path, "ENCRYPT", "SUCCESS")
        print(f"[ENCRYPTED] {file_path}")
    except Exception as e:
        log_action(file_path, "ENCRYPT", f"FAILED - {str(e)}")
        print(f"[FAILED] {file_path}")

# Decrypt file
def decrypt_file(file_path, fernet):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        with open(file_path, "wb") as f:
            f.write(fernet.decrypt(data))
        log_action(file_path, "DECRYPT", "SUCCESS")
        print(f"[DECRYPTED] {file_path}")
    except Exception as e:
        log_action(file_path, "DECRYPT", f"FAILED - {str(e)}")
        print(f"[FAILED] {file_path}")

# Main interface
def main():
    print("\n--- Secure File Vault ---")
    master_password = input("Enter master password: ").strip()
    fernet = generate_key(master_password)

    while True:
        print("\nOptions:")
        print("1. Encrypt all files")
        print("2. Decrypt all files")
        print("3. Encrypt single file")
        print("4. Decrypt single file")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            files = [os.path.join(VAULT_DIR, f) for f in os.listdir(VAULT_DIR)
                     if os.path.isfile(os.path.join(VAULT_DIR, f))]
            for file in files:
                encrypt_file(file, fernet)

        elif choice == "2":
            files = [os.path.join(VAULT_DIR, f) for f in os.listdir(VAULT_DIR)
                     if os.path.isfile(os.path.join(VAULT_DIR, f))]
            for file in files:
                decrypt_file(file, fernet)

        elif choice == "3":
            file_name = input("Enter file name to encrypt: ").strip()
            file_path = os.path.join(VAULT_DIR, file_name)
            if os.path.exists(file_path):
                encrypt_file(file_path, fernet)
            else:
                print("[ERROR] File not found.")

        elif choice == "4":
            file_name = input("Enter file name to decrypt: ").strip()
            file_path = os.path.join(VAULT_DIR, file_name)
            if os.path.exists(file_path):
                decrypt_file(file_path, fernet)
            else:
                print("[ERROR] File not found.")

        elif choice == "5":
            print("Exiting Vault...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
