document.addEventListener("DOMContentLoaded",function(){
    document.querySelector('#NewPostForm').addEventListener('click', ()=> load_popup())
})

function load_popup(){
    const popupfullbody = document.querySelector('body')
    popupfullbody.ariaHidden = 'true';
    const popupvar = document.createElement('div');
    popupvar.setAttribute('id','popupform');
    console.log("popup created!");
    
}