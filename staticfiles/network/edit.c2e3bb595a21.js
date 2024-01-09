document.addEventListener('DOMContentLoaded',function(){
    document.querySelector('#NewPostForm').addEventListener('submit',function(event){
        event.preventDefault();
        edit_post_func();
    })
})

function edit_post_func(){
    fetch(`editpost/${id}`)
}