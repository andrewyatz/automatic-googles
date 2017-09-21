# automatic-googles
The goggles. They do nothing!

# Runing

```bash
pip install -r requirements.txt
FLASK_APP=date.py flask run
```

# Querying

```bash
curl -s http://localhost:5000/date
```

# Output

```json
{
  "date": "Thu Sep 21 18:26:43 CEST 2017"
}
```
