import Vue from 'vue';
import Vuelidate from "vuelidate";
import VueResource from "vue-resource";

import App from './App.vue';

export const eventEmitter = new Vue();

Vue.use(Vuelidate);
Vue.use(VueResource);

Vue.http.options.root = "/";

new Vue({
    el: '#app',
    render: h => h(App),
});
