// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import './assets/styles/reset1.css'
// import './assets/styles/border.css'
import './assets/styles/iconfont/iconfont.css'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import axios from 'axios'
Vue.config.productionTip = false

Vue.use(ElementUI)
/* eslint-disable no-new */
/* 将vue使用vue原型链，则每个组件都可以使用axios */
Vue.prototype.$axios = axios
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
