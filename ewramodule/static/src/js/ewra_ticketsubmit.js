/** @odoo-module **/
import publicWidget from 'web.public.widget';
// odoo.define([
//     'ewra_complain.validation'
// ], function(require) {
//     'use strict';
//     var PublicWidget = require('web.public.widget');
//     var rpc = require('web.rpc');

//     var Dynamic = PublicWidget.Widget.extend({
//         selector: '.dynamic_snippet_blog',
//         start: function () {
//             var self = this;
//             rpc.query({
//                 route: '/ewra-helpdesk-data',
//                 params: {},
//             }).then(function (result) {
//                 classes=result['classfications'];
//                 $("#complain_class").append("<option>أختر واحد </option>");
//                 for(let i=0;i<classes.length();i++){
//                     $("#complain_class").append("<option value='"+classes.id+"'>'"+classes.name+"'</option>");
//                 }
//             });
//         },
//     });



//     PublicWidget.registry.complainform = Dynamic;
//    return Dynamic;
// });




publicWidget.registry.complainInit= publicWidget.Widget.extend({
    selector: '.complainform',
    start() {
            var self = this;
            this._rpc({
                route: '/ewra-helpdesk-data',
                params: {},
            }).then(function (result) {
                $("#complain_class").empty();
               var classes=result['classfications'];
               if(classes){
                $("#complain_class").append("<option value=''>أختر واحد </option>");
                for(let i=0;i<classes.length;i++){
                    $("#complain_class").append("<option value='"+classes[i].id+"'>"+classes[i].name+"</option>");
                }
            }
            // ****************
            $("#governate").empty();
            var governments=result['governments'];
            if(governments){
             $("#governate").append("<option value=''>أختر واحد </option>");
             for(let i=0;i<governments.length;i++){
                 $("#governate").append("<option value='"+governments[i].id+"'>"+governments[i].name+"</option>");
             }
            }
             // ****************
            $("#responsable").empty();
            var responsapleparty=result['responsapleparty'];
            if(responsapleparty){
             $("#responsable").append("<option value=''>أختر واحد </option>");
             for(let i=0;i<responsapleparty.length;i++){
                 $("#responsable").append("<option value='"+responsapleparty[i].id+"'>"+responsapleparty[i].name+"</option>");
             }
            }
              // ****************
            $("#reportingway").empty();
            
            var reportingway=result['reportingway'];
            if(reportingway){
             $("#reportingway").append("<option value=''>أختر واحد </option>");
             for(let i=0;i<reportingway.length;i++){
                 $("#reportingway").append("<option value='"+reportingway[i].id+"'>"+reportingway[i].name+"</option>");
             }
            }
            
            
            
            
            
            
            
            });
            return this._super.apply(this, arguments);
        },
        events: { 
            'change .complain_class':'changecomplainclass',
            'change #responsable':'responsablechange',
            'submit #complainform':'SubmitHelpDeskForm',
            
        },
        changecomplainclass:function(event){
            $("#complain_type").empty();
            var self = this;
            self._rpc({
                route: '/ewra-complain_changereason',
                params: {'id':$('.complain_class').val()},
            }).then(function (result) {
               var types=result['types'];
                $("#complain_type").append("<option value=''>أختر واحد </option>");
                for(let i=0;i<types.length;i++){
                    $("#complain_type").append("<option value='"+types[i].id+"'>"+types[i].name+"</option>");
                }
            });
            
        },
        responsablechange:function(event){

            $("#introducer").empty();
            var self = this;
            self._rpc({
                route: '/ewra-complain_introducer',
                params: {'id':$('#responsable').val()},
            }).then(function (result) {
               var types=result['types'];
                $("#introducer").append("<option value=''>أختر واحد </option>");
                for(let i=0;i<types.length;i++){
                    $("#introducer").append("<option value='"+types[i].id+"'>"+types[i].name+"</option>");
                }
            });

        },


        SubmitHelpDeskForm:function(e){
            e.preventDefault();
            e.stopPropagation();
         var self=this;
         this._rpc({
            model: 'helpdesk.ticket',
            method: 'create_help_ticket_portal',
            args: [{
                'complainername':$("#complainername").val(),
                'national_id':$("#national_id").val(),
                'governate':$("#governate").find(":selected").val(),
                'city':$("#city").val(),
                'adress':$("#adress").val(),
                'complainer_tele':$("#complainer_tele").val(),
                'complaineremail':$("#complaineremail").val(),
                'responsableparty':$("#responsableparty").find(":selected").val(),
                'serviceprovider':$("#serviceprovider").find(":selected").val(),
                'complaintype':$("#complaintype").find(":selected").val(),
                'complainreason':$("#complainreason").find(":selected").val(),
                'subscriptionnumber':$("#subscriptionnumber").val(),
                'areanumber':$("#areanumber").val(),
                'reportingway':$("#reportingway").find(":selected").val(),
                'reportingcode':$("#reportingcode").val(),
                'complaindate':$("#complaindate").val(),
                'complainresponsedate':$("#complainresponsedate").val(),
                'complainername':$("#providerresponse").val(),


            }],
        }).then(function (response) {
            if (response.errors) {
                toastr.error('Something went wrong ' + response.errors + ' , try again.')
                return Promise.reject(response);
            } else {
                
                $(".complainform").html(response['code']).fadeIn(500);
            }
        });
    
    return  false;
        }
    

});
