import truss
from pathlib import Path
import requests

tr = truss.load("./aguila_7b")
output = tr.predict({"prompt": "Hola, que tal estas?"})
print(output)
