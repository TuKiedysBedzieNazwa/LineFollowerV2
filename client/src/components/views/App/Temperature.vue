<script setup lang="ts">

    import { ref } from 'vue';

    const testVal = ref<string>('empty');

    const getTemperature = () => {
        fetch('/api/test').then(
            res => res.json()
        ).then(
            res => console.log(res)
        )
    }

  // const interval = setInterval(getTemperature, 1000);

</script>


<template>
    <div>
        value: {{ testVal }}
    </div>
    <v-btn @click="getTemperature">
        get
    </v-btn>
</template>