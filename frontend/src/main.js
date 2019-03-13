import '@babel/polyfill';
import Vue from 'vue';
import './plugins/vuetify';
import App from './App.vue';
import router from './router';

Vue.config.productionTip = false;

import VueResource from 'vue-resource';
Vue.use(VueResource);

new Vue({
    router,
    render: function(h) {
        return h(App);
    }
}).$mount('#app');
