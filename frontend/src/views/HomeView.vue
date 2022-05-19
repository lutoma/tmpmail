<script setup>
</script>

<template>
	<div class="container home">
		<h1 class="display-1 mb-3">tmpmail</h1>

		<div class="name-form">
			<div class="form-floating">
				<input v-on:keyup.enter="openInbox()" v-model="name" type="text" class="form-control" id="floatingInput" placeholder="Inbox name" autofocus>
				<label for="query">Inbox name</label>
			</div>

			<button class="btn btn-primary" type="submit" @click.stop.prevent="openInbox()">Check mail</button>
		</div>
	</div>
</template>

<script>
export default {
  data: () => ({
    name: '',
  }),

  methods: {
    async openInbox() {
    	this.$router.push({ name: 'inbox', params: { domain: 'p25.li', name: this.name } })
    },
  }
}
</script>

<style lang="scss">
.home {
	display: flex;
	flex-direction: column;
	align-items: center;

	h1 {
		margin-top: 10rem;
	}

	.name-form {
		display: flex;
		flex-direction: row;

		.form-floating {
			flex-grow: 1;

			input {
				width: 100%;
			}
		}

		button {
			margin-left: 1rem;
			padding-left: 1.5rem;
			padding-right: 1.5rem;
		}

		margin-top: 4rem;
		width: 700px;
		max-width: 95vw;
	}
}
</style>

