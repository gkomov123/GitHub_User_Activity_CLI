import requests
import sys

base_url = "https://api.github.com/users/"

## TODO Event handler

# def handle_repo_event():
#     pass


# handlers = {
#     "PushEvent": handle_repo_event(),
# }

def get_user_info(name):
    url = f"https://api.github.com/users/{name}/events"
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        user_activity = response.json() # Fetch the activity of the user
        print(f'Latest activity for {name}:')
        for event in user_activity: # Print all the popular events
            if event['type'] == 'IssueCommentEvent':
                print(f"- commented on issue {event['payload']['issue']['number']}")
            elif event['type'] == 'PushEvent':
                print(f"- pushed to {event['repo']['name']}")
            elif event['type'] == "IssuesEvent":
                print(f"- opened an issue in {event['payload']['issue']['number']}")
            elif event['type'] == "WatchEvent":
                print(f"- starred {event['repo']['name']}")
            elif event['type'] == "PullRequestEvent":
                print(f"- created a pull request {event['payload']['pull_request']['number']}")
            elif event['type'] == "PullRequestReviewEvent":
                print(f"- reviewed a pull request {event['payload']['pull_request']['number']}")
            elif event['type'] == "PullRequestReviewCommentEvent":
                print(f"- commented on pull request {event['payload']['pull_request']['number']}")
            elif event['type'] == "CreateEvent":
                print(f"- created {event['payload']['ref_type']} {event['payload']['ref']}")
            else:
                print(f"- {event['type']}")
    else:
        print(f"Failed to retrieve user_activity for {name}: {response.status_code}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_user_info(sys.argv[1])
    else:
        print("Please provide a Github username")
