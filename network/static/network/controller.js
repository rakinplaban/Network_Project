document.addEventListener("DOMContentLoaded",function(){
    // document.querySelector('#NewPostForm').addEventListener('click', ()=> load_popup())
    document.querySelector('#like').onclick = like_function(like);
})

// function load_popup(){
//     const popupfullbody = document.querySelector('body')
//     popupfullbody.ariaHidden = 'true';
//     const popupvar = document.createElement('div');
//     popupvar.setAttribute('id','popupform');
//     console.log("popup created!");
    
// }

function like_function(like){
    fetch(`/${like.id}/like`)
    .then(response => response.json())
    .then(response => {
        if(response.is_like){
            document.querySelector('#like').style.color = "red";
        }
        else{
            document.querySelector('#like').style.color = "blue"
        }
    })
}
