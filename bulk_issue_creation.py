import requests
import json
import pandas as pd

df = pd.read_excel('bulk_issues.xlsx')
#url = input("Please enter the JIRA URL: \n")

url = "https://gunjandemo.atlassian.net/rest/api/3/issue"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}
for index,row in df.iterrows():
    summary_text = row['summary_text']
    description_text = row['description_text']
    payload = json.dumps(
        {
            "fields": {
                "project":
                {
                    "key": "DJ"
                },
                "summary": summary_text,
                "description": {
                    "type": "doc",
                    "version": 1,
                    "content": [
                        {   
                            "type": "paragraph",
                            "content":[
                                {
                            "type": "text",
                            "text": description_text
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

    response = requests.post(url,headers=headers,data=payload,auth=("gunjanpnd8@gmail.com","ATATT3xFfGF0aedBDLXfNzYSOcgfim97M_bvLCgfsrwoVHUDo4TTFQZUNVgAYDhNacQ4l0m10st28wo7r476V3MnykMM6jYOKDTDXSgUHrj88y3GzwhXnwNbU_OFzJxp2Ps5qc8j2a5X7x-peevgtYgFQQIOhFPq2pY6CqjP3_KeU-wowSSzmwY=53A8799B"))
    print(response.text)