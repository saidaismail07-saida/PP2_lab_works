import re
import json

with open("raw.txt", encoding="utf-8") as f:
    text = f.read()

price_matches = re.findall(r'\b\d[\d\s]*,\d{2}\b', text)
prices = [float(p.replace(' ', '').replace(',', '.')) for p in price_matches]

products = re.findall(r'\d+\.\s*(.+?)\n\d+,\d{2}', text, flags=re.DOTALL)
total_calculated = sum(prices[:-3]) 
total_paid_match = re.search(r'Банковская карта:\s*([\d\s,]+)', text)
total_paid = float(total_paid_match.group(1).replace(' ', '').replace(',', '.')) if total_paid_match else None

datetime_match = re.search(r'Время:\s*(\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2})', text)
datetime_value = datetime_match.group(1) if datetime_match else ""

payment_method = "Банковская карта" if total_paid_match else "Не указано"

receipt_data = {
    "products": [{"name": name.strip()} for name in products],
    "prices": prices,
    "total_calculated": total_calculated,
    "total_paid": total_paid,
    "datetime": datetime_value,
    "payment_method": payment_method
}

print(json.dumps(receipt_data, ensure_ascii=False, indent=2))