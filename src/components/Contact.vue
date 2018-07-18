<template>
<div class="contact">

    <div class="contact__info">
        <div class="contact__name">
            <slot name="name"></slot>
        </div>
        <div class="contact__phone">
            <slot name="phone"></slot>
        </div>
        <a class="contact__mail" href="mailto:vasia@mail.ru">
            <slot name="mail"></slot>
        </a>
    </div>

    <div class="contact__buttons">
        <div class="contact__button">
            <flat-button
                @click="clickChange">
                <span slot="caption">Изменить</span>
            </flat-button>
            <flat-button
                @click="clickDelete"
                :type="'danger'">
                <span slot="caption">Удалить</span>
            </flat-button>
        </div>
        <div class="contact__button">
        </div>
    </div>

</div>
</template>


<script>
import flatButton from "./FlatButton";

export default {

    components: {
        flatButton,
    },

    props: {

        // Уникальный идентификатор контакта
        idContact: {
            type: Number,
            required: true,
        },

    },

    data() {
        return {}
    },

    methods: {

        clickChange() {
            this.$emit("change", this.idContact);
        },

        clickDelete() {
            this.$emit("delete", this.idContact);
        },

    },

}
</script>


<style scoped lang="scss">
@import "../general.scss";

$margin: 5px;

.contact {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 20px;
    border-left: 4px solid $color;
    border-top-right-radius: $border-radius;
    border-bottom-right-radius: $border-radius;
    background-color: lighten($color, 50%);

    &__info {
        > * {
            padding: {
                top: 5px;
                bottom: 5px;
            }
        }
    }

    &__name {
        font-weight: bold;
    }

    &__phone {}

    &__mail {
        color: $blue;
    }

    &__buttons {
        display: flex;
    }

    &__button {
        margin-right: $margin;

        &:last-child {
            margin-right: 0;
        }
    }
}
</style>
