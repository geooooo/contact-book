<template>
<button
    ref="button"
    class="flat-button"
    type="button"
    @click="click">

    <slot name="caption"></slot>

</button>
</template>


<script>
export default {

    props: {

        // Тип кнопки, поумолчанию: обычная,
        // также может быть "primary", "danger"
        type: {
            type: String,
            default: ""
        },

    },

    data() {
        return {}
    },

    methods: {

        click() {
            this.$emit("click");
        }

    },

    mounted() {
        // Контроль типа кнопки
        if (["", "primary", "danger"].includes(this.type)) {
            this.$refs.button.classList.add(`flat-button_${this.type}`);
        } else {
            console.error("Неверный тип кнопки !");
        }
    }

}
</script>


<style scoped lang="scss">
@import "../general.scss";

.flat-button {
    color: white;
    font: {
        family: monospace;
        weight: bold;
    }
    background-color: $color;
    border: 2px solid $color;
    border-radius: $border-radius;
    cursor: pointer;
    transition-duration: $animation-duration;
    transition-timing-function: $animation-timing-function;
    transition-property: background-color, border-color;
    user-select: none;

    &:hover {
        background-color: lighten($color, 4%);
        border-color: lighten($color, 4%);
    }

    &:active {
        background-color: transparent;
        color: $color;
    }

    &_primary {
        background-color: $color-primary;
        border-color: $color-primary;

        &:hover {
            background-color: lighten($color-primary, 4%);
            border-color: lighten($color-primary, 4%);
        }

        &:active {
            background-color: transparent;
            color: $color-primary;
        }
    }

    &_danger {
        background-color: $color-danger;
        border-color: $color-danger;

        &:hover {
            background-color: lighten($color-danger, 4%);
            border-color: lighten($color-danger, 4%);
        }

        &:active {
            background-color: transparent;
            color: $color-danger;
        }
    }
}
</style>
