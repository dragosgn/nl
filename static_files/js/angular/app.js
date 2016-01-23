'use strict';

var coachApp = angular.module('coachApp',['ngRoute','ui.bootstrap']);

coachApp.config(['$routeProvider',
	function($routeProvider) {
		$routeProvider.
			when('/coacheslist', {
				templateUrl: 'localhost/templates/handle_coaches/coaches_list_partial.html',
				controller: 'CoachListController'
			});
	} 
]);

coachApp.config(['$httpProvider', function($httpProvider){
		$httpProvider.defaults.xsrfCookieName = 'csrftoken';
		$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	}
]);


coachApp.filter('myfilter', function(){
   return function( coaches, languages, modes, cash_submodes, sub_modes_2, sng_submodes, mtt_submodes, software ){
    
    var all_modes = modes.cash && modes.sng && modes.mtt && modes.software ;
    var filtered = [];
    var all_languages = languages.english && languages.french && languages.spanish && languages.russian;

    angular.forEach(coaches, function(coach) {
    	//Languages Filter
    	//No languages selected: display all
       if(!languages.english && !languages.french && !languages.spanish && !languages.russian) {
          	filtered.push(coach);
        }
        else if(languages.english && coach.english ){
          	filtered.push(coach);
        }
        else if(languages.french && coach.french ){
          	filtered.push(coach);
        }
        else if(languages.spanish && coach.spanish ){
          	filtered.push(coach);
        }
        else if(languages.russian && coach.russian ){
          	filtered.push(coach);
        }
        //All languages selected: dispaly all
        else if(all_languages && all_modes){
          	filtered.push(coach);
        }
        //Game modes : cash

    });


    var filtered_by_language = filtered;
    var filtered_by_language_and_modes = [];

    var no_modes = !modes.cash && !modes.sng && !modes.mtt && !modes.software ;

    //All modes variables used to display all the options when they are all selected
    var all_cash_submodes = cash_submodes.nl_deep_stack && cash_submodes.nl_multistack && cash_submodes.nl_cap && cash_submodes.plo_deepstack && cash_submodes.plo_multistack && cash_submodes.plo_hu && cash_submodes.cash_other;
    var all_sng_submodes = sng_submodes.normal && sng_submodes.turbo && sng_submodes.hyperturbo;
    var all_mtt_submodes = mtt_submodes.normal && mtt_submodes.sng && mtt_submodes.satelite;
    var all_software = software.hold_them_manager && software.snowie && software.cr_ev && software.flopzilla && software.posolver_simple && software.hold_them_resources;

    //Modes Filter
    angular.forEach(filtered_by_language, function(coach) {
    	//No modes selected: display all
       if(no_modes) {
          	filtered_by_language_and_modes.push(coach);
        }

        //CASH MODE
        else if(modes.cash && coach.cash){
        	if( all_cash_submodes ){
        		filtered_by_language_and_modes.push(coach);
        	} 
        	//NL Deep Stack
          	else if(cash_submodes.nl_deep_stack && (coach.nl_deep_stack_6max || coach.nl_deep_stack_FR)){
          		if(sub_modes_2.full_ring && coach.nl_deep_stack_FR){
					filtered_by_language_and_modes.push(coach);
          		}else if(sub_modes_2.six_max && coach.nl_deep_stack_6max){
    				filtered_by_language_and_modes.push(coach);
          		}else if(sub_modes_2.six_max && sub_modes_2.full_ring) { 
					filtered_by_language_and_modes.push(coach);
          		}else if(!sub_modes_2.six_max && !sub_modes_2.full_ring) { 
					filtered_by_language_and_modes.push(coach);
          		}

          	// NL MultiStack	
          	}else if(cash_submodes.nl_multistack && (coach.nl_multistack_6max || coach.nl_multistack_FR)){
				if(sub_modes_2.full_ring && coach.nl_multistack_FR){
					filtered_by_language_and_modes.push(coach);
          		}else if(sub_modes_2.six_max && coach.nl_multistack_6max){
    				filtered_by_language_and_modes.push(coach);
          		}else if(sub_modes_2.six_max && sub_modes_2.full_ring) { 
					filtered_by_language_and_modes.push(coach);
          		}else if(!sub_modes_2.six_max && !sub_modes_2.full_ring) { 
					filtered_by_language_and_modes.push(coach);
          		}  

          	//NL CAP
          	}else if(cash_submodes.nl_cap && (coach.nl_cap_6max || coach.nl_cap_FR)){
				if(sub_modes_2.full_ring && coach.nl_cap_FR){
					filtered_by_language_and_modes.push(coach);
          		}else if(sub_modes_2.six_max && coach.nl_cap_6max){
    				filtered_by_language_and_modes.push(coach);
          		}else if(sub_modes_2.six_max && sub_modes_2.full_ring) { 
					filtered_by_language_and_modes.push(coach);
          		}else if(!sub_modes_2.six_max && !sub_modes_2.full_ring) { 
					filtered_by_language_and_modes.push(coach);
          		}

          	//PLO DeepStack
            }else if(cash_submodes.plo_deepstack && coach.plo_deepstack_6max){
				      filtered_by_language_and_modes.push(coach); 

			//PLO MultiStack
          	}else if(cash_submodes.plo_multistack && coach.plo_multistack_6max){
				      filtered_by_language_and_modes.push(coach);

			//PLO Heads Up
          	}else if(cash_submodes.plo_heads_up && coach.plo_hu){
				      filtered_by_language_and_modes.push(coach);
			}

        }

        //SNG MODE
        else if(modes.sng && coach.sng ){
          	if( all_sng_submodes){
        		filtered_by_language_and_modes.push(coach);
        	} 
        	//SNG Normal
          	else if(sng_submodes.normal && (coach.sng_normal_FR || coach.sng_normal_hu || coach.sng_normal_6max )){
          		//Full Ring
          		if(sub_modes_2.full_ring && coach.sng_normal_FR ){
					filtered_by_language_and_modes.push(coach);
				//Six Max
          		}else if(sub_modes_2.six_max && coach.sng_normal_6max){
    				filtered_by_language_and_modes.push(coach);
    			//Heads Up
          		}else if(sub_modes_2.six_max && coach.sng_normal_hu){
    				filtered_by_language_and_modes.push(coach);
    			//all selected
          		}else if(sub_modes_2.six_max && sub_modes_2.full_ring && sub_modes_2.heads_up) { 
					filtered_by_language_and_modes.push(coach);
				//none selected
          		}else if(!sub_modes_2.six_max && !sub_modes_2.full_ring && !sub_modes_2.heads_up) { 
					filtered_by_language_and_modes.push(coach);
          		
          		}
        	//SNG Turbo
          	}else if(sng_submodes.turbo && (coach.sng_turbo_FR || coach.sng_turbo_hu || coach.sng_turbo_6max )){
          		//Full Ring
          		if(sub_modes_2.full_ring && coach.sng_turbo_FR ){
					filtered_by_language_and_modes.push(coach);
				//Six Max
          		}else if(sub_modes_2.six_max && coach.sng_turbo_6max){
    				filtered_by_language_and_modes.push(coach);
    			//Heads Up
          		}else if(sub_modes_2.six_max && coach.sng_turbo_hu){
    				filtered_by_language_and_modes.push(coach);
    			//all selected
          		}else if(sub_modes_2.six_max && sub_modes_2.full_ring && sub_modes_2.heads_up) { 
					filtered_by_language_and_modes.push(coach);
				//none selected
          		}else if(!sub_modes_2.six_max && !sub_modes_2.full_ring && !sub_modes_2.heads_up) { 
					filtered_by_language_and_modes.push(coach);
          		}

        	//SNG HyperTurbo
          	}else if(sng_submodes.hyperturbo && (coach.sng_hyperturbo_FR || coach.sng_hyperturbo_hu || coach.sng_hyperturbo_6max )){
          		//Full Ring
          		if(sub_modes_2.full_ring && coach.sng_turbo_FR ){
					filtered_by_language_and_modes.push(coach);
				//Six Max
          		}else if(sub_modes_2.six_max && coach.sng_turbo_6max){
    				filtered_by_language_and_modes.push(coach);
    			//Heads Up
          		}else if(sub_modes_2.six_max && coach.sng_turbo_hu){
    				filtered_by_language_and_modes.push(coach);
    			//all selected
          		}else if(sub_modes_2.six_max && sub_modes_2.full_ring && sub_modes_2.heads_up) { 
					filtered_by_language_and_modes.push(coach);
				//none selected
          		}else if(!sub_modes_2.six_max && !sub_modes_2.full_ring && !sub_modes_2.heads_up) { 
					filtered_by_language_and_modes.push(coach);
          		}

          	//SNG Spin And Go
            }else if(sng_submodes.spin_and_go && coach.sng_spin_and_go){
				filtered_by_language_and_modes.push(coach); 
          	}

        }

        //MTT Mode
        else if(modes.mtt && coach.mtt ){
        	if( all_mtt_submodes){
        		filtered_by_language_and_modes.push(coach);
        	} 
        	//MTT Normal
          	else if(mtt_submodes.normal && coach.mtt_normal){
          		filtered_by_language_and_modes.push(coach);
          	}

          	//MTT SNG
          	else if(mtt_submodes.sng && coach.mtt_sng){
          		filtered_by_language_and_modes.push(coach);
          	}

          	//MTT Satelite
          	else if(mtt_submodes.satelite && coach.mtt_satelite){
          		filtered_by_language_and_modes.push(coach);
          	}
        }

        //SOFTWARE Mode
        else if(modes.software && coach.software ){
          	if( all_mtt_submodes){
        		filtered_by_language_and_modes.push(coach);
        	} 
        	//Software Hold Them Manager
          	else if(mtt_submodes.hold_them_manager && coach.hold_them_manager){
          		filtered_by_language_and_modes.push(coach);
          	}

          	//Software Snowie
          	else if(mtt_submodes.snowie && coach.snowie){
          		filtered_by_language_and_modes.push(coach);
          	}

          	//Software Cr_Ev
          	else if(mtt_submodes.cr_ev && coach.cr_ev){
          		filtered_by_language_and_modes.push(coach);
          	}

          	//Software FlopZilla
          	else if(mtt_submodes.flopzilla && coach.flopzilla){
          		filtered_by_language_and_modes.push(coach);
          	}

          	//Software Posolver Simple
          	else if(mtt_submodes.posolver_simple && coach.posolver_simple){
          		filtered_by_language_and_modes.push(coach);
          	}

          	//Software Hold Them Resources
          	else if(mtt_submodes.hold_them_resources && coach.hold_them_resources){
          		filtered_by_language_and_modes.push(coach);
          	}
        }

        //All modes selected: dispaly all
        else if(all_modes){
          	filtered_by_language_and_modes .push(coach);
        }

    });

    return filtered_by_language_and_modes ;
  };
});

coachApp.filter('startFrom', function(){
  return function(data, start){
    return data.slice(start);
  };
})



coachApp.controller
	











