# Phloton V2 Frontend by Anedya


## Project Setup Instructions

Follow the steps below to set up and run the project on your local machine:

### 1. Create a Virtual Environment

Creating a virtual environment.


### 2. Install Dependencies

Ensure that all necessary libraries and dependencies are installed by using the provided `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 3. Run the Application

Use the following command to start the application on your local host:

```bash
streamlit run Home.py
```

Once the server starts, a local URL (e.g., `http://localhost:8501`) will be displayed. Open this URL in your browser to access the application.

---

### Hosting on Streamlit Cloud

1. Sign Up / Log In to Streamlit Cloud:
Go to [Streamlit Cloud](https://streamlit.io/cloud) and sign in with your GitHub account.
2. Create a New App:
- Click on "New app".
- Select `Deploy a public app from github`.
- Select your repository.
- Set the branch to main.
- Set the main file path to Home.py.
- Click on `Advance settings` and add your secrets (same secrets.toml file data).
3. Deploy:
Click "Deploy" to launch your app on Streamlit Cloud.