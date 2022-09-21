// jdklsjfajfka
if(sessionStorage.getItem('loginFlag')===null||sessionStorage.getItem('loginFlag')==='No'){
  document.getElementById('Login').style.visibility='visible';
  document.getElementById('Home').style.visibility='hidden';
  document.getElementById('Logout').style.visibility='hidden';
}else{
  console.log('here');
  document.getElementById('Login').style.visibility='hidden';
  document.getElementById('Home').style.visibility='visible';
  document.getElementById('Logout').style.visibility='visible';
}

if(window.location.href.indexOf('search')!=-1){
  loaddropdowns()
}

if(window.location.href.indexOf('appointments')!=-1){
  console.log('appointments page')
  myDoctor()
}
if(window.location.href.indexOf('doctorhome')!=-1){
 console.log('dhome')
  showdocapp()
}

function showhome(){
  department=sessionStorage.getItem('dept')
  if (department=='admin') {
    window.open('adminhome','_self');
  }else{
    if (department=='patient') {
      window.open("apphome",'_self');
    }else{
      if (obj.department=='doctor') {          
        window.open("doctorhome",'_self');
      } 
      else{
        window.open("apphome",'_self');
      }

    }
  }
}   


function logout(){
  sessionStorage.setItem('loginFlag','No');
  sessionStorage.removeItem('docid');
  sessionStorage.removeItem('id');
  sessionStorage.removeItem('dept');
  sessionStorage.removeItem('uname');
}

function login(){
  var out='ranom';
  var obj ={};
  var obj1=[];
  uname=document.getElementById('uname').value;
  password=document.getElementById('password').value;

  if(sessionStorage.getItem('loginFlag')===null||sessionStorage.getItem('loginFlag')==='No'){
      if (uname.length > 0 && password.length > 0) {
        fetch("/getLogin/" + uname)
        .then((response) => response.json())
        .then((result) => {
          obj = result[0];
          if(obj!=null && !('error'in obj)){
            if(obj.password==password){
              sessionStorage.setItem('loginFlag','Yes');
              sessionStorage.setItem('dept',obj.department);
              sessionStorage.setItem('uname',obj.name);
              sessionStorage.setItem('id',obj.id)
              if (obj.department=='admin') {
                window.open('adminhome','_self');
              }else{
                if (obj.department=='patient') {
                  window.open("search",'_self');
                }else{
                  if (obj.department=='doctor') {          
                    window.open("doctorhome",'_self');
                  } 
                  else{
                    alert('Unknown successful login. Something is wrong');
                    return;
                  }
      
                }
      
              }
            }else{
              alert('Wrong username or password. Please try again');
              return;
            }
    
          }else{
            alert('Wrong username or password. Please try again');
            return;
          } 
          });
          console.log(obj.password)
 
    
      }
      else{

        out='<h4>Page not loaded fully.Please wait for page to reload or click refresh</h4>'
      }
    //document.getElementById("id01").innerHTML = out;
      
  }else{
    window.open('appointments','_self');
  }
    
}

// JS function to populate search page dropdowns onload
function loaddropdowns(){
  const dept = document.getElementById("dept");
  const doc = document.getElementById("doctor");
  deptarr='';
  docarr='';
  if (dept.selectedIndex.text==null && doc.selectedIndex.value==null) {
    out="/filldropdowns/All/All"
    fetch(out)
    .then((response) => response.json())
    .then((result) => {
        deptarr='<option selected="selected" value=0>All</option>'
        docarr='<option selected="selected" value=0>All</option>'
        result.forEach(element => {
           deptarr+='<option value='+element.id+'>'+element.department+'</option>'
          docarr+='<option value='+element.id+'>'+element.name+'</option>'
        });
        document.getElementById('dept').innerHTML=deptarr;
        document.getElementById('doctor').innerHTML=docarr;
      });

  }
}

// JS function to populate search page dropdowns onchange
function getdropdowns(){
  const dept = document.getElementById("dept");
  const doc = document.getElementById("doctor");
  out=""
  deptname=dept.options[dept.selectedIndex].text
  docname=doc.options[doc.selectedIndex].text
  if (dept.value.length > 0 | doc.value.length > 0) {
    out="/filldropdowns/" + deptname+"/"+docname
  }
  else{
    out="/filldropdowns/All/All"
  }
    fetch(out)
    .then((response) => response.json())
    .then((result) => {
      deptarr='<option value=0>All</option>'
      docarr='<option value=0>All</option>'
      res='';
      result.forEach(element => {
        if(element.department!=deptname){
          deptarr+='<option value='+element.id+'>'+element.department+'</option>'
        }
        else{
          deptarr+='<option selected="true" value='+element.id+'>'+element.department+'</option>'
        }
        if(element.name!=docname){
          docarr+='<option value='+element.id+'>'+element.name+'</option>'
        }
        else{
          console.log('selected doc')
          docarr+='<option selected="true" value='+element.id+'>'+element.name+'</option>'
        }
      });
      document.getElementById('dept').innerHTML=deptarr;
      document.getElementById('doctor').innerHTML=docarr;
    });
}
  

// JS function to display list of doctors in selecred department
function myFunction() {
      console.log('in myfunctions')
      var dept=document.getElementById("dept");
      var doc=document.getElementById("doctor");
      var name=doc.options[doc.selectedIndex];
      console.log(dept,name);
      var out='';
      docarr=[]
      if (dept.value.length > 0 && doc.value.length > 0) {
        fetch("/filldropdowns/" + dept.options[dept.selectedIndex].text+"/"+doc.options[doc.selectedIndex].text)
        .then((response) => response.json())
        .then((result) => {
          console.log(result)
          out=createcard(result);
          document.getElementById("id01").innerHTML = out;
          });
      }
      else{
        out='<h4>Page not loaded fully.Please wait for page to reload or click refresh</h4>'
      }
    document.getElementById("id01").innerHTML = out;
  }

  
// JS function to create card for every doctor
  function createcard(arr){
    console.log('creating cards')
    var out = "";
    var i;
   // out+='<div class="row row-cols-1 row-cols-sm-2 row-cols-md-3">';
    for(i = 0; i < arr.length; i++) {
      out += '<div class="card text-center" > <img class="card-img-top" src="/static/' + arr[i].img + 
      '"><div class="card-body"><h5 class="card-title">' + arr[i].name+'</h5><p class="card-text">Department: '+arr[i].department+
      '</p> <a href="#" class="btn btn-success"onclick=myappoint('+arr[i].id+')>Book appointment</a></div></div>';
    }
   // out+='</div>';
    return out;
  }



// JS function to book doctor
  function myappoint(docid){
    sessionStorage.setItem('docid',docid);
    if(sessionStorage.getItem('loginFlag')===null||sessionStorage.getItem('loginFlag')==='No'){
      window.open('login','_self');
    }else{
      window.open('appointments','_self');
    }
  }


  function myDoctor(){

    var out = "";
    var i=sessionStorage.getItem('docid');
    if(sessionStorage.getItem('dept')==='admin'){
      document.getElementById('patientname').hidden=false;
      document.getElementById('patientid').hidden=false;
      document.getElementById('adminmessage').hidden=false;
    }
    console.log(sessionStorage.getItem('uname'))
    if(sessionStorage.getItem('uname').length>0){
      console.log(sessionStorage.getItem('uname'))
      document.getElementById('patientname').value=sessionStorage.getItem('uname');
    }
    if(sessionStorage.getItem('id').length>0){
      console.log(sessionStorage.getItem('id'))
      document.getElementById('patientid').value=sessionStorage.getItem('id');
    }
    console.log(i);
    //let arr=docarr.filter(obj1 => obj1.id === i);
    if(i===null){
      window.open('search','_self');
    }else{
        fetch("/filldocdiv/" + i)
        .then((response) => response.json())
        .then((result) => {
          arr=result;
          try {
            out+='<div class="col card-class" > <div class="card mx-3 " ><img class="card-img-top" src="/static/' + arr[0].img + '"><div class="card-body"><p class="card-text">' + arr[0].name+
            '</p><p>Department: '+arr[0].department+'</p><p>Description : +'+arr[0].descr+'</p></div></div></div>'; 
            //document.getElementById('patientid').value=1;
            document.getElementById('doctid').value=arr[0].id;  
            document.getElementById('docname').value=arr[0].name;    
          } catch (error) {
            
            out+='<h2>Unable to load doc details</h2>'
          }
          document.getElementById('docdetails').innerHTML=out;

          });
      console.log('hereeeeeee');
    }

  }


function showappointments(){
  document.getElementById('app-time').hidden=false;
  console.log(document.getElementById('app-time').hidden)
  var id=sessionStorage.getItem('docid');
  
  var j = document.getElementById('date').value.toString();
  console.log(j);
  console.log(id);
  fetch("disabledocapp/"+id+'/'+j)
  .then((response) => response.json())
  .then((results) => {
    if('error' in results[0] == false){
      for(i=0;i<results.length;i++){
        document.getElementById(results[i].time).disabled=true;
      }
    }
    else{
      out='<ul class="list-group lists">'

    }              
    // document.getElementById("todo").innerHTML = out
  }); 
}

function setTime(t){
  console.log(t)
  document.getElementById('time').value=t;
  console.log(document.getElementById('time').value);
  console.log(document.getElementById('patientid').value);
  console.log(document.getElementById('doctid').value);  
  console.log(document.getElementById('docname').value); 
  console.log(document.getElementById('date').value)
}

function hideForm(){
  console.log('hide')
  document.getElementById('dbform').hidden='true';
}

function showdocapp(){
  var i=sessionStorage.getItem('id');
  fetch("/filldocapp/"+i)
  .then((response) => response.json())
  .then((results) => {
    out=''
    if('error' in results[0]){
      out+=results[0].error
    }
    else{
      out='<ul class="list-group lists">'
      for(i=0;i<results.length;i++){
        out+='<li class="list-group-item">Patient <a >'+results[i].patientname+'</a> on '+results[i].date+' at '+results[i].time+'</li>'
      }
      out+="</ul>"
    }              
    document.getElementById("todo").innerHTML = out}); 
}
