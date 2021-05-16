const express = require("express");
const bodyParser = require("body-parser");
const ejs = require("ejs");

//const {spawn} = require('child_process');



const app = express();
app.use(express.static("public"));
app.set('view engine','ejs');
app.use(bodyParser.urlencoded({extended:true}));




var spawn = require("child_process").spawn; 




var y;

function callName(req, res) { 

    var process = spawn('python',["ml.py"] ); 
 
    process.stdout.on('data', function(data) { 
        var power = data.toString();
        y = power.split(" ").map((i) => Number(i));
        //console.log(energy);     
          
        res.render("home");

    } ); 
} 

app.get('/', callName); 


/*

app.get("/",function(req,res){
    
});

*/

app.get("/login",function(req,res){
    res.render("login");
})

app.get("/register",function(req,res){
    res.render("register");
})

//var arr = "01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20"
//const b = arr.split(" ").map((i) => Number(i));
//console.log(b);



app.post("/login",function(req,res){
    console.log(req.body.username);
    console.log(req.body.password);
    res.render("secrets",{
    y: y   
    });

})



app.get('/logout',function(req,res){
    res.render("login");
})




app.listen(3000,function(){
    console.log("Server started ");
});