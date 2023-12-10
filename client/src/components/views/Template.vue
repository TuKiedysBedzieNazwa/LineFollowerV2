<script setup lang="ts">

    import router from '../router/router';

    const links: Array<{
        to: string,
        icon: string,
        scale: number
    }> = [
        {
            to:"/",
            icon:"fa-home",
            scale: 3.4
        },
        {
            to:"/Database",
            icon:"fa-database",
            scale: 3
        },
        {
            to:"/RemoteControl",
            icon:"md-settingsremote",
            scale: 3.2
        },
        {
            to:"/Requests",
            icon:"bi-cloud-arrow-up-fill",
            scale: 3.3
        }
    ];

</script>

<template>
    <v-layout>

        <v-app-bar color="rgba(0,0,0, 0.6)"
            class="bgblur d-flex justify-center align-center"
        >
            <v-app-bar-title>Line Follower</v-app-bar-title>
        </v-app-bar>

        <v-main class="h-screen bgimg d-flex align-center">
            <div class="bgbg bgblur w-150px rounded-e-xl pl-5 py-4 d-flex flex-column justify-center align-center" >
                <router-link v-for="link in links"
                    :to="link.to"
                    class="my-7 w-100"
                >
                    <v-icon :name="link.icon"
                        :scale="link.scale"
                        color="white"
                        class="anim"
                        :class="{'ml-10': router.currentRoute.value.path === link.to}"
                    />
                </router-link>
            </div>
            <div class="w-100 h-100 d-flex flex-column justify-space-evenly align-center">
                <router-view></router-view>
            </div>
        </v-main>
    </v-layout>
</template>