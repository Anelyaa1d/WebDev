var txt=document.getElementById("button");
txt.value="New";
document.getElementById("bla").innerHTML="sdfsdfsf";

var input=document.getElementById("textbox");
            var btn=document.getElementById("button");
            btn.onclick = function(){
                var ul=document.getElementById("list");
                var sp=document.createElement("span");
                sp.innerHTML=input.value;
                var li=document.createElement("li");
            
                if (input.value === ""){
                    alert("Empty field!");
                    return false;
                }
                var ch=document.createElement("input");
                ch.type="checkbox";
                ch.id="check";
                li.append(ch);
                li.appendChild(sp);
                var i=document.createElement("IMG");
                i.src="http://module.org/resources/images/symbols/icon-1024x1024-13.png";
                i.style.width="50px";
                i.id="image";
                i.onclick=function(e){
                    e.target.parentElement.remove();
                }
                li.appendChild(i);
                ul.appendChild(li);
                input.value="";
                return false;   
            }