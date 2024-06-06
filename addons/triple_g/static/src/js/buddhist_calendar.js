odoo.define("ggg.buddisht_calendar", function (require) {
    "use strict";
    var core = require('web.core');
    var dom = require('web.dom');
    var session = require('web.session');
    var time = require('web.time');
    var utils = require('web.utils');

    var _t = core._t;
    var field_utils = require("web.field_utils");
    //    console.log(field_utils)
    field_utils.format.date = function (value, field, options) {
        //console.log("new")
        if (value === false || isNaN(value)) {
            return "";
        }
        if (field && field.type === 'datetime') {
            if (!options || !('timezone' in options) || options.timezone) {
                value = value.clone().add(session.getTZOffset(value), 'minutes');
            }
        }
        var date_format = time.getLangDateFormat();
        // kenghot: Buddish calendar
        if (moment.locale() === 'th') {
            var tmp = moment(value);
            tmp.year(tmp.year() + 543);
            return tmp.format(date_format);
        } else {
            return value.format(date_format);
        }

    }
    var date_picker = require("web.datepicker");
    date_picker.DateWidget.include({
        /**
 * @private
 * @param {Moment|false} value
 */
        _setLibInputValue: function (value) {
            this.__libInput++;
            //console.log("_setLibInputValue")
            //kenghot
            var tmp = moment(value)
            if (moment.locale() === 'th') {
                tmp.year(tmp.year() + 543);
            }
            this.$el.datetimepicker('date', tmp || null);
            this.__libInput--;
        },
        /**g
         * set the value from the input value
         *
         * @private
         */
        _setValueFromUi: function () {
            //console.log("_setValueFromUi")
            var value = this.$input.val() || false;
            var d = this._parseClient(value);
            //kenghot
            if (moment.locale() === 'th' && value) {
                d.year(d.year() - 543);
            }
            this.setValue(d);
            //original
            //this.setValue(this._parseClient(value));
        },
    })
}
)