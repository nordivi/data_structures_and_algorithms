import LinkedList from '../data_structures/linked_lists'

var reverse_list = (head) => {
    var prev = null
    var curr = head
    while (curr) {
        var next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    }
    return prev
}