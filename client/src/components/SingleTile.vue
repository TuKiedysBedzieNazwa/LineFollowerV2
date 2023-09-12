<script setup lang="ts">

interface props {
    title?: string,
}
defineProps<props>();
</script>

<template>
    <v-card class="bgbg bgblur rounded-xl">
        <v-card-title>
            {{ title }}
        </v-card-title>
        <v-card-subtitle>
            <slot></slot>
        </v-card-subtitle>
    </v-card>
</template>