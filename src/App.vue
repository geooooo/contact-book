<template>
<div class="app">

    <header class="app__header">
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
                :idContact="Number(contact.id)"
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
            pageSize: 5,
            pageCount: 1,
            pageNumber: 1,
            contacts: [],
            resource: null,
            filterName: "Имя",
            filterValue: "",
        }
    },

    methods: {

        clickAddContact() {
            this.toggleVisibilityEditWindow()
        },

        changeFilter(filterName, filterValue) {
            this.filterName = filterName;
            this.filterValue = filterValue;
            eventEmitter.$emit("page-number-change", 1);
            this.loadPage(1);
        },

        changePage(number) {
            this.loadPage(number);
        },

        changeContact(id) {
            let contact = this.getContactById(id);
            this.toggleVisibilityEditWindow({
                id,
                name:  contact.name,
                phone: contact.phone,
                mail:  contact.mail
            });
        },

        // Возвращает контакта на текущей странице по его идентификатору
        getContactById(id) {
            for (let contact of this.contacts) {
                if (contact.id === id) return contact;
            }
            return null;
        },

        deleteContact(id) {
            this.contacts = this.contacts.filter(c => c.id !== id);
            let self = this;
            this.resource.contact.remove({id}).then(
                () => self.loadPage(self.pageNumber)
            );
        },

        okContactEdit(contact) {
            this.toggleVisibilityEditWindow();
            let self = this;
            let contactOld = self.getContactById(contact.id);
            if (!contact.id) {
                this.resource.contact.save(contact, null).then(
                    () => self.loadPage(this.pageNumber)
                );
            } else if (!this.isEqualContact(contact, contactOld)) {
                this.resource.contact.update(contact, null).then(() => {
                    contactOld.name  = contact.name;
                    contactOld.phone = contact.phone;
                    contactOld.mail  = contact.mail;
                });
            } else {
                return;
            }
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
            if (count === 0) count = 1;
            this.pageCount = count;
            eventEmitter.$emit("page-count-change", count);
        },

        // Показать/скрыть окно редактирования контакта
        toggleVisibilityEditWindow(contact) {
            eventEmitter.$emit("edit-window-toggle-visibility", contact);
        },

        // Загрузка страницы контактов
        loadPage(number) {
            let self = this;
            this.pageNumber = number;
            this.contacts = [];
            let resource = this.resource.contact;
            if (this.filterName && this.filterValue) {
                resource = this.resource.contactFilter;
            }
            resource.get({
                page_size: this.pageSize,
                page_number: number,
                filter_name: this.filterName,
                filter_value: this.filterValue
            }).then(response => self.setContacts(
                response.body.contacts,
                response.body.count
            ));
        },

        // Установить список контактов
        setContacts(contacts, count) {
            let length = this.pageSize - this.contacts.length;
            for (let contact of contacts) {
                if (length === 0) break;
                if (this.getContactById(contact.id)) continue;
                this.contacts.push({
                    id:    contact.id,
                    name:  contact.name,
                    phone: contact.phone,
                    mail:  contact.mail
                });
                length--;
            }
            this.setPageCount(Math.ceil(count / this.pageSize));
        },

    },

    mounted() {
        this.resource = {
            contact: this.$resource("contact"),
            contactFilter: this.$resource("contact/filter"),
        };

        this.loadPage(this.pageNumber);
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
