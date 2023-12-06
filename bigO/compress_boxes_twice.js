function compressBoxesTwice(boxes, boxes2){
    boxes.forEach(function(box){ // O(a)
        console.log(box)
    });

    boxes2.forEach(function(box){ // O(b)
        console.log(box)
    });


}

// O(a + b)

// -------

function compressBoxesTwice2(boxes, boxes2){
    boxes.forEach(function(box){ // O(a)
        console.log(box)
        boxes2.forEach(function(box){ // O(b) -- nested
            console.log(box)
        });
    });
}

// O(a*b)