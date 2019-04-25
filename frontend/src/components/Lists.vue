<template>
	<div class="container">
		<form class="form-inline" @submit.prevent="createList">
			<input v-model="newList" type="text" class="form-control mb-2 mr-sm-2" placeholder="Name" />
			<button type="submit" class="btn btn-primary mb-2">Submit</button>
		</form>
		<h2>Lists</h2>
		<ul class="list-group container">
			<router-link :to="'/list/' + list.id" class="list-group-item list-group-item-action" v-for="list in lists" :key="list.id" :id="list.id">
				{{ list.name }}
			</router-link>
		</ul>
	</div>
</template>
<script>

	import axios from "axios";
	export default {
		name: "Lists",
		data(){
			return {
				/*
				lists: [
				    {
				        created_at: "2019-04-25 01:19:45", 
				        id: 2, 
				        items: [], 
				        name: "Change sample todo list"
				    }, 
				    {
				        created_at: "2019-04-25 08:11:51", 
				        id: 4, 
				        items: [], 
				        name: "dasdszxdas"
				    }, 
				    {
				        created_at: "2019-04-25 08:12:14", 
				        id: 5, 
				        items: [], 
				        name: "Yeah"
				    }, 
				    {
				        created_at: "2019-04-25 08:14:57", 
				        id : 6, 
				        "items": [], 
				        "name": "dsaczxdas"
				    }, 
				],
				*/
				lists: [],
				newList: ""
			}
		},
		created() {
			axios.get('http://127.0.0.1:5000/api/lists').then( (response) => {
				this.lists = response.data;
			})
		},
		watch: {
			lists: function(){
				this.newList = "";
			}
		},
		methods: {
			createList(){
				var data = {
					name: this.newList
				}
				axios.post('http://127.0.0.1:5000/api/lists', data).then( response => {
					this.lists.push(response.data);
				})
			},
			deleteList(id){
				axios.delete('http://127.0.0.1:5000/api/lists', {
					params: {
						id: id
					}
				})
				.then(response => {
					console.log(response.data)
					for(var list of this.lists){
						if(list.id === id){
							var index = this.lists.indexOf(list);
							this.lists.splice(index, 1)
						}
					}
				}).catch(error => {
					if (error) throw error;
				})
			}
		}
	}
</script>
<style>
	div {
		margin-top: 4em;
	}
</style>