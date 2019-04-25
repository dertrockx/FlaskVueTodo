<template>
  <div id="app">
    <h1>Todo List using VueJS + Flask</h1>
    <router-view />
  </div>
</template>

<script>
import List from "./components/Lists"
import axios from "axios";
export default {
  name: 'App',
}
</script>

<style>
  @import "../node_modules/bootstrap/dist/css/bootstrap.min.css"
</style>
