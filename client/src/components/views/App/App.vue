<script setup lang="ts">

    import SingleTile from '../../SingleTile.vue';
    import RequestsTime from './RequestsTime.vue';
    import Sensors from './Sensors.vue';
    import Temperature from './Temperature.vue';

</script>

<template>
    <div class="w-100 h-25 d-flex justify-space-evenly align-stretch">
        <SingleTile title="Czas pomiędzy requestami" class="w-20">
            <RequestsTime />
        </SingleTile>
        <SingleTile title="Sensory" class="w-40">
            <Sensors />
        </SingleTile>
        <SingleTile title="Temperatura" class="w-20">
            <Temperature />
        </SingleTile>
    </div>

    <SingleTile title="Test div" class="w-75 h-50 bgbg bgblur">
        content
    </SingleTile>
</template>