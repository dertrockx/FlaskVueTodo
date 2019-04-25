<template>
	<li class="list-group-item">
		<slot />
	</li>
</template>
<script>
	export default {
		name: "Item",
		props: ["id"]
	}
</script>