import re

class MyLangTokenizer:
    def __init__(self):
        self.patterns = {
            "url": r"https?://[^\s]+", 
            "email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",  
            "number": r"\d{1,3}(?:,\d{2,3})*(?:\.\d+)?|\d+/\d+",  
            "date": r"\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}",  
            "handle": r"[@#][\w]+", 
            "punctuation": r"[!?.,:;\"'()\[\]{}]",  
            "word": r"\w+",  
        }

    def tokenize(self, text):
        pattern = "|".join(f"(?P<{key}>{val})" for key, val in self.patterns.items())
        tokens = []
        for match in re.finditer(pattern, text):
            for key, value in match.groupdict().items():
                if value:
                    tokens.append((key, value))
        return tokens

text = "Visit https://example.com on 12/05/2024! Email me at test@example.com or call 3,22,243. Follow @user_handle."
tokenizer = MyLangTokenizer()
tokens = tokenizer.tokenize(text)
for token in tokens:
    print(token)
