import sys
from github import Github


def find_pr_by_sha(repo, commit_sha):
    open_prs = repo.get_pulls(state="open")
    for pr in open_prs:
        if pr.head.sha == commit_sha:
            return pr
    return None


def check_test_command(github_token, repo_name, commit_sha):
    # Initialize PyGithub with the GitHub token
    g = Github(github_token)

    repo = g.get_repo(repo_name)
    pr = find_pr_by_sha(repo, commit_sha)

    if not pr:
        print("No open PR found for this commit SHA.")
        return

    # Loop through the comments to find one starting with "/test"
    found_command = False
    for comment in pr.get_issue_comments():
        if comment.body.startswith("/test"):
            found_command = True
            print(f"Found /test command in PR #{pr.number} comments.")
            break

    if not found_command:
        raise ValueError("Error: No /test command found in PR comments.")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: python check_test_command.py <GITHUB_TOKEN> <REPO_NAME> <COMMIT_SHA>"
        )
        sys.exit(1)

    github_token, repo_name, commit_sha = sys.argv[1], sys.argv[2], sys.argv[3]
    check_test_command(github_token, repo_name, commit_sha)
