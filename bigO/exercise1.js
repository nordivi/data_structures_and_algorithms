function funChallenge(input) {
    let a = 10 // O(1)
    a = 50 + 3 // O(1)

    for (let i =0; i < input.length; i++) { // O(n) --- input
        anotherFunction() // O(n)
        let stranger = true // O(n)
        a++ // O(n)
    }

    return a // O(1)


}

// 3 + n + n + n + n
// O(3 + 4n) -- GETS SIMPLIFIED TO O(n)
