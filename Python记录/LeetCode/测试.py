for (let i=0; i<classList.length; i++){
    bool flag = False
    for (let j=0; j<classList.length-i-1; j++){
        if mapSortFunction.numSort(classList[j], classList[j+1]){
            int tmp = a[j] //看着改一下
            a[j] = a[j+1]; 
            a[j+1] = tmp
            flag = True
        }
    }
    if flag == False{break}
    }
}