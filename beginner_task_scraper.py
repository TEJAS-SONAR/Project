from bs4 import BeautifulSoup
import pandas as pd


file_path = "Amazon.html"

with open(file_path, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")


products = []

for item in soup.find_all("div", class_="puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-vuc0rjtls2b1d2srya5k882dsm s-latency-cf-section puis-card-border", attrs={"data-cy": "asin-faceout-container"}):
    try:
        name = item.find("div", class_="a-section a-spacing-none puis-padding-right-small s-title-instructions-style", attrs={"data-cy": "title-recipe"})
        Names = name.text.strip() if name else ""
    except:
        Names = ""
    
    try:
        price = item.find("span", class_="a-price-whole")
        Price = price.text.strip() if price else ""
    except:
        Price = ""
    
    try:
        Buyers = item.find("span", class_="a-size-base s-underline-text")
        Buyers = Buyers.text.strip() if Buyers else ""
    except:
        Buyers = ""
    
    products.append([Names, Price, Buyers])


df = pd.DataFrame(products, columns=["Name", "Price", "Buyers"])
df.to_csv("products.csv", index=False)
