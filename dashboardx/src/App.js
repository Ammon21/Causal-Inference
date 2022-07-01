
import React from 'react';
import logo from './logo.svg';
import univariate1 from './bc.png';
import univariate2 from './2.png';
import univariate3 from './3.png';
import univariate4 from './4.png';
import univariate5 from './5.png';
import univariate6 from './6.png';
import univariate7 from './7.png';
import univariate8 from './8.png';
import univariate9 from './9.png';

import './App.css';

function App() {
  return (

    <div className='App-Header'>

     <div class="topnav">
     <a class="active" href="#home">10 Academy</a>
     <a href="#dashboard">Dashboard</a>
     
     
    
      
    </div>   
    <h1>  Breast Cancer Diagnosis Data Analysis </h1>
    <div class = "tabs">
      <p class = "entry"> 596 </p>
      <p class = "subtitle"> Expierment </p>
    </div>
    <div class = "tabs">
      <p class = "entry"> 32 </p>
      <p class = "subtitle"> Features </p>
    </div>
    <div class = "tabs">
      <p class = "entry"> 357 </p>
      <p class = "subtitle"> Benign </p>
    </div>
    <div class = "tabs">
      <p class = "entry"> 212 </p>
      <p class = "subtitle"> Malignant </p>
    </div>
    <div class = "tabs">
      <p class = "entry"> 0% </p>
      <p class = "subtitle"> Missing Values </p>
    </div>

      

    <div>
       
       <br></br>
       <div>
       <img  src={univariate1} Title="It is Right Skewed"/>
       <img  src={univariate2} Title="It is Right Skewed"/>
       <img  src={univariate3} Title="It is Right Skewed"/>
       <img  src={univariate4} Title="It is Right Skewed"/>
       </div>
       <div>
       <img  src={univariate6} Title="It is distrubuted"/>
       <img  src={univariate7} Title="It is distributed"/>
       <img  src={univariate8} Title="It is distributed"/>
       <img  src={univariate9} Title="It is distributed"/>
       </div>
    </div> 

    </div>
    
    
  );
}

export default App;
