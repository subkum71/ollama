## Simple connect to our local model qwen3-vl:4b through end point , make sure server is running

import requests
import json

url= "http://localhost:11434/api/generate"
data={
    "model":"qwen3-vl:4b",
    "prompt":"Tell me about model in 1-2 sentence"
}

response = requests.post(url,json=data,stream=False)
print(response)
if response.status_code==200 :
     for line in response.iter_lines():
        if line:
            decode_line = line.decode("utf-8")
            result = json.loads(decode_line)

            gentext = result.get("response", "")
            print(gentext, end="", flush=True)
else:
    print("Error while getting response from server" , response.status_code)