import Vue from 'vue';
import Vuelidate from "vuelidate";

import App from './App.vue';

export const eventEmitter = new Vue();

Vue.use(Vuelidate);

new Vue({
    el: '#app',
    render: h => h(App),
});
