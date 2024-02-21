import sys
from github import Github


def check_test_command(token, pr_number, repo_name):
    # Initialize PyGithub with a GitHub access token
    g = Github(token)

    # Use the passed repository name
    repo = g.get_repo(repo_name)
    pr = repo.get_pull(int(pr_number))

    # Loop through the comments to find one starting with "/test"
    found_command = False
    for comment in pr.get_issue_comments():
        if comment.body.startswith("/test"):
            found_command = True
            print("Found /test command in comments.")
            break

    if not found_command:
        raise ValueError("Error: No /test command found in PR comments.")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: python check_test_command.py <GITHUB_TOKEN> <PR_NUMBER> <REPO_NAME>"
        )
        sys.exit(1)

    print(sys.argv)
    github_token = sys.argv[1]
    pr_number = sys.argv[2]
    repo_name = sys.argv[3]

    check_test_command(github_token, pr_number, repo_name)
