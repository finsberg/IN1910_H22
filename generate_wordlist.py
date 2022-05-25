# flake8: noqa
import mdformat  # pip install mdformat-myst
import pandas  # pip install pandas

template = """
# Dictionary

Here you will find norwegian (bokmål) and english translations of common words used in this course

```{note}
If you find a word that you want to add to the dictionary please send an email to [henriknf@simula.no](mailto:henriknf@simula.no?subject=Ordliste-IN1910)
```
"""

template_eng_to_nor = """
## English-Norwegian

| **English**            | **Norwegian**           |
| ---------------------- | ----------------------- |
{}
"""

template_nor_to_eng = """
## Norwegian-English

| **Norwegian**           | **English**            |
| ---------------------- | ----------------------- |
{}
"""

df = pandas.read_csv("wordlist.csv", header=0, dtype=str)


eng_to_nor = ""
for _, row in df.sort_values("Engelsk").iterrows():
    eng_to_nor += f"| {row.Engelsk} | {row.Bokmål} |\n"

nor_to_eng = ""
for _, row in df.sort_values("Bokmål").iterrows():
    nor_to_eng += f"| {row.Bokmål} | {row.Engelsk} |\n"

text = (
    template
    + template_eng_to_nor.format(eng_to_nor)
    + template_nor_to_eng.format(nor_to_eng)
)

with open("book/docs/info/dictionary.md", "w") as f:
    f.write(text)

# Make sure tables are formatted correctly
mdformat.file("book/docs/info/dictionary.md", extensions=["myst"])
