<template>
<div class="filter-find">

    <select
        @change="change"
        v-model="filterName"
        class="filter-find__select"
        name="filterName">
        <option value="Имя">Имя</option>
        <option value="Номер">Номер</option>
        <option value="Почта">Почта</option>
    </select>
    <input
        @change="change"
        class="filter-find__input"
        v-model="filterValue"
        type="text"
        name="filterValue"
        placeholder="Поиск">

</div>
</template>


<script>
export default {

    data() {
        return {
            filterValue: "",
            filterName: "Имя",
        }
    },

    methods: {

        change() {
            this.$emit("change", this.filterName, this.filterValue);
        }

    }
}
</script>


<style scoped lang="scss">
@import "../general.scss";

.filter-find {
    display: flex;
    background-color: $color;
    border-radius: $border-radius;

    &__select {
        margin-right: 5px;
    }

    &__select,
    &__select option {
        color: white;
        font: {
            family: monospace;
            weight: bold;
        }
        background-color: $color;
        border-radius: $border-radius;
        cursor: pointer;
    }

    &__input {
        width: 200px;
        color: white;
        font-weight: bold;
        background-color: $color;
        border-radius: $border-radius;
        transition-duration: $animation-duration;
        transition-timing-function: $animation-timing-function;
        transition-property: background-color;

        &::placeholder {
            color: rgba(255, 255, 255, 0.5);
        }
        &:focus {
            background-color: lighten($color, 20%);
            &::placeholder {
                color: transparent;
            }
        }
    }
}
</style>
