import os
import requests
import streamlit as st
from streamlit_oauth import OAuth2Component

# OAuth2 설정
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
AUTHORIZATION_URL = os.getenv("AUTHORIZATION_URL")
TOKEN_URL = os.getenv("TOKEN_URL")
SCOPES = os.getenv("SCOPES")

# OAuth2Component 객체 생성

oauth2 = OAuth2Component(CLIENT_ID, CLIENT_SECRET, AUTHORIZATION_URL, TOKEN_URL)

def get_repositories(access_token):
	url = "https://api.github.com/user/repos"
	headers = {"Authorization": f"token {access_token}"}
	response = requests.get(url, headers=headers)
	return response.json()

def get_pull_requests(access_token, repo_name):
	url = f"https://api.github.com/repos/{repo_name}/pulls"
	headers = {"Authorization": f"token {access_token}"}
	response = requests.get(url, headers=headers)
	return response.json()

# Streamlit App
st.title("Pull Request Reviewer with OpenAI API")

# Step 1: GitHub OAuth Authentication
if "access_token" not in st.session_state:
	# OAuth Button
	result = oauth2.authorize_button("Authorize", REDIRECT_URI, SCOPES)
	if result and 'token' in result:
		# If authorization successful, save token in session state
		access_token = result["token"]["access_token"]
		if access_token:
			st.session_state["access_token"] = access_token
			st.success("GitHub authentication successful!")
		else:
			st.error("GitHub authentication failed. Please try again.")
else:
	st.success("GitHub authentication already completed.")

# Step 2: Select Repository
if "access_token" in st.session_state:
	access_token = st.session_state["access_token"]
	repositories = get_repositories(access_token)
	repo_names = [repo["full_name"] for repo in repositories]
	selected_repo = st.selectbox("Select a Repository", repo_names)

	# Step 3: Display Pull Requests
	if selected_repo:
		pull_requests = get_pull_requests(access_token, selected_repo)
		if pull_requests:
			for pr in pull_requests:
				st.write(f"**#{pr['number']} {pr['title']}**")
				st.write(pr["html_url"])
		else:
			st.write("No pull requests available for this repository.")