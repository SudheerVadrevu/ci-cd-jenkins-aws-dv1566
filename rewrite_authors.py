from git_filter_repo import Commit

# Old names and emails to replace
BAD_EMAILS = {
    b"praveensirvi1212@gmail.com",
    b"choudharysirvi1212@gmail.com",
    b"54717706+praveensirvi1212@users.noreply.github.com"
}

BAD_NAMES = {
    b"Praveen Sirvi",
    b"Sirvi Praveen",
    b"praveensirvi1212"
}

# New name and email
TARGET_NAME = b"Sudheer Vadrevu"
TARGET_EMAIL = b"vadrevusudheer@gmail.com"

def commit_callback(commit: Commit):
    if commit.author_email in BAD_EMAILS or commit.author_name in BAD_NAMES:
        commit.author_name = TARGET_NAME
        commit.author_email = TARGET_EMAIL
    if commit.committer_email in BAD_EMAILS or commit.committer_name in BAD_NAMES:
        commit.committer_name = TARGET_NAME
        commit.committer_email = TARGET_EMAIL
