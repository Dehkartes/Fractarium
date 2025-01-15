<template>
	<div id="app">
		<header>
			<nav>
				<ul class="tools-nav">
					<li v-for="tool in tools" :key="tool.name">
						<button @click="selectTool(tool)">{{ tool.name }}</button>
					</li>
				</ul>
			</nav>
		</header>

		<main>
			<section v-if="selectedTool">
				<component :is="selectedTool.component"></component>
			</section>
			<section v-else>
				<h1>Welcome to AI Agent Tools</h1>
				<p>Select a tool from the navigation above to get started.</p>
			</section>
		</main>
	</div>
</template>

<script>
import TextAnalysisTool from "./components/AutoPRReview.vue";
import AboutMe from "./components/AboutMe.vue";

export default {
	name: "App",
	data() {
		return {
			tools: [
				{ name: "Auto Pull Request Reviewer", description: "Analyze your text efficiently.ss", component: TextAnalysisTool },
				{ name: "About Me", description: "About Me", component: AboutMe },
			],
			selectedTool: null,
		};
	},
	methods: {
		selectTool(tool) {
			if (tool.url) {
				window.location.href = tool.url;
			} else {
				this.selectedTool = tool;
			}
		},
	},
};
</script>

<style>
#app {
	font-family: Avenir, Helvetica, Arial, sans-serif;
	text-align: center;
	margin-top: 20px;
}
header {
	background-color: #333;
	color: white;
	padding: 10px 0;
}
.tools-nav {
	display: flex;
	justify-content: center;
	list-style: none;
	padding: 0;
	margin: 0;
}
.tools-nav li {
	margin: 0 10px;
}
.tools-nav button {
	background: none;
	border: none;
	color: white;
	font-size: 16px;
	cursor: pointer;
}
.tools-nav button:hover {
	text-decoration: underline;
}
main {
	padding: 20px;
}
footer {
	background-color: #f4f4f4;
	padding: 20px;
	margin-top: 20px;
}
h1 {
	font-size: 24px;
	margin-bottom: 10px;
}
p {
	font-size: 16px;
	color: #666;
}
</style>
