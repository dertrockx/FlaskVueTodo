<template>
	<div class="container">
		<form class="form-inline" @submit.prevent="addItem">
			<input v-model="newItem" type="text" class="form-control mb-2 mr-sm-2" placeholder="Name" />
			<button type="submit" class="btn btn-primary mb-2">Submit</button>
		</form>
		<ul class="list-group">
			<Item v-for="item in items" :key="item.id" :id="item.id">
				{{ item.title }}
			</Item>
		</ul>
	</div>
</template>
<script>
	import Item from "./Item";
	import axios from "axios";
	export default {
		props: ["id"],
		name: "List",
		components: {
			Item
		},
		data(){
			return {
				items: [],
				isBlank: true,
				newItem: ''
			}
		},
		created() {
			axios.get('http://127.0.0.1:5000/api/items', {
				params: {
					list_id : this.id
				}
			}).then( response => {
				this.items = response.data;
				this.isBlank = false;
			})
		},
		methods: {
			addItem() {
				var data = {
					title: this.newItem,
					list_id: this.id
				}
				axios.post('http://127.0.0.1:5000/api/items', data)
				.then( response => {
					var item = response.data;
					this.items.push(item)
				})
			}
		},
		watch: {
			items: function(){
				this.newItem = '';
			}
		}
	}
</script>
<style scoped>
	div.container {
		min-height: 200px;
		border: 3px solid black;
	}
</style>
