/*
The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
*/

function square_of_sum(n) {
    var sum = ((n+1)*n)/2;
    var squared = Math.pow(sum, 2);
    return squared;
}
 
function sum_of_squares(n) {
    var sum = 0;
    for (var i = 0; i < n + 1; i++) {
        sum = sum + Math.pow(i, 2);
    }
    return sum;
}

var n = 100 ;

print (square_of_sum(n) - sum_of_squares(n));