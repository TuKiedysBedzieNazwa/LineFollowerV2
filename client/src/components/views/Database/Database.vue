<script setup lang="ts">

    import { ref } from 'vue';

    const response = ref<string>('');
    const input = ref<string>('');
    const areReqOk = ref<string>('');


    const SQLInput = () => {

        fetch('/api/database', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                input: input.value,
            })
        }).then(
            res => res.json()
        ).then(
            res => {
                response.value = res["data"];
                areReqOk.value = res['ok'] ? 'success' : 'error';
            }
        ).catch(
            err => console.log(err)
        )
        input.value = '';
    }

</script>

<template>
    <v-card class="bgbg bgblur rounded-xl w-75 h-50 d-flex flex-column justify-center align-center">
        <div>
            {{ response }}
        </div>
        <v-form class="w-75 mt-10" @submit="SQLInput" >
            <v-text-field v-model="input"
                label="SQL Input"
                :color="areReqOk"
            />
            <v-btn type="sumbit" variant="tonal" >
                Prześlij
            </v-btn>
        </v-form>
    </v-card>
    <v-card class="bgbg bgblur rounded-xl w-75 h-25">
        <v-card-title>
            Cheatsheet
        </v-card-title>
        <v-card-text>
            <h4>Wszystkie tabele</h4>
            SELECT name FROM sqlite_master WHERE type='table';
            <h4>Schemat tabeli</h4>
            PRAGMA table_info(table_name); <br>
            [name, type, nullable, default, primaryKey]
        </v-card-text>
    </v-card>
</template>