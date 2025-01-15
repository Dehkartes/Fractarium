<template>
	<div>
		<h2>Feature Component</h2>
		<p>This component renders an external webpage.</p>
		<iframe :src="url" class="external-page" frameborder="0"></iframe>
	</div>
</template>

<script>
export default {
	name: "FeatureComponent",
	data() {
		return {
			url: "https://fractarium.com",
		};
	},
};
</script>

<style>
.external-page {
	width: 100%;
	height: 90vh;
	border: none;
}
</style>
