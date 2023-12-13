

class LinkedList{
    constructor(value) {
        this.head = {
            value: value,
            next: null
        }

        this.tail = this.head
        this.length = 1
    }

    append(value){
        const newNode = {
            value: value,
            next: null
        }
        this.tail.next = newNode
        this.tail = newNode
        this.length++
        return this
    }

    prepend(value){
        const newNode = {
            value: value,
            next: this.head
        }
        this.head = newNode
        this.length++
        return this
    }

    insert(index, value){
        const newNode = {
            value: value,
            next: null
        }
        let currNode=this.head
        for (let i = 0; i < index - 1; i++){
            currNode = currNode.next
        }
        const lastNode = currNode.next
        newNode.next = lastNode
        currNode.next = newNode
        this.length++
        return this
    }

    remove(index){
        let currNode=this.head
        for (let i = 0; i < index - 1; i++){
            currNode = currNode.next
        }
        currNode.next = currNode.next.next
        this.length--
        return this
    }

    reverse(){
        let tail = this.tail
        let head = this.head
        currNode = this.head
        nextNode = this.head.next
        for (let i = 0; i < this.length-1; i--){
            nextNode.next = CurrNode
            currNode = currNode.next
            nextNode = currNode.next
        }
        this.tail = head
        this.head = tail
        return this
    }

}

const myLinkedList = new LinkedList(20)
myLinkedList.append(10)
myLinkedList.append(11)
myLinkedList.append(13)
myLinkedList.append(14)
myLinkedList.prepend(1)
myLinkedList.insert(1, 23)
console.log(myLinkedList)