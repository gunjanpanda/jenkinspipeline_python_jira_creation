import requests
import json
import pandas as pd


url = "https://gunjandemo.atlassian.net/rest/api/3/issue"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

payload = json.dumps(
    {
        "fields": {
            "project":
            {
                "key": "DEV"
            },
            "summary": "Create jenkins file and run python file by referring",
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {   
                        "type": "paragraph",
                        "content":[
                            {
                        "type": "text",
                        "text": "Creating jenkins file and call python file to run the code and create issue in Jira. Push both files in Github and trigger the Jenkins File from Jenkins."
                    }

                ]
            }
                ]
            },
            "issuetype": {
                "name": "Task"
            }
        }

    }
)

response = requests.post(url,headers=headers,data=payload,auth=("gunjanpnd8@gmail.com","ATATT3xFfGF06xFt7Ei2JRG7WjjUNxnJgtKeRBkUjgkS5Wm-TcnoPgrp5D471l58a4xzALIg1N414K1SOr8OFGLU-JF6c4z3c23lEhvjyi3cIqC1AjWHrdPj47qlzQtpEjXdhUQJJPsJv8hBt86FwfZUtDKHT-ekJUn7tOiBT5J-YfoQMmRwUXE=AC376B91"))
print(response.text)