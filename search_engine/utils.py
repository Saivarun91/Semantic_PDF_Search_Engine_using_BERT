import re

def highlight_keywords(text, query):
    keywords = query.lower().split()
    for kw in keywords:
        text = re.sub(f"(?i)({kw})", r"<mark>\1</mark>", text)
    return text
