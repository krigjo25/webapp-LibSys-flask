import { defineStore } from 'pinia';
import { reactive } from 'vue';

export const storedData = defineStore('shareData', {
    state: () => ({
        data: reactive({}),
    }),
    actions: {
        setData(data) {
            this.data = data;
        },
        clearData() {
            this.data = null;
        },
    },
});