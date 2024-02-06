import requests
import json
import pandas as pd


url = "https://gunjandemo.atlassian.net/rest/api/2/issue"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

summary_text = "Create jenkins file and run python file via vscode"
description_text = "Creating jenkins file and call python file to run the code and create issue in Jira. Push both files in Github and trigger the Jenkins File from Jenkins."
payload = json.dumps(
    {
        "fields": {
            "project":
            {
                "key": "DEV"
            },
            "summary": summary_text,
            "description": description_text,
            
            "issuetype": {
                "name": "Task"
            }
        }

    }
)

response = requests.post(url,headers=headers,data=payload,auth=("gunjanpnd8@gmail.com","ATATT3xFfGF0GVICEM2G3Gs5xtFNfi41WsJAm4GKPlQI_fGYMVXwNk2QuPS-k-YmNP8x0LsRHK6zQXyio9DIo1Mdx9IOBDzB6TRtjYf-n1HRXC-hUIiFR6yRRKMP1JzS_-z51ppDwLGB0zEqOdDaDeggQJ0NF3WzCeoENE5ghzyPDbwiJm0iRmM=5F9D0D6A"))
print(response.text)