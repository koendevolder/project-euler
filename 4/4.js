/*
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.
Find the largest palindrome made from the product of two 3-digit numbers. 
*/

for (var i = 999; i > 900; i--) {
    for (var j = 999; j > 900; j--) {
        var num = i * j;
        if (num.toString() === num.toString().split('').reverse().join('')) {
            print (num);
            print (i);
            print (j);
            throw new Error("Done");
        }
    }
}