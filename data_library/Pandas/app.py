
import pandas as pd

data = {
    "Name": ["Jai", "Princi", "Gaurav", "Anuj"],
    "Age": [27, 24, 22, 32],
    "City": ["Delhi", "Kanpur", "Allahabad", "Kannauj"],
}

df = pd.DataFrame(data)
print(data)

# df.to_excel("output.xlsx", index=False)
df.to_excel("output.json", index=False, engine="json")