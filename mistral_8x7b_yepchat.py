import requests
import json

class Mistral_Inference:
    def __init__(self, max_tokens=2048, temperature=0.7, message=""):
        self.url = "https://api.yep.com/v1/chat/completions"
        self.headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/json; charset=utf-8",
            "Origin": "https://yep.com",
            "Referer": "https://yep.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT   10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0.0.0 Safari/537.36"
        }
        self.payload = {
            "stream": True,
            "max_tokens": max_tokens,
            "top_p": temperature,
            "temperature": 0.6,
            "messages": [{"content": message, "role": "user"}],
            "model": "Mixtral-8x7B-Instruct-v0.1"
        }

    def send_request(self):
        return  requests.post(self.url, headers=self.headers, data=json.dumps(self.payload), stream=False)

    def process_response(self, response):
        processed_text = ""
        for line in response.iter_lines():
            if line:
                try:
                    line_dict = json.loads(line.decode('utf-8')[6:])
                    if "choices" in line_dict and line_dict["choices"][0].get("delta", {}).get("content"):
                        processed_text += line_dict["choices"][0]["delta"]["content"]
                except:
                    continue
        return processed_text

    def chat(self, message):
        self.payload["messages"][0]["content"] = message
        response = self.send_request()
        processed_response = self.process_response(response)
        # print(processed_response.strip())
        return processed_response.strip()
    

if __name__ =="__main__":
    query = "What is the capital of India"
    # Then, create an instance of the YepChat class
    mistral_chat_instance = Mistral_Inference(max_tokens=2048, temperature=0.7)

    # Next, call the chat method with your desired message
    mistral_chat_instance.chat("who developed you")
