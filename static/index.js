const question_text=document.querySelectorAll(".question_text")
const fa_plus=document.querySelector(".fa-plus")
const question_description=document.querySelector(".question_description")


// question_text.addEventListener("click",()=>{
//     question_description.classList.toggle("active")
//     fa_plus.classList.toggle("x")
// })
question_text.forEach(ques=>{
    ques.addEventListener("click",(e)=>{
      ques.lastElementChild.classList.toggle("x")
      ques.parentElement.lastElementChild.classList.toggle("active")
    })
})