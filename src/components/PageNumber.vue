<template>
<div class="page-number">

    <div
        @click="clickPrev"
        class="page-number__arrow">&lt;&lt;</div>

    <div
        v-for="number in pageCurrentCount"
        :key="number"
        @click="click(number)"
        :class="{
            'page-number__number': true,
            'page-number__number_active': number === pageNumberActive
        }">
        {{ number }}
    </div>

    <div
        @click="clickNext"
        class="page-number__arrow">&gt;&gt;</div>

</div>
</template>


<script>
import {eventEmitter} from "../main";

export default {

    data() {
        return {
            pageCurrentCount: 1,
            pageNumberActive: 1,
        }
    },

    methods: {

        clickPrev() {
            if (this.pageNumberActive === 1) return;
            this.changePage(this.pageNumberActive - 1);
        },

        clickNext() {
            if (this.pageNumberActive === this.pageCurrentCount) return;
            this.changePage(this.pageNumberActive + 1);
        },

        click(number) {
            if (this.pageNumberActive === number) return;
            this.changePage(number);
        },

        changePage(number) {
            this.pageNumberActive = number;
            this.$emit("change", number);
        }

    },

    mounted() {
        let self = this;

        eventEmitter.$on("page-count-change", (count) => {
            self.pageCurrentCount = count;
        });

        eventEmitter.$on("page-number-change", (number) => {
            self.pageNumberActive = number;
        });
    },

}
</script>


<style scoped lang="scss">
@import "../general.scss";

.page-number {
    display: flex;
    cursor: pointer;
    user-select: none;

    &__arrow,
    &__number {
        padding: 5px 10px;
        font: {
            family: monospace;
            weight: bold;
        }
        color: $blue;
        transition-duration: $animation-duration;
        transition-timing-function: $animation-timing-function;
        transition-property: color;

        &:hover,
        &:active {
            color: lighten($blue, 20%);
        }
    }

    &__number_active {
        border-radius: 100%;
        background-color: $color-primary;
    }
}
</style>
