//Cotroles for coaches area

coachApp.controller('CoachFilterController',['$scope', '$routeParams', '$http',
	function($scope, $routeParams, $http) {
		$http.get('http://127.0.0.1:8000/api/coaches_api/?format=json')
			.success(
				function(data){
					$scope.coaches = data;
          $scope.totalItems = $scope.coaches.length;
				});

  $scope.pageSize = 6;
  $scope.currentPage = 1;
	//Languages
	$scope.languages = {english: true, french: true, spanish: true, russian: true};

	//Game Modes
	$scope.modes = {cash: true, sng: true, mtt: true, software: true};

	$scope.ModeSelected = function(modes){
		var any_selected = false;
		any_selected = modes.cash || modes.sng || modes.mtt;
		return any_selected;
	}

	//Game SubModes
	$scope.cash_submodes = { nl_deep_stack: true, nl_multistack: true, nl_cap: true, plo_deepstack: true, plo_multistack: true, plo_hu: true, cash_other: true};

	//Game Second Submodes
	$scope.sub_modes_2 = { full_ring: true, six_max: true, heads_up: true };

	//SnG SubModes
	$scope.sng_submodes = {normal: true, turbo: true, hyperturbo:true, spin_and_go: true}

	//MTT SubModes
	$scope.mtt_submodes = {normal: true, sng: true, satelite: true}

	//Software Types
	$scope.software = {hold_them_manager: true, snowie: true, cr_ev: true, flopzilla: true, posolver_simple: true, hold_them_resources: true }


  $scope.swich_cash = function(){
    $scope.modes.cash = true;
    $scope.modes.sng = false;
    $scope.modes.software = false;
    $scope.modes.mtt = false;
  }

  $scope.swich_sng = function(){
    $scope.modes.cash = false;
    $scope.modes.sng = true;
    $scope.modes.software = false;
    $scope.modes.mtt = false;
  }
  $scope.swich_mtt = function(){
    $scope.modes.cash = false;
    $scope.modes.sng = false;
    $scope.modes.software = false;
    $scope.modes.mtt = true;
  }

  $scope.swich_software = function(){
    $scope.modes.cash = false;
    $scope.modes.sng = false;
    $scope.modes.software = true;
    $scope.modes.mtt = false;
  }

  $scope.swich_all = function(){
    $scope.modes.cash = true;
    $scope.modes.sng = true;
    $scope.modes.software = true;
    $scope.modes.mtt = true;
  }

	}

]);


coachApp.controller('CoachListController',['$scope', '$routeParams', '$http',
  function($scope, $routeParams, $http) {
    $http.get('http://localhost:8000/api/coaches_api/?format=json')
      .success(
        function(data){
          $scope.coaches = data;
        });
      }
]);
