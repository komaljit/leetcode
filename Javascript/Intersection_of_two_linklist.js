var getIntersectionNode = function(headA, headB) {
    if(headA === null || headB === null) {
        return null;
    }
    var pointA = headA;
    var pointB = headB;
    var i = 0;
    var j = 0;
    var k = 0;
    while(pointA.next !== null) {
        pointA = pointA.next;
        i++;
    }
    while(pointB.next !== null) {
        pointB = pointB.next;
        j++;
    }
    if(pointB != pointA) {
        return null;
    }
    pointA = headA;
    pointB = headB;

    if(i > j) {
        while(k < i - j){pointA = pointA.next;k++;}
    } else {
        while(k < j - i){pointB = pointB.next;k++;}
    }
    while(pointA != pointB) {
        pointA = pointA.next;
        pointB = pointB.next;
    }
    return pointA;
};
