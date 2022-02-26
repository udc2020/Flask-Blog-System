
// Remove Admin Clicked
const admin = document.querySelector('#admin')

if (admin){

   admin.onclick =  (e) => {
      e.preventDefault()
   }
}



// Rich Text Plugin
tinymce.init({
   selector: 'textarea#conentBlog',
   skin: 'bootstrap',
   menubar: false,
   plugins: 'lists, link, image, media',
   toolbar: 'h1 h2 h3 h4 h5 bold italic strikethrough blockquote bullist numlist backcolor | link image  | removeformat ',
 });


