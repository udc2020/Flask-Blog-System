// snipast 
const snipast = document.querySelectorAll('.snipast')
snipast.forEach(sn => {
  console.log(sn.innerText);
}) 


// Rich Text Plugin
try {

  tinymce.init({
     selector: 'textarea#conentBlog',
     skin: 'bootstrap',
     menubar: false,
     plugins: 'lists, link, image, media',
     toolbar: 'h1 h2 h3 h4 h5 bold italic strikethrough blockquote bullist numlist backcolor | link image  | removeformat ',
   });
}catch(er){
  
}


