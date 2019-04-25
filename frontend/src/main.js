// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
// import router from './router'
import VueRouter from 'vue-router'

import Lists from "./components/Lists"
import List from "./components/List"

Vue.use(VueRouter)

const routes = [
	{
		path: '/',
		component: Lists
	},
	{
		path: '/list/:id',
		component: List,
		props: true
	}
]

const router = new VueRouter({ routes: routes, mode: 'history'})

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App},
  template: '<App/>'
})
