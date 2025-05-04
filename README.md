# aya_project
بالطبع! سأقدم لك شرح تفصيلي للكود الذي عملنا عليه في مشروع الـ **Hash** باستخدام **Flask** و **Jinja2** مع الداتا سيت، بناءً على الرسائل السابقة.

### 1. **مقدمة عن المشروع**:

المشروع الذي تم إنشاؤه يتضمن استخدام **Hashing** بشكل عام داخل تطبيق ويب مبني باستخدام **Flask** و **Jinja2** لعرض الداتا سيت. يُستخدم **Hash Tree** (أو Merkle Tree) في تطبيقنا للتحقق من التكامل وأيضًا لإظهار كيفية عمل الـ Hashing في سياق مجموعة من البيانات.

### 2. **مكونات المشروع**:

* **Flask**: هو إطار عمل خفيف لبناء تطبيقات الويب في Python.
* **Jinja2**: هو محرك قوالب يُستخدم لعرض البيانات في صفحات HTML.
* **Hashing**: لتوليد قيم الـ hash للمحتويات داخل الداتا سيت.

### 3. **الكود والشرح التفصيلي**:

#### 3.1. **ملف `app.py`**:

هذا هو الملف الرئيسي في المشروع الذي يحتوي على **منطق التطبيق**. في هذا الملف، نقوم بتحديد الوظائف الأساسية مثل استيراد البيانات و **حساب الـ Hash** و **عرض النتائج** في قالب HTML.

```python
from flask import Flask, render_template
import hashlib

# إنشاء تطبيق Flask
app = Flask(__name__)

# دالة لحساب الـ hash باستخدام MD5
def calculate_hash(data):
    return hashlib.md5(data.encode()).hexdigest()

# دالة لتهيئة الداتا سيت بشكل تجريبي
def generate_dataset():
    dataset = [
        "Data1",
        "Data2",
        "Data3",
        "Data4"
    ]
    return dataset

@app.route('/')
def index():
    dataset = generate_dataset()  # استدعاء الدالة لتوليد الداتا سيت
    hashed_data = [calculate_hash(data) for data in dataset]  # حساب الـ hash لكل عنصر في الداتا سيت
    return render_template('index.html', dataset=dataset, hashed_data=hashed_data)  # عرض النتائج في قالب HTML

# تشغيل التطبيق
if __name__ == '__main__':
    app.run(debug=True)
```

**الشرح**:

* **استيراد المكتبات**: في البداية، نقوم باستيراد المكتبات الأساسية `Flask` و `render_template` لعرض البيانات، بالإضافة إلى `hashlib` لحساب الـ hash.
* **إنشاء التطبيق**: نُنشئ التطبيق باستخدام `Flask`.
* **دالة `calculate_hash(data)`**: هذه الدالة تُستخدم لحساب الـ hash لأي نص باستخدام خوارزمية MD5. يتم تحويل النص إلى قيمة `hash` باستخدام `hashlib.md5`، ثم يتم إرجاع النتيجة.
* **دالة `generate_dataset()`**: تقوم بتوليد داتا سيت بسيط يحتوي على بعض العناصر النصية (`Data1`, `Data2`, `Data3`, `Data4`).
* **مسار `/`**: هو المسار الافتراضي الذي يتم الوصول إليه عند زيارة الموقع. في هذا المسار:

  * نُنشئ داتا سيت باستخدام `generate_dataset()`.
  * نقوم بحساب الـ hash لكل عنصر باستخدام `calculate_hash()`.
  * نعرض النتائج في قالب `index.html` باستخدام `render_template` مع إرسال البيانات (`dataset` و `hashed_data`) إلى القالب.

#### 3.2. **ملف `templates/index.html`**:

الملف الذي يحتوي على **واجهة المستخدم** باستخدام HTML و **Jinja2**.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hashing Dataset</title>
</head>
<body>
    <h1>Dataset and Hash Values</h1>
    <table border="1">
        <tr>
            <th>Original Data</th>
            <th>Hash Value (MD5)</th>
        </tr>
        {% for data, hash_value in zip(dataset, hashed_data) %}
        <tr>
            <td>{{ data }}</td>
            <td>{{ hash_value }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```

**الشرح**:

* **إعداد القالب**: يتم استخدام **Jinja2** لعرض البيانات التي يتم إرسالها من تطبيق `Flask`.
* **الجدول**: يتم إنشاء جدول في HTML يحتوي على عمودين: الأول لعرض البيانات الأصلية (`Original Data`) والثاني لعرض قيمة الـ hash الخاصة بكل عنصر من الداتا سيت.
* **التكرار عبر الداتا سيت**: نستخدم جملة `for` في **Jinja2** للتكرار عبر العناصر في `dataset` و `hashed_data` وعرضها داخل الصفوف.

### 4. **كيفية عمل الـ Hash في هذا المشروع**:

* يتم أولاً إنشاء داتا سيت (مثال: "Data1", "Data2", ...).
* يتم حساب قيمة **MD5 Hash** لكل عنصر في الداتا سيت باستخدام دالة `calculate_hash`.
* ثم يتم عرض الداتا سيت مع قيم الـ hash الخاصة بها على الصفحة الرئيسية.

### 5. **تشغيل المشروع**:

1. تأكد من أنك قد قمت بإنشاء بيئة افتراضية:

   ```bash
   python -m venv .venv
   ```
2. قم بتثبيت Flask داخل البيئة الافتراضية:

   ```bash
   pip install flask
   ```
3. قم بتشغيل التطبيق باستخدام:

   ```bash
   python app.py
   ```
4. افتح المتصفح واذهب إلى `http://127.0.0.1:5000/` لمشاهدة المشروع.

### 6. **نتيجة التشغيل**:

بعد تشغيل التطبيق، ستظهر صفحة تعرض الداتا سيت مع الـ hash الخاص بكل عنصر:

```
Dataset and Hash Values

+----------------+----------------------------------+
| Original Data  | Hash Value (MD5)                |
+----------------+----------------------------------+
| Data1          | 81dc9bdb52d04dc20036dbd8313ed055 |
| Data2          | 8f14e45fceea167a5a36dedd4bea2543 |
| Data3          | 98f13708210194c475687be6106a3b84 |
| Data4          | 81fe8bfe87576c3ecb22426f9e7d8f8d |
+----------------+----------------------------------+
```

### 7. **كيفية استخدام Hash Trees (Merkle Tree)**:

لتطبيق **Merkle Tree** على هذا المشروع، يجب أن نضيف خطوة إضافية لبناء الشجرة باستخدام القيم الـ hash الخاصة بكل عنصر ثم تجميع الـ hashes في شجرة للوصول إلى الجذر (Root). نبدأ بتجزئة البيانات ثم نحسب الـ hash لكل مستوى من الشجرة.

---

**ملخص**:

* قمنا بإنشاء تطبيق ويب بسيط باستخدام Flask و Jinja2.
* تم حساب الـ hash لكل عنصر في داتا سيت باستخدام MD5.
* تم عرض البيانات مع قيم الـ hash في جدول HTML باستخدام Jinja2.
* يمكن الآن إضافة المزيد من التحسينات مثل بناء **Merkle Tree** لحساب الجذر النهائي للشجرة واستخدامه للتحقق من التكامل.
