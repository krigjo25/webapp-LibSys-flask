import { defineStore } from 'pinia';

export const StoredData = defineStore('shareData', {
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