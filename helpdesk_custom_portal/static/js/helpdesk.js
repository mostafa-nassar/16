odoo.define('helpdesk_custom_portal.helpdesk_custom_portal', function (require) {
    "use strict";

    var rpc = require('web.rpc')
    var publicWidget = require('web.public.widget');
    publicWidget.registry.helpdesk_custom_portal = publicWidget.Widget.extend({

        selector: '.new_helpdesk_form',
        events: {
            // 'change .partner_area': '_onNewHelpDeskConfirm',
            'click .new_helpdesk_confirm': '_onNewHelpDeskConfirm',
        },


        _ppppppppppppppp: function (ev) {
            this._buttonExec($(ev.currentTarget), this._createHelpDeskIssue);

            console.log('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
            console.log(ev.currentTarget.value)
        },
        _buttonExec: function ($btn, callback) {
            // TODO remove once the automatic system which does this lands in master
            $btn.prop('disabled', true);
            return callback.call(this).guardedCatch(function () {
                $btn.prop('disabled', false);
            });
        },

        _createHelpDeskIssue: function () {

            return this._rpc({
                model: 'helpdesk.ticket',
                method: 'create_helpdesk_portal',
                args: [{
                    partner_id: parseInt(document.getElementById("partner_area").value),
                    state_area: parseInt(document.getElementById("partner_area_name").value),
                    water_dark_color: $('.new_helpdesk_form .water_dark_color').prop("checked"),
                    water_bad_smell: $('.new_helpdesk_form .water_bad_smell').prop("checked"),
                    water_bad_teast: $('.new_helpdesk_form .water_bad_teast').prop("checked"),
                    motor: $('.new_helpdesk_form .motor').prop("checked"),
                    water_safe: $('.new_helpdesk_form .water_safe').prop("checked"),
                    follower_phone: $('.new_helpdesk_form .follow_phone').val(),
                    phone: $('.new_helpdesk_form .phone').val(),
                    email: $('.new_helpdesk_form .myemail').val(),
                    customer_info_name: $('.new_helpdesk_form .customer_info_name').val(),
                    door: $('.new_helpdesk_form .door').val(),
                    public_street: $('.new_helpdesk_form .public_street').val(),
                    public_street_near: $('.new_helpdesk_form .public_street_near').val(),
                    customer_home_number: $('.new_helpdesk_form .customer_home_number').val(),
                    customer_home_address: $('.new_helpdesk_form .customer_home_address').val(),
                    identification_number: $('.new_helpdesk_form .identification_number').val(),
                    complain_issue_id: $('.new_helpdesk_form .complain_issue_id').val(),

                    // issue: this._parse_type($('.new_helpdesk_form .complain_issue_id').val(),'drinking'),
                    issue: $('.new_helpdesk_form .get_type').val(),
                    // sewage_watter_id: $('.new_helpdesk_form .medical_issues').val(),
                    // commercial_watter_id: $('.new_helpdesk_form .medical_issues').val(),
                    sup_number: $('.new_helpdesk_form .sup_number').val(),
                    zone_number: $('.new_helpdesk_form .zone_number').val(),


                }],
            }).then(function (response) {
                if (response.errors) {
                    toastr.error('Something went wrong ' + response.errors + ' , try again.')
                    return Promise.reject(response);
                } else {
                    window.location = '/your-submitted'
                }
            });
        },

        // _parse_type: function (value,type) {
        //     let val = false;
        //     console.log('frist vals',val);
        //     rpc.query({
        //         model: 'complain.issue',
        //         method: 'search_read',
        //         fields: ['id', 'issue_type', 'name'],
        //         domain: [['id', '=', parseInt(value)]],
        //
        //     }).then ((rec ) => {
        //         if (rec[0].issue_type === "sewage" & type === 'sewage') {
        //             console.log('555555555555555555555555555555555555555555555555555555555555')
        //              val = $('.new_helpdesk_form .get_type').val();
        //              console.log('55555555555',val)
        //              console.log('55555555555',this.val)
        //             return val
        //         }
        //
        //         if (rec[0].issue_type === 'drinking_water') {
        //
        //         }
        //         if (rec[0].issue_type === 'commercial') {
        //
        //         }
        //         console.log('aaaaaaaaaaa',val)
        //
        //
        //     })
        //
        //
        // },
        _onNewHelpDeskConfirm: function (ev) {

            ev.preventDefault();
            ev.stopPropagation();
            if ($("#helpdesk_form").valid()) {
                this._buttonExec($(ev.currentTarget), this._createHelpDeskIssue);
            } else {
                toastr.warning('Please fill the mandatory fields.')
            }

        },
    });

    $(document).ready(function () {
        $(document).on("click", ".new_helpdesk_confirm", async function () {

        })
        $('.select2bs4').select2({
            theme: 'bootstrap4'
        });
        $('.partner_area_select2').select2({
            theme: 'bootstrap4'
        });

        $('.data-mask').inputmask({
            mask: ["0199-999-9999",],
            greedy: false,
            definitions: {
                '*': {
                    validator: "1",
                    cardinality: 1
                }
            },
            clearIncomplete: true
        });

        $(document).on("change", ".partner_area", async function () {
            var select = document.getElementById("partner_area_name");
            console.log($(this).val());
            var length = select.options.length;
            for (let i = length - 1; i >= 0; i--) {
                select.options[i] = null;
            }
            let partner_id = $(this).val();
            await rpc.query({
                model: 'res.partner',
                method: 'search_read',
                fields: ['id', 'parent_id', 'state_area', 'name'],
                domain: ['|', ['id', '=', parseInt(partner_id)], ['parent_id', '=', parseInt(partner_id)]],
            }).then(function (rec) {

                for (var area in rec) {
                    if ((rec[0].state_area).length > 0) {
                        var x = document.getElementById("partner_area_name");
                        var option = document.createElement("option");
                        option.text = rec[area]['state_area'][1];
                        option.value = rec[area]['state_area'][0];
                        var sel = x.options[x.selectedIndex];
                        x.add(option, sel);
                    }
                }


            })

        });
        $(document).on("change", ".complain_issue_id", async function () {
            var select = document.getElementById("get_type");
            var length = select.options.length;
            for (let i = length - 1; i >= 0; i--) {
                select.options[i] = null;
            }
            let issue_type = $(this).val();
            await rpc.query({
                model: 'complain.issue',
                method: 'search_read',
                fields: ['id', 'issue_type', 'name'],
                domain: [['id', '=', parseInt(issue_type)]],
            }).then(async function (rec) {

                if (rec[0].issue_type === "sewage") {
                    await rpc.query({
                        model: 'sewage.water',
                        method: 'search_read',
                        fields: ['id', 'name'],
                        // domain: ['|', ['id', '=', parseInt(issue_type)], ['parent_id', '=', parseInt(issue_type)]],
                    }).then(function (rec) {

                        for (var area in rec) {
                            var x = document.getElementById("get_type");
                            var option = document.createElement("option");
                            option.text = rec[area]['name'];
                            option.value = rec[area]['id'];
                            var sel = x.options[x.selectedIndex];
                            x.add(option, sel);

                        }

                    })
                }

                if (rec[0].issue_type === 'drinking_water') {
                    await rpc.query({
                        model: 'drinking.water',
                        method: 'search_read',
                        fields: ['id', 'name'],
                        // domain: ['|', ['id', '=', parseInt(issue_type)], ['parent_id', '=', parseInt(issue_type)]],
                    }).then(function (rec) {

                        for (var area in rec) {
                            var x = document.getElementById("get_type");
                            var option = document.createElement("option");
                            option.text = rec[area]['name'];
                            option.value = rec[area]['id'];
                            var sel = x.options[x.selectedIndex];
                            x.add(option, sel);

                        }

                    })
                }
                if (rec[0].issue_type === 'commercial') {
                    await rpc.query({
                        model: 'commercial.water',
                        method: 'search_read',
                        fields: ['id', 'name'],
                        // domain: ['|', ['id', '=', parseInt(issue_type)], ['parent_id', '=', parseInt(issue_type)]],
                    }).then(function (rec) {

                        for (var area in rec) {
                            var x = document.getElementById("get_type");
                            var option = document.createElement("option");
                            option.text = rec[area]['name'];
                            option.value = rec[area]['id'];
                            var sel = x.options[x.selectedIndex];
                            x.add(option, sel);

                        }

                    })
                }

            })


        });

        $(document).on("change", ".complain_issue_id", async function () {
            var issue_id = $(this).val();
            await rpc.query({
                model: 'complain.issue',
                method: 'search_read',
                fields: ['drinking_watter', 'quality', 'billing'],
                domain: [['id', '=', parseInt(issue_id)]],
            }).then(function (rec) {
                for (let issue in rec) {
                    if (rec[issue]['quality'] === true) {
                        document.getElementById("is_quality").style.display = "block";
                    } else {
                        document.getElementById("is_quality").style.display = "none";
                    }
                    if (rec[issue]['billing'] === true) {
                        document.getElementById("is_billing").style.display = "block";
                    } else {
                        document.getElementById("is_billing").style.display = "none";
                    }
                }
                if (rec.length < 1) {
                    document.getElementById("is_quality").style.display = "none";
                    document.getElementById("is_billing").style.display = "none";

                }


            })

        });

    });
});



