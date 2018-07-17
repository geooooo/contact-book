<template>
<div class="app">

    <header class=".app__header">
        <h1 class="app__title">Список контактов</h1>
        <div class="app__top-bar">
            <flat-button
                :type="'primary'"
                @click="clickAddContact">
                <span slot="caption">Добавить</span>
            </flat-button>
            <filter-find
                @change="changeFilter">
            </filter-find>
        </div>
    </header>

    <section class="app__main">
        <div class="app__contact-list">
            <contact
                v-for="(contact, id) in contacts"
                :key="id"
                :idContact="Number(id)"
                @change="changeContact"
                @delete="deleteContact">
                <span slot="name">{{ contact.name }}</span>
                <span slot="phone">{{ contact.phone }}</span>
                <span slot="mail">{{ contact.mail }}</span>
            </contact>
        </div>
    </section>

    <footer class="app__footer">
        <page-number
            @change="changePage"></page-number>
    </footer>

    <edit-window
        @ok="okContactEdit"
        @cancel="cancelContactEdit"></edit-window>

</div>
</template>


<script>
import {eventEmitter} from "./main";

import flatButton from "./components/FlatButton";
import filterFind from "./components/FilterFind";
import pageNumber from "./components/PageNumber";
import contact from "./components/Contact";
import editWindow from "./components/EditWindow";

export default {

    components: {
        flatButton,
        filterFind,
        pageNumber,
        contact,
        editWindow,
    },

    data () {
        return {
            pageCount: 1,
            contacts: {
                5:  {name:"vasia", phone:"123", mail:"v@mail.ru"},
                1:  {name:"petia", phone:"456", mail:"p@mail.ru"},
                88: {name:"ivan",  phone:"789", mail:"i@mail.ru"},
            },
        }
    },

    methods: {

        clickAddContact() {
            this.toggleVisibilityEditWindow()
        },

        // TODO: filterChange
        changeFilter(filterValue) {
            console.warn("filterChange: " + filterValue);
        },

        // TODO: changePage
        changePage(number) {
            console.warn("changePage: " + number);
            //this.setPageCount()
        },

        changeContact(id) {
            this.toggleVisibilityEditWindow({
                id,
                name:  this.contacts[id].name,
                phone: this.contacts[id].phone,
                mail:  this.contacts[id].mail,
            });
        },

        // TODO: deleteContact
        deleteContact(id) {
            console.warn("deleteContact: " + id);
        },

        // TODO: okContactEdit
        okContactEdit(contact) {
            console.warn("okContactEdit: " + contact.name + " " +
                                             contact.phone + " " +
                                             contact.mail + " " +
                                             contact.id);
            this.toggleVisibilityEditWindow();
            // новая запись имеет NULL
            if (this.isEqualContact(contact, this.contacts[contact.id])) return;
        },

        // Проверка равенства двух контактов
        isEqualContact(a, b) {
            return (a.name  === b.name) &&
                   (a.phone === b.phone) &&
                   (a.mail  === b.mail);
        },

        // Отмена добавления/редактирования контакта
        cancelContactEdit() {
            this.toggleVisibilityEditWindow();
        },

        // Изменение количества страниц с контактами
        setPageCount(count) {
            this.pageCount = count;
            eventEmitter.$emit("page-number-change", count);
        },

        // Показать/скрыть окно редактирования контакта
        toggleVisibilityEditWindow(contact) {
            eventEmitter.$emit("edit-window-toggle-visibility", contact);
        },

    },
}
</script>


<style scoped lang="scss">
@import "general.scss";

$bg-color: #eee;

.app {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100%;
    background-color: $bg-color;
    overflow: hidden;

    &__header {
        background-color: lighten($color, 50%);
    }

    &__title {
        padding: {
            top: 10px;
            bottom: 10px;
        }
        text-align: center;
        color: $bg-color;
        background-color: $color;
    }

    &__top-bar {
        display: flex;
        justify-content: space-between;
        padding: 5px;
    }

    &__main {
        padding: 5px;
    }

    &__contact-list {
        padding: {
            left: 20px;
            right: 20px;
        }

        > * {
            margin-bottom: 20px;

            &:last-child {
                margin-bottom: 0;
            }
        }
    }

    &__footer {
        display: flex;
        justify-content: center;
        padding-bottom: 10px;
    }
}
</style>
