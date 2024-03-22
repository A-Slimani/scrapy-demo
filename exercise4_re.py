import re

html = """
<div>
    <span class="actionBar__text"> Showing 18 of 101 products. </span>
</div>
"""

pattern = r"\d+"

match = re.findall(pattern, html)

if match:
    print(f"Total Number of Proudcts: {match[1]}")
