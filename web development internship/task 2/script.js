const inputBox=document.getElementById("search");
const listContainer=document.getElementById("task-list");
function addTask(){
    if(inputBox.value===''){
        alert("You must write a task!");
    }
    else{
        let li=document.createElement("li");
        li.innerHTML='<p class="text">'+inputBox.value+'</p>';
        listContainer.appendChild(li);
        let span=document.createElement("span");
        span.innerHTML="\u00d7";
        li.appendChild(span);
    }
    inputBox.value="";
    saveData();
}

listContainer.addEventListener("click",function(e){
    if(e.target.tagName==="LI"){
        e.target.classList.toggle("checked");
        saveData();
    }
    else if(e.target.tagName==="P"){
        e.target.parentElement.classList.toggle("checked");
        saveData();
    }
    else if(e.target.tagName==="SPAN"){
        e.target.parentElement.remove();
        saveData();
    }
},false);

function saveData(){
    localStorage.setItem("data",listContainer.innerHTML);
}

function showTasks(){
    listContainer.innerHTML=localStorage.getItem("data");
}
showTasks();