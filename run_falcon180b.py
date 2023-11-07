import truss
from pathlib import Path
import requests

tr = truss.load("./falcon_180b")
output = tr.predict({"prompt": "Hi there how are you?"})
print(output)
