// linear search
/*function linearSearch($list, $target){
	return array_search($target, $list);
}

function verify($index){
	if($index == NULL){
		echo "Target not found";
	}else {
		echo "Target found in index: $index";
	}
}

$number = array(1,2,3,4,5,9,10);
$result =  linearSearch($number, 10);
echo verify($result)
*/

// binary search

/*function binarySearch($list, $target){
	if(count($list) == 0) return false;
	$low = 0;
	$high = count($list) - 1;

	while ($low <= $high){
		$mid = floor(($low + $high) /2);

		if($list[$mid] == $target){
			return true;
		}
		elseif($list[$mid] < $target) {
			$low = $mid + 1;
		}
		else{
			$high = $mid -1;
		}
	}

	return false;
}

function verify($bool){
	if($bool == true){
		echo "Target Exists";
	}else{
		echo "Target not found";
	}
}

$number = array(1,2,3,4,5,9,10);
$result =  binarySearch($number, 11);
echo verify($result)*/
echo 'hi';