import { createApp } from 'vue'
//import './style.css'
import App from './App.vue'
import 'primevue/resources/themes/saga-blue/theme.css';
import 'primevue/resources/primevue.min.css';
import 'primeicons/primeicons.css';
import PrimeVue from "primevue/config";
import Menubar from "primevue/menubar";
import router from "./router";
import "bootstrap/dist/css/bootstrap.css";

createApp(App)
.use(router)
.use(PrimeVue, { ripple: true })
.component("Menubar", Menubar)
.mount('#app')
import "bootstrap/dist/js/bootstrap.js";