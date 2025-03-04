import { defineStore } from 'pinia';

export const storedData = defineStore('shareData', {
    state: () => ({
        data: null,
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