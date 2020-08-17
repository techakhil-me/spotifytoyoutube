function check() {
  var url =  document.forms["urlform"]["link"].value;
  if (url.includes("open.spotify.com")) {
    document.getElementById("submit").remove();
    return "location.href='{%  url 'getlink' %}'";
  }else{
    alert("INVALID LINK !!");
    return false;
  }
}
function submitbtn(){  
  if (check()){
  document.getElementById("submit").remove();
  document.getElementById("loading").classList.remove("hidden");
  }
}
