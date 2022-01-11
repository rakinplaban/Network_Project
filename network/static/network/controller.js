document.addEventListener("DOMContentLoaded",function(){
    document.querySelector('#NewPostForm').addEventListener('click', ()=> load_popup())
    document.querySelector('#like').onclick = function like(){
        if (document.querySelector('#like').style.color == "blue"){
            document.querySelector('#like').style.color == "red";
            console.log("Clicked to red");
        }
        if (document.querySelector('#like').style.color == "red"){
            document.querySelector('#like').style.color == "blue";
            console.log("Clicked to blue");
        }
    }
})

function load_popup(){
    const popupfullbody = document.querySelector('body')
    popupfullbody.ariaHidden = 'true';
    const popupvar = document.createElement('div');
    popupvar.setAttribute('id','popupform');
    console.log("popup created!");
    
}

// function like_function(){
//     if (document.querySelector('#like').style.color == "blue"){
//         document.querySelector('#like').style.color == "red";
//         console.log("Clicked to red");
//     }
//     if (document.querySelector('#like').style.color == "red"){
//         document.querySelector('#like').style.color == "blue";
//         console.log("Clicked to blue");
//     }
// }
