import yaml

def main():
    secrets_dict = {"login_details": {}}
    secrets_dict["login_details"]["url"] = input("Enter TCP portal URL: ")
    secrets_dict["login_details"]["badge_number"] = input("Enter TCP badge number: ")
    secrets_dict["login_details"]["pin"] = input("Enter TCP pin: ")
    with open("secrets.yaml", 'w') as file:
        yaml.dump(secrets_dict, file)

if __name__ == "__main__":
    main()

