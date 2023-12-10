import { createApp } from 'vue';
import { createVuetify } from 'vuetify';
import { OhVueIcon, addIcons } from "oh-vue-icons";
import { FaDatabase, FaHome, MdSettingsremote, BiCloudArrowUpFill } from "oh-vue-icons/icons";

import * as directives from 'vuetify/directives';
import * as components from 'vuetify/components';
import Template from './components/views/Template.vue';
import router from './components/router/router';

import 'vuetify/styles';
import './style.css';


const vuetify = createVuetify({
    components,
    directives,
    ssr: true,
    theme: {
        defaultTheme: 'dark'
    },
});


addIcons(
    FaDatabase,
    FaHome,
    MdSettingsremote,
    BiCloudArrowUpFill
);

const app = createApp(Template);

app.use(router)
    .use(vuetify)
    .component("v-icon", OhVueIcon)
    .mount('#app');