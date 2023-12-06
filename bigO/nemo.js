const nemo = ['dasdsa', 'dsadas', 'nemo']
const everyone = ['dory', 'bruce', 'marlin', 'nemo', 'fill']
const large = new Array(1000).fill('nemo')


function findNemo(array) {
    for (let i = 0; i < array.length; i++){ // O(n) -- linear (depends on the number of inputs) --- n elements -> n operations
        if (array[i] === 'nemo') {
            console.log('FOUND NEMO!')
        }
    }
}

findNemo(large)