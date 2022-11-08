<script setup>
</script>

<template>
	<div class="container">
		<h1>Inbox for {{ $route.params.name }}@{{ $route.params.domain }}</h1>

		<table class="table mt-5">
			<thead>
				<tr>
					<th scope="col">Subject</th>
					<th scope="col" style="width: 350px;">From</th>
					<th scope="col" style="width: 250px;">Time</th>
				</tr>
			</thead>
			<tbody>
				<tr style="cursor: pointer;" v-for="mail of emails" :key="mail.id" @click="openUUID=mail.id" data-bs-toggle="offcanvas" data-bs-target="#offcanvasBottom" aria-controls="offcanvasBottom">
					<td><a href="#" @click="openUUID=mail.id" data-bs-toggle="offcanvas" data-bs-target="#offcanvasBottom" aria-controls="offcanvasBottom">{{ mail.subject }}</a></td>
					<td>{{ mail.header_src }}</td>
					<td>{{ mail.received }}</td>
				</tr>
			</tbody>
		</table>

		<div class="offcanvas offcanvas-bottom" tabindex="-1" id="offcanvasBottom" aria-labelledby="offcanvasBottomLabel" style="height: 65%">
			<div class="offcanvas-header">
				<h5 class="offcanvas-title" id="offcanvasBottomLabel"><template v-if="email">{{ email.subject}}</template><template v-else>Loading...</template></h5>
				<button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
			</div>
			<div class="offcanvas-body small">
				<template v-if="email">
					<strong>From: {{ email.headers.From }}</strong><br />
					<strong>To: {{ email.headers.To }}</strong><br />
					<strong>Date: {{ email.headers.Date }}</strong><br />
					<a :href="`https://api.tmpmail.ohai.is/email/${email.id}/raw`" target="_blank" rel="noopener">Raw</a>

					<p class="mt-4" style="white-space: pre-line;">{{ email.text }}</p>
				</template>

			</div>
		</div>
	</div>
</template>

<script>
export default {
  data: () => ({
    emails: null,
    openUUID: null,
    email: null
  }),

  created() {
    this.fetchInbox()
  },

  watch: {
    openUUID: 'fetchEmail'
  },


  methods: {
    async fetchInbox() {
      const url = `https://api.tmpmail.ohai.is/inbox/${this.$route.params.name}@${this.$route.params.domain}`
      this.emails = await (await fetch(url)).json()
    },

    async fetchEmail() {
      const url = `https://api.tmpmail.ohai.is/email/${this.openUUID}`
      this.email = await (await fetch(url)).json()
    }
  }
}
</script>
