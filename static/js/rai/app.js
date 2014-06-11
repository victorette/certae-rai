/*
 This file should extend 'ProtoUL.Application' in order to get integrated to SoftMachine Application.
 */
Ext.application({
    name: 'RAI',
    paths: {
        'RAI' : 'static/js/rai'
    },

    extend: 'ProtoUL.Application',

    controllers: [
		'RAI.controller.RaccordementController'
	]
});
