document.addEventListener("DOMContentLoaded",function(){
    document.querySelector('#likeform').onsubmit = like_function();
})


function like_function(){
    if(document.querySelector('#like').style.color == 'blue'){
        document.querySelector('#like').style.color == 'red';
    }
    else{
        document.querySelector('#like').style.color == 'blue';
    }
}
