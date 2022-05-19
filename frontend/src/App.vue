<script setup>
import 'bootstrap'
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
	<RouterView />
</template>

<style lang="scss">
//@import 'typeface-fira-sans/index';
//@import '@fortawesome/fontawesome-pro/css/fontawesome';
//@import '@fortawesome/fontawesome-pro/css/regular';

//$font-family-sans-serif: 'Fira Sans', system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", "Liberation Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji" !default;

@import 'bootstrap/scss/bootstrap';

html, body, #__nuxt {
	width: 100%;
	height: 100%;
}

body {
	padding: 2rem 0;
}

a {
	text-decoration: none;

	&:hover {
		text-decoration: underline;
	}
}


footer {
	a {
		color: $text-muted;
	}
}
</style>
