import os
import sys

def update_contributors(actor, event_name, pr_url, contributor_login, pr_title, pr_body):
    contributors_dir = "contributions/"
    os.makedirs(contributors_dir, exist_ok=True)

    # Create or update a file with contributor information
    contributor_file_path = f"{contributors_dir}{contributor_login}.md"
    with open(contributor_file_path, "a") as file:
        file.write(f"# {contributor_login}\n")
        file.write(f"- Actor: {actor}\n")
        file.write(f"- Event: {event_name}\n")
        file.write(f"- PR URL: {pr_url}\n")
        file.write(f"- PR Title: {pr_title}\n")
        file.write(f"- PR Body: {pr_body}\n")

if __name__ == "__main__":
    actor = sys.argv[1]
    event_name = sys.argv[2]
    pr_url = sys.argv[3]
    contributor_login = sys.argv[4]
    pr_title = sys.argv[5]
    pr_body = sys.argv[6]

    update_contributors(actor, event_name, pr_url, contributor_login, pr_title, pr_body)
