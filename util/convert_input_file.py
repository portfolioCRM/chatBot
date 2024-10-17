import json
import csv
from typing import List, Dict

def import_faqs_from_json(file_path: str) -> List[Dict[str, str]]:
    """Import FAQs from a JSON file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def import_faqs_from_csv(file_path: str) -> List[Dict[str, str]]:
    """Import FAQs from a CSV file."""
    faqs = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            faqs.append(row)
    return faqs
