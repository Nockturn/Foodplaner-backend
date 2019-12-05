# Foodplaner-backend

## Install dependencies

All dependencies are defined in requirements.txt should be installed first:
```bash
pip install -r requirements.txt
``` 

---
## Update Database Schema

If a an update of the DB Schema is needed, do these changes to the Model.py file and execute the following commands:

```bash
python migrate.py db migrate

python migrate.py db upgrade
```
Everytime an schema change must be done, execute `migrate` and `upgrade` again.

---