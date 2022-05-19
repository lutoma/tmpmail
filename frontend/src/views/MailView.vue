<script setup>
</script>

<template>
	<main>
		<h1>Inbox</h1>
		<h2>{{ $route.params.name }}@{{ $route.params.domain }}</h2>

		<table class="table">
			<thead>
				<tr>
					<th scope="col">From</th>
					<th scope="col">Subject</th>
					<th scope="col">Time</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="mail of emails" :key="mail.id">
					<td>{{ mail.header_src }}</td>
					<td><router-link :to="`/mail/${mail.id}`">{{ mail.subject }}</router-link></td>
					<td>{{ mail.received }}</td>
				</tr>
			</tbody>
		</table>
	</main>
</template>

<script>
import {useRoute} from "vue-router"

export default {
  data: () => ({
    emails: null
  }),

  created() {
    this.fetchData()
  },

/*  watch: {
    // re-fetch whenever currentBranch changes
    currentBranch: 'fetchData'
  },
*/

  methods: {
    async fetchData() {
      const url = `http://127.0.0.1:8000/inbox/${this.$route.params.name}@${this.$route.params.domain}`
      this.emails = await (await fetch(url)).json()
    }
  }
}
</script>
