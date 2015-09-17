function OrderFormController ($scope) {

	// Defina o modelo de propriedades. O View vai fazer o loop
	// através do array services e gerar um elemento li
	// para cada um dos itens.

	$scope.services = [
		{
			name: 'Web Development',
			price: 300,
			active: true
		}, {
			name: 'Design',
			price: 400,
			active: false
		}, {
			name: 'Integration',
			price: 250,
			active: false
		}, {
			name: 'Training',
			price: 220,
			active: false
		}
	];

	$scope.toggleActive = function (s) {
		s.active = !s.active;	
	};

	// Método útil para calcular o preço total
	$scope.total = function () {

		var total = 0;

		// Uso o método auxiliar do Angular 'forEach'
		// para iterar o array services

		angular.forEach ($scope.services, function (s) {
			if (s.active) {
				total += s.price;
			}
		});

		return total;
	};

}