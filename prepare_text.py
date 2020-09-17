import re

REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english'))

def text_prepare(text):
    """
        text: a string
        
        return: modified initial string
    """
    text = text.lower()
    text = re.sub(pattern=REPLACE_BY_SPACE_RE, repl=' ', string=text)
    text = re.sub(pattern=BAD_SYMBOLS_RE, repl='', string=text)
    tokenizer = nltk.tokenize.WhitespaceTokenizer()
    toks = tokenizer.tokenize(text)
    for stopword in STOPWORDS:
      toks = [ tok for tok in toks if tok != stopword]
      text = " ".join(toks)
    return text