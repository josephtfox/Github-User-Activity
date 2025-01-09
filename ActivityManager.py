import cmd
import json
import os
import requests

class ActivityManager:

    def parse_data(self):
        pass

    def fetch_recent(self, username):
        url = f"https://api.github.com/users/{username}/events"
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            events = response.json()
            for event in events[:5]:
                event_type = event['type']
                repo_name = event['repo']['name']
                created_at = event['created_at']
                
                print(f"Event: {event_type}")
                print(f"Repository: {repo_name}")
                print(f"Time: {created_at}")
                print("---")
            # with open("data.json", "w") as file:
            #     json.dump(events, file, indent=4)
        else:
            print(f"Failed to retrieve data: {response.status_code}")
        

class GitShell(cmd.Cmd):
    intro = "Welcome to the Github Activity "
    prompt = '(GithubActivity) '

    def __init__(self):
        super().__init__()
        self.activity_manager = ActivityManager()

    def do_exit(self, arg):
        """
        Exit from the Interface
        """
        print("Goodbye!")
        return True
    
    def default(self, arg):
        """
        Parse and print the recent activity from a github account. Usage: <account name>
        """
        self.activity_manager.fetch_recent(arg)

if __name__ == "__main__":
    GitShell().cmdloop()