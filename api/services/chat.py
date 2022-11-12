import requests
from langdetect import detect

from .util import is_success_response, map_replace


class ChatService:
    def __init__(self, host, input_text, bot):
        self.host = host
        self.input_text = input_text
        self.repl_map = {
            "olivib": bot,
        }

    def talk(self):
        language = detect(self.input_text)

        message = "I'm very tired, talk to you later!"
        if language != "vi":
            language = "en"
        if language == "vi":
            language = "vn"
            message = "Tớ mệt quá rồi, mình nói chiện sau nhóe!"

        try:
            resp = requests.get(f"{self.host}?text={self.input_text}&lc={language}&cf=true&ft=0")
            if is_success_response(resp):
                json_resp = resp.json()
                resp_mess = json_resp.get("messages", [{"response": json_resp.get("message", message)}])
                for m in resp_mess:
                    if m:
                        return map_replace(m.get("response", m), self.repl_map)
        except Exception as e:
            print(e)

        return message
