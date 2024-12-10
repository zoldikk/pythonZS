import json

def load_ids(filename):
    """تحميل قائمة الـ UIDs من ملف JSON"""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_id(filename, ids):
    """حفظ قائمة الـ UIDs في ملف JSON"""
    with open(filename, 'w') as file:
        json.dump(ids, file)

def main(uid):
    """إضافة UID جديد أو إرجاع رسالة إذا كان موجودًا مسبقًا"""
    filename = 'ids.json'
    ids = load_ids(filename)

    if uid in ids:
        return "🚫 already added this uid"
    else:
        ids.append(uid)
        save_id(filename, ids)
        return f"✅ Successfully added this uid"
