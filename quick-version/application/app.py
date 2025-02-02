from flask import Flask, abort, request
from flask import jsonify
import os 
import sqlite3
import logging

log = logging.getLogger('werkzeug') # too many errors, disabling
log.disabled = True

app = Flask(__name__)

allowed_tokens = [
"8a060bc7-e168-4a6c-bdd6-0df4a5822266", # Crypto Mc Cryptface exchange customer
"93cfdb27-3300-44af-9632-080ba6a67dfd", # Bankly customer
"8a50d8f2-ee5a-472b-a2cc-c5b5d0184907", # Jim's personnal debug token
"8bd71e52-01ba-4e35-97f4-f7079872a219", # NFT trader 5000
"5779e738-c3fc-418c-ac9e-ae1aaa90414e", # Jon's backdoor token
]

@app.route('/api/fraud/<investigation_id>')
def investigation_results(investigation_id):
    if not request.headers.get('token') in allowed_tokens:
        abort(401, description="You need a token")
    

    conn = sqlite3.connect(os.environ.get("DB_CONNECTION_STRING","db.sqlite"))
    query = f"SELECT * from investigations where investigation_id='{investigation_id}'"
    cur = conn.execute(query)
    column_names = [d[0] for d in cur.description]
    data = []
    for row in cur.fetchall():
        data.append(dict(zip(column_names, row)))
    return jsonify(data)


def setupDB():
    conn = sqlite3.connect(os.environ.get("DB_CONNECTION_STRING","db.sqlite"))
    conn.execute("""create table if not exists investigations (
    investigation_id varchar not null primary key,
    investigation_status varchar,
    fraud_detected  varchar,
    payee_from_name varchar,
    payee_from_date_of_birth varchar,
    payee_from_address varchar,
    payee_to_name varchar,
    payee_to_date_of_birth varchar,
    payee_to_address varchar,
    transaction_id varchar);""")

    sql = ["""('927b70bc-da1d-4150-9dcf-7224e30cbd9e',
               'COMPLETED',
               'true',
               'Wheezy Joe Kingfish',
               '1993-10-11',
               '"Withington Hall Cottages, Holmes Chapel Road, Lower Withington",SK11 9DS',
               'Lil Debil Moonshine',
               '1828-06-05',
               '"15 Oakleigh Drive, Orton Longueville",PE2 7BG',
               '74c9a7e9-e30c-48f0-8d8f-ec8771849d46')""",
            """('6c1aa358-8d40-4714-a51d-05ab402233c1',
                'COMPLETED',
                'false',
                'Bad News Stevens',
                '1956-07-25',
                '3 Council House, Post Office Lane, Moreton",TF10 9DR',
                'Cinnabuns McFadden',
                '2111-04-29',
                '"18 Kingsley Road, Plymouth",PL4 6QP',
                '04f69367-a34e-48c5-9357-7c0c29b7eba0');
            """]
    cur = conn.cursor()
    for row in sql:
        cur.execute(f"""
                 INSERT into investigations(
                    investigation_id,
                    investigation_status,
                    fraud_detected,
                    payee_from_name,
                    payee_from_date_of_birth,
                    payee_from_address,
                    payee_to_name,
                    payee_to_date_of_birth,
                    payee_to_address,
                    transaction_id
                    ) values  {row}
                """)
        conn.commit()

if __name__ == '__main__':
    setupDB()
    app.run(host='0.0.0.0', port=9000)
