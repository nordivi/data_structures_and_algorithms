class HashTable {
    constructor(size){
        this.data = new Array(size)
}

    _hash(key){
    let hash = 0
    for (let i = 0; i< key.length; i++){
        hash = (hash + key.charCodeAt(i)*i) % this.data.length
        console.log(hash)
    }
    return hash

  }

    set(key, value){
        let address = this._hash(key)
        if (!this.data[address]){
            this.data[address] = []
            this.data[address].push([key,value])
            console.log(this.data)
        }


        this.data[address].push([key,value])
        return this.data

    }

    get(key){
        let address = this._hash(key)
        const currBucket = this.data[address]
        if (currBucket){
            for (let add = 0; add < currBucket.length; add++ ) {
                if (currBucket[i][0] === key){
                    console.log(currBucket[i][0])
                    return currBucket[i][0]
                }

            }

        }
    }

    keys(){
        const keyArray = []
        for (let i = 0; i < currBucket.length; i++ ) {
            if (this.data[i]){
                keyArray.push(data[i][0][0])
            }

        }
        return keyArray
    }


}


const myHashTable = new HashTable(50)
console.log(myHashTable.set('grapes', 10000))
console.log(myHashTable.get('grapes'))
