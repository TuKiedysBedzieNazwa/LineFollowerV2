<script setup lang="ts">

    import { ref } from 'vue';

    const response = ref<string>('');

    const postTemperature = () => {
        fetch('http://192.168.8.111:5173/api/linefollower', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                temperature: 1,
                sens1 : 1,
                sens2 : 1,
                sens3 : 1,
                sens4 : 1,
                sens5 : 1,
                sens6 : 1,
                requestTime: 0
            })
        }).then(
            res => res.json()
        ).then(
            res => response.value = res
        ).catch(
            err => console.log(err)
        )
    }

</script>

<template>
    <v-card class="bgbg bgblur rounded-xl w-75 h-75 d-flex flex-column justify-space-evenly align-center">
        <h2> Simple Requests </h2>
        <div class="w-100 d-flex">

            <div class="w-50 d-flex justify-center align-center">
                {{ response }}
            </div>

            <v-form @submit="postTemperature"
                class="w-50 d-flex flex-column justify-center align-center"
            >
                <h4 class="text-center mb-6"> POST </h4>
                <v-btn type="submit" variant="tonal">
                    Post Data
                </v-btn>
            </v-form>

        </div>
    </v-card>
</template>