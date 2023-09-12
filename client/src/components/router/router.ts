import { createRouter, createWebHashHistory } from 'vue-router';
import App from '../views/App/App.vue';
import Database from '../views/Database/Database.vue';
import RemoteControl from '../views/RemoteControl/RemoteControl.vue';

const routes = [
    {
        path: "/",
        component: App
    },
    {
        path: "/Database",
        component: Database
    },
    {
        path: '/RemoteControl',
        component: RemoteControl
    }
];

export default createRouter({
    history: createWebHashHistory(),
    routes
})
