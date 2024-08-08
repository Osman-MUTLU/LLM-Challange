# Getting Started

Dosya içerisine .env oluşturup "OPENAI_API_KEY" girmelisiniz.

## Setup

Python env oluştur.
```bash
python -m venv env
```

Environment aktif et.

```bash
./env/Script/activate
```
Gerekli kütüphaneleri yükle.

```bash
pip install -r requirements.txt
```
Çalıştır: main.py

```bash
python main.py
```
En son arayüz kullanımı için: 
[Go to swagger ui ](http://localhost:8000/docs/)

## Example Output

```json
{
  "turkish_menu": {
    "after_takeoff_meals": [
      "TÜRK MEZE ÇEŞİTLERİ",
      "ROSTBİF & ERİŞTE SALATASI",
      "DOMATES ÇORBASI",
      "HONG KONG USULÜ DENİZ MAHSULLERİ",
      "IZGARA DANA BONFİLE",
      "MANTARLI FETÜCCİNİ MAKARNA"
    ],
    "desserts": [
      "GELENEKSEL TÜRK TATLILARI",
      "KREM KARAMEL",
      "VİŞNELİ CRUMBLE TART",
      "ÇİKOLATALI DONDURMA",
      "PEYNİR ÇEŞİTLERİ",
      "TAZE MEYVE SALATASI"
    ],
    "before_landing_meals": [
      "Taze portakal suyu",
      "Taze havuç suyu",
      "Mango, çilek, hindistancevizi ve muzlu smoothie",
      "TAZE MEYVE SALATASI",
      "BÖĞÜRTLEN SOSLU YOĞURT",
      "TAVUK GÖĞÜS & FÜME HİNDİ",
      "PEYNİR ÇEŞİTLERİ",
      "BAL",
      "TEREYAĞI",
      "OMLET",
      "Sote patates",
      "ızgara domates",
      "ELMALI KREP",
      "Ahududu sos",
      "IZGARA AHTAPOT",
      "SEBZELİ SOYA FASULYESİ",
      "DENİZ MAHSULLERİ",
      "SEBZELİ ERİŞTE",
      "Taze sıcak ekmek çeşitleri",
      "Kruvasan",
      "danish"
    ]
  },
  "english_menu": {
    "after_takeoff_meals": [
      "BEST OF TURKISH MEZZE",
      "ROAST BEEF & VERMICELLI NOODLE SALAD",
      "CREAMY TOMATO SOUP",
      "HONG KONG STYLE SEAFOOD noodle",
      "GRILLED FILLET OF BEEF",
      "FETTUCCINI WITH MUSHROOMS"
    ],
    "desserts": [
      "POTPOURRI OF TRADITIONAL TURKISH DESSERTS",
      "CRÈME CARAMEL",
      "CHERRY CRUMBLE TART",
      "CHOCOLATE ICE CREAM",
      "SELECTION OF CHEESE",
      "FRESH FRUIT SALAD"
    ],
    "before_landing_meals": [
      "freshly squeezed orange juice",
      "freshly squeezed carrot juice",
      "mango, strawberry, coconut and banana smoothie",
      "FRESH FRUIT SALAD",
      "YOGHURT WITH BLUEBERRY COMPOTE",
      "CHICKEN BREAST & SMOKED TURKEY",
      "SELECTION OF CHEESE",
      "HONEY",
      "BUTTER",
      "OMELETTE",
      "CREPE WITH APPLE",
      "FRIED ABALONE",
      "PRESERVED VEGETABLES WITH BEAN CURD",
      "HONEY SESAME BEEF",
      "SEAFOOD, EGG NOODLE WITH VEGETABLE",
      "ovenfresh bread selection",
      "croissant",
      "danish"
    ]
  }
}


```