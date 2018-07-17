<template>
<div
    ref="window"
    class="edit-window">

    <div class="edit-window__shadow"></div>

    <form class="edit-window__form" action="">

        <div class="edit-window__form-group">
            <label class="edit-window__form-label" for="contactName">Имя:</label>
            <input
                v-model="name"
                class="edit-window__form-input"
                id="contactName"
                type="text">
        </div>

        <div class="edit-window__form-group">
            <label class="edit-window__form-label" for="contactPhone">Телефон:</label>
            <input
                v-model="phone"
                class="edit-window__form-input"
                for="contactPhone"
                type="text">
        </div>

        <div class="edit-window__form-group">
            <label class="edit-window__form-label" for="contactMail">Почта:</label>
            <input
                v-model="mail"
                class="edit-window__form-input"
                id="contactMail"
                type="text">
        </div>

        <div class="edit-window__form-group edit-window__form-group_center">
            <flat-button
                @click="clickOk"
                :type="'primary'">
                <span slot="caption">Ок</span>
            </flat-button>
            <flat-button
                @click="clickCancel">
                <span slot="caption">Отмена</span>
            </flat-button>
        </div>

    </form>

</div>
</template>


<script>
import flatButton from "./FlatButton";
import { eventEmitter } from '../main';

export default {

    // TODO: обработка ошибок ввода

    components: {
        flatButton,
    },

    data() {
        return {
            name: "",
            phone: "",
            mail: "",
            id: null,
        }
    },

    methods: {

        clickOk() {
            let data = {
                id:    this.id,
                name:  this.name,
                phone: this.phone,
                mail:  this.mail,
            };
            console.log(data);
            this.$emit("ok", data);
        },

        clickCancel() {
            this.$emit("cancel");
        },

    },

    mounted() {
        let self = this;

        eventEmitter.$on("edit-window-toggle-visibility", (contact) => {
            let editWindow = self.$refs.window;
            if (editWindow.classList.contains("edit-window_show")) {
                editWindow.classList.remove("edit-window_show");
                editWindow.classList.add("edit-window_hide");
                window.setTimeout(() => {
                    editWindow.style.display = "none";
                    self.id    = null;
                    self.name  = "";
                    self.phone = "";
                    self.mail  = "";
                }, 200);
            } else {
                if (contact) {
                    self.id    = contact.id;
                    self.name  = contact.name;
                    self.phone = contact.phone;
                    self.mail  = contact.mail;
                }
                editWindow.style.display = "";
                editWindow.classList.remove("edit-window_hide");
                editWindow.classList.add("edit-window_show");
            }
        });
    },
}
</script>


<style scoped lang="scss">
@import "../general.scss";

.edit-window {
    position: fixed;
    top: 0;
    left: 0;
    display: none;
    justify-content: center;
    align-items: center;
    height: 100%;
    width: 100%;
    animation-duration: 0.2s;
    animation-timing-function: $animation-timing-function;
    animation-fill-mode: forwards;
    animation-iteration-count: 0;

    &_show {
        display: flex;
        animation-iteration-count: 1;
        animation-name: show;
    }

    &_hide {
        animation-iteration-count: 1;
        animation-name: hide;
    }

    &__shadow {
        position: absolute;
        z-index: 100;
        top: 0;
        left: 0;
        height: 100%;
        width: 100%;
        background-color: rgba(0,0,0,0.5);
    }

    &__form {
        position: relative;
        z-index: 101;
        padding: 10px 20px;
        border-top: 4px solid $color;
        background-color: lighten($color, 50%);
        border-bottom-left-radius: $border-radius;
        border-bottom-right-radius: $border-radius;
        box-shadow: 0 2px 20px 0 rgba(0,0,0,0.5);
    }

    &__form-group {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: {
            top: 5px;
            bottom: 5px;
        }

        &_center {
            justify-content: center;
        }

        > *:first-child {
            margin-right: 10px;
        }

        &:last-child {
            padding-top: 20px;
        }
    }

    &__form-label {
        cursor: pointer;
    }

    &__form-input {
        border-radius: $border-radius;
        border: 2px solid transparent;
        transition-duration: $animation-duration;
        transition-timing-function: $animation-timing-function;
        transition-property: border-color;

        &:focus {
            border-color: $color;
        }

        &_valid {
            border-color: $color-primary;
        }

        &_invalid {
            border-color: $color-danger;
        }
    }
}

@keyframes show {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

@keyframes hide {
    from {
        opacity: 1;
    }
    to {
        opacity: 0;
    }
}
</style>
