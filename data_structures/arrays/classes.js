// reference type
console.log([] === [])
console.log([1] === [1])
var obj1 = {value: 10}
var obj2 = obj1
var obj3 = {value: 10}
console.log(obj1 === obj2)
console.log(obj1 === obj3)
obj1.value = 15
console.log(obj2.value)
console.log(obj3.value)

// context vs scope
function b() { // -- scope
    let a = 4
}
const object = {
    a: function() {
        console.log(this) // - this is the class where are in - context
    }
}

// instantiation
class Player {
    constructor(name, type) {
        console.log(this)
        this.name = name
        this.type = type
    }
    introduce(){
        console.log(`Hi, I'm ${this.name}, I'm a ${this.type}`)
    }
}

class Wizard extends Player{
    constructor(name, type){
        super(name, type)
    }

    play(){
        console.log(`WEEE!, I'm a ${this.type}`)
    }
}

const a = new Player('Victor', 'Minecraft')
console.log(a)
console.log(a.name, a.type)

const wizard1 = new Wizard('Shelly', 'Healer')
const wizard2 = new Wizard('Shawn', 'Dark Magic')
wizard1.play()
wizard2.introduce()