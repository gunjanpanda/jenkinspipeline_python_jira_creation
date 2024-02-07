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

    response = requests.post(url,headers=headers,data=payload,auth=("gunjanpnd8@gmail.com","ATATT3xFfGF0GVICEM2G3Gs5xtFNfi41WsJAm4GKPlQI_fGYMVXwNk2QuPS-k-YmNP8x0LsRHK6zQXyio9DIo1Mdx9IOBDzB6TRtjYf-n1HRXC-hUIiFR6yRRKMP1JzS_-z51ppDwLGB0zEqOdDaDeggQJ0NF3WzCeoENE5ghzyPDbwiJm0iRmM=5F9D0D6A"))
    print(response.text)