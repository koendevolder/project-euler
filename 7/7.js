/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
*/

var a = [];

for (var i = 2; i < 110000; i++){
    a.push(i);
}

i = 0;

while (i < 10001-1) {
    for (var j = i+1; j < a.length; j++) {
        if (a[j] % a[i] == 0) {
            a.splice(j, 1);
        }
    }
    i = i + 1;
}

print (a[i]);

/*

alternative solution

function prime(index) {
    
    var primes = [];
    var n = 1;

    function isPrime(num) {
        for (var i = 2; i < num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return num != 1;
    }
    
    while (primes.length < index) {
        if (isPrime(n)) {
            primes.push(n);
        }
        n = n + 1;
    }
    
    return primes[index - 1];
}

print (prime(10001-1));

*/