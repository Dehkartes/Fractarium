<template>
	<div>
		<h2>Auto Pull Request Reviewer</h2>
		<p>Analyze your text efficiently.</p>
		<div>
			<button @click="loginWithGitHub">Login with GitHub</button>
		</div>
	</div>
</template>

<script>
import axios from 'axios';

export default {
	name: "APRR",
	methods: {
		async loginWithGitHub() {
			const clientId = "YOUR_GITHUB_CLIENT_ID"; // Replace with your GitHub OAuth App Client ID
			const redirectUri = "http://localhost:3000/callback"; // Replace with your server's callback URL

			// Redirect user to GitHub login page
			const githubAuthUrl = `https://github.com/login/oauth/authorize?client_id=${clientId}&redirect_uri=${redirectUri}&scope=repo,user`;
			window.location.href = githubAuthUrl;
		},

		async handleAuthCallback(code) {
			try {
				// Exchange authorization code for access token
				const response = await axios.post('http://localhost:3000/api/github-token', { code });
				const token = response.data.access_token;
				
				// Send the token to the server for further processing
				await axios.post('http://localhost:3000/api/store-token', { token });
				alert('GitHub login successful and token sent to server!');
			} catch (error) {
				console.error('Error during GitHub login:', error);
				alert('Failed to log in with GitHub.');
			}
		}
	},
	mounted() {
		// Check for authorization code in the URL after redirect
		const urlParams = new URLSearchParams(window.location.search);
		const code = urlParams.get('code');
		if (code) {
			this.handleAuthCallback(code);
		}
	}
};
</script>

<style>
button {
	background-color: #2d89ef;
	color: white;
	padding: 10px 15px;
	border: none;
	border-radius: 5px;
	cursor: pointer;
	font-size: 16px;
}
button:hover {
	background-color: #206ecf;
}
</style>
