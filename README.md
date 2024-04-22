Instructions below on how to run

Status:
- frontend completed (react)
- backend completed (python)
- database completed (sqlite3)
- no syncronization

---
Deps:

- `python 3`
- `npm 9.3.1`
- `node 18.14.0`

Install the python packages:

`pip3 install -r requirements.txt`

---
Terminal 1 (backend):

`/usr/bin/python3 -m flask run`

Terminal 2 (frontend):

```
cd frontend/src
npm i
npm start
```

----
Backend runs on `localhost:5000`

Frontend runs on `localhost:3000`

----

Backend can also be tested separately using postman/curl

- `GET /api/v1/addresses` --> get list of all addresses
- `POST /api/v1/addresses/<address>` --> add a new address
- `DELETE /api/v1/addresses/<address>` --> delete an address



- `GET /api/v1/transactions/<address_id>?page=1` --> get list of transactions for address_id on page 1
- `GET /api/v1/transactions/<address_id>/balance` --> get balance for address_id


**Note, blockchain API may rate limit**