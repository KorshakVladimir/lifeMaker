function createTaskCtrl($scope,$http,$window,$document){
	$scope.task_title = 'qw';
	$scope.create_task = function(){
		$http.post('/task/add/', {"title":$scope.task_title}).then(function(success_resolved){
			$window.location.reload();
		}, 
		function(error_resolved){
			$scope.task_error = error_resolved.data;
		});
	};
	$scope.change_all_checkbox = function(){
		var tasks_checkbox = $document.find('.task_list input[type="checkbox"]')
		console.log(tasks_checkbox);
	};
}

taskApp.controller('createTaskCtrl', ['$scope','$http','$window','$document', createTaskCtrl])
