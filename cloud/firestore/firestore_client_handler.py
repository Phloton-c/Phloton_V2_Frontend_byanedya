from google.cloud import firestore
import os
import json
import streamlit as st

FIREBASE_PRIVATE_KEY = os.getenv("FIREBASE_PRIVATE_KEY")


# Authenticate to Firestore with the JSON account key.
def firebase_db_setup():
    FIREBASE_PRIVATE_KEY_JSON = json.loads(FIREBASE_PRIVATE_KEY)
    curt_dir = os.getcwd()
    FIREBASE_PRIVATE_KEY_PATH = f"{curt_dir}/cloud/firestore/FIREBASE_PRIVATE_KEY.json"
    with open(FIREBASE_PRIVATE_KEY_PATH, "w") as outfile:
        json.dump(FIREBASE_PRIVATE_KEY_JSON, outfile)

    st.session_state.firestore_client = firestore.Client.from_service_account_json(
        FIREBASE_PRIVATE_KEY_PATH
    )


# Create a reference to the Google post.
# doc_ref = db.collection("roles").document("mnaveen1888@gmail.com").set({"role": "admin", "password": "password"})
