const boxes = ['a','b','c','d','e']

function logAllPairsOfArray(array){
    for (i=0; i < array.length; i++){ // O(n)
        for (j=0; j<array.length; j++){ // O(n)
            console.log(array[i],array[j])
        }
    }


}
logAllPairsOfArray(boxes) // O(n^2)