import re, random
from collections import Counter, defaultdict

def _tokens(text: str):
    return re.findall(r"\b\w+\b", text.lower())

class BigramModel:
    def __init__(self, corpus: list[str]):
        tokens = []
        for s in corpus:
            tokens += _tokens(s)
        uni = Counter(tokens)
        bi = Counter(zip(tokens[:-1], tokens[1:]))
        self.probs = defaultdict(dict)
        for (w1, w2), c in bi.items():
            self.probs[w1][w2] = c / uni[w1]

    def generate_text(self, start_word: str, length: int):
        w = start_word.lower()
        out = [w]
        for _ in range(max(0, length - 1)):
            nxt = self.probs.get(w)
            if not nxt: break
            w = random.choices(list(nxt.keys()), weights=nxt.values())[0]
            out.append(w)
        return " ".join(out)
